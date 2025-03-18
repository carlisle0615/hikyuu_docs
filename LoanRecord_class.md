## LoanRecord

```python
class LoanRecord:
    """
    借款记录（融资记录）
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
    def __init__(self, arg0: Datetime, arg1: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def datetime(self) -> Datetime:
        """
        借款时间
        """
    @datetime.setter
    def datetime(self, arg0: Datetime) -> None:
        ...
    @property
    def value(self) -> float:
        """
        借款金额
        """
    @value.setter
    def value(self, arg0: float) -> None:
        ...
```

