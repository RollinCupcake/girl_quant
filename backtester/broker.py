import os
import itertools
import numpy as np
import pandas as pd
import collections

from .strategy import BarData, BaseStrategy

class Broker():
    def __init__(self):
        # 策略实例
        self.strategy_instance = None
        # 手续费
        self.commission = 2/1000
        # 杠杆比例，默认使用杠杆
        self.leverage = 1.0
        # 设置滑点率
        self.slipper_rate= 5/10000
        # 购买的资产的估值，作为计算爆仓的时候使用
        self.asset_value = 0
        # 最低保证金比例
        self.min_margin_rate= 0.15
        # 初始本金
        self.cash = 1_000_000

        self.strategy_class = None

        # 交易的数据
        self.trades = []

        # 当前提交的订单
        self.active_oders = []

        # 回测的数据
        self.backtest_data = None

        self.pos = 0 # 当前的持仓量

        # 是否是运行策略的优化的方法
        self.is_optimizing_strategy = False

        # 用于统计策略的优化的参数
        self.optStrategies = []

    def set_strategy(self,strategy_class:BaseStrategy):
        self.strategy_class = strategy_class
    
    def set_leverage(self, leverage:float):
        self.leverage = leverage

    def set_commission(self, commission:float):
        self.commission = commission
    
    def set_backtest_data(self, data:pd.DataFrame):
        self.backtest_data = data
    
    def run(self):

        self.trades = []
        self.strategy_instance = self.strategy_class(self.backtest_data)
        self.strategy_instance.broker = self
        self.strategy_instance.on_start()

        for index,candle in self.backtest_data.iteritems():
            bar = BarData(candle['open_time'],candle['open'],
                        candle['high'],candle['low'],candle['close'],cacndle['volume'])

            self.check_order(bar)
            self.strategy_instance.next_bar(bar)
        
        self.strategy_instance.on_stop()
        self.calculate()

    def calculate(self):
        for trade n self.trades:
            


