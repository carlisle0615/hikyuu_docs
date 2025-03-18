## EnvironmentBase

```python
class EnvironmentBase:
    """
    市场环境判定策略基类
    
    自定义市场环境判定策略接口：
    
        - _calculate : 【必须】子类计算接口
        - _clone : 【必须】克隆接口
        - _reset : 【可选】重载私有变量
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def plot(ev, ref_kdata, new = True, axes = None, upcolor = 'red', downcolor = 'blue', alpha = 0.2):
        """
        绘制市场有效判断
        
            :param EnvironmentBase cn: 系统有效条件
            :param KData ref_kdata: 用于日期参考
            :param new: 仅在未指定axes的情况下生效，当为True时，创建新的窗口对象并在其中进行绘制
            :param axes: 指定在那个轴对象中进行绘制
            :param upcolor: 有效时的颜色
            :param downcolor: 无效时的颜色
            :param alpha: 透明度
            
        """
    def __add__(self, arg0: EnvironmentBase) -> EnvironmentBase:
        ...
    def __and__(self, arg0: EnvironmentBase) -> EnvironmentBase:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: EnvironmentBase) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    def __mul__(self, arg0: EnvironmentBase) -> EnvironmentBase:
        ...
    def __or__(self, arg0: EnvironmentBase) -> EnvironmentBase:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __sub__(self, arg0: EnvironmentBase) -> EnvironmentBase:
        ...
    def __truediv__(self, arg0: EnvironmentBase) -> EnvironmentBase:
        ...
    def _add_valid(self, arg0: Datetime, arg1: float) -> None:
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
        【重载接口】子类复位接口，用于复位内部私有变量
        """
    def clone(self) -> EnvironmentBase:
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
    def query(self) -> Query:
        """
        设置或获取查询条件
        """
    @query.setter
    def query(self, arg1: Query) -> None:
        ...
```

## 相关方法

### 与EnvironmentBase相关的方法

#### EV_Bool

```python
def EV_Bool(ind: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_Bool(ind, market='SH')
    
        布尔信号指标市场环境
    
        :param Indicator ind: bool类型的指标，指标中相应位置>0则代表市场有效，否则无效
        :param str market: 指定的市场，用于获取相应的交易日历
    """
```

#### EV_TwoLine

```python
def EV_TwoLine(fast: Indicator, slow: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_TwoLine(fast, slow[, market = 'SH'])
    
        快慢线判断策略，市场指数的快线大于慢线时，市场有效，否则无效。
    
        :param Indicator fast: 快线指标
        :param Indicator slow: 慢线指标
        :param string market: 市场名称
    """
```

