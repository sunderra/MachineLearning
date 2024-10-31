'''
Created on 23 Sept 2024

@author: sunde
'''
import datetime
import pytz
import MetaTrader5 as mt5
import pandas as pd
import numpy as np

frame_M15 = mt5.TIMEFRAME_M15   # 15 min time frame
frame_M30 = mt5.TIMEFRAME_M30   # 30 min time frame
frame_H1 = mt5.TIMEFRAME_H1   # hourly time frame
frame_H4 = mt5.TIMEFRAME_H4   # 4-hour time frame
frame_D1 = mt5.TIMEFRAME_D1   # daily time frame
frame_W1 = mt5.TIMEFRAME_W1   # weekly time frame
frame_M1 = mt5.TIMEFRAME_M1   # monthly time frame

now = datetime.datetime.now()

assets = ['EURUSD','USDCHF','GBPUSD','USDCAD']

# time-frame is frquency of data hourly daily etc
def get_quotes(time_frame, year=2005, month=1, day=1, asset='EUUSD'):
    
    if not mt5.initialize():
        print("Initialize failed, error code = ", mt5.last_error())
        quit()
        
    timezone = pytz.timezone("Europe/Paris")
    time_from = datetime.datetime(year,month,day,tzinfo=timezone)
    time_to   = datetime.datetime.now(timezone) + datetime.timedelta(days=1)
    rates     = mt5.copy_rates_range(asset,time_frame,time_from, time_to)
    rates_frame = pd.DataFrame(rates)
    #print(rates_frame)
    return rates_frame

def mass_import(asset,time_frame):
    if time_frame == 'H1':
        data = get_quotes(frame_H1,2014,1,1,asset = assets[asset])
        data = data.iloc[:,1:5]
        data = data.round(decimals=5)
        return data
        
eurusd_data = mass_import(0,'H1')
print(eurusd_data.tail(20))     
        
