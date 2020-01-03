

from backtest_rollin.backtester import Broker, BaseStrategy, BarData, Array_Manager
import pandas as pd

class DemoStrategy(BaseStrategy):

    params = {'long_period':110, 'short_period':70}

    def __init__(self, data):
        super().__init__(data)
        self.am = Array_Manager() #计算产生的信号

    def on_start(self):
        print("策略开始运行")

    def on_stop(self):
        print("策略停止运行")
    
    def next_bar(self, bar:BarData):
        """
        这里是核心
        整个策略都在这里实现
        """
        print(bar)
        self.am.update_bar(bar)
        if not self.am.inited:
            return
        
        #计算技术指标。。产生交易信号

        if True:
            self.buy(bar.close_price, 1)
        else:
            self.sell(bar.close_price, 1)


def get_data():
    return data
if __name__ == "__main__":
    data = get_data()
    
    broker = Broker()
    broker.set_strategy(DemoStrategy)
    broker.set_leverage(1.0)
    broker.set_cash(1_000_000)
    broker.set_backtest_data(data)
    broker.run()    
