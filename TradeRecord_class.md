## TradeRecord

```python
class TradeRecord:
    """
    交易记录
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
    def __init__(self, arg0: Stock, arg1: Datetime, arg2: BUSINESS, arg3: float, arg4: float, arg5: float, arg6: float, arg7: CostRecord, arg8: float, arg9: float, arg10: SystemPart) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def is_null(self) -> bool:
        ...
    @property
    def business(self) -> BUSINESS:
        """
        交易类型（BUSINESS）
        """
    @business.setter
    def business(self, arg0: BUSINESS) -> None:
        ...
    @property
    def cash(self) -> float:
        """
        现金余额（float）
        """
    @cash.setter
    def cash(self, arg0: float) -> None:
        ...
    @property
    def cost(self) -> CostRecord:
        """
        交易成本
        """
    @cost.setter
    def cost(self, arg0: CostRecord) -> None:
        ...
    @property
    def datetime(self) -> Datetime:
        """
         交易时间（Datetime）
        """
    @datetime.setter
    def datetime(self, arg0: Datetime) -> None:
        ...
    @property
    def goal_price(self) -> float:
        """
        目标价格（float），如果为0表示未限定目标
        """
    @goal_price.setter
    def goal_price(self, arg0: float) -> None:
        ...
    @property
    def number(self) -> float:
        """
        成交数量（float）
        """
    @number.setter
    def number(self, arg0: float) -> None:
        ...
    @property
    def part(self) -> SystemPart:
        """
        交易指示来源，区别是交易系统哪个部件发出的指示，参见： :py:class:`System.Part`
        """
    @part.setter
    def part(self, arg0: SystemPart) -> None:
        ...
    @property
    def plan_price(self) -> float:
        """
        计划交易价格（float）
        """
    @plan_price.setter
    def plan_price(self, arg0: float) -> None:
        ...
    @property
    def real_price(self) -> float:
        """
        实际交易价格（float）
        """
    @real_price.setter
    def real_price(self, arg0: float) -> None:
        ...
    @property
    def stock(self) -> Stock:
        """
        股票（Stock）
        """
    @stock.setter
    def stock(self, arg0: Stock) -> None:
        ...
    @property
    def stoploss(self) -> float:
        """
        止损价（float）
        """
    @stoploss.setter
    def stoploss(self, arg0: float) -> None:
        ...
```

