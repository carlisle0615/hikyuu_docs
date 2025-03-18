## TransRecord

```python
class TransRecord:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: TransRecord) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Datetime, arg1: float, arg2: float, arg3: ...) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def date(self) -> Datetime:
        """
        时间
        """
    @date.setter
    def date(self, arg0: Datetime) -> None:
        ...
    @property
    def direct(self) -> ...:
        """
        买卖盘性质, 参见: TransRecord.DIRECT
        """
    @direct.setter
    def direct(self, arg0: ...) -> None:
        ...
    @property
    def price(self) -> float:
        """
        价格
        """
    @price.setter
    def price(self, arg0: float) -> None:
        ...
    @property
    def vol(self) -> float:
        """
        成交量
        """
    @vol.setter
    def vol(self, arg0: float) -> None:
        ...
```

