
import numpy as np
import pandas as pd
from .data import BarData


class BaseStrategy():

    broker = None
    data = None

    def __init__(self,data:pd.DataFrame):
        super().__init__()
        self.data = data
    
    def on_start(self):

    def on_stop(self):

    def next_bar(self, bar:BarData)
        raise NotImplementedError("请在子类中实现该方法")
    
    def buy(self, price, volume):
        self.broker.buy(price, volume)

    def sell(self, price, volume):
        self.broker.short(price, volume)

    def cover(self, price, volume):
        """
        平仓
        """
        self.cover(price, volume)


    