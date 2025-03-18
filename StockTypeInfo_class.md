## StockTypeInfo

```python
class StockTypeInfo:
    """
    股票类型详情记录
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
    def __init__(self, arg0: int, arg1: str, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def description(self) -> str:
        """
        描述信息
        """
    @property
    def max_trade_num(self) -> float:
        """
        每笔最大交易量
        """
    @property
    def min_trade_num(self) -> float:
        """
        每笔最小交易量
        """
    @property
    def precision(self) -> int:
        """
        价格精度
        """
    @property
    def tick(self) -> float:
        """
        最小跳动量
        """
    @property
    def tick_value(self) -> float:
        """
        每一个tick价格
        """
    @property
    def type(self) -> int:
        """
        证券类型
        """
    @property
    def unit(self) -> float:
        """
        每最小变动量价格，即单位价格 = tick_value/tick
        """
```

