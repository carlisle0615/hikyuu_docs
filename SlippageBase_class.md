## SlippageBase

```python
class SlippageBase:
    """
    移滑价差算法基类
    
    自定义移滑价差接口：
    
        - getRealBuyPrice : 【必须】计算实际买入价格
        - getRealSellPrice : 【必须】计算实际卖出价格
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
    def __init__(self, arg0: SlippageBase) -> None:
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
    def clone(self) -> SlippageBase:
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
    def get_real_buy_price(self, arg0: Datetime, arg1: float) -> float:
        """
        get_real_buy_price(self, datetime, price)
        
            【重载接口】计算实际买入价格
        
            :param Datetime datetime: 买入时间
            :param float price: 计划买入价格
            :return: 实际买入价格
            :rtype: float
        """
    def get_real_sell_price(self, arg0: Datetime, arg1: float) -> float:
        """
        get_real_sell_price(self, datetime, price)
        
            【重载接口】计算实际卖出价格
        
            :param Datetime datetime: 卖出时间
            :param float price: 计划卖出价格
            :return: 实际卖出价格
            :rtype: float
        """
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
    def to(self) -> KData:
        """
        关联交易对象
        """
    @to.setter
    def to(self, arg1: KData) -> None:
        ...
```

## 相关方法

#### SP_FixedPercent

```python
def SP_FixedPercent(p: float = 0.001) -> SlippageBase:
    """
    SP_FixedPercent([p=0.001])
    
        固定百分比移滑价差算法，买入实际价格 = 计划买入价格 * (1 + p)，卖出实际价格 = 计划卖出价格 * (1 - p)
    
        :param float p: 偏移的固定百分比
        :return: 移滑价差算法实例
    """
```

#### SP_FixedValue

```python
def SP_FixedValue(value: float = 0.01) -> SlippageBase:
    """
    SP_FixedValuet([p=0.001])
    
        固定价格移滑价差算法，买入实际价格 = 计划买入价格 + 偏移价格，卖出实际价格 = 计划卖出价格 - 偏移价格
    
        :param float p: 偏移价格
        :return: 移滑价差算法实例
    """
```

