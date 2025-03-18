## KData

```python
class KData:
    """
    通过 Stock.getKData 获取的K线数据，由 KRecord 组成的数组，可象 list 一样进行遍历
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __getitem__(kdata, i):
        """
        
            :param i: int | Datetime | slice | str 类型
            
        """
    @staticmethod
    def __iter__(kdata):
        ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def kplot(kdata, new = True, axes = None, colorup = 'r', colordown = 'g'):
        """
        绘制K线图
        
            :param KData kdata: K线数据
            :param bool new:    是否在新窗口中显示，只在没有指定axes时生效
            :param axes:        指定的坐标轴
            :param colorup:     the color of the rectangle where close >= open
            :param colordown:   the color of the rectangle where close < open
            
        """
    @staticmethod
    def mkplot(kdata, new = True, axes = None, colorup = 'r', colordown = 'g', ticksize = 3):
        """
        绘制美式K线图
        
            :param KData kdata: K线数据
            :param bool new:    是否在新窗口中显示，只在没有指定axes时生效
            :param axes:        指定的坐标轴
            :param colorup:     the color of the lines where close >= open
            :param colordown:   the color of the lines where close < open
            :param ticksize:    open/close tick marker in points
            
        """
    @staticmethod
    def plot(kdata, new = True, axes = None, colorup = 'r', colordown = 'g'):
        """
        绘制K线图
        
            :param KData kdata: K线数据
            :param bool new:    是否在新窗口中显示，只在没有指定axes时生效
            :param axes:        指定的坐标轴
            :param colorup:     the color of the rectangle where close >= open
            :param colordown:   the color of the rectangle where close < open
            
        """
    @staticmethod
    def to_df(kdata):
        """
        转化为pandas的DataFrame
        """
    @staticmethod
    def to_np(kdata):
        """
        转化为numpy结构数组
        """
    def __eq__(self, arg0: KData) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: KData) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def empty(self) -> bool:
        """
        empty(self)
        
                判断是否为空
        
                :rtype: bool
        """
    def get(self, arg0: int) -> KRecord:
        """
        get(self, pos)
        
                获取指定索引位置的K线记录
        
                :param int pos: 位置索引
                :rtype: KRecord
        """
    def get_by_datetime(self, arg0: Datetime) -> KRecord:
        """
        get_by_datetime(self, datetime)
        
                获取指定时间的K线记录。
        
                :param Datetime datetime: 指定的日期
                :rtype: KRecord
        """
    def get_datetime_list(self) -> DatetimeList:
        """
        get_datetime_list(self)
        
                返回交易日期列表
        
                :rtype: DatetimeList
        """
    def get_kdata(self, arg0: Datetime, arg1: Datetime) -> KData:
        """
        get_kdata(self, start_date, end_date)
              
                通过当前 KData 获取一个保持数据类型、复权类型不变的新的 KData（注意，不是原 KData 的子集）
        
                :param Datetime start: 新的起始日期
                :param Datetime end: 新的结束日期
                :rtype: KData
        """
    def get_pos(self, arg0: Datetime) -> typing.Any:
        """
        get_pos(self, datetime)
        
                获取指定时间的K线记录的索引位置, 如果不在数据范围内，则返回 None
                
                :param Datetime datetime: 指定的日期
                :rtype: int
        """
    def get_pos_in_stock(self, arg0: Datetime) -> typing.Any:
        """
        get_pos_in_stock(self, datetime) 
                
                获取指定时间对应的原始K线中的索引位置
        
                :param Datetime datetime: 指定的时间
                :return: 对应的索引位置，如果不在数据范围内，则返回 None
        """
    def get_query(self) -> Query:
        """
        get_query(self)
        
                获取关联的查询条件
        
                :rtype: KQuery
        """
    def get_stock(self) -> ...:
        """
        get_stock(self)
        
                获取关联的Stock
        
                :rtype: Stock
        """
    def tocsv(self, arg0: str) -> None:
        """
        tocsv(self, filename)
        
                将数据保存至CSV文件
        
                :param str filename: 指定保存的文件名称
        """
    @property
    def amo(self) -> ...:
        """
        返回包含成交金额的 Indicator 实例，相当于 AMO(k)
        """
    @property
    def close(self) -> ...:
        """
        返回包含收盘价的 Indicator 实例，相当于 CLOSE(k)
        """
    @property
    def end_pos(self) -> int:
        """
        获取在原始K线记录中对应范围的下一条记录的位置，如果为空返回0,其他等于lastPos + 1
        """
    @property
    def high(self) -> ...:
        """
        返回包含最高价的 Indicator 实例，相当于 HIGH(k)
        """
    @property
    def last_pos(self) -> int:
        """
        获取在原始K线记录中对应的最后一条记录的位置，如果为空返回0,其他等于endPos - 1
        """
    @property
    def low(self) -> ...:
        """
        返回包含最低价的 Indicator 实例，相当于 LOW(k)
        """
    @property
    def open(self) -> ...:
        """
        返回包含开盘价的 Indicator 实例，相当于 OPEN(k)
        """
    @property
    def start_pos(self) -> int:
        """
        获取在原始K线记录中对应的起始位置，如果KData为空返回0
        """
    @property
    def vol(self) -> ...:
        """
        返回包含成交量的 Indicator 实例，相当于 VOL(k)
        """
```

