## Stock

```python
class Stock:
    """
    证券对象
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: Stock) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    def __hash__(self):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, market: str, code: str, name: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Stock) -> None:
        ...
    def __ne__(self, arg0: Stock) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def get_belong_to_block_list(self, category: typing.Any = None) -> list[...]:
        """
        get_belong_to_block_list(self[, category=None])
              
              获取所属板块列表
        
              :param str category: 指定的板块分类，为 None 时，返回所有板块分类下的所属板块
              :rtype: list
        """
    def get_count(self, ktype: str = 'DAY') -> int:
        """
        get_count(self, [ktype=Query.DAY])
        
                获取不同类型K线数据量
        
                :param Query.KType ktype: K线数据类别
                :return: K线记录数
                :rtype: int
        """
    def get_datetime_list(self, arg0: Query) -> DatetimeList:
        """
        get_datetime_list(self, query)
        
                获取日期列表
        
                :param Query query: 查询条件
                :rtype: DatetimeList
        """
    def get_finance_info(self) -> ...:
        """
        get_finance_info(self)
        
                获取当前财务信息
        
                :rtype: Parameter
        """
    def get_history_finance(self) -> list:
        """
        get_history_finance(self)
                
                获取所有历史财务信息历史记录
        """
    def get_kdata(self, arg0: Query) -> KData:
        """
        get_kdata(self, query)
        
                获取K线数据
        
                :param Query query: 查询条件
                :return: 满足查询条件的K线数据
                :rtype: KData
        """
    @typing.overload
    def get_krecord(self, pos: int, ktype: str = 'DAY') -> KRecord:
        """
        get_krecord(self, pos[, ktype=Query.DAY])
        
                获取指定索引的K线数据记录，未作越界检查
        
                :param int pos: 指定的索引位置
                :param Query.KType ktype: K线数据类别
                :return: K线记录
                :rtype: KRecord
        """
    @typing.overload
    def get_krecord(self, date: Datetime, ktype: str = 'DAY') -> KRecord:
        """
        get_krecord(self, datetime[, ktype=Query.DAY])
        
                根据数据类型（日线/周线等），获取指定时刻的KRecord
        
                :param Datetime datetime: 指定日期时刻
                :param Query.KType ktype: K线数据类别
                :return: K线记录
                :rtype: KRecord
        """
    def get_krecord_list(self, arg0: Query) -> KRecordList:
        """
        get_krecord_list(self, start, end,
                  ktype)
        
                获取K线记录 [start, end)，一般不直接使用.
        
                :param int start: 起始位置
                :param int end: 结束位置
                :param Query.KType ktype: K线类别
                :return: K线记录列表
                :rtype: KRecordList
        """
    def get_market_value(self, arg0: Datetime, arg1: str) -> float:
        """
        get_market_value(self, date, ktype)
        
                获取指定时刻的市值，即小于等于指定时刻的最后一条记录的收盘价
        
                :param Datetime date: 指定时刻
                :param Query.KType ktype: K线数据类别
                :return: 指定时刻的市值
                :rtype: float
        """
    def get_timeline_list(self, arg0: Query) -> TimeLineList:
        """
        get_timeline_list(self, query)
        
                获取分时线
        
                :param Query query: 查询条件（查询条件中的K线类型、复权类型参数此时无用）
                :rtype: TimeLineList
        """
    def get_trading_calendar(self, query: Query) -> DatetimeList:
        """
        get_trading_calendar(self, query)
        
                获取自身市场的交易日日历（（不是本身的交易日期）
        
                :param KQuery query: Query查询条件
                :return: 日期列表
                :rtype: DatetimeList
        """
    def get_trans_list(self, arg0: Query) -> TransList:
        """
        get_trans_list(self, query)
        
                获取历史分笔数据
        
                :param Query query: 查询条件（查询条件中的K线类型、复权类型参数此时无用）
                :rtype: TransList
        """
    def get_weight(self, start: Datetime = ..., end: Datetime = ...) -> StockWeightList:
        """
        get_weight(self, [start, end])
        
                获取指定时间段[start,end)内的权息信息。未指定起始、结束时刻时，获取全部权息记录。
        
                :param Datetime start: 起始时刻
                :param Datetime end: 结束时刻
                :rtype: StockWeightList
        """
    def is_buffer(self, arg0: str) -> bool:
        """
        指定类型的K线数据是否被缓存
        """
    def is_null(self) -> bool:
        """
        is_null(self)
        
                是否为Null
        
                :rtype: bool
        """
    def load_kdata_to_buffer(self, arg0: str) -> None:
        """
        load_kdata_to_buffer(self,
                  ktype)
        
                将指定类别的K线数据加载至内存缓存
        
                :param Query.KType ktype: K线类型
        """
    def realtime_update(self, krecord: KRecord, ktype: str = 'DAY') -> None:
        """
        realtime_update(self, krecord)
        
                只用于更新缓存中的日线数据
        
                :param KRecord krecord: 新增的实时K线记录
                :param KQuery.KType ktype: K 线类型
        """
    def release_kdata_buffer(self, arg0: str) -> None:
        """
        release_kdata_buffer(self,
                  ktype)
        
                释放指定类别的内存K线数据
        
                :param Query.KType ktype: K线类型
        """
    def set_krecord_list(self, krecord_list: typing.Any, ktype: str = 'DAY') -> None:
        """
        set_krecord_list(self, krecord_list, [ktype=Query.DAY])
        
              "谨慎调用！！！直接设置当前内存 KRecordList, 仅供需临时增加的外部 Stock 设置 K 线数据
        
              :param krecord_list: KRecordList or list of KRecord
              :param Query.KType ktype: K线类别
        """
    @property
    def atom(self) -> float:
        """
        最小交易数量，同min_tradeNumber
        """
    @atom.setter
    def atom(self, arg1: float) -> None:
        ...
    @property
    def code(self) -> str:
        """
        证券代码
        """
    @code.setter
    def code(self, arg1: str) -> None:
        ...
    @property
    def id(self) -> int:
        """
        内部id
        """
    @property
    def last_datetime(self) -> Datetime:
        """
        证券最后日期
        """
    @last_datetime.setter
    def last_datetime(self, arg1: Datetime) -> None:
        ...
    @property
    def market(self) -> str:
        """
        所属市场简称，市场简称是市场的唯一标识
        """
    @market.setter
    def market(self, arg1: str) -> None:
        ...
    @property
    def market_code(self) -> str:
        """
        市场简称+证券代码，如: sh000001
        """
    @property
    def max_trade_number(self) -> float:
        """
        最大交易数量
        """
    @max_trade_number.setter
    def max_trade_number(self, arg1: float) -> None:
        ...
    @property
    def min_trade_number(self) -> float:
        """
        最小交易数量
        """
    @min_trade_number.setter
    def min_trade_number(self, arg1: float) -> None:
        ...
    @property
    def name(self) -> str:
        """
        证券名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def precision(self) -> int:
        """
        价格精度
        """
    @precision.setter
    def precision(self, arg1: int) -> None:
        ...
    @property
    def start_datetime(self) -> Datetime:
        """
        证券起始日期
        """
    @start_datetime.setter
    def start_datetime(self, arg1: Datetime) -> None:
        ...
    @property
    def tick(self) -> float:
        """
        最小跳动量
        """
    @tick.setter
    def tick(self, arg1: float) -> None:
        ...
    @property
    def tick_value(self) -> float:
        """
        最小跳动量价值
        """
    @tick_value.setter
    def tick_value(self, arg1: float) -> None:
        ...
    @property
    def type(self) -> int:
        """
        证券类型，参见：constant
        """
    @type.setter
    def type(self, arg1: int) -> None:
        ...
    @property
    def unit(self) -> float:
        """
        每单位价值 = tickValue / tick
        """
    @property
    def valid(self) -> bool:
        """
        该证券当前是否有效
        """
    @valid.setter
    def valid(self, arg1: bool) -> None:
        ...
```

