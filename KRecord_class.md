## KRecord

```python
class KRecord:
    """
    K线记录，组成K线数据，属性可读写
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: KRecord) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Datetime) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Datetime, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> None:
        ...
    def __ne__(self, arg0: KRecord) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def amount(self) -> float:
        """
        成交金额
        """
    @amount.setter
    def amount(self, arg0: float) -> None:
        ...
    @property
    def close(self) -> float:
        """
        收盘价
        """
    @close.setter
    def close(self, arg0: float) -> None:
        ...
    @property
    def datetime(self) -> Datetime:
        """
        时间
        """
    @datetime.setter
    def datetime(self, arg0: Datetime) -> None:
        ...
    @property
    def high(self) -> float:
        """
        最高价
        """
    @high.setter
    def high(self, arg0: float) -> None:
        ...
    @property
    def low(self) -> float:
        """
        最低价
        """
    @low.setter
    def low(self, arg0: float) -> None:
        ...
    @property
    def open(self) -> float:
        """
        开盘价
        """
    @open.setter
    def open(self, arg0: float) -> None:
        ...
    @property
    def volume(self) -> float:
        """
        成交量
        """
    @volume.setter
    def volume(self, arg0: float) -> None:
        ...
```

