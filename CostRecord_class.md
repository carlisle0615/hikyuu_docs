## CostRecord

```python
class CostRecord:
    """
    成本记录
        
        总成本 = 佣金 + 印花税 + 过户费 + 其他费用
        
        该结构主要用于存放成本记录结果，一般当做struct直接使用，
        该类本身不对总成本进行计算，也不保证上面的公式成立
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: CostRecord) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, commission: float, stamptax: float, transferfee: float, others: float, total: float) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def commission(self) -> float:
        """
        佣金
        """
    @commission.setter
    def commission(self, arg0: float) -> None:
        ...
    @property
    def others(self) -> float:
        """
        其他费用
        """
    @others.setter
    def others(self, arg0: float) -> None:
        ...
    @property
    def stamptax(self) -> float:
        """
        印花税
        """
    @stamptax.setter
    def stamptax(self, arg0: float) -> None:
        ...
    @property
    def total(self) -> float:
        """
        总成本(float)，= 佣金 + 印花税 + 过户费 + 其它费用
        """
    @total.setter
    def total(self, arg0: float) -> None:
        ...
    @property
    def transferfee(self) -> float:
        """
        过户费
        """
    @transferfee.setter
    def transferfee(self, arg0: float) -> None:
        ...
```

