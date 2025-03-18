## SystemWeight

```python
class SystemWeight:
    """
    系统权重系数结构，在资产分配时，指定对应系统的资产占比系数
    """
    weight: float
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ..., arg1: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def sys(self) -> ...:
        """
        对应的 System 实例
        """
    @sys.setter
    def sys(self, arg0: ...) -> None:
        ...
```

