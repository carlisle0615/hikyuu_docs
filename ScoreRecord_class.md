## ScoreRecord

```python
class ScoreRecord:
    """
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Stock, arg1: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def stock(self) -> Stock:
        """
        证券
        """
    @stock.setter
    def stock(self, arg0: Stock) -> None:
        ...
    @property
    def value(self) -> float:
        """
        分值
        """
    @value.setter
    def value(self, arg0: float) -> None:
        ...
```

