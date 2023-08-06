import numpy as np
import pandas as pd
from datetime import timedelta

from quantplay.reporting.strategy_report import StrategyReport
from quantplay.utils.data_utils import DataUtils
from quantplay.utils.alpha_factory import QuantplayAlphaFactory

# TODO import all these from quantplay_utils
from quantplay.utils.constant import (
    TickInterval,
    Order,
    Constants,
    StrategyType,
    OrderTableColumns,
)


class Backtesting:

    required_columns = ["date", "symbol", "close", "intraday_forward_high"]

    @staticmethod
    def get_close_price(df):
        df.loc[:, "close_price"] = np.where(
            (df.strategy_type == StrategyType.overnight),
            df.next_day_intraday_open,
            df.weighted_intraday_close,
        )

        df.loc[:, OrderTableColumns.closingTimestamp] = np.where(
            (df.strategy_type == StrategyType.overnight),
            df.next_date.apply(lambda x: x.replace(hour=9, minute=25)),
            df.tick_timestamp.apply(lambda x: x.replace(hour=15, minute=15)),
        )

        return df

    @staticmethod
    def merge_next_day_intraday_open(trades_df, candle_data):
        candle_data.loc[:, "next_day_intraday_open"] = candle_data.close
        intraday_open_df = candle_data[
            (candle_data.date.dt.hour == 9) & (candle_data.date.dt.minute == 25) # Use minute 24 for indexFUT overnight close with minutely data
        ]

        intraday_open_df.loc[:, "next_day_intraday_open"] = intraday_open_df.groupby(
            ["symbol"]
        ).next_day_intraday_open.shift(-1)
        intraday_open_df.loc[:, "next_date"] = intraday_open_df.date.apply(
            lambda x: x.replace(hour=9, minute=15)
        ).shift(-1)
        new_columns_to_add = ["next_day_intraday_open", "next_date"]

        columns_to_drop = [a for a in new_columns_to_add if a in trades_df.columns]
        trades_df = trades_df.drop(columns_to_drop, axis=1)

        trades_df = pd.merge(
            trades_df,
            intraday_open_df[["symbol", "date_only"] + new_columns_to_add],
            how="left",
            left_on=["date_only", "symbol"],
            right_on=["date_only", "symbol"],
        )

        columns_to_drop = [a for a in new_columns_to_add if a in candle_data.columns]
        candle_data = candle_data.drop(columns_to_drop, axis=1)

        return trades_df

    @staticmethod
    def merge_weighted_close(trades_df, candle_data):
        candle_data.loc[:, "weighted_intraday_close"] = candle_data.close

        intraday_close = candle_data[
            (candle_data.date.dt.hour == 15) & (candle_data.date.dt.minute == 5)
        ]

        intraday_close_columns = ["weighted_intraday_close"]
        new_columns_to_add = intraday_close_columns

        columns_to_drop = [a for a in new_columns_to_add if a in trades_df.columns]
        trades_df = trades_df.drop(columns_to_drop, axis=1)

        trades_df = pd.merge(
            trades_df,
            intraday_close[["symbol", "date_only"] + intraday_close_columns],
            how="left",
            left_on=["date_only", "symbol"],
            right_on=["date_only", "symbol"],
        )

        columns_to_drop = [a for a in new_columns_to_add if a in candle_data.columns]
        candle_data = candle_data.drop(columns_to_drop, axis=1)

        return trades_df

    @staticmethod
    def add_tick_timestamp_for_trigger_orders(trades_df, candle_data):
        if "tick_timestamp" in trades_df:
            trades_df = trades_df.drop(["tick_timestamp"], axis=1)

        merge_on = ["symbol", "date_only"]

        candle_data = pd.merge(
            candle_data,
            trades_df[
                [
                    "symbol",
                    "trigger_price",
                    "date_only",
                    "trigger_order_tick_timstamp",
                    "transaction_type",
                ]
            ],
            how="left",
            left_on=merge_on,
            right_on=merge_on,
        )

        candle_data = candle_data[
            candle_data.date > candle_data.trigger_order_tick_timstamp
        ]

        candle_data = candle_data[
            (
                (candle_data.trigger_price > 0)
                & (
                    (
                        (candle_data.high >= candle_data.trigger_price)
                        & (candle_data.transaction_type == Order.buy)
                    )
                    | (
                        (candle_data.low <= candle_data.trigger_price)
                        & (candle_data.transaction_type == Order.sell)
                    )
                )
            )
            | (
                (candle_data.trigger_price < 0)
                & (
                    (
                        (candle_data.low <= abs(candle_data.trigger_price))
                        & (candle_data.transaction_type == Order.buy)
                    )
                    | (
                        (candle_data.high >= abs(candle_data.trigger_price))
                        & (candle_data.transaction_type == Order.sell)
                    )
                )
            )
        ]

        trades_df_copy = (
            candle_data.groupby(["symbol", "date_only"]).first().reset_index()
        )
        trades_df_copy.loc[:, "tick_timestamp"] = trades_df_copy.date

        trades_df_copy.loc[:, "time_diff_minutes"] = (
            trades_df_copy.tick_timestamp - trades_df_copy.trigger_order_tick_timstamp
        ) / pd.Timedelta(minutes=1)
        
        trades_df_copy = trades_df_copy[
            (trades_df_copy.trigger_price > 0)
            | (
                (trades_df_copy.trigger_price < 0)
                & (trades_df_copy.time_diff_minutes <= 300)
            )
        ]

        trades_df_copy.loc[:, "entry_price"] = np.where(
            (trades_df_copy.transaction_type == Order.buy)
            & (trades_df_copy.trigger_price > 0),
            np.maximum(trades_df_copy.low, trades_df_copy.trigger_price),
            np.minimum(trades_df_copy.high, trades_df_copy.trigger_price),
        )

        trades_df_copy.loc[:, "entry_price"] = np.where(
            (trades_df_copy.transaction_type == Order.buy)
            & (trades_df_copy.trigger_price < 0),
            np.minimum(trades_df_copy.high, abs(trades_df_copy.trigger_price)),
            np.maximum(trades_df_copy.low, abs(trades_df_copy.trigger_price)),
        )

        trades_df = trades_df.drop(["entry_price"], axis=1)

        trades_df = pd.merge(
            trades_df,
            trades_df_copy[["symbol", "date_only", "entry_price", "tick_timestamp"]],
            how="right",
            left_on=merge_on,
            right_on=merge_on,
        )

        return trades_df

    @staticmethod
    def evaluate_performance(
        trades_df, candle_data=None, is_fno=False, use_overnight_stoploss=False
    ):

        trades_df.loc[:, "entry_price"] = np.nan
        trades_df.loc[:, "high_from_now"] = np.nan

        if Order.trigger_price in trades_df.columns:
            temp_df = trades_df[trades_df.trigger_price.notnull()]
            assert len(temp_df) == len(trades_df)

            trades_df = Backtesting.add_tick_timestamp_for_trigger_orders(
                trades_df, candle_data
            )

        trades_df = Backtesting().merge_weighted_close(trades_df, candle_data)
        trades_df = Backtesting().merge_next_day_intraday_open(trades_df, candle_data)

        if use_overnight_stoploss:
            if "intraday_forward_low" in candle_data.columns:
                candle_data = candle_data[
                    Backtesting.required_columns + ["intraday_forward_low"]
                ]
            else:
                print(f"Adding intraday_forward_low in candle_data")
                candle_data = (
                    QuantplayAlphaFactory.add_intraday_forward_low_in_candle_data(
                        candle_data
                    )
                )
        else:
            candle_data = candle_data[Backtesting.required_columns]

        print("Evaluating performance ......")

        merge_columns = ["close", "intraday_forward_high"]

        if use_overnight_stoploss:
            merge_columns.append("intraday_forward_low")

        trades_df = DataUtils.midday_data_merge_v2(
            trades_df,
            candle_data,
            columns_to_retrieve=merge_columns,
        )

        if Order.trigger_price not in trades_df.columns:
            trades_df.loc[:, "entry_price"] = trades_df.tick_close

        # TODO put assert here
        print(
            "Number of NaN data points ..{}".format(trades_df.entry_price.isna().sum())
        )
        trades_df = trades_df[trades_df.entry_price > 0]

        trades_df.loc[:, Order.quantity] = trades_df.exposure / trades_df.entry_price
        trades_df.loc[:, Order.quantity] = trades_df.quantity.astype(int)

        trades_df.loc[:, "my_max_return"] = (
            trades_df.tick_intraday_forward_high / trades_df.entry_price - 1
        )

        trades_df.loc[:, "short_close_price"] = np.where(
            trades_df.my_max_return > trades_df.stoploss,
            (1 + trades_df.stoploss) * trades_df.entry_price,
            trades_df.weighted_intraday_close,
        )

        trades_df = Backtesting.get_close_price(trades_df)
        trades_df.loc[:, "close_price"] = np.where(
            trades_df.strategy_type == StrategyType.intraday,
            trades_df.short_close_price,
            trades_df.close_price,
        )
        
        if "take_profit" in trades_df.columns:
            trades_df.loc[:, "long_close_price"] = np.where(
                trades_df.my_max_return > trades_df.take_profit,
                (1 + trades_df.take_profit) * trades_df.entry_price,
                trades_df.close_price,
            )
            
            trades_df.loc[:, "close_price"] = np.where(
                trades_df.strategy_type == StrategyType.overnight,
                trades_df.long_close_price,
                trades_df.close_price,
            )
            
            

        if use_overnight_stoploss:
            trades_df.loc[:, "my_min_return"] = (
                trades_df.tick_intraday_forward_low / trades_df.entry_price - 1
            )
            trades_df.loc[:, "close_price"] = np.where(
                (trades_df.strategy_type == StrategyType.overnight)
                & (trades_df.my_min_return < -trades_df.stoploss),
                (1 - trades_df.stoploss) * trades_df.entry_price,
                trades_df.close_price,
            )

        trades_df = trades_df[trades_df.close_price > 0]

        if Order.trigger_price in trades_df.columns:
            trades_df.loc[:, "order_timestamp"] = trades_df.tick_timestamp
        else:
            trades_df.loc[:, "order_timestamp"] = trades_df.tick_timestamp.apply(
                lambda x: x + timedelta(minutes=5)
            )

        trades_df = trades_df[
            abs(trades_df.close_price / trades_df.entry_price - 1) < 0.45
        ]

        response = StrategyReport.create_report_by_df(trades_df)
        result = pd.DataFrame(response)
        print(
            result[
                [
                    "year",
                    "bps",
                    "monthly_pnl",
                    "max_drawdown",
                    "max_drawdown_days",
                    "sharpe_ratio",
                    "total_signals",
                    "total_trading_days",
                    "drawdown_pnl_ratio",
                    "success_ratio",
                    "exposure_90",
                ]
            ]
        )

        trades_df = StrategyReport.add_more_params(trades_df)

        return response, trades_df
