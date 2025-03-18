## Strategy

```python
class Strategy:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, code_list: list[str], ktype_list: list[str], name: str = 'Strategy', config: str = '') -> None:
        """
        创建策略运行时
                   
            :param list code_list: 证券代码列表，如：["sz000001", "sz000002"], "all" 代表全部证券
            :param list ktype_list: K线类型列表, 如: ["day", "min"]
            :param str name: 策略名称
            :param str config: 配置文件名称(如需要使用独立的配置文件，否则为空时使用默认的hikyuu配置文件)
        """
    @typing.overload
    def __init__(self, context: StrategyContext, name: str = 'Strategy', config: str = '') -> None:
        """
        使用上下文创建策略运行时
        
            :param StrategyContext context: 上下文实例
            :param str name: 策略名称
            :param str config: 配置文件名称(如需要使用独立的配置文件，否则为空时使用默认的hikyuu配置文件)
        """
    def on_change(self, arg0: typing.Any) -> None:
        """
        onchang(self, func)
                   
            设置证券数据更新回调通知
        
            :param func: 一个可调用的对象如普通函数，需接收 stock 和 ktype 参数
        """
    def on_received_spot(self, arg0: typing.Any) -> None:
        """
        on_received_spot(self, func)
        
            设置证券数据更新通知回调
        
            :param func: 可调用对象如普通函数，没有参数
        """
    def run_daily(self, func: typing.Any, time: TimeDelta, market: str = 'SH', ignore_market: bool = False) -> None:
        """
        run_daily(self, func)
                
            设置日内循环执行回调。如果忽略市场开闭市，则自启动时刻开始按间隔时间循环，
            否则第一次执行时将开盘时间对齐时间间隔，且在非开市时间停止执行。
        
            :param func: 可调用对象如普通函数，没有参数
            :param TimeDelta time: 间隔时间，如间隔3秒：TimeDelta(0, 0, 0, 3) 或 Seconds(3)
            :param str market: 使用哪个市场的开闭市时间
            :param ignore_market: 忽略市场开闭市时间
        """
    def run_daily_at(self, func: typing.Any, time: TimeDelta, ignore_holiday: bool = True) -> None:
        """
        run_daily_at(self, func)
        
            设置每日定点执行回调
        
            :param func: 可调用对象如普通函数，没有参数
            :param TimeDelta time: 执行时刻，如每日15点：TimeDelta(0, 15)
            :param ignore_holiday: 节假日不执行
        """
    def start(self, auto_recieve_spot: bool = True) -> None:
        """
        start(self)
        
            启动策略执行，请在完成相关回调设置后执行。
        
            :param bool auto_recieve_spot: 是否自动接收行情数据
        """
    @property
    def context(self) -> StrategyContext:
        """
        获取策略上下文
        """
    @property
    def name(self) -> str:
        """
        策略名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
```

## 相关方法

#### crt_pf_strategy

```python
def crt_pf_strategy(pf: Portfolio, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, name: str = 'PFStrategy', other_brokers: list[OrderBrokerBase] = [], config: str = '') -> Strategy:
    ...
```

#### crt_sys_strategy

```python
def crt_sys_strategy(sys: System, stk_market_code: str, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: str = [], name: list[OrderBrokerBase] = 'SYSStrategy', config: str = '') -> Strategy:
    ...
```

