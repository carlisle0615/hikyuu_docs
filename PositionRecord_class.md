## PositionRecord

```python
class PositionRecord:
    """
    持仓记录
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Stock, arg1: Datetime, arg2: Datetime, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def buy_money(self) -> float:
        """
        累计买入资金（float）
        """
    @buy_money.setter
    def buy_money(self, arg0: float) -> None:
        ...
    @property
    def clean_datetime(self) -> Datetime:
        """
        平仓日期，当前持仓记录中为 constant.null_datetime
        """
    @clean_datetime.setter
    def clean_datetime(self, arg0: Datetime) -> None:
        ...
    @property
    def goal_price(self) -> float:
        """
        当前的目标价格（float）
        """
    @goal_price.setter
    def goal_price(self, arg0: float) -> None:
        ...
    @property
    def number(self) -> float:
        """
        当前持仓数量（float）
        """
    @number.setter
    def number(self, arg0: float) -> None:
        ...
    @property
    def sell_money(self) -> float:
        """
        累计卖出资金（float）
        """
    @sell_money.setter
    def sell_money(self, arg0: float) -> None:
        ...
    @property
    def stock(self) -> Stock:
        """
        交易对象（Stock）
        """
    @stock.setter
    def stock(self, arg0: Stock) -> None:
        ...
    @property
    def stoploss(self) -> float:
        """
        当前止损价（float）
        """
    @stoploss.setter
    def stoploss(self, arg0: float) -> None:
        ...
    @property
    def take_datetime(self) -> Datetime:
        """
        初次建仓时刻（Datetime）
        """
    @take_datetime.setter
    def take_datetime(self, arg0: Datetime) -> None:
        ...
    @property
    def total_cost(self) -> float:
        """
        累计交易总成本（float）
        """
    @total_cost.setter
    def total_cost(self, arg0: float) -> None:
        ...
    @property
    def total_number(self) -> float:
        """
        累计持仓数量（float）
        """
    @total_number.setter
    def total_number(self, arg0: float) -> None:
        ...
    @property
    def total_profit(self) -> float:
        """
        total_profit(self):
        
            累计盈利 = 累计卖出资金 - 累计买入资金 - 累计交易成本
            注意: 只对已清仓的记录有效, 未清仓的记录返回0  
        """
    @property
    def total_risk(self) -> float:
        """
        累计交易风险 = 各次 （买入价格-止损)*买入数量, 不包含交易成本
        """
    @total_risk.setter
    def total_risk(self, arg0: float) -> None:
        ...
```