## 相关方法

#### ALIGN

```python
def ALIGN(data: Indicator, ref: KData, fill_null: bool = True) -> Indicator:
    """
    ALIGN(data, ref):
    
        按指定的参考日期对齐
    
        :param Indicator data: 输入数据
        :param DatetimeList|Indicator|KData ref: 指定做为日期参考的 DatetimeList、Indicator 或 KData
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
        :retype: Indicator
    """
```

#### ATR

```python
def ATR(kdata: KData, n: int = 14) -> Indicator:
    """
    ATR([kdata, n=14])
    
        平均真实波幅(Average True Range), 真实波动幅度 TR 的简单移动均值
    
        :param KData kdata 待计算的源数据
        :param int n: 计算均值的周期窗口，必须为大于1的整数
        :rtype: Indicator
    """
```

#### CONTEXT_K

```python
def CONTEXT_K(arg0: Indicator) -> KData:
    """
    CONTEXT_K(ind)
    
        获取指标上下文。Indicator::getContext()方法获取的是当前的上下文，但对于 CONTEXT 独立上下文指标无法获取其指定的独立上下文，需用此方法获取
    
        :param Indicator ind: 指标对象
        :rtype: KData
    """
```

#### COST

```python
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
```

#### CYCLE

```python
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
```

#### FINANCE

```python
def FINANCE(kdata: KData, ix: int) -> Indicator:
    ...
```

#### FINANCE

```python
def FINANCE(kdata: KData, name: str) -> Indicator:
    """
    FINANCE([kdata, ix, name])
    
        获取历史财务信息。（可通过 StockManager.get_history_finance_all_fields 查询相应的历史财务字段信息）
    
        ix, name 使用时，为二选一。即要不使用 ix，要不就使用 name 进行获取。
    
        :param KData kdata: K线数据
        :param int ix: 历史财务信息字段索引
        :param int name: 历史财务信息字段名称
    """
```

#### INBLOCK

```python
def INBLOCK(data: KData, category: str, name: str) -> Indicator:
    """
    INBLOCK(data, category, name)        
    
        当前上下文证券是否在指定的板块中。
    
        :param KData data: 指定的K线数据(上下文)
        :param string category: 板块类别
        :param string name: 板块名称
        :rtype: Indicator
    """
```

#### INDEXA

