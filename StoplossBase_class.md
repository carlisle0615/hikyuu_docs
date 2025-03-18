## StoplossBase

```python
class StoplossBase:
    """
    止损/止赢算法基类
    自定义止损/止赢策略接口：
    
        - _calculate : 【必须】子类计算接口
        - _clone : 【必须】克隆接口
        - _reset : 【可选】重载私有变量
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
    def __init__(self, arg0: StoplossBase) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        """
        初始化构造函数
                
            :param str name: 名称
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def _calculate(self) -> None:
        """
        【重载接口】子类计算接口
        """
    def _reset(self) -> None:
        """
        【重载接口】子类复位接口，复位内部私有变量
        """
    def clone(self) -> StoplossBase:
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
    def get_price(self, arg0: Datetime, arg1: float) -> float:
        """
        get_price(self, datetime, price)
        
            【重载接口】获取本次预期交易（买入）时的计划止损价格，如果不存在止损价，则返回0。用于系统在交易执行前向止损策略模块查询本次交易的计划止损价。
        
            .. note::
                一般情况下，止损/止赢的算法可以互换，但止损的getPrice可以传入计划交易的价格，比如以买入价格的30%做为止损。而止赢则不考虑传入的price参数，即认为price为0.0。实际上，即使止损也不建议使用price参数，如可以使用前日最低价的30%作为止损，则不需要考虑price参数。
        
            :param Datetime datetime: 交易时间
            :param float price: 计划买入的价格
            :return: 止损价格
            :rtype: float
        """
    def get_short_price(self, arg0: Datetime, arg1: float) -> float:
        ...
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
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
    def tm(self) -> TradeManager:
        """
        关联交易管理实例
        """
    @tm.setter
    def tm(self, arg1: TradeManager) -> None:
        ...
    @property
    def to(self) -> KData:
        """
        关联交易对象
        """
    @to.setter
    def to(self, arg1: KData) -> None:
        ...
```

## 相关方法

#### ST_FixedPercent

```python
def ST_FixedPercent(p: float = 0.03) -> StoplossBase:
    """
    ST_FixedPercent([p=0.03])
    
        固定百分比止损策略，即当价格低于买入价格的某一百分比时止损
    
        :param float p: 百分比(0,1]
        :return: 止损/止赢策略实例
    """
```

#### ST_Indicator

```python
def ST_Indicator(ind: Indicator) -> StoplossBase:
    """
    ST_Indicator(ind)
    
        使用技术指标作为止损价。如使用10日EMA作为止损：::
    
            ST_Indicator(EMA(CLOSE(), n=10))
    
        :param Indicator ind:
        :return: 止损/止赢策略实例
    """
```

#### ST_Saftyloss

```python
def ST_Saftyloss(n1: int = 10, n2: int = 3, p: float = 2.0) -> StoplossBase:
    """
    ST_Saftyloss([n1=10, n2=3, p=2.0])
    
        参见《走进我的交易室》（2007年 地震出版社） 亚历山大.艾尔德(Alexander Elder) P202
        计算说明：在回溯周期内（一般为10到20天），将所有向下穿越的长度相加除以向下穿越的次数，
        得到噪音均值（即回溯期内所有最低价低于前一日最低价的长度除以次数），并用今日
        最低价减去（前日噪音均值乘以一个倍数）得到该止损线。为了抵消波动并且保证止损线的
        上移，在上述结果的基础上再取起N日（一般为3天）内的最高值
    
        :param int n1: 计算平均噪音的回溯时间窗口，默认为10天
        :param int n2: 对初步止损线去n2日内的最高值，默认为3
        :param double p: 噪音系数，默认为2
        :return: 止损/止赢策略实例
    """
```

