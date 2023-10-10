import numpy as np
import pandas as pd

class Analysis:
    def __init__(self, homedir):
        self.homedir=homedir

    def readyahoo(self, sym):
        symobj=pd.read_csv(self.homedir + '/' + sym + '.csv',skiprows=0) 
        symobj=symobj.rename(columns={"Date":"time","Open":"open","Close":"close","High":"high","Low":"low","Adj Close":"adjclose","Volume":"volume"})
        symobj.time=pd.to_datetime(symobj.time + ' 08:59:59')
        symobj.index=symobj.time
        symobj=symobj.dropna()
        symobj['sma10']=symobj.rolling(10).adjclose.mean()
        symobj['sma20']=symobj.rolling(20).adjclose.mean()
        symobj['sma50']=symobj.rolling(50).adjclose.mean()
        return symobj
