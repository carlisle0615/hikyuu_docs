## System

```python
class System:
    """
    系统基类。需要扩展或实现更复杂的系统交易行为，可从此类继承。
    
    系统是指针对单个交易对象的完整策略，包括环境判断、系统有效条件、资金管理、止损、止盈、盈利目标、移滑价差的完整策略，用于模拟回测。
    
    公共参数：
    
      - delay=True (bool) : 是否延迟到下一个bar开盘时进行交易
      - delay_use_current_price=True (bool) : 延迟操作的情况下，是使用当前交易时bar的价格计算新的止损价/止赢价/目标价还是使用上次计算的结果
      - max_delay_count=3 (int) : 连续延迟交易请求的限制次数，应大于等于0，0表示只允许延迟1次
      - tp_monotonic=True (bool) : 止赢单调递增
      - tp_delay_n=3 (int) : 止盈延迟开始的天数，即止盈策略判断从实际交易几天后开始生效
      - ignore_sell_sg=False (bool) : 忽略卖出信号，只使用止损/止赢等其他方式卖出
      - ev_open_position=False (bool): 是否使用市场环境判定进行初始建仓
      - cn_open_position=False (bool): 是否使用系统有效性条件进行初始建仓
    """
    CONDITION: typing.ClassVar[SystemPart]  # value = <SystemPart.CONDITION: 1>
    ENVIRONMENT: typing.ClassVar[SystemPart]  # value = <SystemPart.ENVIRONMENT: 0>
    INVALID: typing.ClassVar[SystemPart]  # value = <SystemPart.INVALID: 10>
    MONEYMANAGER: typing.ClassVar[SystemPart]  # value = <SystemPart.MONEYMANAGER: 5>
    PROFITGOAL: typing.ClassVar[SystemPart]  # value = <SystemPart.PROFITGOAL: 6>
    SIGNAL: typing.ClassVar[SystemPart]  # value = <SystemPart.SIGNAL: 2>
    SLIPPAGE: typing.ClassVar[SystemPart]  # value = <SystemPart.SLIPPAGE: 7>
    STOPLOSS: typing.ClassVar[SystemPart]  # value = <SystemPart.STOPLOSS: 3>
    TAKEPROFIT: typing.ClassVar[SystemPart]  # value = <SystemPart.TAKEPROFIT: 4>
    Part = SystemPart
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
    @staticmethod
    def plot(sys, new = True, axes = None, style = 1, only_draw_close = False):
        """
        绘制系统实际买入/卖出信号
        
            :param SystemBase sys: 系统实例
            :param new:   仅在未指定axes的情况下生效，当为True时，
                           创建新的窗口对象并在其中进行绘制
            :param axes:  指定在那个轴对象中进行绘制
            :param style: 1 | 2 信号箭头绘制样式
            :param bool only_draw_close: 不绘制K线，仅绘制 close
            
        """
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: System) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: TradeManager, arg1: MoneyManagerBase, arg2: EnvironmentBase, arg3: ConditionBase, arg4: SignalBase, arg5: StoplossBase, arg6: StoplossBase, arg7: ProfitGoalBase, arg8: SlippageBase, arg9: str) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def clone(self) -> System:
        """
        clone(self)
        
            克隆操作，会依据部件的共享特性进行克隆，共享部件不进行实际的克隆操作，保持共享。
        """
    def force_reset_all(self) -> None:
        """
        force_reset_all(self)
        
            强制复位所有组件以及清空已有的交易对象，忽略组件的共享属性。
        """
    def get_buy_short_trade_request(self) -> TradeRequest:
        ...
    def get_buy_trade_request(self) -> TradeRequest:
        """
        get_buy_trade_request(self)
          
            获取买入请求，“delay”模式下查看下一时刻是否存在买入操作
        
            :rtype: TradeRequest
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_sell_short_trade_request(self) -> TradeRequest:
        ...
    def get_sell_trade_request(self) -> TradeRequest:
        """
        get_sell_trade_request(self)
        
            获取卖出请求，“delay”模式下查看下一时刻是否存在卖出操作
        
            :rtype: TradeRequest
        """
    def get_stock(self) -> Stock:
        """
        get_stock(self)
        
            获取关联的证券
        
            :rtype: Stock
        """
    def get_trade_record_list(self) -> TradeRecordList:
        """
        get_trade_record_list(self)
        
            获取实际执行的交易记录，和 TM 的区别是不包含权息调整带来的交易记录
        
            :rtype: TradeRecordList
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def ready(self) -> None:
        ...
    def reset(self) -> None:
        """
        reset(self)
        
            复位，但不包括已有的交易对象，以及共享的部件。
        """
    @typing.overload
    def run(self, query: Query, reset: bool = True, reset_all: bool = False) -> None:
        ...
    @typing.overload
    def run(self, kdata: KData, reset: bool = True, reset_all: bool = False) -> None:
        ...
    @typing.overload
    def run(self, stock: Stock, query: Query, reset: bool = True, reset_all: bool = False) -> None:
        """
        run(self, stock, query[, reset=True])
          
            运行系统，执行回测
        
            :param Stock stock: 交易的证券
            :param Query query: K线数据查询条件
            :param bool reset: 执行前是否依据系统部件共享属性复位
            :param bool reset_all: 强制复位所有部件
        """
    def set_not_shared_all(self) -> None:
        """
        将所有组件设置为非共享
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
    def cn(self) -> ConditionBase:
        """
        系统有效条件
        """
    @cn.setter
    def cn(self, arg1: ConditionBase) -> None:
        ...
    @property
    def ev(self) -> EnvironmentBase:
        """
        市场环境判断策略
        """
    @ev.setter
    def ev(self, arg1: EnvironmentBase) -> None:
        ...
    @property
    def mm(self) -> MoneyManagerBase:
        """
        资金管理策略
        """
    @mm.setter
    def mm(self, arg1: MoneyManagerBase) -> None:
        ...
    @property
    def name(self) -> str:
        """
        系统名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def pg(self) -> ProfitGoalBase:
        """
        盈利目标策略
        """
    @pg.setter
    def pg(self, arg1: ProfitGoalBase) -> None:
        ...
    @property
    def query(self) -> Query:
        """
        查询条件
        """
    @property
    def sg(self) -> SignalBase:
        """
        信号指示器
        """
    @sg.setter
    def sg(self, arg1: SignalBase) -> None:
        ...
    @property
    def sp(self) -> SlippageBase:
        """
        移滑价差算法
        """
    @sp.setter
    def sp(self, arg1: SlippageBase) -> None:
        ...
    @property
    def st(self) -> StoplossBase:
        """
        止损策略
        """
    @st.setter
    def st(self, arg1: StoplossBase) -> None:
        ...
    @property
    def tm(self) -> TradeManager:
        """
        关联的交易管理实例
        """
    @tm.setter
    def tm(self, arg1: TradeManager) -> None:
        ...
    @property
    def to(self) -> KData:
        """
        交易对象 KData
        """
    @to.setter
    def to(self, arg1: KData) -> None:
        ...
    @property
    def tp(self) -> StoplossBase:
        """
        止盈策略
        """
    @tp.setter
    def tp(self, arg1: StoplossBase) -> None:
        ...
```

