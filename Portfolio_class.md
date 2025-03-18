## Portfolio

```python
class Portfolio:
    """
    实现多标的、多策略的投资组合
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def heatmap(sys, axes = None):
        """
        
            绘制系统收益年-月收益热力图
            
        """
    @staticmethod
    def performance(sys, ref_stk = None):
        """
        
            绘制系统绩效，即账户累积收益率曲线
        
            :param SystemBase | PortfolioBase sys: SYS或PF实例
            :param Stock ref_stk: 参考股票, 默认为沪深300: sh000300, 绘制参考标的的收益曲线
            :return: None
            
        """
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: TradeManager, arg2: SelectorBase, arg3: AllocateFundsBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def clone(self) -> Portfolio:
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
    def reset(self) -> None:
        """
        复位操作
        """
    def run(self, query: Query, force: bool = False) -> None:
        """
        run(self, query[, force=false])
            
            运行投资组合策略。在查询条件及各组件没有变化时，PF在第二次执行时，默认不会实际进行计算。
            但由于各个组件的参数可能改变，此种情况无法自动判断是否需要重计算，可以手工指定进行强制计算。
        
            调仓模式 adjust_mode 说明：
            - "query" 模式，跟随输入参数 query 中的 ktype，此时 adjust_cycle 为以 query 中的 ktype
              决定周期间隔；
            - "day" 模式，adjust_cycle 为调仓间隔天数
            - "week" | "month" | "quarter" | "year" 模式时，adjust_cycle
              为对应的每周第N日、每月第n日、每季度第n日、每年第n日，在 delay_to_trading_day 为 false 时
              如果当日不是交易日将会被跳过调仓；当 delay_to_trading_day 为 true时，如果当日不是交易日
              将会顺延至当前周期内的第一个交易日，如指定每月第1日调仓，但当月1日不是交易日，则将顺延至当月
              的第一个交易日。
                
            :param Query query: 查询条件
            :param bool force: 强制重新计算
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
    def af(self) -> AllocateFundsBase:
        """
        设置或获取资产分配算法
        """
    @af.setter
    def af(self, arg1: AllocateFundsBase) -> None:
        ...
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
        查询条件
        """
    @query.setter
    def query(self, arg1: Query) -> None:
        ...
    @property
    def real_sys_list(self) -> list[...]:
        """
        由 PF 运行时设定的实际运行系统列表
        """
    @property
    def se(self) -> SelectorBase:
        """
        设置或获取交易对象选择算法
        """
    @se.setter
    def se(self, arg1: SelectorBase) -> None:
        ...
    @property
    def tm(self) -> TradeManager:
        """
        设置或获取交易管理对象
        """
    @tm.setter
    def tm(self, arg1: TradeManager) -> None:
        ...
```

## 相关方法

#### PF_Simple

```python
def PF_Simple(tm: TradeManager = None, se: SelectorBase = ..., af: AllocateFundsBase = ..., adjust_cycle: int = 1, adjust_mode: str = 'query', delay_to_trading_day: bool = True) -> Portfolio:
    """
    PF_Simple([tm, se, af, adjust_cycle=1, adjust_mode="query", delay_to_trading_day=True])
    
        创建一个多标的、单系统策略的投资组合
    
        调仓模式 adjust_mode 说明：
        - "query" 模式，跟随输入参数 query 中的 ktype，此时 adjust_cycle 为以 query 中的 ktype
          决定周期间隔；
        - "day" 模式，adjust_cycle 为调仓间隔天数
        - "week" | "month" | "quarter" | "year" 模式时，adjust_cycle
          为对应的每周第N日、每月第n日、每季度第n日、每年第n日，在 delay_to_trading_day 为 false 时
          如果当日不是交易日将会被跳过调仓；当 delay_to_trading_day 为 true时，如果当日不是交易日
          将会顺延至当前周期内的第一个交易日，如指定每月第1日调仓，但当月1日不是交易日，则将顺延至当月
          的第一个交易日。    
    
        :param TradeManager tm: 交易管理
        :param SelectorBase se: 交易对象选择算法
        :param AllocateFundsBase af: 资金分配算法
        :param int adjust_cycle: 调仓周期
        :param str adjust_mode: 调仓模式
        :param bool delay_to_trading_day: 如果当日不是交易日将会被顺延至当前周期内的第一个交易日
    """
```

#### PF_WithoutAF

```python
def PF_WithoutAF(tm: TradeManager = None, se: SelectorBase = ..., adjust_cycle: int = 1, adjust_mode: str = 'query', delay_to_trading_day: bool = True, trade_on_close: bool = True, sys_use_self_tm: bool = False, sell_at_not_selected: bool = False) -> Portfolio:
    """
    PF_WithoutAF([tm, se, adjust_cycle=1, adjust_mode="query", delay_to_trading_day=True, trade_on_close=True, sys_use_self_tm=False,sell_at_not_selected=False])
        
        创建无资金分配算法的投资组合，所有单系统策略使用共同的 tm 管理账户
    
        调仓模式 adjust_mode 说明：
        - "query" 模式，跟随输入参数 query 中的 ktype，此时 adjust_cycle 为以 query 中的 ktype
          决定周期间隔；
        - "day" 模式，adjust_cycle 为调仓间隔天数
        - "week" | "month" | "quarter" | "year" 模式时，adjust_cycle
          为对应的每周第N日、每月第n日、每季度第n日、每年第n日，在 delay_to_trading_day 为 false 时
          如果当日不是交易日将会被跳过调仓；当 delay_to_trading_day 为 true时，如果当日不是交易日
          将会顺延至当前周期内的第一个交易日，如指定每月第1日调仓，但当月1日不是交易日，则将顺延至当月
          的第一个交易日。    
    
        :param TradeManager tm: 交易管理
        :param SelectorBase se: 交易对象选择算法
        :param int adjust_cycle: 调仓周期
        :param str adjust_mode: 调仓模式
        :param bool delay_to_trading_day: 如果当日不是交易日将会被顺延至当前周期内的第一个交易日
        :param bool trade_on_close: 交易是否在收盘时进行
        :param bool sys_use_self_tm: 原型系统使用自身附带的tm进行计算
        :param bool sell_at_not_selected: 调仓日未选中的股票是否强制卖出
    """
```

#### crt_pf_strategy

```python
def crt_pf_strategy(pf: Portfolio, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, name: str = 'PFStrategy', other_brokers: list[OrderBrokerBase] = [], config: str = '') -> Strategy:
    ...
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

