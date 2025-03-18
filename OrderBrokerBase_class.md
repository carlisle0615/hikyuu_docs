## OrderBrokerBase

```python
class OrderBrokerBase:
    """
    订单代理包装基类，用户可以参考自定义自己的订单代理，加入额外的处理
          
        :param bool real: 下单前是否重新实时获取实时分笔数据
        :param float slip: 如果当前的卖一价格和指示买入的价格绝对差值不超过slip则下单，否则忽略; 对卖出操作无效，立即以当前价卖出
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        """
            :param str name: 代理名称
        """
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def _buy(self, arg0: Datetime, arg1: str, arg2: str, arg3: float, arg4: float, arg5: float, arg6: float, arg7: SystemPart) -> None:
        """
        _buy(self, datetime, market, code, price, num, stoploss, goal_price, part_from)
        
            【子类接口】执行买入操作
        
            :param Datetime datetime: 策略指示时间
            :param str market: 市场标识
            :param str code: 证券代码
            :param float price: 买入价格
            :param float num: 买入数量
            :param float stoploss: 计划止损价
            :param float goal_price: 计划盈利目标价
            :param SystemPart part_from: 信号来源
        """
    def _get_asset_info(self) -> str:
        """
        _get_asset_info(self)
        
            【子类接口】获取当前资产信息，子类需返回符合如下规范的 json 字符串:
        
            {
                "datetime": "2001-01-01 18:00:00.12345",
                "cash": 0.0,
                "positions": [
                    {"market": "SZ", "code": "000001", "number": 100.0, "stoploss": 0.0, "goal_price": 0.0,
                     "cost_price": 0.0},
                    {"market": "SH", "code": "600001", "number": 100.0, "stoploss": 0.0, "goal_price": 0.0,
                     "cost_price": 0.0},
                 ]
            }    
        
            :return: 以字符串（json格式）方式返回当前资产信息
            :rtype: str
        """
    def _sell(self, arg0: Datetime, arg1: str, arg2: str, arg3: float, arg4: float, arg5: float, arg6: float, arg7: SystemPart) -> None:
        """
        _sell(self, datetime, market, code, price, num, stoploss, goal_price, part_from)
        
            【子类接口】执行卖出操作
        
            :param Datetime datetime: 策略指示时间
            :param str market: 市场标识
            :param str code: 证券代码
            :param float price: 卖出价格
            :param float num: 卖出数量
            :param float stoploss: 计划止损价
            :param float goal_price: 计划盈利目标价
            :param SystemPart part_from: 信号来源
        """
    def buy(self, arg0: Datetime, arg1: str, arg2: str, arg3: float, arg4: float, arg5: float, arg6: float, arg7: SystemPart) -> None:
        """
        详情见子类实现接口: _buy
        """
    def get_asset_info(self) -> str:
        """
        详情见子类实现接口: _get_asset_info
        """
    def sell(self, arg0: Datetime, arg1: str, arg2: str, arg3: float, arg4: float, arg5: float, arg6: float, arg7: SystemPart) -> None:
        """
        详情见子类实现接口: _sell
        """
    @property
    def name(self) -> str:
        """
        名称（可读写）
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
```

## 相关方法

#### crtBrokerTM

```python
def crtBrokerTM(broker: OrderBrokerBase, cost_func: TradeCostBase = ..., name: str = 'SYS', other_brokers: list[OrderBrokerBase] = []) -> TradeManager:
    ...
```

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

#### run_in_strategy

```python
def run_in_strategy(sys: System, stock: Stock, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: list[OrderBrokerBase] = []) -> None:
    """
    run_in_strategy(sys, stk, query, broker, costfunc, [other_brokers=[]])
              
        在策略运行时中执行系统交易 SYS
        目前仅支持 buy_delay| sell_delay 均为 false 的系统，即 close 时执行交易
     
        :param sys: 交易系统
        :param stk: 交易对象
        :param query: 查询条件
        :param broker: 订单代理（专用与和账户资产同步的订单代理）
        :param costfunc: 成本函数
        :param other_brokers: 其他的订单代理
    """
```

#### run_in_strategy

```python
def run_in_strategy(pf: Portfolio, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: list[OrderBrokerBase] = []) -> None:
    """
    run_in_strategy(pf, query, adjust_cycle, broker, costfunc, [other_brokers=[]])
              
        在策略运行时中执行组合策略 PF
        目前仅支持 buy_delay| sell_delay 均为 false 的系统，即 close 时执行交易
    
        :param Portfolio pf: 资产组合
        :param Query query: 查询条件
        :param broker: 订单代理（专用与和账户资产同步的订单代理）
        :param costfunc: 成本函数
        :param other_brokers: 其他的订单代理
    """
```

