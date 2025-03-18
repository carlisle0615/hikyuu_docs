## ConditionBase

```python
class ConditionBase:
    """
    系统有效条件基类自定义系统有效条件接口：
    
        - _calculate : 【必须】子类计算接口
        - _clone : 【必须】克隆接口
        - _reset : 【可选】重载私有变量
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def plot(cn, new = True, axes = None, kdata = None, upcolor = 'red', downcolor = 'blue', alpha = 0.2):
        """
        绘制系统有效条件
        
            :param ConditionBase cn: 系统有效条件
            :param new: 仅在未指定axes的情况下生效，当为True时，创建新的窗口对象并在其中进行绘制
            :param axes: 指定在那个轴对象中进行绘制
            :param KData kdata: 指定的KData，如该值为None，则认为该系统有效条件已经
                                指定了交易对象，否则，使用该参数作为交易对象
            :param upcolor: 有效数时的颜色
            :param downcolor: 无效时的颜色
            :param alpha: 透明度
            
        """
    def __add__(self, arg0: ConditionBase) -> ConditionBase:
        ...
    def __and__(self, arg0: ConditionBase) -> ConditionBase:
        ...
    def __getitem__(self, arg0: int) -> float:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ConditionBase) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        """
        初始化构造函数
                
            :param str name: 名称
        """
    def __iter__(self):
        ...
    def __len__(self) -> int:
        ...
    def __mul__(self, arg0: ConditionBase) -> ConditionBase:
        ...
    def __or__(self, arg0: ConditionBase) -> ConditionBase:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __sub__(self, arg0: ConditionBase) -> ConditionBase:
        ...
    def __truediv__(self, arg0: ConditionBase) -> ConditionBase:
        ...
    def _add_valid(self, datetime: Datetime, value: float = 1.0) -> None:
        """
        _add_valid(self, datetime)
        
            加入有效时间，在_calculate中调用
        
            :param Datetime datetime: 有效时间
        """
    def _calculate(self) -> None:
        """
        【重载接口】子类计算接口
        """
    def _reset(self) -> None:
        """
        【重载接口】子类复位接口，复位内部私有变量
        """
    def clone(self) -> ConditionBase:
        """
        克隆操作
        """
    def get_datetime_list(self) -> DatetimeList:
        """
        get_datetime_list(self)
            
            获取系统有效的日期。注意仅返回系统有效的日期列表，和交易对象不等长
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_values(self) -> Indicator:
        """
        get_values(self)
                   
            以指标的形式获取实际值，与交易对象等长，0表示无效，1表示系统有效
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def is_valid(self, arg0: Datetime) -> bool:
        """
        is_valid(self, datetime)
        
            指定时间系统是否有效
        
            :param Datetime datetime: 指定时间
            :return: True 有效 | False 无效
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
        名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def sg(self) -> ...:
        """
        设置或获取交易信号指示器
        """
    @sg.setter
    def sg(self, arg1: ...) -> None:
        ...
    @property
    def tm(self) -> TradeManager:
        """
        设置或获取交易管理账户
        """
    @tm.setter
    def tm(self, arg1: TradeManager) -> None:
        ...
    @property
    def to(self) -> KData:
        """
        设置或获取交易对象
        """
    @to.setter
    def to(self, arg1: KData) -> None:
        ...
```

## 相关方法

### 与ConditionBase相关的方法

#### CN_Bool

```python
def CN_Bool(arg0: Indicator) -> ConditionBase:
    """
    CN_Bool(ind)
    
        布尔信号指标系统有效条件, 指标中相应位置>0则代表系统有效，否则无效
    
        :param Indicator ind: bool型指标，输入为 KData
        :return: 系统有效条件实例
        :rtype: ConditionBase
    """
```

#### CN_OPLine

```python
def CN_OPLine(arg0: Indicator) -> ConditionBase:
    """
    CN_OPLine(ind)
    
        固定使用股票最小交易量进行交易，计算权益曲线的ind值，当权益曲线高于ind时，系统有效，否则无效。
    
        :param Indicator ind: Indicator实例
        :return: 系统有效条件实例
        :rtype: ConditionBase
    """
```