## 相关方法

### 与System相关的方法

#### SYS_Simple

```python
def SYS_Simple(tm: typing.Any = None, mm: typing.Any = None, ev: typing.Any = None, cn: typing.Any = None, sg: typing.Any = None, st: typing.Any = None, tp: typing.Any = None, pg: typing.Any = None, sp: typing.Any = None) -> System:
    """
    SYS_Simple([tm=None, mm=None, ev=None, cn=None, sg=None, st=None, tp=None, pg=None, sp=None])
    
      创建简单系统实例（每次交易不进行多次加仓或减仓，即每次买入后在卖出时全部卖出），  系统实例在运行时(调用run方法），至少需要一个配套的交易管理实例、一个资金管理策略
      和一个信号指示器），可以在创建系统实例后进行指定。如果出现调用run时没有任何输出，
      且没有正确结果的时候，可能是未设置tm、sg、mm。进行回测时，使用 run 方法，如::
        
            #创建模拟交易账户进行回测，初始资金30万
            my_tm = crtTM(init_cash = 300000)
    
            #创建信号指示器（以5日EMA为快线，5日EMA自身的10日EMA作为慢线，快线向上穿越慢线时买入，反之卖出）
            my_sg = SG_Flex(EMA(C, n=5), slow_n=10)
    
            #固定每次买入1000股
            my_mm = MM_FixedCount(1000)
    
            #创建交易系统并运行
            sys = SYS_Simple(tm = my_tm, sg = my_sg, mm = my_mm)
            sys.run(sm['sz000001'], Query(-150))
        
        :param TradeManager tm: 交易管理实例 
        :param MoneyManager mm: 资金管理策略
        :param EnvironmentBase ev: 市场环境判断策略
        :param ConditionBase cn: 系统有效条件
        :param SignalBase sg: 信号指示器
        :param StoplossBase st: 止损策略
        :param StoplossBase tp: 止盈策略
        :param ProfitGoalBase pg: 盈利目标策略
        :param SlippageBase sp: 移滑价差算法
        :return: system实例
    """
```

#### SYS_WalkForward

```python
def SYS_WalkForward(sys_list: typing.Sequence, tm: TradeManager = None, train_len: int = 100, test_len: int = 20, se: SelectorBase = None, train_tm: TradeManager = None) -> System:
    """
    SYS_WalkForward(sys_list, tm, train_len, test_len, train_tm)
    
      创建滚动寻优系统，当输入的候选系统列表中仅有一个候选系统时，即为滚动系统
    
      :param sequence sys_list: 候选系统列表
      :param TradeManager tm: 交易账户
      :param int train_len: 滚动评估系统绩效时使用的数据长度
      :param int test_len: 使用在 train_len 中选出的最优系统执行的数据长度
      :param SelectorBase se: 寻优选择器，默认为按“帐户平均年收益率%”最大选择
      :param TradeManager train_tm: 滚动评估时使用的交易账户, 为None时, 使用 tm 的拷贝进行评估
    """
```

#### crt_sys_strategy

```python
def crt_sys_strategy(sys: System, stk_market_code: str, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: str = [], name: list[OrderBrokerBase] = 'SYSStrategy', config: str = '') -> Strategy:
    ...
```

#### inner_combinate_ind_analysis

```python
def inner_combinate_ind_analysis(arg0: Stock, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
    ...
```

#### inner_combinate_ind_analysis_with_block

```python
def inner_combinate_ind_analysis_with_block(arg0: Block, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
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