```python
def INDEXA(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXA([kdata])
        
        返回对应的大盘成交金额,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXC

```python
def INDEXC(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXC([kdata])
        
        返回对应的大盘收盘价,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXH

```python
def INDEXH(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXH([kdata])
        
        返回对应的大盘最高价,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXL

```python
def INDEXL(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXL([kdata])
        
        返回对应的大盘最低价,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXO

```python
def INDEXO(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXO([kdata])
        
        返回对应的大盘开盘价,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXV

```python
def INDEXV(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXV([kdata])
        
        返回对应的大盘成交量,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### KDATA_PART

```python
def KDATA_PART(data: KData, kpart: str) -> Indicator:
    ...
```

#### TA_ACCBANDS

```python
def TA_ACCBANDS(data: KData, n: int = 20) -> Indicator:
    """
    TA_ACCBANDS - Acceleration Bands
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_ADOSC

```python
def TA_ADOSC(data: KData, fast_n: int = 3, slow_n: int = 10) -> Indicator:
    """
    TA_ADOSC - Chaikin A/D Oscillator
    
    :param KData data: input KData
    :param int fast_n: Number of period for the fast MA (From 2 to 100000)
    :param int slow_n: Number of period for the slow MA (From 2 to 100000)
    """
```

#### TA_ADX

```python
def TA_ADX(data: KData, n: int = 14) -> Indicator:
    """
    TA_ADX - Average Directional Movement Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_ADXR

```python
def TA_ADXR(data: KData, n: int = 14) -> Indicator:
    """
    TA_ADXR - Average Directional Movement Index Rating
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_AROON

```python
def TA_AROON(data: KData, n: int = 14) -> Indicator:
    """
    TA_AROON - Aroon
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - Aroon down
             result(2) - Aroon up
    """
```

#### TA_AROONOSC

```python
def TA_AROONOSC(data: KData, n: int = 14) -> Indicator:
    """
    TA_AROONOSC - Aroon Oscillator
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_ATR

```python
def TA_ATR(data: KData, n: int = 14) -> Indicator:
    """
    TA_ATR - Average True Range
        
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_CCI

```python
def TA_CCI(data: KData, n: int = 14) -> Indicator:
    """
    TA_CCI - Commodity Channel Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_CDLABANDONEDBABY

```python
def TA_CDLABANDONEDBABY(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLABANDONEDBABY - Abandoned Baby
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_CDLDARKCLOUDCOVER

```python
def TA_CDLDARKCLOUDCOVER(data: KData, penetration: float = 0.5) -> Indicator:
    """
    TA_CDLDARKCLOUDCOVER - Dark Cloud Cover
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_CDLEVENINGDOJISTAR

```python
def TA_CDLEVENINGDOJISTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLEVENINGDOJISTAR - Evening Doji Star
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_CDLEVENINGSTAR

```python
def TA_CDLEVENINGSTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLEVENINGSTAR - Evening Star
                
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_CDLMATHOLD

```python
def TA_CDLMATHOLD(data: KData, penetration: float = 0.5) -> Indicator:
    """
    TA_CDLMATHOLD - Mat Hold
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_CDLMORNINGDOJISTAR

```python
def TA_CDLMORNINGDOJISTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLMORNINGDOJISTAR - Morning Doji Star
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_CDLMORNINGSTAR

```python
def TA_CDLMORNINGSTAR(data: KData, penetration: float = 0.3) -> Indicator:
    """
    TA_CDLMORNINGSTAR - Morning Star
    
    :param KData data: input KData
    :param float penetration: Percentage of penetration of a candle within another candle (>=0)
    """
```

#### TA_DX

```python
def TA_DX(data: KData, n: int = 14) -> Indicator:
    """
    TA_DX - Directional Movement Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_IMI

```python
def TA_IMI(data: KData, n: int = 14) -> Indicator:
    """
    TA_IMI - Intraday Momentum Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MFI

```python
def TA_MFI(data: KData, n: int = 14) -> Indicator:
    """
    TA_MFI - Money Flow Index
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MIDPRICE

```python
def TA_MIDPRICE(data: KData, n: int = 14) -> Indicator:
    """
    TA_MIDPRICE - Midpoint Price over period
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MINUS_DI

```python
def TA_MINUS_DI(data: KData, n: int = 14) -> Indicator:
    """
    A_MINUS_DI - Minus Directional Indicator
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_MINUS_DM

```python
def TA_MINUS_DM(data: KData, n: int = 14) -> Indicator:
    """
    TA_MINUS_DM - Minus Directional Movement
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_NATR

```python
def TA_NATR(data: KData, n: int = 14) -> Indicator:
    """
    TA_NATR - Normalized Average True Range
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_PLUS_DI

```python
def TA_PLUS_DI(data: KData, n: int = 14) -> Indicator:
    """
    TA_PLUS_DI - Plus Directional Indicator
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_PLUS_DM

```python
def TA_PLUS_DM(data: KData, n: int = 14) -> Indicator:
    """
    TA_PLUS_DM - Plus Directional Movement
    
    :param KData data: input KData
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_SAR

```python
def TA_SAR(data: KData, acceleration: float = 0.02, maximum: float = 0.2) -> Indicator:
    """
    TA_SAR - Parabolic SAR
    
    :param KData data: input KData object
    :param float acceleration: Acceleration Factor used up to the Maximum value (>= 0.0)
    :param float maximum: Acceleration Factor Maximum value (>= 0.0)
    """
```

#### TA_SAREXT

```python
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
```

#### TA_STOCH

```python
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
```

#### TA_STOCHF

```python
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
```

#### TA_ULTOSC

```python
def TA_ULTOSC(data: KData, n1: int = 7, n2: int = 14, n3: int = 28) -> Indicator:
    """
    TA_ULTOSC - Ultimate Oscillator
    
    :param KData data: input KData object
    :param int n1: Number of bars for 1st period (From 1 to 100000)
    :param int n2: Number of bars fro 2nd period (From 1 to 100000)
    :param int n3: Number of bars for 3rd period (From 1 to 100000)
    """
```

#### TA_WILLR

```python
def TA_WILLR(data: KData, n: int = 14) -> Indicator:
    """
    TA_WILLR - Williams' %R
        
    :param KData data: input KData object
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TURNOVER

```python
def TURNOVER(kdata: KData, n: int = 1) -> Indicator:
    """
    TURNOVER(data[,n=1])
        换手率=股票成交量/流通股股数×100%
    
        :param int n: 时间窗口
    """
```

#### VIGOR

```python
def VIGOR(kdata: KData, n: int = 2) -> Indicator:
    ...
```

#### ZHBOND10

```python
def ZHBOND10(data: KData, default_val: float = 0.4) -> Indicator:
    ...
```

#### get_kdata

```python
def get_kdata(arg0: str, arg1: Query) -> KData:
    ...
```

#### get_kdata

```python
def get_kdata(market_code: str, start: int = 0, end: int = 9223372036854775807, ktype: str = 'DAY', recover_type: Query.RecoverType = ...) -> KData:
    """
    根据证券代码及起止位置获取 [start, end) 范围的 K 线数据
    
        :param str market_code: 证券代码，如: 'sh000001'
        :param int start: 起始索引
        :param int end: 结束索引
        :param Query.KType ktype: K 线类型, 'DAY'|'WEEK'|'MONTH'|'QUARTER'|'HALFYEAR'|'YEAR'|'MIN'|'MIN5'|'MIN15'|'MIN30'|'MIN60'
        :param Query.RecoverType recover_type: 复权类型
    """
```

#### get_kdata

```python
def get_kdata(market_code: str, start: Datetime = ..., end: Datetime = ..., ktype: str = 'DAY', recover_type: Query.RecoverType = ...) -> KData:
    """
    根据证券代码及起止日期获取 [start, end) 范围的 K 线数据
    
        :param str market_code: 证券代码，如: 'sh000001'
        :param int start: 起始日期
        :param int end: 结束日期
        :param Query.KType ktype: K 线类型, 'DAY'|'WEEK'|'MONTH'|'QUARTER'|'HALFYEAR'|'YEAR'|'MIN'|'MIN5'|'MIN15'|'MIN30'|'MIN60'
        :param Query.RecoverType recover_type: 复权类型
    """
```

