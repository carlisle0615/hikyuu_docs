## StrategyContext

```python
class StrategyContext:
    """
    策略上下文
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, stock_code_list = None):
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def empty(self) -> bool:
        """
        上下文证券代码列表是否为空
        """
    @property
    def ktype_list(self) -> list[str]:
        """
        需要的K线类型
        """
    @ktype_list.setter
    def ktype_list(self, arg1: list[str]) -> None:
        ...
    @property
    def preload_num(self) -> dict[str, int]:
        """
        预加载数量
        """
    @preload_num.setter
    def preload_num(self, arg1: dict[str, int]) -> None:
        ...
    @property
    def start_datetime(self) -> Datetime:
        """
        起始日期
        """
    @property
    def stock_list(self) -> list[str]:
        """
        股票代码列表
        """
    @stock_list.setter
    def stock_list(self, arg1: list[str]) -> None:
        ...
```

