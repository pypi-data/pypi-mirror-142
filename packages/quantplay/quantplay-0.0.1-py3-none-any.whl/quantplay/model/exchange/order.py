from quantplay.utils.constant import Product, OrderType, OrderVariety, Order, ExchangeName
import pandas as pd
 

class ExchangeOrder:
    
    @staticmethod
    def round_to_tick(number):
        return round(number * 20) / 20
    
    @staticmethod
    def get_exchange_orders(trades, oms_version=1, orderType=OrderType.limit, product=Product.mis, variety=OrderVariety.regular, exchange=ExchangeName.nse, is_long=False):
        all_trades = []
        for trade in trades:
            all_trades.append(ExchangeOrder(trade, oms_version=oms_version, orderType=orderType, product=product, variety=variety, exchange=exchange, is_long=is_long))
        return all_trades
        
    def __init__(self, trade, oms_version=1, orderType=OrderType.limit, product=Product.mis, variety=OrderVariety.regular, exchange=ExchangeName.nse, is_long=False):
    
        self.orderType = str(orderType)
        self.product = str(product)
        self.variety = str(variety)
        self.exchange = exchange
        self.oms_version = oms_version
        
        #TODO P0 remove these once check is removed from oms
        self.trade_amount = trade["exposure"]
        
        if "tag" in trade:
            self.tag = str(trade["tag"])
        else:
            raise Exception("Tag should be present in trade but not found. Trade: {}".format(trade))
        
        if "quantity" in trade:
            self.quantity = abs(int(trade["quantity"]))
            if not is_long:
                self.quantity = -self.quantity
        else:
            raise Exception("Quantity should be present in trade but not found. Trade: {}".format(trade))
        
        if "symbol" in trade:
            self.tradingsymbol = str(trade["symbol"])
        else:
            raise Exception("Symbol should be present in trade but not found. Trade: {}".format(trade))
        
        if "price" in trade:
            self.price = ExchangeOrder.round_to_tick(float(trade["price"]))
        else:
            raise Exception("Price should be present in trade but not found. Trade: {}".format(trade))

        if "stoploss" in trade:
            self.stoploss = ExchangeOrder.round_to_tick(float(self.price * trade["stoploss"]))
        else:
            self.stoploss = None

        if "squareoff" in trade:
            self.squareoff = ExchangeOrder.round_to_tick(float(self.price * 0.3))
        else:
            self.squareoff = None
            
        if "strategy_type" in trade:
            self.strategy_type = trade["strategy_type"]
            if trade["strategy_type"] == "overnight":
                self.place_without_stoploss = True
        else:
            raise Exception("strategy_type should be present in trade but not found. Trade: {}".format(trade))

        if "trigger_price" in trade:
            self.trigger_price = ExchangeOrder.round_to_tick(float(trade["trigger_price"]))
        
        if "order_timestamp" in trade:
            self.order_timestamp = trade["order_timestamp"]
            
            
        if "lot_size" in trade and not pd.isna(trade["lot_size"]):
            self.lot_size = trade["lot_size"]
            
