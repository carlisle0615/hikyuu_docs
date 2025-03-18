## TradeManager

```python
class TradeManager:
    """
    交易管理类，可理解为一个模拟账户进行模拟交易。一般使用 crtTM 创建交易管理实例。
    
    交易管理可理解为一个模拟账户进行模拟交易。一般使用 crtTM 创建交易管理实例。
    
    公共参数：
    
        - precision=2 (int) : 价格计算精度
        - support_borrow_cash=False (bool) : 是否自动融资
        - support_borrow_stock=False (bool) : 是否自动融券
        - save_action=True (bool) : 是否保存Python命令序列
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def heatmap(tm, start_date, end_date = None, axes = None):
        """
        
            绘制账户收益年-月收益热力图
        
            :param tm: 交易账户
            :param start_date: 开始日期
            :param end_date: 结束日期，默认为今天
            :param axes: 绘制的轴对象，默认为None，表示创建新的轴对象
            :return: None
            
        """
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: TradeCostBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def add_position(self, arg0: PositionRecord) -> bool:
        """
        add_postion(self, position)
        
            建立初始账户后，直接加入持仓记录，仅用于构建初始有持仓的账户
        
            :param PositionRecord position: 持仓记录
            return True | False
        """
    def add_trade_record(self, arg0: TradeRecord) -> bool:
        """
        add_trade_record(self, tr)
        
            直接加入交易记录，如果加入初始化账户记录，将清除全部已有交易及持仓记录。
        
            :param TradeRecord tr: 交易记录
            :return: True（成功） | False（失败）
            :rtype: bool
        """
    def borrow_cash(self, arg0: Datetime, arg1: float) -> bool:
        ...
    def borrow_stock(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> bool:
        ...
    def buy(self, datetime: Datetime, stock: Stock, real_price: float, num: float, stoploss: float = 0.0, goal_price: float = 0.0, plan_price: float = 0.0, part: SystemPart = ...) -> TradeRecord:
        """
        buy(self, datetime, stock, real_price, number[, stoploss=0.0, goal_price=0.0, plan_price=0.0, part=System.INVALID])
        
            买入操作
        
            :param Datetime datetime: 买入时间
            :param Stock stock:       买入的证券
            :param float real_price:  实际买入价格
            :param float num:         买入数量
            :param float stoploss:    止损价
            :param float goal_price:  目标价格
            :param float plan_price:  计划买入价格
            :param SystemPart part:   交易指示来源
            :rtype: TradeRecord
        """
    def buy_short(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: SystemPart) -> TradeRecord:
        ...
    def cash(self, datetime: Datetime, ktype: str = 'DAY') -> float:
        """
        cash(self, datetime[, ktype=Query.KType.DAY])
        
            获取指定时刻的现金。（注：如果不带日期参数，无法根据权息信息调整持仓。）
        
            :param Datetime datetime: 指定时刻
            :param ktype: K线类型
            :rtype: float
        """
    def checkin(self, arg0: Datetime, arg1: float) -> bool:
        """
        checkin(self, datetime, cash)
        
            向账户内存入现金
        
            :param Datetime datetime: 交易时间
            :param float cash: 存入的现金量
            :rtype: TradeRecord
        """
    def checkin_stock(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> bool:
        ...
    def checkout(self, arg0: Datetime, arg1: float) -> bool:
        """
        checkout(self, datetime, cash)
        
            从账户内取出现金
        
            :param Datetime datetime: 交易时间
            :param float cash: 取出的资金量
            :rtype: TradeRecord
        """
    def checkout_stock(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> bool:
        ...
    def clear_broker(self) -> None:
        """
        clear_broker(self)
        
            清空所有已注册订单代理
        """
    def clone(self) -> TradeManager:
        """
        克隆（深复制）实例
        """
    def fetch_asset_info_from_broker(self, arg0: OrderBrokerBase) -> None:
        ...
    def getParam(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_base_assets_curve(self, dates: DatetimeList, ktype: str = 'DAY') -> list[float]:
        """
        get_profit_curve(self, dates[, ktype = Query.DAY])
        
            获取投入本值资产曲线（投入本钱）
        
            :param DatetimeList dates: 日期列表
            :param Query.KType ktype: K线类型，必须与日期列表匹配
            :rtype: PriceList
        """
    def get_borrow_cash_cost(self, arg0: Datetime, arg1: float) -> CostRecord:
        ...
    def get_borrow_stock_cost(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> CostRecord:
        ...
    def get_buy_cost(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> CostRecord:
        """
        get_buy_cost(self, datetime, stock, price, num)
        
            计算买入成本
        
            :param Datetime datetime: 交易时间
            :param Stock stock:       交易的证券
            :param float price:       买入价格
            :param float num:         买入数量
            :rtype: CostRecord
        """
    @typing.overload
    def get_funds(self, ktype: str = 'DAY') -> FundsRecord:
        ...
    @typing.overload
    def get_funds(self, datetime: Datetime, ktype: str = 'DAY') -> FundsRecord:
        """
        get_funds(self, [datetime, ktype = Query.DAY])
        
            获取指定时刻的资产市值详情
        
            :param Datetime datetime:  指定时刻
            :param Query.KType ktype: K线类型
            :rtype: FundsRecord
        """
    def get_funds_curve(self, dates: DatetimeList, ktype: str = 'DAY') -> list[float]:
        """
        get_funds_curve(self, dates[, ktype = Query.DAY])
        
            获取资产净值曲线
        
            :param DatetimeList dates: 日期列表，根据该日期列表获取其对应的资产净值曲线
            :param Query.KType ktype: K线类型，必须与日期列表匹配
            :return: 资产净值列表
            :rtype: PriceList
        """
    def get_funds_list(self, dates: DatetimeList, ktype: str = 'DAY') -> list[FundsRecord]:
        """
        get_funds_list(self, dates[, ktype = Query.DAY])
            
            获取指定日期列表的每日资产记录
            :param Datetime datetime:  指定时刻
            :param Query.KType ktype: K线类型
            :rtype: FundsList
        """
    def get_history_position_list(self) -> PositionRecordList:
        """
        get_history_position_list(self)
        
            获取全部历史持仓记录，即已平仓记录
        
            :rtype: PositionRecordList
        """
    def get_hold_num(self, arg0: Datetime, arg1: Stock) -> float:
        """
        get_hold_num(self, datetime, stock)
        
                获取指定时刻指定证券的持有数量
                
                :param Datetime datetime: 指定时刻
                :param Stock stock: 指定的证券
                :rtype: int
        """
    def get_margin_rate(self, arg0: Datetime, arg1: Stock) -> float:
        ...
    def get_position(self, arg0: Datetime, arg1: Stock) -> PositionRecord:
        """
        get_position(self, date, stock)
        
            获取指定日期指定证券的持仓记录，如当前未持有该票，返回PositionRecord()
        
            :param Datetime date: 指定日期
            :param Stock stock: 指定的证券
            :rtype: PositionRecord
        """
    def get_position_list(self) -> PositionRecordList:
        """
        get_position_list(self)
        
            获取当前全部持仓记录
        
            :rtype: PositionRecordList
        """
    def get_profit_cum_change_curve(self, dates: DatetimeList, ktype: str = 'DAY') -> list[float]:
        """
        get_profit_cum_change_curve(self, dates[, ktype = Query.DAY])
        
            获取累积收益率曲线
        
            :param DatetimeList dates: 日期列表
            :param Query.KType ktype: K线类型，必须与日期列表匹配
            :rtype: PriceList
        """
    def get_profit_curve(self, dates: DatetimeList, ktype: str = 'DAY') -> list[float]:
        """
        get_profit_curve(self, dates[, ktype = Query.DAY])
        
            获取收益曲线，即扣除历次存入资金后的资产净值曲线
        
            :param DatetimeList dates: 日期列表，根据该日期列表获取其对应的收益曲线，应为递增顺序
            :param Query.KType ktype: K线类型，必须与日期列表匹配
            :return: 收益曲线
            :rtype: PriceList
        """
    def get_return_cash_cost(self, arg0: Datetime, arg1: Datetime, arg2: float) -> CostRecord:
        ...
    def get_return_stock_cost(self, arg0: Datetime, arg1: Datetime, arg2: Stock, arg3: float, arg4: float) -> CostRecord:
        ...
    def get_sell_cost(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> CostRecord:
        """
        get_sell_cost(self, datetime, stock, price, num)
        
            计算卖出成本
        
            :param Datetime datetime: 交易时间
            :param Stock stock:       交易的证券
            :param float price:       卖出价格
            :param float num:         卖出数量
            :rtype: CostRecord
        """
    def get_short_hold_num(self, arg0: Datetime, arg1: Stock) -> float:
        ...
    def get_short_stock_num(self) -> int:
        ...
    def get_stock_num(self) -> int:
        """
        get_stock_num(self)
        
            当前持有的证券种类数量，即当前持有几只股票（非各个股票的持仓数）
        
            :rtype: int
        """
    @typing.overload
    def get_trade_list(self) -> TradeRecordList:
        ...
    @typing.overload
    def get_trade_list(self, arg0: Datetime, arg1: Datetime) -> TradeRecordList:
        """
        get_trade_list(self[, start, end])
        
            获取交易记录，未指定参数时，获取全部交易记录
        
            :param Datetime start: 起始日期
            :param Datetime end: 结束日期
            :rtype: TradeRecordList
        """
    def have(self, arg0: Stock) -> bool:
        """
        have(self, stock)
        
            当前是否持有指定的证券
        
            :param Stock stock: 指定证券
            :rtype: bool
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def reg_broker(self, arg0: OrderBrokerBase) -> None:
        """
        reg_broker(self, broker)
            
            注册订单代理。可执行多次该命令注册多个订单代理。
                
            :param OrderBrokerBase broker: 订单代理实例
        """
    def reset(self) -> None:
        """
        复位，清空交易、持仓记录
        """
    def return_cash(self, arg0: Datetime, arg1: float) -> bool:
        ...
    def return_stock(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float) -> bool:
        ...
    def sell(self, datetime: Datetime, stock: Stock, real_price: float, num: float = 1.7976931348623157e+308, stoploss: float = 0.0, goal_price: float = 0.0, plan_price: float = 0.0, part: SystemPart = ...) -> TradeRecord:
        """
        sell(self, datetime, stock, realPrice[, number=constant.max_double, stoploss=0.0, goal_price=0.0, plan_price=0.0, part=System.INVALID])
        
            卖出操作
        
            :param Datetime datetime: 卖出时间
            :param Stock stock:       卖出的证券
            :param float real_price:  实际卖出价格
            :param float num:         卖出数量，如果等于constant.max_double，表示全部卖出
            :param float stoploss:    新的止损价
            :param float goal_price:  新的目标价格
            :param float plan_price:  原计划卖出价格
            :param SystemPart part:   交易指示来源
            :rtype: TradeRecord
        """
    def sell_short(self, arg0: Datetime, arg1: Stock, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: SystemPart) -> TradeRecord:
        ...
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        set_param(self, name, value)
        
            设置参数
        
            :param str name: 参数名称
            :param value: 参数值
            :type value: int | bool | float | string | Query | KData | Stock | DatetimeList
            :raises logic_error: Unsupported type! 不支持的参数类型
        """
    def tocsv(self, arg0: str) -> None:
        """
        tocsv(self, path)
        
            以csv格式输出交易记录、未平仓记录、已平仓记录、资产净值曲线
        
            :param str path: 输出文件所在目录
        """
    def update_with_weight(self, arg0: Datetime) -> None:
        """
        update_with_weight(self, date)
        
              根据权息信息更新当前持仓及交易记录，必须按时间顺序被调用
        
              :param Datetime date: 当前时刻
        """
    @property
    def broker_last_datetime(self) -> Datetime:
        """
        实际开始订单代理操作的时刻。
                
            默认情况下，TradeManager会在执行买入/卖出操作时，调用订单代理执行代理的买入/卖出动作，但这样在实盘操作时会存在问题。因为系统在计算信号指示时，需要回溯历史数据才能得到最新的信号，这样TradeManager会在历史时刻就执行买入/卖出操作，此时如果订单代理本身没有对发出买入/卖出指令的时刻进行控制，会导致代理发送错误的指令。此时，需要指定在某一个时刻之后，才允许指定订单代理的买入/卖出操作。属性 brokeLastDatetime 即用于指定该时刻。
        """
    @broker_last_datetime.setter
    def broker_last_datetime(self, arg1: Datetime) -> None:
        ...
    @property
    def cost_func(self) -> TradeCostBase:
        """
        交易成本算法
        """
    @cost_func.setter
    def cost_func(self, arg1: TradeCostBase) -> None:
        ...
    @property
    def current_cash(self) -> float:
        """
        （只读）当前资金
        """
    @property
    def first_datetime(self) -> Datetime:
        """
        （只读）第一笔买入交易发生日期，如未发生交易返回 Datetime>()
        """
    @property
    def init_cash(self) -> float:
        """
        （只读）初始资金
        """
    @property
    def init_datetime(self) -> Datetime:
        """
        （只读）账户建立日期
        """
    @property
    def last_datetime(self) -> Datetime:
        """
        （只读）最后一笔交易日期，注意和交易类型无关，如未发生交易返回账户建立日期
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
    def precision(self) -> int:
        """
        （只读）价格精度，同公共参数“precision”
        """
```

## 相关方法

### 与TradeManager相关的方法

#### crtBrokerTM

```python
def crtBrokerTM(broker: OrderBrokerBase, cost_func: TradeCostBase = ..., name: str = 'SYS', other_brokers: list[OrderBrokerBase] = []) -> TradeManager:
    ...
```

#### crtTM

```python
def crtTM(date: Datetime = ..., init_cash: float = 100000, cost_func: TradeCostBase = ..., name: str = 'SYS') -> TradeManager:
    """
    crtTM([date = Datetime(199001010000), init_cash = 100000, cost_func = TC_Zero(), name = "SYS"])
    
        创建交易管理模块，管理帐户的交易记录及资金使用情况
        
        :param Datetime date:  账户建立日期
        :param float init_cash:    初始资金
        :param TradeCost cost_func: 交易成本算法
        :param string name:        账户名称
        :rtype: TradeManager
    """
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

