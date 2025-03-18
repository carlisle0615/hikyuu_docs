## ProfitGoalBase

```python
class ProfitGoalBase:
    """
    盈利目标策略基类
        
    自定义盈利目标策略接口：
    
    - getGoal : 【必须】获取目标价格
    - _calculate : 【必须】子类计算接口
    - _clone : 【必须】克隆接口
    - _reset : 【可选】重载私有变量
    - buyNotify : 【可选】接收实际买入通知，预留用于多次增减仓处理
    - sellNotify : 【可选】接收实际卖出通知，预留用于多次增减仓处理
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
    def __init__(self, arg0: ProfitGoalBase) -> None:
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
    def buy_notify(self, arg0: TradeRecord) -> None:
        """
        buy_notify(self, trade_record)
            
            【重载接口】交易系统发生实际买入操作时，通知交易变化情况，一般存在多次增减仓的情况才需要重载
        
            :param TradeRecord trade_record: 发生实际买入时的实际买入交易记录
        """
    def clone(self) -> ProfitGoalBase:
        """
        克隆操作
        """
    def get_goal(self, arg0: Datetime, arg1: float) -> float:
        """
        get_goal(self, datetime, price)
        
            【重载接口】获取盈利目标价格，返回constant.null_price时，表示未限定目标；返回0意味着需要卖出
        
            :param Datetime datetime: 买入时间
            :param float price: 买入价格
            :return: 目标价格
            :rtype: float
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
    def reset(self) -> None:
        """
        复位操作
        """
    def sell_notify(self, arg0: TradeRecord) -> None:
        """
        sell_notify(self, trade_record)
            
            【重载接口】交易系统发生实际卖出操作时，通知实际交易变化情况，一般存在多次增减仓的情况才需要重载
                
            :param TradeRecord trade_record: 发生实际卖出时的实际卖出交易记录
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

#### PG_FixedHoldDays

```python
def PG_FixedHoldDays(days: int = 5) -> ProfitGoalBase:
    """
    PG_FixedHoldDays([days=5])
    
        固定持仓天数盈利目标策略
        
        :param int days: 允许持仓天数（按交易日算）,默认5天
        :return: 盈利目标策略实例
    """
```

#### PG_FixedPercent

```python
def PG_FixedPercent(p: float = 0.2) -> ProfitGoalBase:
    """
    PG_FixedPercent([p = 0.2])
    
        固定百分比盈利目标，目标价格 = 买入价格 * (1 + p)
        
        :param float p: 百分比
        :return: 盈利目标策略实例
    """
```

#### PG_NoGoal

```python
def PG_NoGoal() -> ProfitGoalBase:
    """
    PG_NoGoal()
    
        无盈利目标策略，通常为了进行测试或对比。
        
        :return: 盈利目标策略实例
    """
```

