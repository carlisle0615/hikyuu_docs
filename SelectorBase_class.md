## SelectorBase

```python
class SelectorBase:
    """
    选择器策略基类，实现标的、系统策略的评估和选取算法，自定义选择器策略子类接口：
    
        - get_selected - 【必须】获取指定时刻选择的系统实例列表
        - _calculate - 【必须】计算接口
        - _reset - 【可选】重置私有属性
        - _clone - 【必须】克隆接口
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __add__(self, arg0: SelectorBase) -> SelectorBase:
        ...
    @typing.overload
    def __add__(self, arg0: float) -> SelectorBase:
        ...
    def __and__(self, arg0: SelectorBase) -> SelectorBase:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: SelectorBase) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        """
        初始化构造函数
                
            :param str name: 名称
        """
    @typing.overload
    def __mul__(self, arg0: SelectorBase) -> SelectorBase:
        ...
    @typing.overload
    def __mul__(self, arg0: float) -> SelectorBase:
        ...
    def __or__(self, arg0: SelectorBase) -> SelectorBase:
        ...
    def __radd__(self, arg0: float) -> SelectorBase:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: float) -> SelectorBase:
        ...
    def __rsub__(self, arg0: float) -> SelectorBase:
        ...
    def __rtruediv__(self, arg0: float) -> SelectorBase:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def __sub__(self, arg0: SelectorBase) -> SelectorBase:
        ...
    @typing.overload
    def __sub__(self, arg0: float) -> SelectorBase:
        ...
    @typing.overload
    def __truediv__(self, arg0: SelectorBase) -> SelectorBase:
        ...
    @typing.overload
    def __truediv__(self, arg0: float) -> SelectorBase:
        ...
    def _calculate(self) -> None:
        """
        【重载接口】子类计算接口
        """
    def _reset(self) -> None:
        """
        子类复位操作实现
        """
    def add_stock(self, stock: Stock, sys: ...) -> None:
        """
        add_stock(self, stock, sys)
        
            加入初始标的及其对应的系统策略原型
        
            :param Stock stock: 加入的初始标的
            :param System sys: 系统策略原型
        """
    def add_stock_list(self, stk_list: typing.Sequence, sys: ...) -> None:
        """
        add_stock_list(self, stk_list, sys)
        
            加入初始标的列表及其系统策略原型
        
            :param StockList stk_list: 加入的初始标的列表
            :param System sys: 系统策略原型
        """
    def add_sys(self, arg0: ...) -> None:
        ...
    def add_sys_list(self, arg0: list[...]) -> None:
        ...
    def calculate(self, arg0: list[...], arg1: Query) -> None:
        ...
    def clone(self) -> SelectorBase:
        """
        克隆操作
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_proto_sys_list(self) -> list[...]:
        ...
    def get_real_sys_list(self) -> list[...]:
        ...
    def get_selected(self, arg0: Datetime) -> SystemWeightList:
        """
        get_selected(self, datetime)
        
            【重载接口】获取指定时刻选取的系统实例
        
            :param Datetime datetime: 指定时刻
            :return: 选取的系统实例列表
            :rtype: SystemList
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def is_match_af(self, arg0: ...) -> bool:
        """
        is_match_af(self)
        
            【重载接口】判断是否和 AF 匹配
        
            :param AllocateFundsBase af: 资产分配算法
        """
    def remove_all(self) -> None:
        """
        清除所有已加入的原型系统
        """
    def reset(self) -> None:
        """
        复位操作
        """
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        set_param(self, name, value)
        
            设置参数
        
            :param str name: 参数名称
            :param value: 参数值
            :raises logic_error: Unsupported type! 不支持的参数类型
        """
    @property
    def name(self) -> str:
        """
        算法名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def proto_sys_list(self) -> list[...]:
        """
        原型系统列表
        """
    @property
    def real_sys_list(self) -> list[...]:
        """
        由 PF 运行时设定的实际运行系统列表
        """
```

## 相关方法

#### SE_Fixed

```python
def SE_Fixed(weight: float = 1.0) -> SelectorBase:
    ...
```

#### SE_Fixed

```python
def SE_Fixed(stk_list: typing.Sequence, sys: ..., weight: float = 1.0) -> SelectorBase:
    """
    SE_Fixed([stk_list, sys])
    
        固定选择器，即始终选择初始划定的标的及其系统策略原型
    
        :param list stk_list: 初始划定的标的
        :param System sys: 系统策略原型
        :param float weight: 默认权重
        :return: SE选择器实例
    """
```

#### SE_MaxFundsOptimal

```python
def SE_MaxFundsOptimal() -> SelectorBase:
    """
    账户资产最大寻优选择器
    """
```

#### SE_MultiFactor

```python
def SE_MultiFactor(mf: ..., topn: int = 10) -> SelectorBase:
    ...
```

#### SE_MultiFactor

```python
def SE_MultiFactor(inds: typing.Sequence, topn: int = 10, ic_n: int = 5, ic_rolling_n: int = 120, ref_stk: typing.Any = None, spearman: bool = True, mode: str = 'MF_ICIRWeight') -> SelectorBase:
    """
    SE_MultiFactor
    
        创建基于多因子评分的选择器，两种创建方式
    
        - 直接指定 MF:
          :param MultiFactorBase mf: 直接指定的多因子合成算法
          :param int topn: 只选取时间截面中前 topn 个系统
    
        - 参数直接创建:
          :param sequense(Indicator) inds: 原始因子列表
          :param int topn: 只选取时间截面中前 topn 个系统，小于等于0时代表不限制
          :param int ic_n: 默认 IC 对应的 N 日收益率
          :param int ic_rolling_n: IC 滚动周期
          :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
          :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
          :param str mode: "MF_ICIRWeight" | "MF_ICWeight" | "MF_EqualWeight" 因子合成算法名称
    """
```

#### SE_PerformanceOptimal

```python
def SE_PerformanceOptimal(key: str = '帐户平均年收益率%', mode: int = 0) -> SelectorBase:
    """
    SE_PerformanceOptimal(key="帐户平均年收益率%", mode=0)
    
        使用 Performance 统计结果进行寻优的选择器
    
        :param string key: Performance 统计项
        :param int mode:  0 取统计结果最大的值系统 | 1 取统计结果为最小值的系统
    """
```

#### SE_Signal

```python
def SE_Signal() -> SelectorBase:
    ...
```

#### SE_Signal

```python
def SE_Signal(arg0: list[Stock], arg1: ...) -> SelectorBase:
    """
    SE_Signal([stk_list, sys])
    
        信号选择器，仅依靠系统买入信号进行选中
    
        :param list stk_list: 初始划定的标的
        :param System sys: 系统策略原型
        :return: SE选择器实例
    """
```

#### crtSEOptimal

```python
def crtSEOptimal(arg0: typing.Callable) -> SelectorBase:
    """
    crtSEOptimal(func)
        
        快速创建自定义绩效评估函数的寻优选择器
    
        :param func: 一个可调用对象，接收参数为 (sys, lastdate)，返回一个 float 数值
    """
```

