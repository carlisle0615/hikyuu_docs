## 工具函数

```python
__all__ = ['ABS', 'ACOS', 'AD', 'ADVANCE', 'AF_EqualWeight', 'AF_FixedWeight', 'AF_FixedWeightList', 'AF_MultiFactor', 'ALIGN', 'AMA', 'ASIN', 'ATAN', 'ATR', 'AVEDEV', 'AllocateFundsBase', 'BACKSET', 'BARSCOUNT', 'BARSLAST', 'BARSSINCE', 'BARSSINCEN', 'BETWEEN', 'BLOCKSETNUM', 'BUSINESS', 'Block', 'BlockInfoDriver', 'BorrowRecord', 'BrokerPositionRecord', 'CEILING', 'CN_Bool', 'CN_OPLine', 'CONTEXT', 'CONTEXT_K', 'CORR', 'COS', 'COST', 'COUNT', 'CROSS', 'CVAL', 'CYCLE', 'C_AMO', 'C_CLOSE', 'C_HIGH', 'C_KDATA', 'C_LOW', 'C_OPEN', 'C_VOL', 'ConditionBase', 'Constant', 'CostRecord', 'DATE', 'DAY', 'DEBUG', 'DECLINE', 'DEVSQ', 'DIFF', 'DIRECT', 'DISCARD', 'DMA', 'DOWNNDAY', 'DROPNA', 'DataDriverFactory', 'Datetime', 'DatetimeList', 'Days', 'EMA', 'ERROR', 'EVERY', 'EV_Bool', 'EV_TwoLine', 'EXIST', 'EXP', 'EnvironmentBase', 'FATAL', 'FILTER', 'FINANCE', 'FLOOR', 'FundsRecord', 'HHV', 'HHVBARS', 'HKUException', 'HOUR', 'HSL', 'Hours', 'IC', 'ICIR', 'IF', 'INBLOCK', 'INDEXA', 'INDEXADV', 'INDEXC', 'INDEXDEC', 'INDEXH', 'INDEXL', 'INDEXO', 'INDEXV', 'INFO', 'INSUM', 'INTPART', 'IR', 'ISINF', 'ISINFA', 'ISLASTBAR', 'ISNA', 'IndParam', 'Indicator', 'IndicatorImp', 'JUMPDOWN', 'JUMPUP', 'KALMAN', 'KDATA_PART', 'KData', 'KDataDriver', 'KRecord', 'KRecordList', 'LAST', 'LASTVALUE', 'LIUTONGPAN', 'LLV', 'LLVBARS', 'LN', 'LOG', 'LOG_LEVEL', 'LONGCROSS', 'LoanRecord', 'MA', 'MACD', 'MAX', 'MDD', 'MF_EqualWeight', 'MF_ICIRWeight', 'MF_ICWeight', 'MF_Weight', 'MIN', 'MINUTE', 'MM_FixedCapital', 'MM_FixedCapitalFunds', 'MM_FixedCount', 'MM_FixedCountTps', 'MM_FixedPercent', 'MM_FixedRisk', 'MM_FixedUnits', 'MM_Nothing', 'MM_WilliamsFixedRisk', 'MOD', 'MONTH', 'MRR', 'MarketInfo', 'Microseconds', 'Milliseconds', 'Minutes', 'MoneyManagerBase', 'MultiFactorBase', 'NDAY', 'NOT', 'OFF', 'OrderBrokerBase', 'PF_Simple', 'PF_WithoutAF', 'PG_FixedHoldDays', 'PG_FixedPercent', 'PG_NoGoal', 'POS', 'POW', 'PRICELIST', 'Parameter', 'Performance', 'Portfolio', 'PositionRecord', 'PositionRecordList', 'ProfitGoalBase', 'Query', 'RECOVER_BACKWARD', 'RECOVER_EQUAL_BACKWARD', 'RECOVER_EQUAL_FORWARD', 'RECOVER_FORWARD', 'REF', 'REPLACE', 'RESULT', 'REVERSE', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'ROUND', 'ROUNDDOWN', 'ROUNDUP', 'RSI', 'SAFTYLOSS', 'SE_Fixed', 'SE_MaxFundsOptimal', 'SE_MultiFactor', 'SE_PerformanceOptimal', 'SE_Signal', 'SGN', 'SG_Add', 'SG_AllwaysBuy', 'SG_And', 'SG_Band', 'SG_Bool', 'SG_Buy', 'SG_Cross', 'SG_CrossGold', 'SG_Cycle', 'SG_Div', 'SG_Flex', 'SG_Mul', 'SG_OneSide', 'SG_Or', 'SG_Sell', 'SG_Single', 'SG_Single2', 'SG_Sub', 'SIN', 'SLICE', 'SLOPE', 'SMA', 'SPEARMAN', 'SP_FixedPercent', 'SP_FixedValue', 'SQRT', 'STDEV', 'STDP', 'ST_FixedPercent', 'ST_Indicator', 'ST_Saftyloss', 'SUM', 'SUMBARS', 'SYS_Simple', 'SYS_WalkForward', 'ScoreRecord', 'ScoreRecordList', 'Seconds', 'SelectorBase', 'SignalBase', 'SlippageBase', 'SpotRecord', 'Stock', 'StockManager', 'StockTypeInfo', 'StockWeight', 'StockWeightList', 'StoplossBase', 'Strategy', 'StrategyContext', 'System', 'SystemPart', 'SystemWeight', 'SystemWeightList', 'TAN', 'TA_ACCBANDS', 'TA_ACOS', 'TA_AD', 'TA_ADD', 'TA_ADOSC', 'TA_ADX', 'TA_ADXR', 'TA_APO', 'TA_AROON', 'TA_AROONOSC', 'TA_ASIN', 'TA_ATAN', 'TA_ATR', 'TA_AVGDEV', 'TA_AVGPRICE', 'TA_BBANDS', 'TA_BETA', 'TA_BOP', 'TA_CCI', 'TA_CDL2CROWS', 'TA_CDL3BLACKCROWS', 'TA_CDL3INSIDE', 'TA_CDL3LINESTRIKE', 'TA_CDL3OUTSIDE', 'TA_CDL3STARSINSOUTH', 'TA_CDL3WHITESOLDIERS', 'TA_CDLABANDONEDBABY', 'TA_CDLADVANCEBLOCK', 'TA_CDLBELTHOLD', 'TA_CDLBREAKAWAY', 'TA_CDLCLOSINGMARUBOZU', 'TA_CDLCONCEALBABYSWALL', 'TA_CDLCOUNTERATTACK', 'TA_CDLDARKCLOUDCOVER', 'TA_CDLDOJI', 'TA_CDLDOJISTAR', 'TA_CDLDRAGONFLYDOJI', 'TA_CDLENGULFING', 'TA_CDLEVENINGDOJISTAR', 'TA_CDLEVENINGSTAR', 'TA_CDLGAPSIDESIDEWHITE', 'TA_CDLGRAVESTONEDOJI', 'TA_CDLHAMMER', 'TA_CDLHANGINGMAN', 'TA_CDLHARAMI', 'TA_CDLHARAMICROSS', 'TA_CDLHIGHWAVE', 'TA_CDLHIKKAKE', 'TA_CDLHIKKAKEMOD', 'TA_CDLHOMINGPIGEON', 'TA_CDLIDENTICAL3CROWS', 'TA_CDLINNECK', 'TA_CDLINVERTEDHAMMER', 'TA_CDLKICKING', 'TA_CDLKICKINGBYLENGTH', 'TA_CDLLADDERBOTTOM', 'TA_CDLLONGLEGGEDDOJI', 'TA_CDLLONGLINE', 'TA_CDLMARUBOZU', 'TA_CDLMATCHINGLOW', 'TA_CDLMATHOLD', 'TA_CDLMORNINGDOJISTAR', 'TA_CDLMORNINGSTAR', 'TA_CDLONNECK', 'TA_CDLPIERCING', 'TA_CDLRICKSHAWMAN', 'TA_CDLRISEFALL3METHODS', 'TA_CDLSEPARATINGLINES', 'TA_CDLSHOOTINGSTAR', 'TA_CDLSHORTLINE', 'TA_CDLSPINNINGTOP', 'TA_CDLSTALLEDPATTERN', 'TA_CDLSTICKSANDWICH', 'TA_CDLTAKURI', 'TA_CDLTASUKIGAP', 'TA_CDLTHRUSTING', 'TA_CDLTRISTAR', 'TA_CDLUNIQUE3RIVER', 'TA_CDLUPSIDEGAP2CROWS', 'TA_CDLXSIDEGAP3METHODS', 'TA_CEIL', 'TA_CMO', 'TA_CORREL', 'TA_COS', 'TA_COSH', 'TA_DEMA', 'TA_DIV', 'TA_DX', 'TA_EMA', 'TA_EXP', 'TA_FLOOR', 'TA_HT_DCPERIOD', 'TA_HT_DCPHASE', 'TA_HT_PHASOR', 'TA_HT_SINE', 'TA_HT_TRENDLINE', 'TA_HT_TRENDMODE', 'TA_IMI', 'TA_KAMA', 'TA_LINEARREG', 'TA_LINEARREG_ANGLE', 'TA_LINEARREG_INTERCEPT', 'TA_LINEARREG_SLOPE', 'TA_LN', 'TA_LOG10', 'TA_MA', 'TA_MACD', 'TA_MACDEXT', 'TA_MACDFIX', 'TA_MAMA', 'TA_MAVP', 'TA_MAX', 'TA_MAXINDEX', 'TA_MEDPRICE', 'TA_MFI', 'TA_MIDPOINT', 'TA_MIDPRICE', 'TA_MIN', 'TA_MININDEX', 'TA_MINMAX', 'TA_MINMAXINDEX', 'TA_MINUS_DI', 'TA_MINUS_DM', 'TA_MOM', 'TA_MULT', 'TA_NATR', 'TA_OBV', 'TA_PLUS_DI', 'TA_PLUS_DM', 'TA_PPO', 'TA_ROC', 'TA_ROCP', 'TA_ROCR', 'TA_ROCR100', 'TA_RSI', 'TA_SAR', 'TA_SAREXT', 'TA_SIN', 'TA_SINH', 'TA_SMA', 'TA_SQRT', 'TA_STDDEV', 'TA_STOCH', 'TA_STOCHF', 'TA_STOCHRSI', 'TA_SUB', 'TA_SUM', 'TA_T3', 'TA_TAN', 'TA_TANH', 'TA_TEMA', 'TA_TRANGE', 'TA_TRIMA', 'TA_TRIX', 'TA_TSF', 'TA_TYPPRICE', 'TA_ULTOSC', 'TA_VAR', 'TA_WCLPRICE', 'TA_WILLR', 'TA_WMA', 'TC_FixedA', 'TC_FixedA2015', 'TC_FixedA2017', 'TC_TestStub', 'TC_Zero', 'TIME', 'TIMELINE', 'TIMELINEVOL', 'TR', 'TRACE', 'TURNOVER', 'TimeDelta', 'TimeLineList', 'TimeLineRecord', 'TradeCostBase', 'TradeManager', 'TradeRecord', 'TradeRecordList', 'TradeRequest', 'TransList', 'TransRecord', 'UPNDAY', 'VAR', 'VARP', 'VIGOR', 'WARN', 'WEAVE', 'WEEK', 'WINNER', 'WMA', 'YEAR', 'ZHBOND10', 'ZONGGUBEN', 'ZSCORE', 'batch_calculate_inds', 'can_upgrade', 'close_ostream_to_python', 'close_spend_time', 'combinate_ind', 'combinate_index', 'constant', 'crtBrokerTM', 'crtSEOptimal', 'crtTM', 'crt_pf_strategy', 'crt_sys_strategy', 'find_optimal_system', 'find_optimal_system_multi', 'get_block', 'get_business_name', 'get_data_from_buffer_server', 'get_date_range', 'get_kdata', 'get_last_version', 'get_log_level', 'get_stock', 'get_system_part_enum', 'get_system_part_name', 'get_version', 'get_version_git', 'get_version_with_build', 'hikyuu_init', 'inner_analysis_sys_list', 'inner_combinate_ind_analysis', 'inner_combinate_ind_analysis_with_block', 'isinf', 'isnan', 'open_ostream_to_python', 'open_spend_time', 'roundDown', 'roundEx', 'roundUp', 'run_in_strategy', 'set_log_level', 'set_python_in_interactive', 'set_python_in_jupyter', 'start_spot_agent', 'stop_spot_agent', 'toPriceList']
@typing.overload
def ABS() -> Indicator:
    ...
@typing.overload
def ABS(arg0: float) -> Indicator:
    ...
@typing.overload
def ABS(arg0: Indicator) -> Indicator:
    """
    ABS([data])
    
        求绝对值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def ACOS() -> Indicator:
    ...
@typing.overload
def ACOS(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def ACOS(arg0: float) -> Indicator:
    """
    ACOS([data])
    
        反余弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def AD() -> Indicator:
    ...
@typing.overload
def AD(arg0: KData) -> Indicator:
    """
    AD(kdata)
    
       累积/派发线
    
       :param KData kdata: k线数据
       :rtype: Indicator
    """
def ADVANCE(query: Query = ..., market: str = 'SH', stk_type: int = 1, ignore_context: bool = False, fill_null: bool = True) -> Indicator:
    """
    ADVANCE([query=Query(-100), market='SH', stk_type='constant.STOCKTYPE_A'])
    
        上涨家数。当存在指定上下文且 ignore_context 为 false 时，将忽略 query, market, stk_type 参数。
    
        :param Query query: 查询条件
        :param str market: 所属市场，等于 "" 时，获取所有市场
        :param int stk_type: 证券类型, 大于 constant.STOCKTYPE_TMP 时，获取所有类型证券
        :param bool ignore_context: 是否忽略上下文。忽略时，强制使用 query, market, stk_type 参数。
        :para. bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
        :rtype: Indicator
    """
def AF_EqualWeight() -> AllocateFundsBase:
    """
    AF_EqualWeight()
        
        等权重资产分配，对选中的资产进行等比例分配
    """
def AF_FixedWeight(weight: float = 0.1) -> AllocateFundsBase:
    """
    AF_FixedWeight(weight)
        
        固定比例资产分配
    
        :param float weight:  指定的资产比例 [0, 1]
    """
def AF_FixedWeightList(weights: list[float]) -> AllocateFundsBase:
    """
    AF_FixedWeightList(weights)
        
        固定比例资产分配列表.
    
        :param float weights:  指定的资产比例列表
    """
def AF_MultiFactor() -> AllocateFundsBase:
    """
    AF_MultiFactor()
          
        创建 MultiFactor 评分权重的资产分配算法实例, 即直接以SE返回的评分作为权重。
    """
@typing.overload
def ALIGN(ref: DatetimeList, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def ALIGN(data: Indicator, ref: DatetimeList, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def ALIGN(data: Indicator, ref: Indicator, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def ALIGN(data: Indicator, ref: KData, fill_null: bool = True) -> Indicator:
    """
    ALIGN(data, ref):
    
        按指定的参考日期对齐
    
        :param Indicator data: 输入数据
        :param DatetimeList|Indicator|KData ref: 指定做为日期参考的 DatetimeList、Indicator 或 KData
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
        :retype: Indicator
    """
@typing.overload
def AMA(n: int = 10, fast_n: int = 2, slow_n: int = 30) -> Indicator:
    ...
@typing.overload
def AMA(n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
@typing.overload
def AMA(data: Indicator, n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
@typing.overload
def AMA(data: Indicator, n: Indicator, fast_n: Indicator, slow_n: Indicator) -> Indicator:
    ...
@typing.overload
def AMA(data: Indicator, n: int = 10, fast_n: int = 2, slow_n: int = 30) -> Indicator:
    """
    AMA([data, n=10, fast_n=2, slow_n=30])
    
        佩里.J 考夫曼（Perry J.Kaufman）自适应移动平均 [BOOK1]_
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 计算均值的周期窗口，必须为大于2的整数
        :param int|Indicator|IndParam fast_n: 对应快速周期N
        :param int|Indicator|IndParam slow_n: 对应慢速EMA线的N值
        :rtype: Indicator
    
        * result(0): AMA
        * result(1): ER
    """
@typing.overload
def ASIN() -> Indicator:
    ...
@typing.overload
def ASIN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def ASIN(arg0: float) -> Indicator:
    """
    ASIN([data])
    
        反正弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def ATAN() -> Indicator:
    ...
@typing.overload
def ATAN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def ATAN(arg0: float) -> Indicator:
    """
    ATAN([data])
    
        反正切值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def ATR(n: int = 14) -> Indicator:
    ...
@typing.overload
def ATR(kdata: KData, n: int = 14) -> Indicator:
    """
    ATR([kdata, n=14])
    
        平均真实波幅(Average True Range), 真实波动幅度 TR 的简单移动均值
    
        :param KData kdata 待计算的源数据
        :param int n: 计算均值的周期窗口，必须为大于1的整数
        :rtype: Indicator
    """
@typing.overload
def AVEDEV(data: Indicator, n: int = 22) -> Indicator:
    ...
@typing.overload
def AVEDEV(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def AVEDEV(data: Indicator, n: Indicator) -> Indicator:
    """
    AVEDEV(data[, n=22])
    
        平均绝对偏差，求X的N日平均绝对偏差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def BACKSET(n: int = 2) -> Indicator:
    ...
@typing.overload
def BACKSET(n: IndParam) -> Indicator:
    ...
@typing.overload
def BACKSET(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def BACKSET(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def BACKSET(data: Indicator, n: int = 2) -> Indicator:
    """
    BACKSET([data, n=2])
    
        向前赋值将当前位置到若干周期前的数据设为1。
    
        用法：BACKSET(X,N),X非0,则将当前位置到N周期前的数值设为1。
    
        例如：BACKSET(CLOSE>OPEN,2)若收阳则将该周期及前一周期数值设为1,否则为0
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: N周期
        :rtype: Indicator
    """
@typing.overload
def BARSCOUNT() -> Indicator:
    ...
@typing.overload
def BARSCOUNT(arg0: Indicator) -> Indicator:
    """
    BARSCOUNT([data])
    
        有效值周期数, 求总的周期数。
    
        用法：BARSCOUNT(X)第一个有效数据到当前的天数。
    
        例如：BARSCOUNT(CLOSE)对于日线数据取得上市以来总交易日数，对于1分钟线取得当日交易分钟数。
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def BARSLAST() -> Indicator:
    ...
@typing.overload
def BARSLAST(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def BARSLAST(arg0: float) -> Indicator:
    """
    BARSLAST([data])
    
        上一次条件成立位置 上一次条件成立到当前的周期数。
    
        用法：BARSLAST(X): 上一次 X 不为 0 到现在的天数。
    
        例如：BARSLAST(CLOSE/REF(CLOSE,1)>=1.1) 表示上一个涨停板到当前的周期数
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def BARSSINCE() -> Indicator:
    ...
@typing.overload
def BARSSINCE(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def BARSSINCE(arg0: float) -> Indicator:
    """
    BARSSINCE([data])
    
        第一个条件成立位置到当前的周期数。
    
        用法：BARSSINCE(X):第一次X不为0到现在的天数。
    
        例如：BARSSINCE(HIGH>10)表示股价超过10元时到当前的周期数
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def BARSSINCEN(n: int) -> Indicator:
    ...
@typing.overload
def BARSSINCEN(cond: Indicator, n: int) -> Indicator:
    """
    BARSSINCEN(cond, n)
        
        N周期内第一个条件成立到当前的周期数
    
        用法：BARSSINCEN(X,N):N周期内第一次X不为0到现在的周期数,N为常量BARSSINCEN(X,N)
        例如：BARSSINCEN(HIGH>10,10)表示10个周期内股价超过10元时到当前的周期数
    
        :param Indicator cond: 条件
        :param int|Indicator n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: Indicator, arg1: float, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: Indicator, arg1: float, arg2: float) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: float, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: float, arg1: Indicator, arg2: float) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: float, arg1: float, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def BETWEEN(arg0: float, arg1: float, arg2: float) -> Indicator:
    """
    BETWEEN(a, b, c)
    
        介于(介于两个数之间)
    
        用法：BETWEEN(A,B,C)表示A处于B和C之间时返回1，否则返回0
    
        例如：BETWEEN(CLOSE,MA(CLOSE,10),MA(CLOSE,5))表示收盘价介于5日均线和10日均线之间
    
        :param Indicator a: A
        :param Indicator b: B
        :param Indicator c: C
        :rtype: Indicator
    """
@typing.overload
def BLOCKSETNUM(block: Block) -> Indicator:
    ...
@typing.overload
def BLOCKSETNUM(block: Block, query: Query) -> Indicator:
    """
    BLOCKSETNUM(block, query)
        
        横向统计（返回板块股个数）
    
        :param Block block: 待统计的板块
        :param Query query: 统计范围
    """
@typing.overload
def BLOCKSETNUM(stks: typing.Sequence) -> Indicator:
    ...
@typing.overload
def BLOCKSETNUM(stks: typing.Sequence, query: Query) -> Indicator:
    """
    BLOCKSETNUM(block, query)
        
        横向统计（返回板块股个数）
    
        :param Sequence stks: stock list
        :param Query query: 统计范围
    """
@typing.overload
def CEILING() -> Indicator:
    ...
@typing.overload
def CEILING(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def CEILING(arg0: float) -> Indicator:
    """
    CEILING([data])
    
        向上舍入(向数值增大方向舍入)取整
       
        用法：CEILING(A)返回沿A数值增大方向最接近的整数
       
        例如：CEILING(12.3)求得13；CEILING(-3.5)求得-3
       
        :param data: 输入数据
        :rtype: Indicator
    """
def CN_Bool(arg0: Indicator) -> ConditionBase:
    """
    CN_Bool(ind)
    
        布尔信号指标系统有效条件, 指标中相应位置>0则代表系统有效，否则无效
    
        :param Indicator ind: bool型指标，输入为 KData
        :return: 系统有效条件实例
        :rtype: ConditionBase
    """
def CN_OPLine(arg0: Indicator) -> ConditionBase:
    """
    CN_OPLine(ind)
    
        固定使用股票最小交易量进行交易，计算权益曲线的ind值，当权益曲线高于ind时，系统有效，否则无效。
    
        :param Indicator ind: Indicator实例
        :return: 系统有效条件实例
        :rtype: ConditionBase
    """
@typing.overload
def CONTEXT(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def CONTEXT(ind: Indicator, fill_null: bool = True) -> Indicator:
    """
    CONTEXT(ind)
        
        独立上下文。使用 ind 自带的上下文。当指定新的上下文时，不会改变已有的上下文。
        例如：ind = CLOSE(k1), 当指定新的上下文 ind = ind(k2) 时，使用的是 k2 的收盘价。如想仍使用 k1 收盘价，
        则需使用 ind = CONTEXT(CLOSE(k1)), 此时 ind(k2) 将仍旧使用 k1 的收盘价。
        
        :param Indicator ind: 指标对象
        :param bool fill_null: 日期对齐时，缺失日期对应填充空值
        :rtype: Indicator
    """
def CONTEXT_K(arg0: Indicator) -> KData:
    """
    CONTEXT_K(ind)
    
        获取指标上下文。Indicator::getContext()方法获取的是当前的上下文，但对于 CONTEXT 独立上下文指标无法获取其指定的独立上下文，需用此方法获取
    
        :param Indicator ind: 指标对象
        :rtype: KData
    """
@typing.overload
def CORR(ref_ind: Indicator, n: int = 10, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def CORR(ind: Indicator, ref_ind: Indicator, n: int = 10, fill_null: bool = True) -> Indicator:
    """
    CORR(ind, ref_ind[, n=10, fill_null=True])
    
        计算 ind 和 ref_ind 的相关系数。返回中存在两个结果，第一个为相关系数，第二个为协方差。
        与 CORR(ref_ind, n)(ind) 等效。
    
        :param Indicator ind: 指标1
        :param Indicator ref_ind: 指标2
        :param int n: 按指定 n 的长度计算两个 ind 直接数据相关系数。如果为0，使用输入的ind长度。
        :param bool fill_null: 日期对齐时缺失日期填充nan值
        :rtype: Indicator
    """
@typing.overload
def COS() -> Indicator:
    ...
@typing.overload
def COS(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def COS(arg0: float) -> Indicator:
    """
    COS([data])
    
        余弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def COST(x: float = 10.0) -> Indicator:
    ...
@typing.overload
def COST(k: KData, x: float = 10.0) -> Indicator:
    """
    COST(k[, x=10.0])
    
        成本分布。该函数仅对日线分析周期有效，对不能存在流通盘权息数据的指数、ETF等无效。
        用法：COST(k, X) 表示X%获利盘的价格是多少
        例如：COST(k, 10),表示10%获利盘的价格是多少，即有10%的持仓量在该价格以下，其余90%在该价格以上，为套牢盘
    
        :param KData k: 关联的K线数据
        :param float x: x%获利价格, 0~100
        :rtype: Indicator
    """
@typing.overload
def COUNT(n: int = 20) -> Indicator:
    ...
@typing.overload
def COUNT(n: IndParam) -> Indicator:
    ...
@typing.overload
def COUNT(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def COUNT(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def COUNT(data: Indicator, n: int = 20) -> Indicator:
    """
    COUNT([data, n=20])
    
        统计满足条件的周期数。
    
        用法：COUNT(X,N),统计N周期中满足X条件的周期数,若N=0则从第一个有效值开始。
    
        例如：COUNT(CLOSE>OPEN,20)表示统计20周期内收阳的周期数
    
        :param Indicator data: 条件
        :param int|Indicator|IndParam n: 周期
        :rtype: Indicator
    """
@typing.overload
def CROSS(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def CROSS(arg0: Indicator, arg1: float) -> Indicator:
    ...
@typing.overload
def CROSS(arg0: float, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def CROSS(arg0: float, arg1: float) -> Indicator:
    """
    CROSS(x, y)
    
        交叉函数
    
        :param x: 变量或常量，判断交叉的第一条线
        :param y: 变量或常量，判断交叉的第二条线
        :rtype: Indicator
    """
@typing.overload
def CVAL(value: float = 0.0, discard: int = 0) -> Indicator:
    ...
@typing.overload
def CVAL(data: Indicator, value: float = 0.0, discard: int = 0) -> Indicator:
    """
    CVAL([data, value=0.0, discard=0])
    
        data 为 Indicator 实例，创建和 data 等长的常量指标，其值和为value，抛弃长度discard和data一样
    
        :param Indicator data: Indicator实例
        :param float value: 常数值
        :param int discard: 抛弃数量
        :rtype: Indicator
    """
@typing.overload
def CYCLE(adjust_cycle: int = 1, adjust_mode: str = 'query', delay_to_trading_day: bool = True) -> Indicator:
    ...
@typing.overload
def CYCLE(kdata: KData, adjust_cycle: int = 1, adjust_mode: str = 'query', delay_to_trading_day: bool = True) -> Indicator:
    """
    CYCLE(kdata, [adjust_cycle=1], [adjust_mode='query'], [delay_to_trading_day=True])
              
        PF调仓周期指标，主要用于PF调仓日验证，及作为SG
    
        :param KData kdata: K线数据
        :param int adjust_cycle: 调整周期
        :param string adjust_mode: 调整方式
        :param bool delay_to_trading_day: 调整周期是否延至交易日
        :rtype: Indicator
    """
@typing.overload
def C_AMO(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_AMO() -> Indicator:
    """
    AMO([data])
    
        获取成交金额，包装KData的成交金额成Indicator
        
        :param data: 输入数据（KData 或 Indicator）
        :rtype: Indicator
    """
@typing.overload
def C_CLOSE(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_CLOSE() -> Indicator:
    """
    CLOSE([data])
    
        获取收盘价，包装KData的收盘价成Indicator
    
        :param data: 输入数据（KData 或 Indicator）
        :rtype: Indicator
    """
@typing.overload
def C_HIGH(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_HIGH() -> Indicator:
    """
    HIGH([data])
    
        获取最高价，包装KData的最高价成Indicator
    
        :param data: 输入数据（KData 或 Indicator） 
        :rtype: Indicator
    """
@typing.overload
def C_KDATA(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_KDATA() -> Indicator:
    """
    KDATA([data])
    
        包装KData成Indicator，用于其他指标计算
    
        :param data: KData 或 具有6个返回结果的Indicator（如KDATA生成的Indicator）
        :rtype: Indicator
    """
@typing.overload
def C_LOW(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_LOW() -> Indicator:
    """
    LOW([data])
    
        获取最低价，包装KData的最低价成Indicator
    
        :param data: 输入数据（KData 或 Indicator） 
        :rtype: Indicator
    """
@typing.overload
def C_OPEN(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_OPEN() -> Indicator:
    """
    OPEN([data])
    
        获取开盘价，包装KData的开盘价成Indicator
    
        :param data: 输入数据（KData 或 Indicator） 
        :rtype: Indicator
    """
@typing.overload
def C_VOL(arg0: KData) -> Indicator:
    ...
@typing.overload
def C_VOL() -> Indicator:
    """
    VOL([data])
    
        获取成交量，包装KData的成交量成Indicator
    
        :param data: 输入数据（KData 或 Indicator）
        :rtype: Indicator
    """
@typing.overload
def DATE() -> Indicator:
    ...
@typing.overload
def DATE(arg0: KData) -> Indicator:
    """
    DATE([data])
    
        取得该周期从1900以来的年月日。用法: DATE 例如函数返回1000101，表示2000年1月1日。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
@typing.overload
def DAY() -> Indicator:
    ...
@typing.overload
def DAY(arg0: KData) -> Indicator:
    """
    DAY([data])
    
        取得该周期的日期。用法: DAY 函数返回有效值范围为(1-31)。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
def DECLINE(query: Query = ..., market: str = 'SH', stk_type: int = 1, ignore_context: bool = False, fill_null: bool = True) -> Indicator:
    """
    DECLINE([query=Query(-100), market='SH', stk_type='constant.STOCKTYPE_A'])
    
        下跌家数。当存在指定上下文且 ignore_context 为 false 时，将忽略 query, market, stk_type 参数。
    
        :param Query query: 查询条件
        :param str market: 所属市场，等于 "" 时，获取所有市场
        :param int stk_type: 证券类型, 大于 constant.STOCKTYPE_TMP 时，获取所有类型证券
        :param bool ignore_context: 是否忽略上下文。忽略时，强制使用 query, market, stk_type 参数。
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
        :rtype: Indicator
    """
@typing.overload
def DEVSQ(n: int = 10) -> Indicator:
    ...
@typing.overload
def DEVSQ(n: IndParam) -> Indicator:
    ...
@typing.overload
def DEVSQ(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def DEVSQ(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def DEVSQ(data: Indicator, n: int = 10) -> Indicator:
    """
    DEVSQ([data, n=10])
    
        数据偏差平方和，求X的N日数据偏差平方和
    
        :param Indicator data: 输入数据
        :param int|Indicator n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def DIFF() -> Indicator:
    ...
@typing.overload
def DIFF(arg0: Indicator) -> Indicator:
    """
    DIFF([data])
    
        差分指标，即data[i] - data[i-1]
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def DISCARD(discard: int) -> Indicator:
    ...
@typing.overload
def DISCARD(ind: Indicator, discard: int) -> Indicator:
    """
    DISCARD(data, discard)
        
        以指标公式的方式设置指标结果的丢弃数据量。
    
        :param Indicator data: 指标
        :param int discard: 丢弃数据量
        :rtype: Indicator
    """
def DMA(x: Indicator, a: Indicator, fill_null: bool = True) -> Indicator:
    """
    DMA(ind, a[, fill_null=True])
    
        动态移动平均
    
        用法：DMA(X,A),求X的动态移动平均。
    
        算法：若Y=DMA(X,A) 则 Y=A*X+(1-A)*Y',其中Y'表示上一周期Y值。
    
        例如：DMA(CLOSE,VOL/CAPITAL)表示求以换手率作平滑因子的平均价
    
        :param Indicator ind: 输入数据
        :param Indicator a: 动态系数
        :param bool fill_null: 日期对齐时缺失数据填充 nan 值。
        :rtype: Indicator
    """
@typing.overload
def DOWNNDAY(data: Indicator, n: int = 3) -> Indicator:
    ...
@typing.overload
def DOWNNDAY(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def DOWNNDAY(data: Indicator, n: Indicator) -> Indicator:
    """
    DOWNNDAY(data[, n=3])
    
        连跌周期数, DOWNNDAY(CLOSE,M)表示连涨M个周期
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def DROPNA() -> Indicator:
    ...
@typing.overload
def DROPNA(arg0: Indicator) -> Indicator:
    """
    DROPNA([data])
    
        删除 nan 值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
def Days(arg0: int) -> TimeDelta:
    """
    Days(days)
    
          TimeDelta 快捷创建函数
    
          :param int days: 天数 [-99999999, 99999999]
          :rtype: TimeDelta
    """
@typing.overload
def EMA(n: int = 22) -> Indicator:
    ...
@typing.overload
def EMA(n: IndParam) -> Indicator:
    ...
@typing.overload
def EMA(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def EMA(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def EMA(data: Indicator, n: int = 22) -> Indicator:
    """
    EMA([data, n=22])
    
        指数移动平均线(Exponential Moving Average)
    
        :param data: 输入数据
        :param int|Indicator|IndParam n n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
@typing.overload
def EVERY(n: int = 20) -> Indicator:
    ...
@typing.overload
def EVERY(n: IndParam) -> Indicator:
    ...
@typing.overload
def EVERY(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def EVERY(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def EVERY(data: Indicator, n: int = 20) -> Indicator:
    """
    EVERY([data, n=20])
    
        一直存在
    
        用法：EVERY (X,N) 表示条件X在N周期一直存在
    
        例如：EVERY(CLOSE>OPEN,10) 表示前10日内一直是阳线
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
def EV_Bool(ind: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_Bool(ind, market='SH')
    
        布尔信号指标市场环境
    
        :param Indicator ind: bool类型的指标，指标中相应位置>0则代表市场有效，否则无效
        :param str market: 指定的市场，用于获取相应的交易日历
    """
def EV_TwoLine(fast: Indicator, slow: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_TwoLine(fast, slow[, market = 'SH'])
    
        快慢线判断策略，市场指数的快线大于慢线时，市场有效，否则无效。
    
        :param Indicator fast: 快线指标
        :param Indicator slow: 慢线指标
        :param string market: 市场名称
    """
@typing.overload
def EXIST(n: int = 20) -> Indicator:
    ...
@typing.overload
def EXIST(n: IndParam) -> Indicator:
    ...
@typing.overload
def EXIST(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def EXIST(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def EXIST(data: Indicator, n: int = 20) -> Indicator:
    """
    EXIST([data, n=20])
    
        存在, EXIST(X,N) 表示条件X在N周期有存在
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
@typing.overload
def EXP() -> Indicator:
    ...
@typing.overload
def EXP(arg0: float) -> Indicator:
    ...
@typing.overload
def EXP(arg0: Indicator) -> Indicator:
    """
    EXP([data])
    
        EXP(X)为e的X次幂
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def FILTER(n: int = 5) -> Indicator:
    ...
@typing.overload
def FILTER(n: IndParam) -> Indicator:
    ...
@typing.overload
def FILTER(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def FILTER(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def FILTER(data: Indicator, n: int = 5) -> Indicator:
    """
    FILTER([data, n=5])
    
        信号过滤, 过滤连续出现的信号。
    
        用法：FILTER(X,N): X 满足条件后，删除其后 N 周期内的数据置为 0。
    
        例如：FILTER(CLOSE>OPEN,5) 查找阳线，5 天内再次出现的阳线不被记录在内。
    
        :param Indicator data: 输入数据
        :param int|Indicaot|IndParam n: 过滤周期
        :rtype: Indicator
    """
@typing.overload
def FINANCE(ix: int) -> Indicator:
    ...
@typing.overload
def FINANCE(name: str) -> Indicator:
    ...
@typing.overload
def FINANCE(kdata: KData, ix: int) -> Indicator:
    ...
@typing.overload
def FINANCE(kdata: KData, name: str) -> Indicator:
    """
    FINANCE([kdata, ix, name])
    
        获取历史财务信息。（可通过 StockManager.get_history_finance_all_fields 查询相应的历史财务字段信息）
    
        ix, name 使用时，为二选一。即要不使用 ix，要不就使用 name 进行获取。
    
        :param KData kdata: K线数据
        :param int ix: 历史财务信息字段索引
        :param int name: 历史财务信息字段名称
    """
@typing.overload
def FLOOR() -> Indicator:
    ...
@typing.overload
def FLOOR(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def FLOOR(arg0: float) -> Indicator:
    """
    FLOOR([data])
    
        向下舍入(向数值减小方向舍入)取整
    
        用法：FLOOR(A)返回沿A数值减小方向最接近的整数
    
        例如：FLOOR(12.3)求得12
    
        :param data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def HHV(n: int = 20) -> Indicator:
    ...
@typing.overload
def HHV(n: IndParam) -> Indicator:
    ...
@typing.overload
def HHV(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def HHV(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def HHV(data: Indicator, n: int = 20) -> Indicator:
    """
    HHV([data, n=20])
    
        N日内最高价，N=0则从第一个有效值开始。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
@typing.overload
def HHVBARS(n: int = 20) -> Indicator:
    ...
@typing.overload
def HHVBARS(n: IndParam) -> Indicator:
    ...
@typing.overload
def HHVBARS(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def HHVBARS(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def HHVBARS(data: Indicator, n: int = 20) -> Indicator:
    """
    HHVBARS([data, n=20])
    
        上一高点位置 求上一高点到当前的周期数。
    
        用法：HHVBARS(X,N):求N周期内X最高值到当前周期数N=0表示从第一个有效值开始统计
    
        例如：HHVBARS(HIGH,0)求得历史新高到到当前的周期数
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
@typing.overload
def HOUR() -> Indicator:
    ...
@typing.overload
def HOUR(arg0: KData) -> Indicator:
    """
    HOUR([data])
    
        取得该周期的小时数。用法：HOUR 函数返回有效值范围为(0-23)，对于日线及更长的分析周期值为0。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
@typing.overload
def HSL() -> Indicator:
    ...
@typing.overload
def HSL(arg0: KData) -> Indicator:
    """
    HSL(kdata)
    
        获取换手率, 乘以 100 才是百分比，等于 VOL(k) / CAPITAL(k) * 0.01
    
        :param KData kdata: k线数据
        :rtype: Indicator
    """
def Hours(arg0: int) -> TimeDelta:
    """
    Hours(hours)
    
          TimeDelta 快捷创建函数
    
          :param int hours: 小时数
          :rtype: TimeDelta
    """
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
@typing.overload
def IF(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def IF(arg0: Indicator, arg1: float, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def IF(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
@typing.overload
def IF(arg0: Indicator, arg1: float, arg2: float) -> Indicator:
    """
    IF(x, a, b)
    
        条件函数, 根据条件求不同的值。
    
        用法：IF(X,A,B)若X不为0则返回A,否则返回B
    
        例如：IF(CLOSE>OPEN,HIGH,LOW)表示该周期收阳则返回最高值,否则返回最低值
    
        :param Indicator x: 条件指标
        :param Indicator a: 待选指标 a
        :param Indicator b: 待选指标 b
        :rtype: Indicator
    """
@typing.overload
def INBLOCK(category: str, name: str) -> Indicator:
    ...
@typing.overload
def INBLOCK(data: KData, category: str, name: str) -> Indicator:
    """
    INBLOCK(data, category, name)        
    
        当前上下文证券是否在指定的板块中。
    
        :param KData data: 指定的K线数据(上下文)
        :param string category: 板块类别
        :param string name: 板块名称
        :rtype: Indicator
    """
@typing.overload
def INDEXA(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INDEXA(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXA([kdata])
        
        返回对应的大盘成交金额,分别是上证指数,深证成指,科创50,创业板指
    """
@typing.overload
def INDEXADV() -> Indicator:
    ...
@typing.overload
def INDEXADV(arg0: Query) -> Indicator:
    """
    INDEXADV([query])
        
        通达信 880005 大盘上涨家数, 可能无法盘中更新!
    """
@typing.overload
def INDEXC(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INDEXC(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXC([kdata])
        
        返回对应的大盘收盘价,分别是上证指数,深证成指,科创50,创业板指
    """
@typing.overload
def INDEXDEC() -> Indicator:
    ...
@typing.overload
def INDEXDEC(arg0: Query) -> Indicator:
    """
    INDEXDEC([query])
        
        通达信 880005 大盘下跌家数, 可能无法盘中更新!
    """
@typing.overload
def INDEXH(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INDEXH(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXH([kdata])
        
        返回对应的大盘最高价,分别是上证指数,深证成指,科创50,创业板指
    """
@typing.overload
def INDEXL(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INDEXL(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXL([kdata])
        
        返回对应的大盘最低价,分别是上证指数,深证成指,科创50,创业板指
    """
@typing.overload
def INDEXO(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INDEXO(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXO([kdata])
        
        返回对应的大盘开盘价,分别是上证指数,深证成指,科创50,创业板指
    """
@typing.overload
def INDEXV(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INDEXV(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXV([kdata])
        
        返回对应的大盘成交量,分别是上证指数,深证成指,科创50,创业板指
    """
@typing.overload
def INSUM(block: Block, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INSUM(block: Block, query: Query, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    """
    INSUM(block, query, ind, mode[, fill_null=True])
    
        返回板块各成分该指标相应输出按计算类型得到的计算值.计算类型:0-累加,1-平均数,2-最大值,3-最小值.
    
        :param Block block: 指定板块
        :param Query query: 指定范围
        :param Indicator ind: 指定指标
        :param int mode: 计算类型:0-累加,1-平均数,2-最大值,3-最小值.
        :param bool fill_null: 日期对齐时缺失数据填充 nan 值。
        :rtype: Indicator
    """
@typing.overload
def INSUM(stks: typing.Sequence, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def INSUM(stks: typing.Sequence, query: Query, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    """
    INSUM(stks, query, ind, mode[, fill_null=True])
    
        返回板块各成分该指标相应输出按计算类型得到的计算值.计算类型:0-累加,1-平均数,2-最大值,3-最小值.
    
        :param Sequence stks: stock list
        :param Query query: 指定范围
        :param Indicator ind: 指定指标
        :param int mode: 计算类型:0-累加,1-平均数,2-最大值,3-最小值.
        :param bool fill_null: 日期对齐时缺失数据填充 nan 值。
        :rtype: Indicator
    """
@typing.overload
def INTPART() -> Indicator:
    ...
@typing.overload
def INTPART(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def INTPART(arg0: float) -> Indicator:
    """
    INTPART([data])
    
        取整(绝对值减小取整，即取得数据的整数部分)
    
        :param data: 输入数据
        :rtype: Indicator
    """
def IR(p: Indicator, b: Indicator, n: int = 100) -> Indicator:
    """
    IR(p, b[, n])
    
        信息比率（Information Ratio，IR）
    
        公式: (P-B) / TE
        P: 组合收益率
        B: 比较基准收益率
        TE: 投资周期中每天的 p 和 b 之间的标准差
        实际使用时，P 一般为 TM 的资产曲线，B 为沪深 3000 收盘价，如:
        ref_k = sm["sh000300"].get_kdata(query)
        funds = my_tm.get_funds_curve(ref_k.get_datetime.list())
        ir = IR(PRICELIST(funds), ref_k.close, 0)
    
        :param Indicator p:
        :param Indicator b:
        :param int n: 时间窗口，如果只想使用最后的值，可以使用 0, 或 len(p),len(b) 指定
    """
@typing.overload
def ISINF() -> Indicator:
    ...
@typing.overload
def ISINF(ind: Indicator) -> Indicator:
    """
    ISINF(ind)
    
        判断指标是否为正无穷大 (+inf) 值，若为 +inf 值, 则返回1, 否则返回0。如判断负无穷大, 使用 ISINFA。
    
        :param Indicator ind: 指定指标
        :rtype: Indicator
    """
@typing.overload
def ISINFA() -> Indicator:
    ...
@typing.overload
def ISINFA(ind: Indicator) -> Indicator:
    """
    ISINFA(ind)
    
        判断指标是否为负无穷大 (-inf) 值，若为 -inf 值, 则返回1, 否则返回0。如判断正无穷大, 使用 ISINF。
    
        :param Indicator ind: 指定指标
        :rtype: Indicator
    """
@typing.overload
def ISLASTBAR() -> Indicator:
    ...
@typing.overload
def ISLASTBAR(data: KData) -> Indicator:
    ...
@typing.overload
def ISLASTBAR(data: Indicator) -> Indicator:
    """
    ISLASTBAR(ind)
    
        判断当前数据是否为最后一个数据，若为最后一个数据，则返回1，否则返回0.
    
        :param Indicator|KData data: 指定指标
        :rtype: Indicator
    """
@typing.overload
def ISNA(ignore_discard: bool = False) -> Indicator:
    ...
@typing.overload
def ISNA(ind: Indicator, ignore_discard: bool = False) -> Indicator:
    """
    ISNA(ind[, ignore_discard=False])
    
        判断指标是否为 nan 值，若为 nan 值, 则返回1, 否则返回0.
    
        :param Indicator ind: 指定指标
        :param bool ignore_discard: 忽略指标丢弃数据
    """
@typing.overload
def JUMPDOWN() -> Indicator:
    ...
@typing.overload
def JUMPDOWN(arg0: Indicator) -> Indicator:
    """
    JUMPDOWN([ind])
        
        边缘跳变，从大于0.0，跳变到 <= 0.0
    
        :param Indicator ind: 指标
        :rtype: Indicator
    """
@typing.overload
def JUMPUP() -> Indicator:
    ...
@typing.overload
def JUMPUP(arg0: Indicator) -> Indicator:
    """
    JUMPUP([ind])
        
        边缘跳变，从小于等于0.0，跳变到 > 0.0
        
        :param Indicator ind: 指标
        :rtype: Indicator
    """
@typing.overload
def KALMAN(q: float = 0.01, r: float = 0.1) -> Indicator:
    ...
@typing.overload
def KALMAN(ind: Indicator, q: float = 0.01, r: float = 0.1) -> Indicator:
    """
    KALMAN(ind, [q=0.01], [r=0.1])
    
        Kalman滤波器, 用于平滑指标, 可设置平滑系数q和r, 默认q=0.01, r=0.1
    
        :param Indicator ind: 指标
        :param float q: 平滑系数
        :param float r: 噪声系数
        :rtype: Indicator
    """
@typing.overload
def KDATA_PART(data: KData, kpart: str) -> Indicator:
    ...
@typing.overload
def KDATA_PART(kpart: str) -> Indicator:
    """
    KDATA_PART([data, kpart])
    
        根据字符串选择返回指标KDATA/OPEN/HIGH/LOW/CLOSE/AMO/VOL，如:KDATA_PART("CLOSE")等同于CLOSE()
    
        :param data: 输入数据（KData 或 Indicator） 
        :param string kpart: KDATA|OPEN|HIGH|LOW|CLOSE|AMO|VOL
        :rtype: Indicator
    """
@typing.overload
def LAST(m: int = 10, n: int = 5) -> Indicator:
    ...
@typing.overload
def LAST(m: int, n: IndParam) -> Indicator:
    ...
@typing.overload
def LAST(m: IndParam, n: int = 5) -> Indicator:
    ...
@typing.overload
def LAST(m: IndParam, n: IndParam) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: int = 10, n: int = 5) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: int, n: IndParam) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: IndParam, n: int = 5) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: IndParam, n: IndParam) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: int, n: Indicator) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: Indicator, n: int = 5) -> Indicator:
    ...
@typing.overload
def LAST(data: Indicator, m: Indicator, n: Indicator) -> Indicator:
    """
    LAST([data, m=10, n=5])
    
        区间存在。
    
        用法：LAST (X,M,N) 表示条件 X 在前 M 周期到前 N 周期存在。
    
        例如：LAST(CLOSE>OPEN,10,5) 表示从前10日到前5日内一直阳线。
    
        :param data: 输入数据
        :param int|Indicator|IndParam m: m周期
        :param int|Indicator|IndParam n: n周期
        :rtype: Indicator
    """
@typing.overload
def LASTVALUE(ignore_discard: bool = False) -> Indicator:
    ...
@typing.overload
def LASTVALUE(ind: Indicator, ignore_discard: bool = False) -> Indicator:
    """
    LASTVALUE(ind, [ignore_discard=False])
    
        等同于通达信CONST指标。取输入指标最后值为常数, 即结果中所有值均为输入指标的最后值, 谨慎使用。含未来函数, 谨慎使用。
    
        :param Indicator ind: 指标
        :param bool ignore_discard: 忽略指标丢弃数据
        :rtype: Indicator
    """
@typing.overload
def LIUTONGPAN() -> Indicator:
    ...
@typing.overload
def LIUTONGPAN(arg0: KData) -> Indicator:
    """
    LIUTONGPAN(kdata)
    
       获取流通盘（单位：万股），同 CAPITAL
    
       :param KData kdata: k线数据
       :rtype: Indicator
    """
@typing.overload
def LLV(n: int = 20) -> Indicator:
    ...
@typing.overload
def LLV(n: IndParam) -> Indicator:
    ...
@typing.overload
def LLV(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def LLV(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def LLV(data: Indicator, n: int = 20) -> Indicator:
    """
    LLV([data, n=20])
    
        N日内最低价，N=0则从第一个有效值开始。
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
@typing.overload
def LLVBARS(n: int = 20) -> Indicator:
    ...
@typing.overload
def LLVBARS(n: IndParam) -> Indicator:
    ...
@typing.overload
def LLVBARS(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def LLVBARS(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def LLVBARS(data: Indicator, n: int = 20) -> Indicator:
    """
    LLVBARS([data, n=20])
    
        上一低点位置 求上一低点到当前的周期数。
    
        用法：LLVBARS(X,N):求N周期内X最低值到当前周期数N=0表示从第一个有效值开始统计
    
        例如：LLVBARS(HIGH,20)求得20日最低点到当前的周期数
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
@typing.overload
def LN() -> Indicator:
    ...
@typing.overload
def LN(arg0: float) -> Indicator:
    ...
@typing.overload
def LN(arg0: Indicator) -> Indicator:
    """
    LN([data])
    
        求自然对数, LN(X)以e为底的对数
    
        :param data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def LOG() -> Indicator:
    ...
@typing.overload
def LOG(arg0: float) -> Indicator:
    ...
@typing.overload
def LOG(arg0: Indicator) -> Indicator:
    """
    LOG([data])
    
        以10为底的对数
    
        :param data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def LONGCROSS(a: Indicator, b: Indicator, n: int = 3) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: Indicator, b: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: Indicator, b: float, n: int = 3) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: Indicator, b: float, n: Indicator) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: float, b: Indicator, n: int = 3) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: float, b: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: float, b: float, n: int = 3) -> Indicator:
    ...
@typing.overload
def LONGCROSS(a: float, b: float, n: Indicator) -> Indicator:
    """
    LONGCROSS(a, b[, n=3])
    
        两条线维持一定周期后交叉
    
        用法：LONGCROSS(A,B,N)表示A在N周期内都小于B，本周期从下方向上穿过B时返 回1，否则返回0
    
        例如：LONGCROSS(MA(CLOSE,5),MA(CLOSE,10),5)表示5日均线维持5周期后与10日均线交金叉
    
        :param Indicator a:
        :param Indicator b:
        :param int|Indicator n:
        :rtype: Indicator
    """
@typing.overload
def MA(n: int = 22) -> Indicator:
    ...
@typing.overload
def MA(n: IndParam) -> Indicator:
    ...
@typing.overload
def MA(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def MA(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def MA(data: Indicator, n: int = 22) -> Indicator:
    """
    MA([data, n=22])
    
        简单移动平均
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def MACD(n1: int = 12, n2: int = 26, n3: int = 9) -> Indicator:
    ...
@typing.overload
def MACD(n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
@typing.overload
def MACD(data: Indicator, n1: int = 12, n2: int = 26, n3: int = 9) -> Indicator:
    ...
@typing.overload
def MACD(data: Indicator, n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
@typing.overload
def MACD(data: Indicator, n1: Indicator, n2: Indicator, n3: Indicator) -> Indicator:
    """
    MACD([data, n1=12, n2=26, n3=9])
    
        平滑异同移动平均线
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n1: 短期EMA时间窗
        :param int|Indicator|IndParam n2: 长期EMA时间窗
        :param int|Indicator|IndParam n3: （短期EMA-长期EMA）EMA平滑时间窗
        :rtype: 具有三个结果集的 Indicator
    
        * result(0): MACD_BAR：MACD直柱，即MACD快线－MACD慢线
        * result(1): DIFF: 快线,即（短期EMA-长期EMA）
        * result(2): DEA: 慢线，即快线的n3周期EMA平滑
    """
@typing.overload
def MAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def MAX(arg0: Indicator, arg1: float) -> Indicator:
    ...
@typing.overload
def MAX(arg0: float, arg1: Indicator) -> Indicator:
    """
    MAX(ind1, ind2)
    
        求最大值, MAX(A,B)返回A和B中的较大值。
    
        :param Indicator ind1: A
        :param Indicator ind2: B
        :rtype: Indicator
    """
@typing.overload
def MDD() -> Indicator:
    ...
@typing.overload
def MDD(arg0: Indicator) -> Indicator:
    """
    MDD([data])
        
        当前价格相对历史最高值的回撤百分比，通常用于计算最大回撤
    """
@typing.overload
def MF_EqualWeight() -> MultiFactorBase:
    ...
@typing.overload
def MF_EqualWeight(inds: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5])
    
        等权重合成因子
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
@typing.overload
def MF_ICIRWeight() -> MultiFactorBase:
    ...
@typing.overload
def MF_ICIRWeight(inds: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, ic_rolling_n: int = 120, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5, ic_rolling_n=120])
    
        滚动ICIR权重合成因子
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param int ic_rolling_n: IC 滚动周期
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
@typing.overload
def MF_ICWeight() -> MultiFactorBase:
    ...
@typing.overload
def MF_ICWeight(inds: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, ic_rolling_n: int = 120, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5, ic_rolling_n=120])
    
        滚动IC权重合成因子
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk:  (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param int ic_rolling_n: IC 滚动周期
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
@typing.overload
def MF_Weight() -> MultiFactorBase:
    ...
@typing.overload
def MF_Weight(inds: typing.Sequence, weights: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5])
    
        按指定权重合成因子 = ind1 * weight1 + ind2 * weight2 + ... + indn * weightn
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(float) weights: 权重列表(需和 inds 等长)
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
@typing.overload
def MIN(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def MIN(arg0: Indicator, arg1: float) -> Indicator:
    ...
@typing.overload
def MIN(arg0: float, arg1: Indicator) -> Indicator:
    """
    MIN(ind1, ind2)
    
        求最小值, MIN(A,B)返回A和B中的较小值。
    
        :param Indicator ind1: A
        :param Indicator ind2: B
        :rtype: Indicator
    """
@typing.overload
def MINUTE() -> Indicator:
    ...
@typing.overload
def MINUTE(arg0: KData) -> Indicator:
    """
    MINUTE([data])
    
        取得该周期的分钟数。用法：MINUTE 函数返回有效值范围为(0-59)，对于日线及更长的分析周期值为0。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
def MM_FixedCapital(capital: float = 10000.0) -> MoneyManagerBase:
    """
    MM_FixedCapital([capital = 10000.0])
    
        固定资金管理策略。买入数量 = 当前现金 / capital
    
        :param float capital: 固定资本单位
        :return: 资金管理策略实例
    """
def MM_FixedCapitalFunds(capital: float = 10000.0) -> MoneyManagerBase:
    """
    MM_FixedCapitalFunds([capital = 10000.0]) 
    
        固定资本管理策略。买入数量 = 当前总资产 / capital
      
        :param float capital: 固定资本单位
        :return: 资金管理策略实例
    """
def MM_FixedCount(n: float = 100) -> MoneyManagerBase:
    """
    MM_FixedCount([n = 100])
    
        固定交易数量资金管理策略。每次买入固定的数量。
        
        :param float n: 每次买入的数量（应该是交易对象最小交易数量的整数，此处程序没有此进行判断）
        :return: 资金管理策略实例
    """
def MM_FixedCountTps(buy_counts: list[float], sell_counts: list[float]) -> MoneyManagerBase:
    """
    MM_FixedCountTps([buy_counts, sell_counts])
              
        连续买入/卖出固定数量资金管理策略。
        
        :param list buy_counts: 买入数量列表
        :param list sell_counts: 卖出数量列表
        :return: 资金管理策略实例
    """
def MM_FixedPercent(p: float = 0.03) -> MoneyManagerBase:
    """
    MM_FixedPercent([p = 0.03])
    
        固定百分比风险模型。公式：P（头寸规模）＝ 账户余额 * 百分比 / R（每股的交易风险）。[BOOK3]_, [BOOK4]_ .
        
        :param float p: 百分比
        :return: 资金管理策略实例
    """
def MM_FixedRisk(risk: float = 1000.0) -> MoneyManagerBase:
    """
    MM_FixedRisk([risk = 1000.00])
    
        固定风险资金管理策略对每笔交易限定一个预先确定的或者固定的资金风险，如每笔交易固定风险1000元。公式：交易数量 = 固定风险 / 交易风险。
    
        :param float risk: 固定风险
        :return: 资金管理策略实例
    """
def MM_FixedUnits(n: int = 33) -> MoneyManagerBase:
    """
    MM_FixedUnits([n = 33])
    
        固定单位资金管理策略。公式: 买入数量 = 当前现金 / n / 当前风险risk
    
        :param int n: n个资金单位
        :return: 资金管理策略实例
    """
def MM_Nothing() -> MoneyManagerBase:
    """
    MM_Nothing()
    
        特殊的资金管理策略，相当于不做资金管理，有多少钱买多少。
    """
def MM_WilliamsFixedRisk(p: float = 0.1, max_loss: float = 1000.0) -> MoneyManagerBase:
    """
     MM_WilliamsFixedRisk([p=0.1, max_loss=1000.0])
    
        威廉斯固定风险资金管理策略。买入数量 =（账户余额 × 风险百分比p）÷ 最大损失(max_loss)
    
        :param float p: 风险百分比
        :param float max_loss: 最大损失
        :return: 资金管理策略实例
    """
@typing.overload
def MOD(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def MOD(arg0: Indicator, arg1: float) -> Indicator:
    ...
@typing.overload
def MOD(arg0: float, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def MOD(arg0: float, arg1: float) -> Indicator:
    """
    MOD(ind1, ind2)
    
        取整后求模。该函数仅为兼容通达信。实际上，指标求模可直接使用 % 操作符
    
        用法：MOD(A,B)返回A对B求模
    
        例如：MOD(26,10) 返回 6
    
        :param Indicator ind1:
        :param Indicator ind2:
        :rtype: Indicator
    """
@typing.overload
def MONTH() -> Indicator:
    ...
@typing.overload
def MONTH(arg0: KData) -> Indicator:
    """
    MONTH([data])
    
        取得该周期的月份。用法: MONTH 函数返回有效值范围为(1-12)。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
@typing.overload
def MRR() -> Indicator:
    ...
@typing.overload
def MRR(arg0: Indicator) -> Indicator:
    """
    MRR([data])
        
        当前价格相对历史最低值的盈利百分比，可用于计算历史最高盈利比例
    """
def Microseconds(arg0: int) -> TimeDelta:
    """
    Microseconds(microsecs)
    
          TimeDelta 快捷创建函数
    
          :param int microsecs: 微秒数
          :rtype: TimeDelta
    """
def Milliseconds(arg0: int) -> TimeDelta:
    """
    Milliseconds(milliseconds)
    
          TimeDelta 快捷创建函数
    
          :param int milliseconds: 毫秒数
          :rtype: TimeDelta
    """
def Minutes(arg0: int) -> TimeDelta:
    """
    Minutes(mins)
    
          TimeDelta 快捷创建函数
    
          :param int mins: 分钟数
          :rtype: TimeDelta
    """
@typing.overload
def NDAY(x: Indicator, y: Indicator, n: int = 3) -> Indicator:
    ...
@typing.overload
def NDAY(x: Indicator, y: Indicator, n: int) -> Indicator:
    ...
@typing.overload
def NDAY(x: Indicator, y: Indicator, n: IndParam) -> Indicator:
    """
    NDAY(x, y[, n=3])
    
        连大, NDAY(X,Y,N)表示条件X>Y持续存在N个周期
    
        :param Indicator x:
        :param Indicator y:
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def NOT() -> Indicator:
    ...
@typing.overload
def NOT(arg0: Indicator) -> Indicator:
    """
    NOT([data])
    
        求逻辑非。NOT(X)返回非X,即当X=0时返回1，否则返回0。
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
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
def PG_FixedHoldDays(days: int = 5) -> ProfitGoalBase:
    """
    PG_FixedHoldDays([days=5])
    
        固定持仓天数盈利目标策略
        
        :param int days: 允许持仓天数（按交易日算）,默认5天
        :return: 盈利目标策略实例
    """
def PG_FixedPercent(p: float = 0.2) -> ProfitGoalBase:
    """
    PG_FixedPercent([p = 0.2])
    
        固定百分比盈利目标，目标价格 = 买入价格 * (1 + p)
        
        :param float p: 百分比
        :return: 盈利目标策略实例
    """
def PG_NoGoal() -> ProfitGoalBase:
    """
    PG_NoGoal()
    
        无盈利目标策略，通常为了进行测试或对比。
        
        :return: 盈利目标策略实例
    """
def POS(block: Block, query: Query, sg: ...) -> Indicator:
    ...
@typing.overload
def POW(n: int) -> Indicator:
    ...
@typing.overload
def POW(n: IndParam) -> Indicator:
    ...
@typing.overload
def POW(data: Indicator, n: int) -> Indicator:
    ...
@typing.overload
def POW(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def POW(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def POW(data: float, n: int) -> Indicator:
    """
    POW(data, n)
    
        乘幂
    
        用法：POW(A,B)返回A的B次幂
    
        例如：POW(CLOSE,3)求得收盘价的3次方
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 幂
        :rtype: Indicator
    """
def PRICELIST(data: typing.Any, result_index: int = 0, discard: int = 0, align_dates: typing.Any = None) -> Indicator:
    ...
@typing.overload
def RECOVER_BACKWARD() -> Indicator:
    ...
@typing.overload
def RECOVER_BACKWARD(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def RECOVER_BACKWARD(arg0: KData) -> Indicator:
    """
    RECOVER_BACKWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行后向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
@typing.overload
def RECOVER_EQUAL_BACKWARD() -> Indicator:
    ...
@typing.overload
def RECOVER_EQUAL_BACKWARD(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def RECOVER_EQUAL_BACKWARD(arg0: KData) -> Indicator:
    """
    RECOVER_EQUAL_BACKWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行等比后向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
@typing.overload
def RECOVER_EQUAL_FORWARD() -> Indicator:
    ...
@typing.overload
def RECOVER_EQUAL_FORWARD(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def RECOVER_EQUAL_FORWARD(arg0: KData) -> Indicator:
    """
    RECOVER_EQUAL_FORWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行等比前向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
@typing.overload
def RECOVER_FORWARD() -> Indicator:
    ...
@typing.overload
def RECOVER_FORWARD(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def RECOVER_FORWARD(arg0: KData) -> Indicator:
    """
    RECOVER_FORWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行前向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
@typing.overload
def REF(n: int) -> Indicator:
    ...
@typing.overload
def REF(n: IndParam) -> Indicator:
    ...
@typing.overload
def REF(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def REF(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def REF(data: Indicator, n: int) -> Indicator:
    """
    REF([data, n])
    
        向前引用 （即右移），引用若干周期前的数据。
    
        用法：REF(X，A)　引用A周期前的X值。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 引用n周期前的值，即右移n位
        :rtype: Indicator
    """
@typing.overload
def REPLACE(old_value: float = ..., new_value: float = 0.0, ignore_discard: bool = False) -> Indicator:
    ...
@typing.overload
def REPLACE(ind: Indicator, old_value: float = ..., new_value: float = 0.0, ignore_discard: bool = False) -> Indicator:
    """
    REPLACE(ind, [old_value=constant.nan, new_value=0.0, ignore_discard=False]
              
        替换指标中指定值，默认为替换 nan 值为 0.0。
    
        :param Indicator ind: 指定指标
        :param double old_value: 指定值
        :param double new_value: 替换值
        :param bool ignore_discard: 忽略指标丢弃数据
        :rtype: Indicator
    """
@typing.overload
def RESULT(arg0: int) -> Indicator:
    ...
@typing.overload
def RESULT(data: Indicator, result_ix: int) -> Indicator:
    """
    RESULT(data, result_ix)
              
        以公式指标的方式返回指定指标中的指定结果集
    
        :param Indicator data: 指定的指标
        :param int result_ix: 指定的结果集
    """
@typing.overload
def REVERSE() -> Indicator:
    ...
@typing.overload
def REVERSE(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def REVERSE(arg0: float) -> Indicator:
    """
    REVERSE([data])
    
        求相反数，REVERSE(X)返回-X
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def ROC(n: int = 10) -> Indicator:
    ...
@typing.overload
def ROC(n: IndParam) -> Indicator:
    ...
@typing.overload
def ROC(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def ROC(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def ROC(data: Indicator, n: int = 10) -> Indicator:
    """
    ROC([data, n=10])
    
        变动率指标: ((price / prevPrice)-1)*100
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def ROCP(n: int = 10) -> Indicator:
    ...
@typing.overload
def ROCP(n: IndParam) -> Indicator:
    ...
@typing.overload
def ROCP(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def ROCP(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def ROCP(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCP([data, n=10])
    
        变动率指标: (price - prevPrice) / prevPrice
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def ROCR(n: int = 10) -> Indicator:
    ...
@typing.overload
def ROCR(n: IndParam) -> Indicator:
    ...
@typing.overload
def ROCR(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def ROCR(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def ROCR(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCR([data, n=10])
    
        变动率指标: (price / prevPrice)
    
        :param data: 输入数据
        :param int n|Indicator|IndParam: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def ROCR100(n: int = 10) -> Indicator:
    ...
@typing.overload
def ROCR100(n: IndParam) -> Indicator:
    ...
@typing.overload
def ROCR100(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def ROCR100(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def ROCR100(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCR100([data, n=10])
    
        变动率指标: (price / prevPrice) * 100
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def ROUND(ndigits: int = 2) -> Indicator:
    ...
@typing.overload
def ROUND(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
@typing.overload
def ROUND(data: float, ndigits: int = 2) -> Indicator:
    """
    ROUND([data, ndigits=2])
    
        四舍五入
    
        :param data: 输入数据
        :param int ndigits: 保留的小数点后位数
        :rtype: Indicator
    """
@typing.overload
def ROUNDDOWN(ndigits: int = 2) -> Indicator:
    ...
@typing.overload
def ROUNDDOWN(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
@typing.overload
def ROUNDDOWN(data: float, ndigits: int = 2) -> Indicator:
    """
    ROUND([data, ndigits=2])
    
        四舍五入
    
        :param data: 输入数据
        :param int ndigits: 保留的小数点后位数
        :rtype: Indicator
    """
@typing.overload
def ROUNDUP(ndigits: int = 2) -> Indicator:
    ...
@typing.overload
def ROUNDUP(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
@typing.overload
def ROUNDUP(data: float, ndigits: int = 2) -> Indicator:
    """
    ROUNDUP([data, ndigits=2])
    
        向上截取，如10.1截取后为11
    
        :param data: 输入数据
        :param int ndigits: 保留的小数点后位数
        :rtype: Indicator
    """
@typing.overload
def RSI(n: int = 14) -> Indicator:
    ...
@typing.overload
def RSI(data: Indicator, n: int = 14) -> Indicator:
    """
    RSI([data, n=14])
    
        相对强弱指数
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def SAFTYLOSS(n1: int = 10, n2: int = 3, p: float = 2.0) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(data: Indicator, n1: int = 10, n2: int = 3, p: float = 2.0) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(data: Indicator, n1: Indicator, n2: Indicator, p: float = 2.0) -> Indicator:
    ...
@typing.overload
def SAFTYLOSS(data: Indicator, n1: Indicator, n2: Indicator, p: Indicator) -> Indicator:
    """
    SAFTYLOSS([data, n1=10, n2=3, p=2.0])
    
        亚历山大 艾尔德安全地带止损线，参见 [BOOK2]_
    
        计算说明：在回溯周期内（一般为10到20天），将所有向下穿越的长度相加除以向下穿越的次数，得到噪音均值（即回溯期内所有最低价低于前一日最低价的长度除以次数），并用今日最低价减去（前日噪音均值乘以一个倍数）得到该止损线。为了抵消波动并且保证止损线的上移，在上述结果的基础上再取起N日（一般为3天）内的最高值
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n1: 计算平均噪音的回溯时间窗口
        :param int|Indicator|IndParam n2: 对初步止损线去n2日内的最高值
        :param float|Indicator|IndParam p: 噪音系数
        :rtype: Indicator
    """
@typing.overload
def SE_Fixed(weight: float = 1.0) -> SelectorBase:
    ...
@typing.overload
def SE_Fixed(stk_list: typing.Sequence, sys: ..., weight: float = 1.0) -> SelectorBase:
    """
    SE_Fixed([stk_list, sys])
    
        固定选择器，即始终选择初始划定的标的及其系统策略原型
    
        :param list stk_list: 初始划定的标的
        :param System sys: 系统策略原型
        :param float weight: 默认权重
        :return: SE选择器实例
    """
def SE_MaxFundsOptimal() -> SelectorBase:
    """
    账户资产最大寻优选择器
    """
@typing.overload
def SE_MultiFactor(mf: ..., topn: int = 10) -> SelectorBase:
    ...
@typing.overload
def SE_MultiFactor(inds: typing.Sequence, topn: int = 10, ic_n: int = 5, ic_rolling_n: int = 120, ref_stk: typing.Any = None, spearman: bool = True, mode: str = 'MF_ICIRWeight') -> SelectorBase:
    """
    SE_MultiFactor
    
        创建基于多因子评分的选择器，两种创建方式
    
        - 直接指定 MF:
          :param MultiFactorBase mf: 直接指定的多因子合成算法
          :param int topn: 只选取时间截面中前 topn 个系统
    
        - 参数直接创建:
          :param sequense(Indicator) inds: 原始因子列表
          :param int topn: 只选取时间截面中前 topn 个系统，小于等于0时代表不限制
          :param int ic_n: 默认 IC 对应的 N 日收益率
          :param int ic_rolling_n: IC 滚动周期
          :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
          :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
          :param str mode: "MF_ICIRWeight" | "MF_ICWeight" | "MF_EqualWeight" 因子合成算法名称
    """
def SE_PerformanceOptimal(key: str = '帐户平均年收益率%', mode: int = 0) -> SelectorBase:
    """
    SE_PerformanceOptimal(key="帐户平均年收益率%", mode=0)
    
        使用 Performance 统计结果进行寻优的选择器
    
        :param string key: Performance 统计项
        :param int mode:  0 取统计结果最大的值系统 | 1 取统计结果为最小值的系统
    """
@typing.overload
def SE_Signal() -> SelectorBase:
    ...
@typing.overload
def SE_Signal(arg0: list[Stock], arg1: ...) -> SelectorBase:
    """
    SE_Signal([stk_list, sys])
    
        信号选择器，仅依靠系统买入信号进行选中
    
        :param list stk_list: 初始划定的标的
        :param System sys: 系统策略原型
        :return: SE选择器实例
    """
@typing.overload
def SGN() -> Indicator:
    ...
@typing.overload
def SGN(arg0: float) -> Indicator:
    ...
@typing.overload
def SGN(arg0: Indicator) -> Indicator:
    """
    SGN([data])
    
        求符号值, SGN(X)，当 X>0, X=0, X<0分别返回 1, 0, -1。
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def SG_Add(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
@typing.overload
def SG_Add(sg1: SignalBase, sg2: SignalBase, alternate: bool) -> SignalBase:
    """
    SG_Add(sg1, sg2, alternate)
    
        生成两个指标之和的信号
    
        由于 SG 的 alternate 默认为 True, 在使用如  "sg1 + sg2 + sg3" 的形式时，容易忽略 sg1 + sg2 的 alternate 属性
        建议使用: SG_Add(sg1, sg2, False) + sg3 来避免 alternate 的问题
    
        :param SignalBase sg1: 输入信号1
        :param SignalBase sg2: 输入信号2
        :param bool alternate: 是否交替买入卖出，默认为True
        :return: 信号指示器
    """
def SG_AllwaysBuy() -> SignalBase:
    """
    SG_AllwaysBuy()
        
        一个特殊的SG，持续每天发出买入信号，通常配合 PF 使用
    """
@typing.overload
def SG_And(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
@typing.overload
def SG_And(sg1: SignalBase, sg2: SignalBase, alternate: bool) -> SignalBase:
    """
    SG_And(sg1, sg2, alternate)
    
        生成两个指标与的信号
    
        由于 SG 的 alternate 默认为 True, 在使用如  "sg1 + sg2 + sg3" 的形式时，容易忽略 sg1 + sg2 的 alternate 属性
        建议使用: SG_Add(sg1, sg2, False) + sg3 来避免 alternate 的问题
    
        :param SignalBase sg1: 输入信号1
        :param SignalBase sg2: 输入信号2
        :param bool alternate: 是否交替买入卖出，默认为True
    """
@typing.overload
def SG_Band(ind: Indicator, lower: Indicator, upper: Indicator) -> SignalBase:
    ...
@typing.overload
def SG_Band(ind: Indicator, lower: float, upper: float) -> SignalBase:
    """
    SG_Band(ind, lower, upper)
              
        指标区间指示器, 当指标超过上轨时，买入；
        当指标低于下轨时，卖出。::
    
            SG_Band(MA(C, n=10), 100, 200)
            SG_Band(CLOSE, MA(LOW), MA(HIGH))
    """
def SG_Bool(buy: Indicator, sell: Indicator, alternate: bool = True) -> SignalBase:
    """
    SG_Bool(buy, sell)
    
        布尔信号指示器，使用运算结果为类似bool数组的Indicator分别作为买入、卖出指示。
    
        :param Indicator buy: 买入指示（结果Indicator中相应位置>0则代表买入）
        :param Indicator sell: 卖出指示（结果Indicator中相应位置>0则代表卖出）
        :param bool alternate: 是否交替买入卖出，默认为True
        :return: 信号指示器
    """
def SG_Buy(ind: Indicator) -> SignalBase:
    """
    SG_Buy(ind)
        
        生成单边买入信号
    
        :param Indicator ind: 输入指标
        :return: 信号指示器
    """
def SG_Cross(fast: Indicator, slow: Indicator) -> SignalBase:
    """
    SG_Cross(fast, slow)
    
        双线交叉指示器，当快线从下向上穿越慢线时，买入；当快线从上向下穿越慢线时，卖出。如：5日MA上穿10日MA时买入，5日MA线下穿MA10日线时卖出:: 
    
            SG_Cross(MA(C, n=10), MA(C, n=30))
    
        :param Indicator fast: 快线
        :param Indicator slow: 慢线
        :return: 信号指示器
    """
def SG_CrossGold(fast: Indicator, slow: Indicator) -> SignalBase:
    """
    SG_CrossGold(fast, slow)
    
        金叉指示器，当快线从下向上穿越慢线且快线和慢线的方向都是向上时为金叉，买入；
        当快线从上向下穿越慢线且快线和慢线的方向都是向下时死叉，卖出。::
    
            SG_CrossGold(MA(C, n=10), MA(C, n=30))
    
        :param Indicator fast: 快线
        :param Indicator slow: 慢线
        :return: 信号指示器
    """
def SG_Cycle() -> SignalBase:
    """
    SG_Cycle()
        
        一个特殊的SG，配合PF使用，以 PF 调仓周期为买入信号
    """
@typing.overload
def SG_Div(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
@typing.overload
def SG_Div(sg1: SignalBase, sg2: SignalBase, alternate: bool) -> SignalBase:
    """
    SG_Div(sg1, sg2, alternate)
    
        生成两个指标之差的信号
    
        由于 SG 的 alternate 默认为 True, 在使用如  "sg1 + sg2 + sg3" 的形式时，容易忽略 sg1 + sg2 的 alternate 属性
        建议使用: SG_Add(sg1, sg2, False) + sg3 来避免 alternate 的问题
    
        :param SignalBase sg1: 输入信号1
        :param SignalBase sg2: 输入信号2
        :param bool alternate: 是否交替买入卖出，默认为True
    """
def SG_Flex(op: Indicator, slow_n: int) -> SignalBase:
    """
    SG_Flex(ind, slow_n)
    
        使用自身的EMA(slow_n)作为慢线，自身作为快线，快线向上穿越慢线买入，快线向下穿越慢线卖出。
    
        :param Indicator ind:
        :param int slow_n: 慢线EMA周期
        :return: 信号指示器
    """
@typing.overload
def SG_Mul(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
@typing.overload
def SG_Mul(sg1: SignalBase, sg2: SignalBase, alternate: bool) -> SignalBase:
    """
    SG_Mul(sg1, sg2, alternate)
    
        生成两个指标之差的信号
    
        由于 SG 的 alternate 默认为 True, 在使用如  "sg1 + sg2 + sg3" 的形式时，容易忽略 sg1 + sg2 的 alternate 属性
        建议使用: SG_Add(sg1, sg2, False) + sg3 来避免 alternate 的问题
    
        :param SignalBase sg1: 输入信号1
        :param SignalBase sg2: 输入信号2
        :param bool alternate: 是否交替买入卖出，默认为True
    """
def SG_OneSide(ind: Indicator, is_buy: bool) -> SignalBase:
    """
    SG_OneSide(ind, is_buy)
              
        根据输入指标构建单边信号（单纯的只包含买入或卖出信号），如果指标值大于0，则加入信号。也可以使用 SG_Buy 或 SG_Sell 函数。
        
        :param Indicator ind: 输入指标
        :param bool is_buy: 构建的是买入信号，否则为卖出信号
        :return: 信号指示器
    """
@typing.overload
def SG_Or(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
@typing.overload
def SG_Or(sg1: SignalBase, sg2: SignalBase, alternate: bool) -> SignalBase:
    """
    SG_Or(sg1, sg2, alternate)
    
        生成两个指标与的信号
    
        由于 SG 的 alternate 默认为 True, 在使用如  "sg1 + sg2 + sg3" 的形式时，容易忽略 sg1 + sg2 的 alternate 属性
        建议使用: SG_Add(sg1, sg2, False) + sg3 来避免 alternate 的问题
    
        :param SignalBase sg1: 输入信号1
        :param SignalBase sg2: 输入信号2
        :param bool alternate: 是否交替买入卖出，默认为True
    """
def SG_Sell(ind: Indicator) -> SignalBase:
    """
    SG_Sell(ind)
        
        生成单边卖出信号
    
        :param Indicator ind: 输入指标
        :return: 信号指示器
    """
def SG_Single(ind: Indicator, filter_n: int = 10, filter_p: float = 0.1) -> SignalBase:
    """
    SG_Single(ind[, filter_n = 10, filter_p = 0.1])
        
        生成单线拐点信号指示器。使用《精明交易者》 [BOOK1]_ 中给出的曲线拐点算法判断曲线趋势，公式见下::
    
            filter = percentage * STDEV((AMA-AMA[1], N)
    
            Buy  When AMA - AMA[1] > filter
            or Buy When AMA - AMA[2] > filter
            or Buy When AMA - AMA[3] > filter 
        
        :param Indicator ind:
        :param int filer_n: N日周期
        :param float filter_p: 过滤器百分比
        :return: 信号指示器
    """
def SG_Single2(ind: Indicator, filter_n: int = 10, filter_p: float = 0.1) -> SignalBase:
    """
    SG_Single2(ind[, filter_n = 10, filter_p = 0.1])
        
        生成单线拐点信号指示器2 [BOOK1]_::
    
            filter = percentage * STDEV((AMA-AMA[1], N)
    
            Buy  When AMA - @lowest(AMA,n) > filter
            Sell When @highest(AMA, n) - AMA > filter
        
        :param Indicator ind:
        :param int filer_n: N日周期
        :param float filter_p: 过滤器百分比
        :return: 信号指示器
    """
@typing.overload
def SG_Sub(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
@typing.overload
def SG_Sub(sg1: SignalBase, sg2: SignalBase, alternate: bool) -> SignalBase:
    """
    SG_Sub(sg1, sg2, alternate)
    
        生成两个指标之差的信号
    
        由于 SG 的 alternate 默认为 True, 在使用如  "sg1 + sg2 + sg3" 的形式时，容易忽略 sg1 + sg2 的 alternate 属性
        建议使用: SG_Add(sg1, sg2, False) + sg3 来避免 alternate 的问题
    
        :param SignalBase sg1: 输入信号1
        :param SignalBase sg2: 输入信号2
        :param bool alternate: 是否交替买入卖出，默认为True
        :return: 信号指示器
    """
@typing.overload
def SIN() -> Indicator:
    ...
@typing.overload
def SIN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def SIN(arg0: float) -> Indicator:
    """
    SIN([data])
    
        正弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def SLICE(data: list[float], start: int, end: int) -> Indicator:
    ...
@typing.overload
def SLICE(start: int, end: int, result_index: int = 0) -> Indicator:
    ...
@typing.overload
def SLICE(data: Indicator, start: int, end: int, result_index: int = 0) -> Indicator:
    """
    SLICE(data, start, end, result_index=0)
    
        获取某指标中指定范围 [start, end) 的数据，生成新的指标
    
        :param Indicator|PriceList data: 输入数据
        :param int start: 起始位置
        :param int end: 终止位置（不包含本身）
        :param int result_index: 原输入数据中的结果集
    """
@typing.overload
def SLOPE(n: int = 22) -> Indicator:
    ...
@typing.overload
def SLOPE(n: IndParam) -> Indicator:
    ...
@typing.overload
def SLOPE(data: Indicator, n: int = 22) -> Indicator:
    ...
@typing.overload
def SLOPE(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def SLOPE(data: Indicator, n: Indicator) -> Indicator:
    """
    SLOPE([data, n=22])
    
        计算线性回归斜率，N支持变量
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def SMA(n: int = 22, m: float = 2.0) -> Indicator:
    ...
@typing.overload
def SMA(n: int, m: IndParam) -> Indicator:
    ...
@typing.overload
def SMA(n: IndParam, m: float = 2.0) -> Indicator:
    ...
@typing.overload
def SMA(n: IndParam, m: IndParam) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: int = 22, m: float = 2.0) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: int, m: IndParam) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: IndParam, m: float = 2.0) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: IndParam, m: IndParam) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: int, m: Indicator) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: Indicator, m: float = 2.0) -> Indicator:
    ...
@typing.overload
def SMA(data: Indicator, n: Indicator, m: Indicator) -> Indicator:
    """
    SMA([data, n=22, m=2])
    
        求移动平均
    
        用法：若Y=SMA(X,N,M) 则 Y=[M*X+(N-M)*Y')/N,其中Y'表示上一周期Y值
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :param float|Indicator|IndParam m: 系数
        :rtype: Indicator
    """
@typing.overload
def SPEARMAN(ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def SPEARMAN(ind: Indicator, ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    """
    SPEARMAN(ind, ref_ind[, n=0, fill_null=True])
    
        Spearman 相关系数。与 SPEARMAN(ref_ind, n)(ind) 等效。
    
        :param Indicator ind: 输入参数1
        :param Indicator ref_ind: 输入参数2
        :param int n: 滚动窗口(大于2 或 等于0)，等于0时，代表 n 实际使用 ind 的长度
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
    """
def SP_FixedPercent(p: float = 0.001) -> SlippageBase:
    """
    SP_FixedPercent([p=0.001])
    
        固定百分比移滑价差算法，买入实际价格 = 计划买入价格 * (1 + p)，卖出实际价格 = 计划卖出价格 * (1 - p)
    
        :param float p: 偏移的固定百分比
        :return: 移滑价差算法实例
    """
def SP_FixedValue(value: float = 0.01) -> SlippageBase:
    """
    SP_FixedValuet([p=0.001])
    
        固定价格移滑价差算法，买入实际价格 = 计划买入价格 + 偏移价格，卖出实际价格 = 计划卖出价格 - 偏移价格
    
        :param float p: 偏移价格
        :return: 移滑价差算法实例
    """
@typing.overload
def SQRT() -> Indicator:
    ...
@typing.overload
def SQRT(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def SQRT(arg0: float) -> Indicator:
    """
    SQRT([data])
    
        开平方
    
        用法：SQRT(X)为X的平方根
    
        例如：SQRT(CLOSE)收盘价的平方根
    
        :param data: 输入数据
        :rtype: Indicator
    """
@typing.overload
def STDEV(n: int = 10) -> Indicator:
    ...
@typing.overload
def STDEV(n: IndParam) -> Indicator:
    ...
@typing.overload
def STDEV(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def STDEV(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def STDEV(data: Indicator, n: int = 10) -> Indicator:
    """
    STDEV([data, n=10])
    
        计算N周期内样本标准差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def STDP(n: int = 10) -> Indicator:
    ...
@typing.overload
def STDP(n: IndParam) -> Indicator:
    ...
@typing.overload
def STDP(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def STDP(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def STDP(data: Indicator, n: int = 10) -> Indicator:
    """
    STDP([data, n=10])
    
        总体标准差，STDP(X,N)为X的N日总体标准差
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
def ST_FixedPercent(p: float = 0.03) -> StoplossBase:
    """
    ST_FixedPercent([p=0.03])
    
        固定百分比止损策略，即当价格低于买入价格的某一百分比时止损
    
        :param float p: 百分比(0,1]
        :return: 止损/止赢策略实例
    """
def ST_Indicator(ind: Indicator) -> StoplossBase:
    """
    ST_Indicator(ind)
    
        使用技术指标作为止损价。如使用10日EMA作为止损：::
    
            ST_Indicator(EMA(CLOSE(), n=10))
    
        :param Indicator ind:
        :return: 止损/止赢策略实例
    """
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
@typing.overload
def SUM(n: int = 20) -> Indicator:
    ...
@typing.overload
def SUM(n: IndParam) -> Indicator:
    ...
@typing.overload
def SUM(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def SUM(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def SUM(data: Indicator, n: int = 20) -> Indicator:
    """
    SUM([data, n=20])
    
        求总和。SUM(X,N),统计N周期中X的总和,N=0则从第一个有效值开始。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def SUMBARS(a: float) -> Indicator:
    ...
@typing.overload
def SUMBARS(a: IndParam) -> Indicator:
    ...
@typing.overload
def SUMBARS(data: Indicator, a: IndParam) -> Indicator:
    ...
@typing.overload
def SUMBARS(data: Indicator, a: Indicator) -> Indicator:
    ...
@typing.overload
def SUMBARS(data: Indicator, a: float) -> Indicator:
    """
    SUMBARS([data,] a)
    
        累加到指定周期数, 向前累加到指定值到现在的周期数
    
        用法：SUMBARS(X,A):将X向前累加直到大于等于A,返回这个区间的周期数
    
        例如：SUMBARS(VOL,CAPITAL)求完全换手到现在的周期数
    
        :param Indicator data: 输入数据
        :param float a|Indicator|IndParam: 指定累加和
        :rtype: Indicator
    """
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
def Seconds(arg0: int) -> TimeDelta:
    """
    Seconds(secs)
    
          TimeDelta 快捷创建函数
    
          :param int secs: 秒数
          :rtype: TimeDelta
    """
@typing.overload
def TAN() -> Indicator:
    ...
@typing.overload
def TAN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TAN(arg0: float) -> Indicator:
    """
    TAN([data])
    
        正切值
    
        :param Indicator data: 输入数据
        :rtype: Indicato
    """
@typing.overload
def TA_ACCBANDS(n: int = 20) -> Indicator:
    ...
@typing.overload
def TA_ACCBANDS(data: KData, n: int = 20) -> Indicator:
    """
    TA_ACCBANDS - Acceleration Bands
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_ACOS() -> Indicator:
    ...
@typing.overload
def TA_ACOS(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ACOS(arg0: float) -> Indicator:
    """
    TA_ACOS - Vector Trigonometric ACos
    """
@typing.overload
def TA_AD() -> Indicator:
    ...
@typing.overload
def TA_AD(data: KData) -> Indicator:
    """
    TA_AD - Chaikin A/D Line
    """
@typing.overload
def TA_ADD(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_ADD(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_ADD - Vector Arithmetic Add
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
@typing.overload
def TA_ADOSC(fast_n: int = 3, slow_n: int = 10) -> Indicator:
    ...
@typing.overload
def TA_ADOSC(data: KData, fast_n: int = 3, slow_n: int = 10) -> Indicator:
    """
    TA_ADOSC - Chaikin A/D Oscillator
    
    :param KData data: input KData
    :param int fast_n: Number of period for the fast MA (From 2 to 100000)
    :param int slow_n: Number of period for the slow MA (From 2 to 100000)
    """
@typing.overload
def TA_ADX(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_ADX(data: KData, n: int = 14) -> Indicator:
    """
    TA_ADX - Average Directional Movement Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_ADXR(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_ADXR(data: KData, n: int = 14) -> Indicator:
    """
    TA_ADXR - Average Directional Movement Index Rating
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_APO(fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_APO(data: Indicator, fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    """
    TA_APO - Absolute Price Oscillator
    
    :param Indicator data: input data
    :param int fast_n: Number of period for the fast MA (From 2 to 100000)
    :param int slow_n: Number of period for the slow MA (From 2 to 100000)    
    :param int matype: Type of Moving Average
    """
@typing.overload
def TA_AROON(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_AROON(data: KData, n: int = 14) -> Indicator:
    """
    TA_AROON - Aroon
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - Aroon down
             result(2) - Aroon up
    """
@typing.overload
def TA_AROONOSC(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_AROONOSC(data: KData, n: int = 14) -> Indicator:
    """
    TA_AROONOSC - Aroon Oscillator
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_ASIN() -> Indicator:
    ...
@typing.overload
def TA_ASIN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ASIN(arg0: float) -> Indicator:
    """
    TA_ASIN - Vector Trigonometric ASin
    """
@typing.overload
def TA_ATAN() -> Indicator:
    ...
@typing.overload
def TA_ATAN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ATAN(arg0: float) -> Indicator:
    """
    TA_ATAN - Vector Trigonometric ATan
    """
@typing.overload
def TA_ATR(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_ATR(data: KData, n: int = 14) -> Indicator:
    """
    TA_ATR - Average True Range
        
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_AVGDEV(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_AVGDEV(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_AVGDEV(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_AVGDEV(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_AVGDEV(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_AVGDEV - Average Deviation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_AVGPRICE() -> Indicator:
    ...
@typing.overload
def TA_AVGPRICE(data: KData) -> Indicator:
    """
    TA_AVGPRICE - Average Price
    """
@typing.overload
def TA_BBANDS(n: int = 5, nbdevup: float = 2.0, nbdevdn: float = 2.0, matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_BBANDS(data: Indicator, n: int = 5, nbdevup: float = 2.0, nbdevdn: float = 2.0, matype: int = 0) -> Indicator:
    """
    TA_BBANDS - Bollinger Bands
              
    :param Indicator data: input data
    :param int n: Number of periode (From 1 to 100000)
    :param float nbdevup: Deviation multiplier for upper band
    :param float nbdevdn: Deviation multiplier for lower band
    :rtype: 具有三个结果集的 Indicator
    
        * result(0): Upper Band
        * result(1): Middle Band
        * result(2): Lower Band
    """
@typing.overload
def TA_BETA(n: int = 5, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_BETA(ind1: Indicator, ind2: Indicator, n: int = 5, fill_null: bool = True) -> Indicator:
    """
    TA_BETA - Beta
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
@typing.overload
def TA_BOP() -> Indicator:
    ...
@typing.overload
def TA_BOP(data: KData) -> Indicator:
    """
    TA_BOP - Balance Of Power
    """
@typing.overload
def TA_CCI(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_CCI(data: KData, n: int = 14) -> Indicator:
    """
    TA_CCI - Commodity Channel Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_CDL2CROWS() -> Indicator:
    ...
@typing.overload
def TA_CDL2CROWS(data: KData) -> Indicator:
    """
    TA_CDL2CROWS - Two Crows
    """
@typing.overload
def TA_CDL3BLACKCROWS() -> Indicator:
    ...
@typing.overload
def TA_CDL3BLACKCROWS(data: KData) -> Indicator:
    """
    TA_CDL3BLACKCROWS - Three Black Crows
    """
@typing.overload
def TA_CDL3INSIDE() -> Indicator:
    ...
@typing.overload
def TA_CDL3INSIDE(data: KData) -> Indicator:
    """
    TA_CDL3INSIDE - Three Inside Up/Down
    """
@typing.overload
def TA_CDL3LINESTRIKE() -> Indicator:
    ...
@typing.overload
def TA_CDL3LINESTRIKE(data: KData) -> Indicator:
    """
    TA_CDL3LINESTRIKE - Three-Line Strike
    """
@typing.overload
def TA_CDL3OUTSIDE() -> Indicator:
    ...
@typing.overload
def TA_CDL3OUTSIDE(data: KData) -> Indicator:
    """
    TA_CDL3OUTSIDE - Three Outside Up/Down
    """
@typing.overload
def TA_CDL3STARSINSOUTH() -> Indicator:
    ...
@typing.overload
def TA_CDL3STARSINSOUTH(data: KData) -> Indicator:
    """
    TA_CDL3STARSINSOUTH - Three Stars In The South
    """
@typing.overload
def TA_CDL3WHITESOLDIERS() -> Indicator:
    ...
@typing.overload
def TA_CDL3WHITESOLDIERS(data: KData) -> Indicator:
    """
    TA_CDL3WHITESOLDIERS - Three Advancing White Soldiers
    """
@typing.overload
def TA_CDLABANDONEDBABY(penetration: float = 0.3) -> Indicator:
    ...
@typing.overload
def TA_CDLABANDONEDBABY(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLABANDONEDBABY - Abandoned Baby
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLADVANCEBLOCK() -> Indicator:
    ...
@typing.overload
def TA_CDLADVANCEBLOCK(data: KData) -> Indicator:
    """
    TA_CDLADVANCEBLOCK - Advance Block
    """
@typing.overload
def TA_CDLBELTHOLD() -> Indicator:
    ...
@typing.overload
def TA_CDLBELTHOLD(data: KData) -> Indicator:
    """
    TA_CDLBELTHOLD - Belt-hold
    """
@typing.overload
def TA_CDLBREAKAWAY() -> Indicator:
    ...
@typing.overload
def TA_CDLBREAKAWAY(data: KData) -> Indicator:
    """
    TA_CDLBREAKAWAY - Breakaway
    """
@typing.overload
def TA_CDLCLOSINGMARUBOZU() -> Indicator:
    ...
@typing.overload
def TA_CDLCLOSINGMARUBOZU(data: KData) -> Indicator:
    """
    TA_CDLCLOSINGMARUBOZU - Closing Marubozu
    """
@typing.overload
def TA_CDLCONCEALBABYSWALL() -> Indicator:
    ...
@typing.overload
def TA_CDLCONCEALBABYSWALL(data: KData) -> Indicator:
    """
    TA_CDLCONCEALBABYSWALL - Concealing Baby Swallow
    """
@typing.overload
def TA_CDLCOUNTERATTACK() -> Indicator:
    ...
@typing.overload
def TA_CDLCOUNTERATTACK(data: KData) -> Indicator:
    """
    TA_CDLCOUNTERATTACK - Counterattack
    """
@typing.overload
def TA_CDLDARKCLOUDCOVER(penetration: float = 0.5) -> Indicator:
    ...
@typing.overload
def TA_CDLDARKCLOUDCOVER(data: KData, penetration: float = 0.5) -> Indicator:
    """
    TA_CDLDARKCLOUDCOVER - Dark Cloud Cover
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLDOJI() -> Indicator:
    ...
@typing.overload
def TA_CDLDOJI(data: KData) -> Indicator:
    """
    TA_CDLDOJI - Doji
    """
@typing.overload
def TA_CDLDOJISTAR() -> Indicator:
    ...
@typing.overload
def TA_CDLDOJISTAR(data: KData) -> Indicator:
    """
    TA_CDLDOJISTAR - Doji Star
    """
@typing.overload
def TA_CDLDRAGONFLYDOJI() -> Indicator:
    ...
@typing.overload
def TA_CDLDRAGONFLYDOJI(data: KData) -> Indicator:
    """
    TA_CDLDRAGONFLYDOJI - Dragonfly Doji
    """
@typing.overload
def TA_CDLENGULFING() -> Indicator:
    ...
@typing.overload
def TA_CDLENGULFING(data: KData) -> Indicator:
    """
    TA_CDLENGULFING - Engulfing Pattern
    """
@typing.overload
def TA_CDLEVENINGDOJISTAR(penetration: float = 0.3) -> Indicator:
    ...
@typing.overload
def TA_CDLEVENINGDOJISTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLEVENINGDOJISTAR - Evening Doji Star
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLEVENINGSTAR(penetration: float = 0.3) -> Indicator:
    ...
@typing.overload
def TA_CDLEVENINGSTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLEVENINGSTAR - Evening Star
                
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLGAPSIDESIDEWHITE() -> Indicator:
    ...
@typing.overload
def TA_CDLGAPSIDESIDEWHITE(data: KData) -> Indicator:
    """
    TA_CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    """
@typing.overload
def TA_CDLGRAVESTONEDOJI() -> Indicator:
    ...
@typing.overload
def TA_CDLGRAVESTONEDOJI(data: KData) -> Indicator:
    """
    TA_CDLGRAVESTONEDOJI - Gravestone Doji
    """
@typing.overload
def TA_CDLHAMMER() -> Indicator:
    ...
@typing.overload
def TA_CDLHAMMER(data: KData) -> Indicator:
    """
    TA_CDLHAMMER - Hammer
    """
@typing.overload
def TA_CDLHANGINGMAN() -> Indicator:
    ...
@typing.overload
def TA_CDLHANGINGMAN(data: KData) -> Indicator:
    """
    TA_CDLHANGINGMAN - Hanging Man
    """
@typing.overload
def TA_CDLHARAMI() -> Indicator:
    ...
@typing.overload
def TA_CDLHARAMI(data: KData) -> Indicator:
    """
    TA_CDLHARAMI - Harami Pattern
    """
@typing.overload
def TA_CDLHARAMICROSS() -> Indicator:
    ...
@typing.overload
def TA_CDLHARAMICROSS(data: KData) -> Indicator:
    """
    TA_CDLHARAMICROSS - Harami Cross Pattern
    """
@typing.overload
def TA_CDLHIGHWAVE() -> Indicator:
    ...
@typing.overload
def TA_CDLHIGHWAVE(data: KData) -> Indicator:
    """
    TA_CDLHIGHWAVE - High-Wave Candle
    """
@typing.overload
def TA_CDLHIKKAKE() -> Indicator:
    ...
@typing.overload
def TA_CDLHIKKAKE(data: KData) -> Indicator:
    """
    TA_CDLHIKKAKE - Hikkake Pattern
    """
@typing.overload
def TA_CDLHIKKAKEMOD() -> Indicator:
    ...
@typing.overload
def TA_CDLHIKKAKEMOD(data: KData) -> Indicator:
    """
    TA_CDLHIKKAKEMOD - Modified Hikkake Pattern
    """
@typing.overload
def TA_CDLHOMINGPIGEON() -> Indicator:
    ...
@typing.overload
def TA_CDLHOMINGPIGEON(data: KData) -> Indicator:
    """
    TA_CDLHOMINGPIGEON - Homing Pigeon
    """
@typing.overload
def TA_CDLIDENTICAL3CROWS() -> Indicator:
    ...
@typing.overload
def TA_CDLIDENTICAL3CROWS(data: KData) -> Indicator:
    """
    TA_CDLIDENTICAL3CROWS - Identical Three Crows
    """
@typing.overload
def TA_CDLINNECK() -> Indicator:
    ...
@typing.overload
def TA_CDLINNECK(data: KData) -> Indicator:
    """
    TA_CDLINNECK - In-Neck Pattern
    """
@typing.overload
def TA_CDLINVERTEDHAMMER() -> Indicator:
    ...
@typing.overload
def TA_CDLINVERTEDHAMMER(data: KData) -> Indicator:
    """
    TA_CDLINVERTEDHAMMER - Inverted Hammer
    """
@typing.overload
def TA_CDLKICKING() -> Indicator:
    ...
@typing.overload
def TA_CDLKICKING(data: KData) -> Indicator:
    """
    TA_CDLKICKING - Kicking
    """
@typing.overload
def TA_CDLKICKINGBYLENGTH() -> Indicator:
    ...
@typing.overload
def TA_CDLKICKINGBYLENGTH(data: KData) -> Indicator:
    """
    TA_CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    """
@typing.overload
def TA_CDLLADDERBOTTOM() -> Indicator:
    ...
@typing.overload
def TA_CDLLADDERBOTTOM(data: KData) -> Indicator:
    """
    TA_CDLLADDERBOTTOM - Ladder Bottom
    """
@typing.overload
def TA_CDLLONGLEGGEDDOJI() -> Indicator:
    ...
@typing.overload
def TA_CDLLONGLEGGEDDOJI(data: KData) -> Indicator:
    """
    TA_CDLLONGLEGGEDDOJI - Long Legged Doji
    """
@typing.overload
def TA_CDLLONGLINE() -> Indicator:
    ...
@typing.overload
def TA_CDLLONGLINE(data: KData) -> Indicator:
    """
    TA_CDLLONGLINE - Long Line Candle
    """
@typing.overload
def TA_CDLMARUBOZU() -> Indicator:
    ...
@typing.overload
def TA_CDLMARUBOZU(data: KData) -> Indicator:
    """
    TA_CDLMARUBOZU - Marubozu
    """
@typing.overload
def TA_CDLMATCHINGLOW() -> Indicator:
    ...
@typing.overload
def TA_CDLMATCHINGLOW(data: KData) -> Indicator:
    """
    TA_CDLMATCHINGLOW - Matching Low
    """
@typing.overload
def TA_CDLMATHOLD(penetration: float = 0.5) -> Indicator:
    ...
@typing.overload
def TA_CDLMATHOLD(data: KData, penetration: float = 0.5) -> Indicator:
    """
    TA_CDLMATHOLD - Mat Hold
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLMORNINGDOJISTAR(penetration: float = 0.3) -> Indicator:
    ...
@typing.overload
def TA_CDLMORNINGDOJISTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLMORNINGDOJISTAR - Morning Doji Star
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLMORNINGSTAR(penetration: float = 0.3) -> Indicator:
    ...
@typing.overload
def TA_CDLMORNINGSTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLMORNINGSTAR - Morning Star
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
@typing.overload
def TA_CDLONNECK() -> Indicator:
    ...
@typing.overload
def TA_CDLONNECK(data: KData) -> Indicator:
    """
    TA_CDLONNECK - On-Neck Pattern
    """
@typing.overload
def TA_CDLPIERCING() -> Indicator:
    ...
@typing.overload
def TA_CDLPIERCING(data: KData) -> Indicator:
    """
    TA_CDLPIERCING - Piercing Pattern
    """
@typing.overload
def TA_CDLRICKSHAWMAN() -> Indicator:
    ...
@typing.overload
def TA_CDLRICKSHAWMAN(data: KData) -> Indicator:
    """
    TA_CDLRICKSHAWMAN - Rickshaw Man
    """
@typing.overload
def TA_CDLRISEFALL3METHODS() -> Indicator:
    ...
@typing.overload
def TA_CDLRISEFALL3METHODS(data: KData) -> Indicator:
    """
    TA_CDLRISEFALL3METHODS - Rising/Falling Three Methods
    """
@typing.overload
def TA_CDLSEPARATINGLINES() -> Indicator:
    ...
@typing.overload
def TA_CDLSEPARATINGLINES(data: KData) -> Indicator:
    """
    TA_CDLSEPARATINGLINES - Separating Lines
    """
@typing.overload
def TA_CDLSHOOTINGSTAR() -> Indicator:
    ...
@typing.overload
def TA_CDLSHOOTINGSTAR(data: KData) -> Indicator:
    """
    TA_CDLSHOOTINGSTAR - Shooting Star
    """
@typing.overload
def TA_CDLSHORTLINE() -> Indicator:
    ...
@typing.overload
def TA_CDLSHORTLINE(data: KData) -> Indicator:
    """
    TA_CDLSHORTLINE - Short Line Candle
    """
@typing.overload
def TA_CDLSPINNINGTOP() -> Indicator:
    ...
@typing.overload
def TA_CDLSPINNINGTOP(data: KData) -> Indicator:
    """
    TA_CDLSPINNINGTOP - Spinning Top
    """
@typing.overload
def TA_CDLSTALLEDPATTERN() -> Indicator:
    ...
@typing.overload
def TA_CDLSTALLEDPATTERN(data: KData) -> Indicator:
    """
    TA_CDLSTALLEDPATTERN - Stalled Pattern
    """
@typing.overload
def TA_CDLSTICKSANDWICH() -> Indicator:
    ...
@typing.overload
def TA_CDLSTICKSANDWICH(data: KData) -> Indicator:
    """
    TA_CDLSTICKSANDWICH - Stick Sandwich
    """
@typing.overload
def TA_CDLTAKURI() -> Indicator:
    ...
@typing.overload
def TA_CDLTAKURI(data: KData) -> Indicator:
    """
    TA_CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
    """
@typing.overload
def TA_CDLTASUKIGAP() -> Indicator:
    ...
@typing.overload
def TA_CDLTASUKIGAP(data: KData) -> Indicator:
    """
    TA_CDLTASUKIGAP - Tasuki Gap
    """
@typing.overload
def TA_CDLTHRUSTING() -> Indicator:
    ...
@typing.overload
def TA_CDLTHRUSTING(data: KData) -> Indicator:
    """
    TA_CDLTHRUSTING - Thrusting Pattern
    """
@typing.overload
def TA_CDLTRISTAR() -> Indicator:
    ...
@typing.overload
def TA_CDLTRISTAR(data: KData) -> Indicator:
    """
    TA_CDLTRISTAR - Tristar Pattern
    """
@typing.overload
def TA_CDLUNIQUE3RIVER() -> Indicator:
    ...
@typing.overload
def TA_CDLUNIQUE3RIVER(data: KData) -> Indicator:
    """
    TA_CDLUNIQUE3RIVER - Unique 3 River
    """
@typing.overload
def TA_CDLUPSIDEGAP2CROWS() -> Indicator:
    ...
@typing.overload
def TA_CDLUPSIDEGAP2CROWS(data: KData) -> Indicator:
    """
    TA_CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    """
@typing.overload
def TA_CDLXSIDEGAP3METHODS() -> Indicator:
    ...
@typing.overload
def TA_CDLXSIDEGAP3METHODS(data: KData) -> Indicator:
    """
    TA_CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    """
@typing.overload
def TA_CEIL() -> Indicator:
    ...
@typing.overload
def TA_CEIL(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_CEIL(arg0: float) -> Indicator:
    """
    TA_CEIL - Vector Ceil
    """
@typing.overload
def TA_CMO(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_CMO(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_CMO(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_CMO(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_CMO(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_CMO - Chande Momentum Oscillator
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_CORREL(n: int = 30, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_CORREL(ind1: Indicator, ind2: Indicator, n: int = 30, fill_null: bool = True) -> Indicator:
    """
    TA_CORREL - Pearson's Correlation Coefficient (r)
        
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
@typing.overload
def TA_COS() -> Indicator:
    ...
@typing.overload
def TA_COS(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_COS(arg0: float) -> Indicator:
    """
    TA_COS - Vector Trigonometric Cos
    """
@typing.overload
def TA_COSH() -> Indicator:
    ...
@typing.overload
def TA_COSH(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_COSH(arg0: float) -> Indicator:
    """
    TA_COSH - Vector Trigonometric Cosh
    """
@typing.overload
def TA_DEMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_DEMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_DEMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_DEMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_DEMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_DEMA - Double Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_DIV(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_DIV(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_DIV - Vector Arithmetic Div
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
@typing.overload
def TA_DX(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_DX(data: KData, n: int = 14) -> Indicator:
    """
    TA_DX - Directional Movement Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_EMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_EMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_EMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_EMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_EMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_EMA - Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_EXP() -> Indicator:
    ...
@typing.overload
def TA_EXP(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_EXP(arg0: float) -> Indicator:
    """
    TA_EXP - Vector Arithmetic Exp
    """
@typing.overload
def TA_FLOOR() -> Indicator:
    ...
@typing.overload
def TA_FLOOR(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_FLOOR(arg0: float) -> Indicator:
    """
    TA_FLOOR - Vector Floor
    """
@typing.overload
def TA_HT_DCPERIOD() -> Indicator:
    ...
@typing.overload
def TA_HT_DCPERIOD(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_HT_DCPERIOD(arg0: float) -> Indicator:
    """
    TA_HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period
    """
@typing.overload
def TA_HT_DCPHASE() -> Indicator:
    ...
@typing.overload
def TA_HT_DCPHASE(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_HT_DCPHASE(arg0: float) -> Indicator:
    """
    TA_HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase
    """
@typing.overload
def TA_HT_PHASOR() -> Indicator:
    ...
@typing.overload
def TA_HT_PHASOR(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_HT_PHASOR(arg0: float) -> Indicator:
    """
    TA_HT_PHASOR - Hilbert Transform - Phasor Components
    
    :return: result(0) - outInPhase
             result(1) - outQuadrature
    """
@typing.overload
def TA_HT_SINE() -> Indicator:
    ...
@typing.overload
def TA_HT_SINE(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_HT_SINE(arg0: float) -> Indicator:
    """
    TA_HT_SINE - Hilbert Transform - SineWave
    :return: result(0) - outSine
             result(1) - outLeadSine
    """
@typing.overload
def TA_HT_TRENDLINE() -> Indicator:
    ...
@typing.overload
def TA_HT_TRENDLINE(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_HT_TRENDLINE(arg0: float) -> Indicator:
    """
    TA_HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    """
@typing.overload
def TA_HT_TRENDMODE() -> Indicator:
    ...
@typing.overload
def TA_HT_TRENDMODE(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_HT_TRENDMODE(arg0: float) -> Indicator:
    """
    TA_HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode
    """
@typing.overload
def TA_IMI(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_IMI(data: KData, n: int = 14) -> Indicator:
    """
    TA_IMI - Intraday Momentum Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_KAMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_KAMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_KAMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_KAMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_KAMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_KAMA - Kaufman Adaptive Moving Average
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_LINEARREG(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG - Linear Regression
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_LINEARREG_ANGLE(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_ANGLE(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_ANGLE(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_ANGLE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_ANGLE(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_ANGLE - Linear Regression Angle
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_LINEARREG_INTERCEPT(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_INTERCEPT(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_INTERCEPT(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_INTERCEPT(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_INTERCEPT(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_INTERCEPT - Linear Regression Intercept
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_LINEARREG_SLOPE(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_SLOPE(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_SLOPE(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_SLOPE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_LINEARREG_SLOPE(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_SLOPE - Linear Regression Slope
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_LN() -> Indicator:
    ...
@typing.overload
def TA_LN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_LN(arg0: float) -> Indicator:
    """
    TA_LN - Vector Log Natural
    """
@typing.overload
def TA_LOG10() -> Indicator:
    ...
@typing.overload
def TA_LOG10(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_LOG10(arg0: float) -> Indicator:
    """
    TA_LOG10 - Vector Log10
    """
@typing.overload
def TA_MA(n: int = 30, matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_MA(data: Indicator, n: int = 30, matype: int = 0) -> Indicator:
    """
    TA_MA - Moving average
    
    :param Indicator data: input data
    :param int n: Number of periode (From 1 to 100000)
    :param int matype: Type of Moving Average
    """
@typing.overload
def TA_MACD(fast_n: int = 12, slow_n: int = 26, signal_n: int = 9) -> Indicator:
    ...
@typing.overload
def TA_MACD(data: Indicator, fast_n: int = 30, slow_n: int = 26, signal_n: int = 9) -> Indicator:
    """
    TA_MACD - Moving Average Convergence/Divergence
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int signal_n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    """
@typing.overload
def TA_MACDEXT(fast_n: int = 12, slow_n: int = 26, signal_n: int = 9, fast_matype: int = 0, slow_matype: int = 0, signal_matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_MACDEXT(data: Indicator, fast_n: int = 30, slow_n: int = 26, signal_n: int = 9, fast_matype: int = 0, slow_matype: int = 0, signal_matype: int = 0) -> Indicator:
    """
    TA_MACDEXT - MACD with controllable MA type
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int signal_n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    :param int fast_matype: Type of Moving Average for fast MA
    :param int slow_matype: Type of Moving Average for slow MA
    :param int signal_matype: Type of Moving Average for signal line
    """
@typing.overload
def TA_MACDFIX(n: int = 9) -> Indicator:
    ...
@typing.overload
def TA_MACDFIX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MACDFIX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MACDFIX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MACDFIX(data: Indicator, n: int = 9) -> Indicator:
    """
    TA_MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    
    :param Indicator data: input data
    :param int n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    :return: result(0) - outMACD
             result(1) - outMACDSignal
             result(2) - outMACDHist
    """
@typing.overload
def TA_MAMA(fast_limit: float = 0.5, slow_limit: float = 0.05) -> Indicator:
    ...
@typing.overload
def TA_MAMA(data: Indicator, fast_limit: float = 0.5, slow_limit: float = 0.05) -> Indicator:
    """
    TA_MAMA - MESA Adaptive Moving Average
    
    :param Indicator data: input data
    :param float fast_limit: Fast limit (From 0.01 to 0.99)
    :param float slow_limit: Slow limit (From 0.01 to 0.99)
    """
@typing.overload
def TA_MAVP(ref_ind: Indicator, min_n: int = 2, max_n: int = 30, matype: int = 0, fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_MAVP(ind1: Indicator, ind2: Indicator, min_n: int = 2, max_n: int = 30, fill_null: int = True, matype: bool = 0) -> Indicator:
    """
    TA_MAVP - Moving average with variable period
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int min_n: Value less than minimum will be changed to Minimum period (From 2 to 100000)
    :param int max_n: Value higher than maximum will be changed to Maximum period (From 2 to 100000)
    :param int matype: Type of Moving Average
    :param bool fill_null: 日期对齐时，缺失日期数据填充nan值
    """
@typing.overload
def TA_MAX(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_MAX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MAX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MAX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MAX - Highest value over a specified period
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MAXINDEX(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_MAXINDEX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MAXINDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MAXINDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MAXINDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MAXINDEX - Index of highest value over a specified period
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MEDPRICE() -> Indicator:
    ...
@typing.overload
def TA_MEDPRICE(data: KData) -> Indicator:
    """
    TA_MEDPRICE - Median Price
    """
@typing.overload
def TA_MFI(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_MFI(data: KData, n: int = 14) -> Indicator:
    """
    TA_MFI - Money Flow Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MIDPOINT(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_MIDPOINT(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MIDPOINT(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MIDPOINT(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MIDPOINT(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_MIDPOINT - MidPoint over period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MIDPRICE(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_MIDPRICE(data: KData, n: int = 14) -> Indicator:
    """
    TA_MIDPRICE - Midpoint Price over period
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MIN(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_MIN(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MIN(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MIN(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MIN(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MIN - Lowest value over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MININDEX(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_MININDEX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MININDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MININDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MININDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MININDEX - Index of lowest value over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_MINMAX(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_MINMAX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MINMAX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MINMAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MINMAX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MINMAX - Lowest and highest values over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - outMin
             result(1) - outMax
    """
@typing.overload
def TA_MINMAXINDEX(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_MINMAXINDEX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MINMAXINDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MINMAXINDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MINMAXINDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MINMAXINDEX - Indexes of lowest and highest values over a specified period
        
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - outMinIdx
             result(1) - outMaxIdx
    """
@typing.overload
def TA_MINUS_DI(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_MINUS_DI(data: KData, n: int = 14) -> Indicator:
    """
    A_MINUS_DI - Minus Directional Indicator
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_MINUS_DM(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_MINUS_DM(data: KData, n: int = 14) -> Indicator:
    """
    TA_MINUS_DM - Minus Directional Movement
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_MOM(n: int = 10) -> Indicator:
    ...
@typing.overload
def TA_MOM(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MOM(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_MOM(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_MOM(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_MOM - Momentum
        
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_MULT(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_MULT(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_MULT - Vector Arithmetic Mult
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
@typing.overload
def TA_NATR(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_NATR(data: KData, n: int = 14) -> Indicator:
    """
    TA_NATR - Normalized Average True Range
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_OBV() -> Indicator:
    ...
@typing.overload
def TA_OBV(data: KData) -> Indicator:
    """
    TA_OBV - On Balance Volume
    """
@typing.overload
def TA_PLUS_DI(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_PLUS_DI(data: KData, n: int = 14) -> Indicator:
    """
    TA_PLUS_DI - Plus Directional Indicator
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_PLUS_DM(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_PLUS_DM(data: KData, n: int = 14) -> Indicator:
    """
    TA_PLUS_DM - Plus Directional Movement
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_PPO(fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_PPO(data: Indicator, fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    """
    TA_PPO - Percentage Price Oscillator
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int matype: Type of Moving Average
    """
@typing.overload
def TA_ROC(n: int = 10) -> Indicator:
    ...
@typing.overload
def TA_ROC(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROC(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROC(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ROC(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROC - Rate of change : ((price/prevPrice)-1)*100
        
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_ROCP(n: int = 10) -> Indicator:
    ...
@typing.overload
def TA_ROCP(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROCP(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROCP(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ROCP(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_ROCR(n: int = 10) -> Indicator:
    ...
@typing.overload
def TA_ROCR(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROCR(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROCR(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ROCR(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCR - Rate of change ratio: (price/prevPrice)
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_ROCR100(n: int = 10) -> Indicator:
    ...
@typing.overload
def TA_ROCR100(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROCR100(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_ROCR100(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_ROCR100(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_RSI(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_RSI(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_RSI(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_RSI(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_RSI(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_RSI - Relative Strength Index
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_SAR(acceleration: float = 0.02, maximum: float = 0.2) -> Indicator:
    ...
@typing.overload
def TA_SAR(data: KData, acceleration: float = 0.02, maximum: float = 0.2) -> Indicator:
    """
    TA_SAR - Parabolic SAR
    
    :param KData data: input KData object
    :param float acceleration: Acceleration Factor used up to the Maximum value (>= 0.0)
    :param float maximum: Acceleration Factor Maximum value (>= 0.0)
    """
@typing.overload
def TA_SAREXT(startvalue: float = 0.0, offsetonreverse: float = 0.0, accelerationinitlong: float = 0.02, accelerationlong: float = 0.02, accelerationmaxlong: float = 0.2, accelerationinitshort: float = 0.02, accelerationshort: float = 0.02, accelerationmaxshort: float = 0.2) -> Indicator:
    ...
@typing.overload
def TA_SAREXT(data: KData, startvalue: float = 0.0, offsetonreverse: float = 0.0, accelerationinitlong: float = 0.02, accelerationlong: float = 0.02, accelerationmaxlong: float = 0.2, accelerationinitshort: float = 0.02, accelerationshort: float = 0.02, accelerationmaxshort: float = 0.2) -> Indicator:
    """
    TA_SAREXT - Parabolic SAR - Extended
    
    :param KData data: input KData object
    :param float startvalue: Start value and direction. 0 for Auto, >0 for Long, <0 for Short
    :param float offsetonreverse: Percent offset added/removed to initial stop on short/long reversal (>= 0.0)
    :param float accelerationinitlong: Acceleration Factor initial value for the Long direction (>= 0.0)
    :param float accelerationlong: Acceleration Factor for the Long direction (>= 0.0)
    :param float accelerationmaxlong: Acceleration Factor maximum value for the Long direction (>= 0.0)
    :param float accelerationinitshort: Acceleration Factor initial value for the Short direction (>= 0.0)
    :param float accelerationshort: Acceleration Factor for the Short direction (>= 0.0)
    :param float accelerationmaxshort: Acceleration Factor maximum value for the Short direction(>= 0.0)
    """
@typing.overload
def TA_SIN() -> Indicator:
    ...
@typing.overload
def TA_SIN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_SIN(arg0: float) -> Indicator:
    """
    TA_SIN - Vector Trigonometric Sin
    """
@typing.overload
def TA_SINH() -> Indicator:
    ...
@typing.overload
def TA_SINH(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_SINH(arg0: float) -> Indicator:
    """
    TA_SINH - Vector Trigonometric Sinh
    """
@typing.overload
def TA_SMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_SMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_SMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_SMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_SMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_SMA - Simple Moving Average
        
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_SQRT() -> Indicator:
    ...
@typing.overload
def TA_SQRT(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_SQRT(arg0: float) -> Indicator:
    """
    TA_SQRT - Vector Square Root
    """
@typing.overload
def TA_STDDEV(n: int = 5, nbdev: float = 1.0) -> Indicator:
    ...
@typing.overload
def TA_STDDEV(data: Indicator, n: int = 5, nbdev: float = 1.0) -> Indicator:
    """
    TA_STDDEV - Standard Deviation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param float nbdev: Nb of deviations
    """
@typing.overload
def TA_STOCH(fastk_n: int = 5, slowk_n: int = 3, slowk_matype: int = 0, slowd_n: int = 3, slowd_matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_STOCH(data: KData, fastk_n: int = 5, slowk_n: int = 3, slowk_matype: int = 0, slowd_n: int = 3, slowd_matype: int = 0) -> Indicator:
    """
    TA_STOCH - Stochastic
              
    :parma KData data: KData object
    :param int fastk_n: Time period for building the Fast-K line (From 1 to 100000)
    :param int slowk_n: Smoothing for making the Slow-K line. Usually set to 3 (From 1 to 100000)
    :param int slowk_matype: Type of Moving Average for Slow K (From 0 to 8)
    :param int slowd_n: Smoothing for making the Slow-D line (From 1 to 100000)
    :param int slowd_matype: Type of Moving Average for Slow D (From 0 to 8))  
    :return: result0 - slow K 
             result1 - slow D
    """
@typing.overload
def TA_STOCHF(fastk_n: int = 5, fastd_n: int = 3, fastd_matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_STOCHF(data: KData, fastk_n: int = 5, fastd_n: int = 3, fastd_matype: int = 0) -> Indicator:
    """
    TA_STOCHF - Stochastic Fast
    
    :param KData data: input KData object
    :param int fastk_n: Time period for building the Fast-K line (From 1 to 100000)
    :param int fastd_n: Smoothing for making the Fast-D line. Usually set to 3 (From 1 to 100000)
    :param int fastd_matype: Type of Moving Average for Fast D (From 0 to 8))
    :return: result0 - fast K 
             result1 - fast D
    """
@typing.overload
def TA_STOCHRSI(n: int = 14, fastk_n: int = 5, fastd_n: int = 3, matype: int = 0) -> Indicator:
    ...
@typing.overload
def TA_STOCHRSI(data: Indicator, n: int = 14, fastk_n: int = 5, fastd_n: int = 3, matype: int = 0) -> Indicator:
    """
    TA_STOCHRSI - Stochastic Relative Strength Index
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param int fastk_n: Time period for building the Fast-K line (From 1 to 100000)
    :param int fastd_n: Smoothing for making the Fast-D line. Usually set to 3 (From 1 to 100000)
    :param int matype: Type of Moving Average for Fast D (From 0 to 8))
    :return: result0 - fast K 
             result1 - fast D
    """
@typing.overload
def TA_SUB(fill_null: bool = True) -> Indicator:
    ...
@typing.overload
def TA_SUB(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_SUB - Vector Arithmetic Subtraction
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
@typing.overload
def TA_SUM(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_SUM(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_SUM(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_SUM(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_SUM(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_SUM - Summation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_T3(n: int = 5, vfactor: float = 0.7) -> Indicator:
    ...
@typing.overload
def TA_T3(data: Indicator, n: int = 5, vfactor: float = 0.7) -> Indicator:
    """
    TA_T3 - Triple Exponential Moving Average (T3)
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param float vfactor: Volume Factor (From 0 to 1)
    """
@typing.overload
def TA_TAN() -> Indicator:
    ...
@typing.overload
def TA_TAN(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_TAN(arg0: float) -> Indicator:
    """
    TA_TAN - Vector Trigonometric Tan
    """
@typing.overload
def TA_TANH() -> Indicator:
    ...
@typing.overload
def TA_TANH(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def TA_TANH(arg0: float) -> Indicator:
    """
    TA_TANH - Vector Trigonometric Tanh
    """
@typing.overload
def TA_TEMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_TEMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TEMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TEMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_TEMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TEMA - Triple Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_TRANGE() -> Indicator:
    ...
@typing.overload
def TA_TRANGE(data: KData) -> Indicator:
    """
    TA_TRANGE - True Range
    """
@typing.overload
def TA_TRIMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_TRIMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TRIMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TRIMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_TRIMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TRIMA - Triangular Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_TRIX(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_TRIX(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TRIX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TRIX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_TRIX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
@typing.overload
def TA_TSF(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_TSF(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TSF(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_TSF(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_TSF(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_TSF - Time Series Forecast
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_TYPPRICE() -> Indicator:
    ...
@typing.overload
def TA_TYPPRICE(data: KData) -> Indicator:
    """
    TA_TYPPRICE - Typical Price
    """
@typing.overload
def TA_ULTOSC(n1: int = 7, n2: int = 14, n3: int = 28) -> Indicator:
    ...
@typing.overload
def TA_ULTOSC(data: KData, n1: int = 7, n2: int = 14, n3: int = 28) -> Indicator:
    """
    TA_ULTOSC - Ultimate Oscillator
    
    :param KData data: input KData object
    :param int n1: Number of bars for 1st period (From 1 to 100000)
    :param int n2: Number of bars fro 2nd period (From 1 to 100000)
    :param int n3: Number of bars for 3rd period (From 1 to 100000)
    """
@typing.overload
def TA_VAR(n: int = 5, nbdev: float = 1.0) -> Indicator:
    ...
@typing.overload
def TA_VAR(data: Indicator, n: int = 5, nbdev: float = 1.0) -> Indicator:
    """
    TA_VAR - Variance
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    :param float nbdev: Nb of deviations
    """
@typing.overload
def TA_WCLPRICE() -> Indicator:
    ...
@typing.overload
def TA_WCLPRICE(data: KData) -> Indicator:
    """
    TA_WCLPRICE - Weighted Close Price
    """
@typing.overload
def TA_WILLR(n: int = 14) -> Indicator:
    ...
@typing.overload
def TA_WILLR(data: KData, n: int = 14) -> Indicator:
    """
    TA_WILLR - Williams' %R
        
    :param KData data: input KData object
    :param int n: Number of period (From 2 to 100000)
    """
@typing.overload
def TA_WMA(n: int = 30) -> Indicator:
    ...
@typing.overload
def TA_WMA(arg0: IndParam) -> Indicator:
    ...
@typing.overload
def TA_WMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
@typing.overload
def TA_WMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def TA_WMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_WMA - Weighted Moving Average
        
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
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
def TC_TestStub() -> TradeCostBase:
    """
    仅用于测试
    """
def TC_Zero() -> TradeCostBase:
    """
    零交易成本算法
    """
@typing.overload
def TIME() -> Indicator:
    ...
@typing.overload
def TIME(arg0: KData) -> Indicator:
    """
    TIME([data])
    
        取得该周期的时分秒。用法: TIME 函数返回有效值范围为(000000-235959)。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
@typing.overload
def TIMELINE() -> Indicator:
    ...
@typing.overload
def TIMELINE(arg0: KData) -> Indicator:
    """
    TIMELINE([k])
    
        分时价格数据
    
        :param KData k: 上下文
        :rtype: Indicator
    """
@typing.overload
def TIMELINEVOL() -> Indicator:
    ...
@typing.overload
def TIMELINEVOL(arg0: KData) -> Indicator:
    """
    TIMELINEVOL([k])
    
        分时成交量数据
    
        :param KData k: 上下文
        :rtype: Indicator
    """
@typing.overload
def TR() -> Indicator:
    ...
@typing.overload
def TR(kdata: KData) -> Indicator:
    """
    TR([kdata])
    
        真实波动幅度(TR)是以下三个值中的最大值:
        1. 当前周期最高价与最低价之差
        2. 当前周期最高价与前一周期收盘价之差的绝对值
        3. 当前周期最低价与前一周期收盘价之差的绝对值
    
        :param KData kdata: K线数据
        :rtype: Indicator
    """
@typing.overload
def TURNOVER(n: int = 1) -> Indicator:
    ...
@typing.overload
def TURNOVER(kdata: KData, n: int = 1) -> Indicator:
    """
    TURNOVER(data[,n=1])
        换手率=股票成交量/流通股股数×100%
    
        :param int n: 时间窗口
    """
@typing.overload
def UPNDAY(data: Indicator, n: int = 3) -> Indicator:
    ...
@typing.overload
def UPNDAY(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def UPNDAY(data: Indicator, n: Indicator) -> Indicator:
    """
    UPNDAY(data[, n=3])
    
        连涨周期数, UPNDAY(CLOSE,M)表示连涨M个周期
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def VAR(n: int = 10) -> Indicator:
    ...
@typing.overload
def VAR(n: IndParam) -> Indicator:
    ...
@typing.overload
def VAR(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def VAR(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def VAR(data: Indicator, n: int = 10) -> Indicator:
    """
    VAR([data, n=10])
    
        估算样本方差, VAR(X,N)为X的N日估算样本方差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def VARP(n: int = 10) -> Indicator:
    ...
@typing.overload
def VARP(n: IndParam) -> Indicator:
    ...
@typing.overload
def VARP(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def VARP(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def VARP(data: Indicator, n: int = 10) -> Indicator:
    """
    VARP([data, n=10])
    
        总体样本方差, VARP(X,N)为X的N日总体样本方差
    
        :param Indicator data: 输入数据
        :param int n|Indicator|IndParam: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def VIGOR(kdata: KData, n: int = 2) -> Indicator:
    ...
@typing.overload
def VIGOR(n: int = 2) -> Indicator:
    """
    VIGOR([kdata, n=2])
    
        亚历山大.艾尔德力度指数 [BOOK2]_
    
        计算公式：（收盘价今－收盘价昨）＊成交量今
    
        :param KData data: 输入数据
        :param int n: EMA平滑窗口
        :rtype: Indicator
    """
@typing.overload
def WEAVE(arg0: typing.Sequence) -> Indicator:
    ...
@typing.overload
def WEAVE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
@typing.overload
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
@typing.overload
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator) -> Indicator:
    ...
@typing.overload
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator) -> Indicator:
    ...
@typing.overload
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator, arg5: Indicator) -> Indicator:
    """
    WEAVE(ind1, ind2[, ind3, ind4, ind5, ind6])
    
        将最多6个Indicator的结果组合在一起放在一个Indicator中。如ind = WEAVE(ind1, ind2), 则此时ind包含多个结果，按ind1、ind2的顺序存放。
        
        :param Indicator ind1: 指标1
        :param Indicator ind2: 指标2
        :param Indicator ind3: 指标3, 可省略
        :param Indicator ind4: 指标4, 可省略
        :param Indicator ind5: 指标5, 可省略
        :param Indicator ind6: 指标6, 可省略
        :rtype: Indicator
    """
@typing.overload
def WEEK() -> Indicator:
    ...
@typing.overload
def WEEK(arg0: KData) -> Indicator:
    """
    WEEK([data])
    
        取得该周期的星期数。用法：WEEK 函数返回有效值范围为(0-6)，0表示星期天。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
@typing.overload
def WINNER() -> Indicator:
    ...
@typing.overload
def WINNER(arg0: Indicator) -> Indicator:
    ...
@typing.overload
def WINNER(arg0: float) -> Indicator:
    """
    WINNER([ind])
        
        获利盘比例
        用法: WINNER(CLOSE)　表示以当前收市价卖出的获利盘比例。
        例如: 返回0.1表示10%获利盘;WINNER(10.5)表示10.5元价格的获利盘比例
        该函数仅对日线分析周期有效，且仅对存在流通盘权息数据的证券有效，对指数、基金等无效。
    """
@typing.overload
def WMA(n: int = 22) -> Indicator:
    ...
@typing.overload
def WMA(n: IndParam) -> Indicator:
    ...
@typing.overload
def WMA(data: Indicator, n: IndParam) -> Indicator:
    ...
@typing.overload
def WMA(data: Indicator, n: Indicator) -> Indicator:
    ...
@typing.overload
def WMA(data: Indicator, n: int = 22) -> Indicator:
    """
    WMA([data, n=22])
    
        加权移动平均，算法:Yn=(1*X1+2*X2+...+n*Xn)/(1+2+...+n)
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
@typing.overload
def YEAR() -> Indicator:
    ...
@typing.overload
def YEAR(arg0: KData) -> Indicator:
    """
    YEAR([data])
    
        取得该周期的年份。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
@typing.overload
def ZHBOND10(default_val: float = 0.4) -> Indicator:
    ...
@typing.overload
def ZHBOND10(data: DatetimeList, default_val: float = 0.4) -> Indicator:
    ...
@typing.overload
def ZHBOND10(data: KData, default_val: float = 0.4) -> Indicator:
    ...
@typing.overload
def ZHBOND10(data: Indicator, default_val: float = 0.4) -> Indicator:
    """
    ZHBOND10([data, defaut_val])
    
        获取10年期中国国债收益率
    
        :param DatetimeList|KDate|Indicator data: 输入的日期参考，优先使用上下文中的日期
        :param float default_val: 如果输入的日期早于已有国债数据的最早记录，则使用此默认值
    """
@typing.overload
def ZONGGUBEN() -> Indicator:
    ...
@typing.overload
def ZONGGUBEN(arg0: KData) -> Indicator:
    """
    ZONGGUBEN(kdata)
    
       获取总股本（单位：万股）
    
       :param KData kdata: k线数据
       :rtype: Indicator
    """
@typing.overload
def ZSCORE(out_extreme: bool = False, nsigma: float = 3.0, recursive: bool = False) -> Indicator:
    ...
@typing.overload
def ZSCORE(data: Indicator, out_extreme: bool = False, nsigma: float = 3.0, recursive: bool = False) -> Indicator:
    """
    ZSCORE(data[, out_extreme, nsigma, recursive])
    
        对数据进行标准化（归一），可选进行极值排除
    
        注：非窗口滚动，如需窗口滚动的标准化，直接 (x - MA(x, n)) / STDEV(x, n) 即可。
        
        :param Indicator data: 待剔除异常值的数据
        :param bool outExtreme: 指示剔除极值，默认 False
        :param float nsigma: 剔除极值时使用的 nsigma 倍 sigma，默认 3.0
        :param bool recursive: 是否进行递归剔除极值，默认 False
        :rtype: Indicator
    """
def batch_calculate_inds(arg0: typing.Sequence, arg1: KData) -> list:
    """
    batch_calculate_inds(inds, kdata) -> list)
        
        并行计算多个指标
        
        :param list inds: 指标列表
        :param KData kdata: K线数据
        :return: 指标计算结果列表
        :rtype: list
    """
def can_upgrade() -> bool:
    ...
def close_ostream_to_python() -> None:
    ...
def close_spend_time() -> None:
    """
    全局关闭 c++ 部分耗时打印
    """
def combinate_ind(inds: typing.Sequence, n: int = 7) -> list:
    """
    combinate_ind(inds[, n=7])
    
        对输入的指标序列进行组合, 如输入为 [ind1, ind2], 输出为 [EXIST(ind1,n), EXIST(ind2,n),
        EXIST(ind1,n)&EXIST(ind2,n)]
    
        :param list|tuple|seq inds: 待组合的指标列表
        :param int n: 指标在 n 周期内存在
        :return: 组合后的指标列表
        :rtype: list
    """
def combinate_index(arg0: typing.Any) -> list:
    """
    combinate_index(seq)
    
        获取序列组合的下标索引, 输入序列的长度最大不超过15，否则抛出异常
    
        :param inds: list 或 tuple 等可使用索引的可迭代对象
        :return: 返回组合的索引，可用于获取输入中相应索引位置的值
        :rtype: list
    """
def crtBrokerTM(broker: OrderBrokerBase, cost_func: TradeCostBase = ..., name: str = 'SYS', other_brokers: list[OrderBrokerBase] = []) -> TradeManager:
    ...
def crtSEOptimal(arg0: typing.Callable) -> SelectorBase:
    """
    crtSEOptimal(func)
        
        快速创建自定义绩效评估函数的寻优选择器
    
        :param func: 一个可调用对象，接收参数为 (sys, lastdate)，返回一个 float 数值
    """
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
def crt_pf_strategy(pf: Portfolio, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, name: str = 'PFStrategy', other_brokers: list[OrderBrokerBase] = [], config: str = '') -> Strategy:
    ...
def crt_sys_strategy(sys: System, stk_market_code: str, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: str = [], name: list[OrderBrokerBase] = 'SYSStrategy', config: str = '') -> Strategy:
    ...
def find_optimal_system(sys_list: list[System], stock: Stock, query: Query, sort_key: str = '', sort_mode: int = 0) -> tuple[float, System]:
    ...
def find_optimal_system_multi(sys_list: list[System], stock: Stock, query: Query, sort_key: str = '', sort_mode: int = 0) -> tuple[float, System]:
    ...
def get_block(arg0: str, arg1: str) -> Block:
    """
    get_block(category: str, name: str)
        
        获取预定义板块
    
        :param str category: 板块分类
        :param str name: 板块名称
        :rtype: Block
    """
def get_business_name(arg0: BUSINESS) -> str:
    """
    get_business_name(business)
    
        :param BUSINESS business: 交易业务类型
        :return: 交易业务类型名称("INIT"|"BUY"|"SELL"|"GIFT"|"BONUS"|"CHECKIN"|"CHECKOUT"|"UNKNOWN"
        :rtype: string
    """
def get_data_from_buffer_server(arg0: str, arg1: list[Stock], arg2: str) -> None:
    ...
def get_date_range(start: Datetime, end: Datetime) -> DatetimeList:
    """
    get_date_range(start, end)
    
        获取指定 [start, end) 日期时间范围的自然日日历日期列表，仅支持到日
        为防止内存占用过大，end如果超出系统明日日期，则强制为系统明日日期。
        
        :param Datetime start: 起始日期
        :param Datetime end: 结束日期
        :rtype: DatetimeList
    """
@typing.overload
def get_kdata(arg0: str, arg1: Query) -> KData:
    ...
@typing.overload
def get_kdata(market_code: str, start: int = 0, end: int = 9223372036854775807, ktype: str = 'DAY', recover_type: Query.RecoverType = ...) -> KData:
    """
    根据证券代码及起止位置获取 [start, end) 范围的 K 线数据
    
        :param str market_code: 证券代码，如: 'sh000001'
        :param int start: 起始索引
        :param int end: 结束索引
        :param Query.KType ktype: K 线类型, 'DAY'|'WEEK'|'MONTH'|'QUARTER'|'HALFYEAR'|'YEAR'|'MIN'|'MIN5'|'MIN15'|'MIN30'|'MIN60'
        :param Query.RecoverType recover_type: 复权类型
    """
@typing.overload
def get_kdata(market_code: str, start: Datetime = ..., end: Datetime = ..., ktype: str = 'DAY', recover_type: Query.RecoverType = ...) -> KData:
    """
    根据证券代码及起止日期获取 [start, end) 范围的 K 线数据
    
        :param str market_code: 证券代码，如: 'sh000001'
        :param int start: 起始日期
        :param int end: 结束日期
        :param Query.KType ktype: K 线类型, 'DAY'|'WEEK'|'MONTH'|'QUARTER'|'HALFYEAR'|'YEAR'|'MIN'|'MIN5'|'MIN15'|'MIN30'|'MIN60'
        :param Query.RecoverType recover_type: 复权类型
    """
def get_last_version() -> str:
    ...
def get_log_level() -> LOG_LEVEL:
    """
    获取当前日志级别
    """
def get_stock(arg0: str) -> Stock:
    """
    get_stock(market_code)
    
            根据"市场简称证券代码"获取对应的证券实例
    
            :param str market_code: 格式：“市场简称证券代码”，如"sh000001"
            :return: 对应的证券实例，如果实例不存在，则返回空实例，即Stock()，不抛出异常
            :rtype: Stock
    """
def get_system_part_enum(arg0: str) -> SystemPart:
    """
    get_system_part_enum(part_name)
    
         根据系统部件的字符串名称获取相应的枚举值
    
        :param str part_name: 系统部件的字符串名称，参见：:py:func:`getSystemPartName`
        :rtype: System.Part
    """
def get_system_part_name(arg0: int) -> str:
    """
    get_system_part_name(part)
    
        获取部件的字符串名称
        
            - System.Part.ENVIRONMENT  - "EV"
            - System.Part.CONDITION    - "CN"
            - System.Part.SIGNAL       - "SG"
            - System.Part.STOPLOSS     - "ST"
            - System.Part.TAKEPROFIT   - "TP"
            - System.Part.MONEYMANAGER - "MM"
            - System.Part.PROFITGOAL   - "PG"
            - System.Part.SLIPPAGE     - "SP"
            - System.Part.INVALID      - "--"
    
        :param int part: System.Part 枚举值
        :rtype: str
    """
def get_version() -> str:
    """
    getVersion()
    
            :return: hikyuu 当前版本
            :rtype: str
    """
def get_version_git() -> str:
    ...
def get_version_with_build() -> str:
    ...
def hikyuu_init(filename: str, ignore_preload: bool = False, context: StrategyContext = ...) -> None:
    ...
def inner_analysis_sys_list(arg0: typing.Any, arg1: Query, arg2: System) -> dict:
    ...
def inner_combinate_ind_analysis(arg0: Stock, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
    ...
def inner_combinate_ind_analysis_with_block(arg0: Block, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
    ...
def isinf(arg0: float) -> bool:
    """
    是否是无穷大或无穷小
    """
def isnan(arg0: float) -> bool:
    """
    是否为非数字
    """
def open_ostream_to_python() -> None:
    ...
def open_spend_time() -> None:
    """
    全局开启 c++ 部分耗时打印
    """
@typing.overload
def roundDown(number: float, ndigits: int = 0) -> float:
    ...
@typing.overload
def roundDown(number: float, ndigits: int = 0) -> float:
    """
    roundDown(number[, ndigits=0])
    
        向下截取，如10.1截取后为10
    
        :param float number  待处理数据
        :param int ndigits 保留小数位数
        :rtype: float
    """
@typing.overload
def roundEx(number: float, ndigits: int = 0) -> float:
    ...
@typing.overload
def roundEx(number: float, ndigits: int = 0) -> float:
    """
    roundEx(number[, ndigits=0])
    
        四舍五入，ROUND_HALF_EVEN 银行家舍入法
    
        :param float number  待四舍五入的数据
        :param int ndigits 保留小数位数
        :rype: float
    """
@typing.overload
def roundUp(number: float, ndigits: int = 0) -> float:
    ...
@typing.overload
def roundUp(number: float, ndigits: int = 0) -> float:
    """
    roundUp(number[, ndigits=0])
    
        向上截取，如10.1截取后为11
    
        :param float number  待处理数据
        :param int ndigits 保留小数位数
        :rtype: float
    """
@typing.overload
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
@typing.overload
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
def set_log_level(arg0: LOG_LEVEL) -> None:
    """
    设置当前日志级别
    """
def set_python_in_interactive(arg0: bool) -> None:
    ...
def set_python_in_jupyter(arg0: bool) -> None:
    ...
def start_spot_agent(print: bool = False, worker_num: int = 1, addr: str = '') -> None:
    ...
def stop_spot_agent() -> None:
    ...
def toPriceList(arg0: typing.Sequence) -> list[float]:
    """
    将 python list/tuple/np.arry 对象转化为 PriceList 对象
    """
DEBUG: LOG_LEVEL  # value = <LOG_LEVEL.DEBUG: 1>
ERROR: LOG_LEVEL  # value = <LOG_LEVEL.ERROR: 4>
FATAL: LOG_LEVEL  # value = <LOG_LEVEL.FATAL: 5>
INFO: LOG_LEVEL  # value = <LOG_LEVEL.INFO: 2>
OFF: LOG_LEVEL  # value = <LOG_LEVEL.OFF: 6>
TRACE: LOG_LEVEL  # value = <LOG_LEVEL.TRACE: 0>
WARN: LOG_LEVEL  # value = <LOG_LEVEL.WARN: 3>
constant: Constant  # value = <hikyuu.cpp.core311.Constant object>

```