## 相关方法

### 与Stock相关的方法

#### IC

```python
def IC(ind: Indicator, stks: typing.Any, query: Query, ref_stk: Stock, n: int = 1, spearman: bool = True) -> Indicator:
    """
    IC(ind, stks, query, ref_stk[, n=1])
    
        计算指定的因子相对于参考证券的 IC （实际为 RankIC）
        
        :param Indicator ind: 输入因子
        :param sequence(stock)|Block stks 证券组合
        :param Query query: 查询条件
        :param Stock ref_stk: 参照证券，通常使用 sh000300 沪深300
        :param int n: 时间窗口
        :param bool spearman: 使用 spearman 相关系数，否则为 pearson
    """
```

#### ICIR

```python
def ICIR(ind: Indicator, stks: typing.Any, query: Query, ref_stk: Stock, n: int = 1, rolling_n: int = 120, spearman: bool = True) -> Indicator:
    """
    ICIR(ind, stks, query, ref_stk[, n=1, rolling_n=120])
    
        计算 IC 因子 IR = IC的多周期均值/IC的标准方差
    
        :param Indicator ind: 输入因子
        :param sequence(stock)|Block stks 证券组合
        :param Query query: 查询条件
        :param Stock ref_stk: 参照证券，通常使用 sh000300 沪深300
        :param int n: 计算IC时对应的 n 日收益率
        :param int rolling_n: 滚动周期
        :param bool spearman: 使用 spearman 相关系数，否则为 pearson
    """
```

#### find_optimal_system

```python
def find_optimal_system(sys_list: list[System], stock: Stock, query: Query, sort_key: str = '', sort_mode: int = 0) -> tuple[float, System]:
    ...
```

#### find_optimal_system_multi

```python
def find_optimal_system_multi(sys_list: list[System], stock: Stock, query: Query, sort_key: str = '', sort_mode: int = 0) -> tuple[float, System]:
    ...
```

#### get_stock

```python
def get_stock(arg0: str) -> Stock:
    """
    get_stock(market_code)
    
            根据"市场简称证券代码"获取对应的证券实例
    
            :param str market_code: 格式：“市场简称证券代码”，如"sh000001"
            :return: 对应的证券实例，如果实例不存在，则返回空实例，即Stock()，不抛出异常
            :rtype: Stock
    """
```

#### inner_combinate_ind_analysis

```python
def inner_combinate_ind_analysis(arg0: Stock, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
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

