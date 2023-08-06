import requests
import datetime
import pandas as pd


import requests
import datetime
import pandas as pd

class utilities: 
    
    def __init__(self, email):
        self.email = email
        self.url = "http://historical.maticalgos.com"
        self.check_login = False
    
    def get_expiry_kite(self):
    try:
        df_inst = pd.read_csv("https://api.kite.trade/instruments")
        df = df_inst[df_inst['segment'] == "NFO-OPT"]
        df = df[df['tradingsymbol'].str.startswith("{}".format("BANKNIFTY"))]
        df['expiry'] = pd.to_datetime(df['expiry'])

        expirylist = list(set(df[['tradingsymbol', 'expiry']].sort_values(
            by=['expiry'])['expiry'].values))
        expirylist = np.array([np.datetime64(x, 'D') for x in expirylist])
        expirylist = np.sort(expirylist)
        today = np.datetime64('today', 'D') + np.timedelta64(0, 'D')
        expirylist = expirylist[expirylist >= today]
        expiry_index = 0
        next_expiry = expirylist[expiry_index]
        next_expiry = pd.to_datetime(str(next_expiry))

        return date(next_expiry.year, next_expiry.month, next_expiry.day)
    except:
        return None
