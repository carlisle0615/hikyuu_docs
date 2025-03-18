## BrokerPositionRecord

```python
class BrokerPositionRecord:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Stock, arg1: float, arg2: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def money(self) -> float:
        """
        买入花费总资金
        """
    @money.setter
    def money(self, arg0: float) -> None:
        ...
    @property
    def number(self) -> float:
        """
        持仓数量
        """
    @number.setter
    def number(self, arg0: float) -> None:
        ...
    @property
    def stock(self) -> Stock:
        """
        持仓对象
        """
    @stock.setter
    def stock(self, arg0: Stock) -> None:
        ...
```

