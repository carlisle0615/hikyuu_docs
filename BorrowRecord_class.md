## BorrowRecord

```python
class BorrowRecord:
    """
    记录当前借入的股票信息
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
    def __init__(self, arg0: Stock, arg1: float, arg2: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def number(self) -> float:
        """
        借入总数量
        """
    @number.setter
    def number(self, arg0: float) -> None:
        ...
    @property
    def stock(self) -> Stock:
        """
        借入的证券
        """
    @stock.setter
    def stock(self, arg0: Stock) -> None:
        ...
    @property
    def value(self) -> float:
        """
        借入总价值
        """
    @value.setter
    def value(self, arg0: float) -> None:
        ...
```

