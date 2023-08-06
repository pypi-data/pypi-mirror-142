from quantplay.utils.data_utils import DataUtils
import requests
import json
from quantplay.utils.config_util import QuantplayConfig
import pandas as pd
from quantplay.exception.exceptions import AccessDeniedException

class Market:
    GET_SYMBOLS_URL = 'https://7tpcay1yyk.execute-api.ap-south-1.amazonaws.com/prod/get_symbols'
    EXPIRY_DATA_URL = ' https://7tpcay1yyk.execute-api.ap-south-1.amazonaws.com/prod/nearest_expiry'
    
    def __init__(self):
        pass

    def get_expiry_data(self):
        credentials = QuantplayConfig.get_credentials()
        if 'DEFAULT' not in credentials or 'access_token' not in credentials['DEFAULT']:
            raise AccessDeniedException("Access Denied, please signin using [quantplay user signin]")

        access_token = credentials['DEFAULT']['access_token']
        input = {
            "access_token" : access_token
        }

        x = requests.post(Market.EXPIRY_DATA_URL, data=json.dumps(input))
        data = json.loads(x.text)

        return pd.DataFrame(data)

    def add_expiry(self, data):
        columns_to_be_added = ['expiry_date', 'strike_spread']

        for column in columns_to_be_added:
            if column in data.columns:
                data = data.drop([column], axis=1)

        expiry_data = self.get_expiry_data()

        data.loc[:, 'date_only'] = data.date.dt.date

        data.loc[:, 'date_only'] = pd.to_datetime(data.date.dt.date)
        expiry_data.loc[:, 'date_only'] = pd.to_datetime(expiry_data.date)

        expiry_data.loc['symbol'] = expiry_data['symbol'].replace(['NIFTY'], 'NIFTY 50')
        expiry_data.loc['symbol'] = expiry_data['symbol'].replace(['BANKNIFTY'], 'NIFTY BANK')
        expiry_data.loc['symbol'] = expiry_data['symbol'].replace(['FINNIFTY'], 'NIFTY FIN SERVICE')

        data = pd.merge(data, expiry_data[['date_only', 'symbol', 'expiry_date', 'strike_spread']],
                        how='left',
                        left_on=['symbol', 'date_only'],
                        right_on=['symbol', 'date_only'])
        return data


    def symbols(self, universe=None):
        input = {}
        if universe != None:
            input['universe'] = universe
        
        x = requests.post(Market.GET_SYMBOLS_URL, data = json.dumps(input))
        return json.loads(x.text)
        
    def equity_data(self, interval=None, symbols=None):
        return DataUtils.load_data_using_pandas(stocks=symbols, interval=interval, path='/NSE_EQ/')

    def options_data(self, interval=None, symbols=None):
        return DataUtils.load_data_using_pandas(stocks=symbols, interval=interval, path='/NSE_OPT/')

    def future_data(self, interval=None, symbols=None):
        return DataUtils.load_data_using_pandas(stocks=symbols, interval=interval, path='/NSE_FUT/')
        
    def get_trades(self, data, minute=None, hour=None):
        return data[(data.date.dt.minute == minute) & (data.date.dt.hour == hour)]