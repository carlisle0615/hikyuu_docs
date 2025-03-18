## TradeCostBase

```python
class TradeCostBase:
    """
    交易成本算法基类
    
        自定义交易成本算法接口：
    
        :py:meth:`TradeCostBase.getBuyCost` - 【必须】获取买入成本
        :py:meth:`TradeCostBase.getSellCost` - 【必须】获取卖出成本
        :py:meth:`TradeCostBase._clone` - 【必须】子类克隆接口
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getstate__(self) -> tuple:
        ...
    def __init__(self, arg0: str) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def clone(self) -> TradeCostBase:
        """
        克隆操作
        """
    def get_buy_cost(self, date: Datetime, stock: Stock, price: float, num: float) -> CostRecord:
        """
        get_buy_cost(self, datetime, stock, price, num)
            
                【重载接口】获取买入成本
                
                :param Datetime datetime: 买入时刻
                :param Stock stock: 买入对象
                :param float price: 买入价格
                :param int num: 买入数量
                :return: 交易成本记录
                :rtype: CostRecord
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_sell_cost(self, date: Datetime, stock: Stock, price: float, num: float) -> CostRecord:
        """
        get_sell_cost(self, datetime, stock, price, num)
            
                【重载接口】获取卖出成本
                
                :param Datetime datetime: 卖出时刻
                :param Stock stock: 卖出对象
                :param float price: 卖出价格
                :param int num: 卖出数量
                :return: 交易成本记录
                :rtype: CostRecord
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
        成本算法名称
        """
```

## 相关方法

#### TC_FixedA

```python
def TC_FixedA(commission: float = 0.0018, lowest_commission: float = 5.0, stamptax: float = 0.001, transferfee: float = 0.001, lowest_transferfee: float = 1.0) -> TradeCostBase:
    """
    TC_FixedA([commission=0.0018, lowestCommission=5.0, stamptax=0.001, transferfee=0.001, lowestTransferfee=1.0])
    
        2015年8月1日之前的A股交易成本算法
    
        :param float commission: 佣金比例
        :param float lowestCommission: 最低佣金值
        :param float stamptax: 印花税
        :param float transferfee: 过户费
        :param float lowestTransferfee: 最低过户费
        :return: :py:class:`TradeCostBase` 子类实例
    """
```

#### TC_FixedA2015

```python
def TC_FixedA2015(commission: float = 0.0018, lowest_commission: float = 5.0, stamptax: float = 0.001, transferfee: float = 2e-05) -> TradeCostBase:
    """
    TC_FixedA2015([commission=0.0018, lowestCommission=5.0, stamptax=0.001, transferfee=0.00002])
    
        2015年8月1日上证过户费改为成交金额的千分之0.02
    
        :param float commission: 佣金比例
        :param float lowestCommission: 最低佣金值
        :param float stamptax: 印花税
        :param float transferfee: 过户费
        :return: :py:class:`TradeCostBase` 子类实例
    """
```

#### TC_FixedA2017

```python
def TC_FixedA2017(commission: float = 0.0018, lowest_commission: float = 5.0, stamptax: float = 0.001, transferfee: float = 2e-05) -> TradeCostBase:
    """
    TC_FixedA2015([commission=0.0018, lowestCommission=5.0, stamptax=0.001, transferfee=0.00002])
    
        2017年1月1日起将对深市过户费项目单独列示，标准为成交金额0.02‰双向收取。
    
        :param float commission: 佣金比例
        :param float lowestCommission: 最低佣金值
        :param float stamptax: 印花税
        :param float transferfee: 过户费
        :return: :py:class:`TradeCostBase` 子类实例
    """
```

#### TC_TestStub

```python
def TC_TestStub() -> TradeCostBase:
    """
    仅用于测试
    """
```

#### TC_Zero

```python
def TC_Zero() -> TradeCostBase:
    """
    零交易成本算法
    """
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

