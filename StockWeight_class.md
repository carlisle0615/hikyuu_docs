## StockWeight

```python
class StockWeight:
    """
    权息记录
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
    def __init__(self, arg0: Datetime) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Datetime, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def bonus(self) -> float:
        """
        每10股红利
        """
    @property
    def count_as_gift(self) -> float:
        """
        每10股送X股
        """
    @property
    def count_for_sell(self) -> float:
        """
        每10股配X股
        """
    @property
    def datetime(self) -> Datetime:
        """
        权息日期
        """
    @property
    def free_count(self) -> float:
        """
        流通股（万股）
        """
    @property
    def increasement(self) -> float:
        """
        每10股转增X股
        """
    @property
    def price_for_sell(self) -> float:
        """
        配股价
        """
    @property
    def suogu(self) -> float:
        """
        扩缩股比例
        """
    @property
    def total_count(self) -> float:
        """
        总股本（万股）
        """
```

