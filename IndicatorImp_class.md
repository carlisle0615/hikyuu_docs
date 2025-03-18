## IndicatorImp

```python
class IndicatorImp:
    """
    指标实现类，定义新指标时，应从此类继承
        
        子类需实现以下接口：
    
            - _clone() -> IndicatorImp
            - _calculate(ind) ：指标计算
            - isNeedContext(bool) ：是否依赖上下文
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
    def __init__(self, arg0: str) -> None:
        """
            :param str name: 指标名称
        """
    @typing.overload
    def __init__(self, arg0: str, arg1: int) -> None:
        """
            :param str name: 指标名称
            :param int result_num: 指标结果集数量
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def _calculate(self, arg0: Indicator) -> None:
        ...
    def _dyn_calculate(self, arg0: Indicator) -> None:
        ...
    def _dyn_run_one_step(self, arg0: Indicator, arg1: int, arg2: int) -> None:
        ...
    def _ready_buffer(self, arg0: int, arg1: int) -> None:
        ...
    def _set(self, val: float, pos: int, num: int = 0) -> None:
        ...
    def calculate(self) -> Indicator:
        ...
    def clone(self) -> IndicatorImp:
        ...
    def get_ind_param(self, arg0: str) -> ...:
        ...
    def get_param(self, arg0: str) -> any:
        ...
    def get_parameter(self) -> Parameter:
        """
        获取内部参数类对象
        """
    def get_result_as_price_list(self, arg0: int) -> list[float]:
        ...
    def get_result_num(self) -> int:
        ...
    def have_ind_param(self, arg0: str) -> bool:
        ...
    def have_param(self, arg0: str) -> bool:
        ...
    def is_leaf(self) -> bool:
        ...
    def is_need_context(self) -> bool:
        ...
    def is_serial(self) -> bool:
        ...
    def set_discard(self, arg0: int) -> None:
        ...
    @typing.overload
    def set_ind_param(self, arg0: str, arg1: Indicator) -> None:
        ...
    @typing.overload
    def set_ind_param(self, arg0: str, arg1: ...) -> None:
        ...
    def set_param(self, arg0: str, arg1: any) -> None:
        ...
    def support_ind_param(self) -> bool:
        ...
    @property
    def discard(self) -> int:
        """
        结果中需抛弃的个数
        """
    @property
    def name(self) -> str:
        """
        指标名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
```

