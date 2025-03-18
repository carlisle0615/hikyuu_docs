## Indicator

```python
class Indicator:
    """
    技术指标
    """
    @staticmethod
    def __getitem__(data, i):
        """
        
            :param i: int | Datetime | slice | str 类型
            
        """
    @staticmethod
    def __iter__(indicator):
        ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def bar(indicator, new = True, axes = None, kref = None, legend_on = False, text_on = False, text_color = 'k', label = None, width = 0.4, color = 'r', edgecolor = 'r', zero_on = False, *args, **kwargs):
        """
        绘制indicator柱状图
        
            :param Indicator indicator: Indicator实例
            :param axes:       指定的坐标轴
            :param new:        是否在新窗口中显示，只在没有指定axes时生效
            :param kref:       参考的K线数据，以便绘制日期X坐标
            :param legend_on:  是否打开图例
            :param text_on:    是否在左上角显示指标名称及其参数
            :param text_color: 指标名称解释文字的颜色，默认为黑色
            :param str label:  label显示文字信息，text_on 及 legend_on 为 True 时生效
            :param zero_on:    是否需要在y=0轴上绘制一条直线
            :param width:      Bar的宽度
            :param color:      Bar的颜色
            :param edgecolor:  Bar边缘颜色
            :param args:       pylab plot参数
            :param kwargs:     pylab plot参数
            
        """
    @staticmethod
    def exist_nan(*args, **kwargs) -> bool:
        """
        exist_nan(self, result_index)
        
            判断是否存在NaN值
        
            :param int result_index: 指定的结果集
            :rtype: bool
        """
    @staticmethod
    def heatmap(ind, axes = None):
        """
        
            绘制指标收益年-月收益热力图
        
            指标收益率 = (当前月末值 - 上月末值) / 上月末值 * 100
        
            指标应已计算（即有值），且为时间序列
        
            :param ind: 指定指标
            :param axes: 绘制的轴对象，默认为None，表示创建新的轴对象
            :return: None
            
        """
    @staticmethod
    def plot(indicator, new = True, axes = None, kref = None, legend_on = False, text_on = False, text_color = 'k', zero_on = False, label = None, linestyle = '-', *args, **kwargs):
        """
        绘制indicator曲线
        
            :param Indicator indicator: indicator实例
            :param axes:            指定的坐标轴
            :param new:             是否在新窗口中显示，只在没有指定axes时生效
            :param kref:            参考的K线数据，以便绘制日期X坐标
            :param legend_on:       是否打开图例
            :param text_on:         是否在左上角显示指标名称及其参数
            :param text_color:      指标名称解释文字的颜色，默认为黑色
            :param zero_on:         是否需要在y=0轴上绘制一条直线
            :param str label:       label显示文字信息，text_on 及 legend_on 为 True 时生效
            :param args:            pylab plot参数
            :param kwargs:          pylab plot参数，如：marker（标记类型）、
                                     markerfacecolor（标记颜色）、
                                     markeredgecolor（标记的边缘颜色）
            
        """
    @staticmethod
    def to_df(indicator):
        """
        转化为pandas.DataFrame
        """
    @typing.overload
    def __add__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __add__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __and__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __and__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __call__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __call__(self, arg0: KData) -> Indicator:
        ...
    @typing.overload
    def __call__(self) -> Indicator:
        ...
    @typing.overload
    def __eq__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __eq__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __eq__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __ge__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __ge__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __ge__(self, arg0: float) -> Indicator:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __gt__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __gt__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __gt__(self, arg0: float) -> Indicator:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        ...
    @typing.overload
    def __le__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __le__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __le__(self, arg0: float) -> Indicator:
        ...
    def __len__(self) -> int:
        ...
    @typing.overload
    def __lt__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __lt__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __lt__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __mod__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __mod__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __mul__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __mul__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __ne__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __ne__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __ne__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __or__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __or__(self, arg0: float) -> Indicator:
        ...
    def __radd__(self, arg0: float) -> Indicator:
        ...
    def __rand__(self, arg0: float) -> Indicator:
        ...
    def __repr__(self) -> str:
        ...
    def __rmod__(self, arg0: float) -> Indicator:
        ...
    def __rmul__(self, arg0: float) -> Indicator:
        ...
    def __ror__(self, arg0: float) -> Indicator:
        ...
    def __rsub__(self, arg0: float) -> Indicator:
        ...
    def __rtruediv__(self, arg0: float) -> Indicator:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def __sub__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __sub__(self, arg0: float) -> Indicator:
        ...
    @typing.overload
    def __truediv__(self, arg0: Indicator) -> Indicator:
        ...
    @typing.overload
    def __truediv__(self, arg0: float) -> Indicator:
        ...
    def clone(self) -> Indicator:
        """
        克隆操作
        """
    def empty(self) -> bool:
        """
        是否为空
        """
    def equal(self, arg0: Indicator) -> bool:
        ...
    def formula(self) -> str:
        """
        formula(self)
        
            打印指标公式
        
            :rtype: str
        """
    def get(self, pos: int, result_index: int = 0) -> float:
        """
        get(self, pos[, result_index=0])
        
            获取指定位置的值
        
            :param int pos: 指定的位置索引
            :param int result_index: 指定的结果集
            :rtype: float
        """
    def get_by_datetime(self, datetime: Datetime, result_index: int = 0) -> float:
        """
        get_by_datetime(self, date[, result_index=0])
        
            获取指定日期数值。如果对应日期无结果，返回 constant.null_price
        
            :param Datetime datetime: 指定日期
            :param int result_index: 指定的结果集
            :rtype: float
        """
    def get_context(self) -> KData:
        """
        get_context(self)
        
            获取上下文
        
            :rtype: KData
        """
    def get_datetime(self, arg0: int) -> Datetime:
        """
        get_datetime(self, pos)
        
            获取指定位置的日期
        
            :param int pos: 指定的位置索引
            :rtype: float
        """
    def get_datetime_list(self) -> DatetimeList:
        """
        get_datetime_list(self)
        
            返回对应的日期列表
        
            :rtype: DatetimeList
        """
    def get_imp(self) -> ...:
        ...
    def get_ind_param(self, arg0: str) -> ...:
        """
        get_ind_param(self, name)
            
            获取指定的动态指标参数
            
            :param str name: 参数名称
            :return: 动态指标参数
            :rtype: IndParam
            :raises out_of_range: 无此参数
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_pos(self, arg0: Datetime) -> typing.Any:
        """
        get_pos(self, date):
        
            获取指定日期相应的索引位置, 如果没有对应位置返回 None
        
            :param Datetime date: 指定日期
            :rtype: int
        """
    def get_result(self, arg0: int) -> Indicator:
        """
        get_result(self, result_index)
        
            获取指定结果集
        
            :param int result_index: 指定的结果集
            :rtype: Indicator
        """
    def get_result_as_price_list(self, arg0: int) -> list[float]:
        """
        get_result_as_price_list(self, result_index)
        
            获取指定结果集
        
            :param int result_index: 指定的结果集
            :rtype: PriceList
        """
    def get_result_num(self) -> int:
        """
        get_result_num(self)
        
            获取结果集数量
        
            :rtype: int
        """
    def have_ind_param(self, arg0: str) -> bool:
        """
        是否存在指定的动态指标参数
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def is_same(self, arg0: Indicator) -> bool:
        ...
    @typing.overload
    def set_context(self, arg0: Stock, arg1: Query) -> None:
        ...
    @typing.overload
    def set_context(self, arg0: KData) -> None:
        """
        set_context(self, kdata)
        
            设置上下文
        
            :param KData kdata: 关联的上下文K线)
              
        set_context(self, stock, query)
        
            设置上下文
        
            :param Stock stock: 指定的 Stock
            :param Query query: 指定的查询条件
        """
    def set_discard(self, arg0: int) -> None:
        """
        set_discard(self, discard)
            
            设置抛弃的个数，如果小于原有的discard则无效
            :param int discard: 需抛弃的点数，大于0
        """
    @typing.overload
    def set_ind_param(self, arg0: str, arg1: Indicator) -> None:
        ...
    @typing.overload
    def set_ind_param(self, arg0: str, arg1: ...) -> None:
        """
        set_param(self, name, ind)
        
            设置动态指标参数
        
            :param str name: 参数名称
            :param Indicator|IndParam: 参数值（可为 Indicator 或 IndParam 实例）
        """
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        set_param(self, name, value)
        
            设置参数
        
            :param str name: 参数名称
            :param value: 参数值
            :type value: int | bool | float | string | Query | KData | Stock | DatetimeList
            :raises logic_error: Unsupported type! 不支持的参数类型
        """
    def support_ind_param(self) -> bool:
        """
        是否支持动态指标参数
        """
    def to_np(self) -> numpy.ndarray[numpy.float64]:
        """
        转化为np.array，如果indicator存在多个值，只返回第一个
        """
    @property
    def discard(self) -> int:
        """
        结果中需抛弃的个数
        """
    @property
    def long_name(self) -> str:
        """
        返回形如：Name(param1_val,param2_val,...)
        """
    @property
    def name(self) -> str:
        """
        指标名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
```

## 相关方法

### 与Indicator相关的方法

#### ABS

```python
def ABS() -> Indicator:
    ...
```

#### ABS

```python
def ABS(arg0: float) -> Indicator:
    ...
```

#### ABS

```python
def ABS(arg0: Indicator) -> Indicator:
    """
    ABS([data])
    
        求绝对值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### ACOS

```python
def ACOS() -> Indicator:
    ...
```

#### ACOS

```python
def ACOS(arg0: Indicator) -> Indicator:
    ...
```

#### ACOS

```python
def ACOS(arg0: float) -> Indicator:
    """
    ACOS([data])
    
        反余弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### AD

```python
def AD() -> Indicator:
    ...
```

#### AD

```python
def AD(arg0: KData) -> Indicator:
    """
    AD(kdata)
    
       累积/派发线
    
       :param KData kdata: k线数据
       :rtype: Indicator
    """
```

#### ADVANCE

```python
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
```

#### ALIGN

```python
def ALIGN(ref: DatetimeList, fill_null: bool = True) -> Indicator:
    ...
```

#### ALIGN

```python
def ALIGN(data: Indicator, ref: DatetimeList, fill_null: bool = True) -> Indicator:
    ...
```

#### ALIGN

```python
def ALIGN(data: Indicator, ref: DatetimeList, fill_null: bool = True) -> Indicator:
    ...
```

#### ALIGN

```python
def ALIGN(data: Indicator, ref: Indicator, fill_null: bool = True) -> Indicator:
    ...
```

#### ALIGN

```python
def ALIGN(data: Indicator, ref: Indicator, fill_null: bool = True) -> Indicator:
    ...
```

#### ALIGN

```python
def ALIGN(data: Indicator, ref: Indicator, fill_null: bool = True) -> Indicator:
    ...
```

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

#### AMA

```python
def AMA(n: int = 10, fast_n: int = 2, slow_n: int = 30) -> Indicator:
    ...
```

#### AMA

```python
def AMA(n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: IndParam, fast_n: IndParam, slow_n: IndParam) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: Indicator, fast_n: Indicator, slow_n: Indicator) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: Indicator, fast_n: Indicator, slow_n: Indicator) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: Indicator, fast_n: Indicator, slow_n: Indicator) -> Indicator:
    ...
```

#### AMA

```python
def AMA(data: Indicator, n: Indicator, fast_n: Indicator, slow_n: Indicator) -> Indicator:
    ...
```

#### AMA

```python
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
```

#### AMA

```python
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
```

#### ASIN

```python
def ASIN() -> Indicator:
    ...
```

#### ASIN

```python
def ASIN(arg0: Indicator) -> Indicator:
    ...
```

#### ASIN

```python
def ASIN(arg0: float) -> Indicator:
    """
    ASIN([data])
    
        反正弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### ATAN

```python
def ATAN() -> Indicator:
    ...
```

#### ATAN

```python
def ATAN(arg0: Indicator) -> Indicator:
    ...
```

#### ATAN

```python
def ATAN(arg0: float) -> Indicator:
    """
    ATAN([data])
    
        反正切值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### ATR

```python
def ATR(n: int = 14) -> Indicator:
    ...
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

#### AVEDEV

```python
def AVEDEV(data: Indicator, n: int = 22) -> Indicator:
    ...
```

#### AVEDEV

```python
def AVEDEV(data: Indicator, n: int = 22) -> Indicator:
    ...
```

#### AVEDEV

```python
def AVEDEV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### AVEDEV

```python
def AVEDEV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### AVEDEV

```python
def AVEDEV(data: Indicator, n: Indicator) -> Indicator:
    """
    AVEDEV(data[, n=22])
    
        平均绝对偏差，求X的N日平均绝对偏差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### AVEDEV

```python
def AVEDEV(data: Indicator, n: Indicator) -> Indicator:
    """
    AVEDEV(data[, n=22])
    
        平均绝对偏差，求X的N日平均绝对偏差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### BACKSET

```python
def BACKSET(n: int = 2) -> Indicator:
    ...
```

#### BACKSET

```python
def BACKSET(n: IndParam) -> Indicator:
    ...
```

#### BACKSET

```python
def BACKSET(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### BACKSET

```python
def BACKSET(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### BACKSET

```python
def BACKSET(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### BACKSET

```python
def BACKSET(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### BACKSET

```python
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
```

#### BACKSET

```python
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
```

#### BARSCOUNT

```python
def BARSCOUNT() -> Indicator:
    ...
```

#### BARSCOUNT

```python
def BARSCOUNT(arg0: Indicator) -> Indicator:
    """
    BARSCOUNT([data])
    
        有效值周期数, 求总的周期数。
    
        用法：BARSCOUNT(X)第一个有效数据到当前的天数。
    
        例如：BARSCOUNT(CLOSE)对于日线数据取得上市以来总交易日数，对于1分钟线取得当日交易分钟数。
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### BARSLAST

```python
def BARSLAST() -> Indicator:
    ...
```

#### BARSLAST

```python
def BARSLAST(arg0: Indicator) -> Indicator:
    ...
```

#### BARSLAST

```python
def BARSLAST(arg0: float) -> Indicator:
    """
    BARSLAST([data])
    
        上一次条件成立位置 上一次条件成立到当前的周期数。
    
        用法：BARSLAST(X): 上一次 X 不为 0 到现在的天数。
    
        例如：BARSLAST(CLOSE/REF(CLOSE,1)>=1.1) 表示上一个涨停板到当前的周期数
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### BARSSINCE

```python
def BARSSINCE() -> Indicator:
    ...
```

#### BARSSINCE

```python
def BARSSINCE(arg0: Indicator) -> Indicator:
    ...
```

#### BARSSINCE

```python
def BARSSINCE(arg0: float) -> Indicator:
    """
    BARSSINCE([data])
    
        第一个条件成立位置到当前的周期数。
    
        用法：BARSSINCE(X):第一次X不为0到现在的天数。
    
        例如：BARSSINCE(HIGH>10)表示股价超过10元时到当前的周期数
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### BARSSINCEN

```python
def BARSSINCEN(n: int) -> Indicator:
    ...
```

#### BARSSINCEN

```python
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
```

#### BARSSINCEN

```python
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
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: float, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: float, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: float, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: Indicator, arg1: float, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: float, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: float, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: float, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: float, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### BETWEEN

```python
def BETWEEN(arg0: float, arg1: float, arg2: Indicator) -> Indicator:
    ...
```

#### BETWEEN

```python
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
```

#### BLOCKSETNUM

```python
def BLOCKSETNUM(block: Block) -> Indicator:
    ...
```

#### BLOCKSETNUM

```python
def BLOCKSETNUM(block: Block, query: Query) -> Indicator:
    """
    BLOCKSETNUM(block, query)
        
        横向统计（返回板块股个数）
    
        :param Block block: 待统计的板块
        :param Query query: 统计范围
    """
```

#### BLOCKSETNUM

```python
def BLOCKSETNUM(stks: typing.Sequence) -> Indicator:
    ...
```

#### BLOCKSETNUM

```python
def BLOCKSETNUM(stks: typing.Sequence, query: Query) -> Indicator:
    """
    BLOCKSETNUM(block, query)
        
        横向统计（返回板块股个数）
    
        :param Sequence stks: stock list
        :param Query query: 统计范围
    """
```

#### CEILING

```python
def CEILING() -> Indicator:
    ...
```

#### CEILING

```python
def CEILING(arg0: Indicator) -> Indicator:
    ...
```

#### CEILING

```python
def CEILING(arg0: float) -> Indicator:
    """
    CEILING([data])
    
        向上舍入(向数值增大方向舍入)取整
       
        用法：CEILING(A)返回沿A数值增大方向最接近的整数
       
        例如：CEILING(12.3)求得13；CEILING(-3.5)求得-3
       
        :param data: 输入数据
        :rtype: Indicator
    """
```

#### CONTEXT

```python
def CONTEXT(fill_null: bool = True) -> Indicator:
    ...
```

#### CONTEXT

```python
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
```

#### CONTEXT

```python
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
```

#### CORR

```python
def CORR(ref_ind: Indicator, n: int = 10, fill_null: bool = True) -> Indicator:
    ...
```

#### CORR

```python
def CORR(ref_ind: Indicator, n: int = 10, fill_null: bool = True) -> Indicator:
    ...
```

#### CORR

```python
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
```

#### CORR

```python
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
```

#### CORR

```python
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
```

#### COS

```python
def COS() -> Indicator:
    ...
```

#### COS

```python
def COS(arg0: Indicator) -> Indicator:
    ...
```

#### COS

```python
def COS(arg0: float) -> Indicator:
    """
    COS([data])
    
        余弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### COST

```python
def COST(x: float = 10.0) -> Indicator:
    ...
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

#### COUNT

```python
def COUNT(n: int = 20) -> Indicator:
    ...
```

#### COUNT

```python
def COUNT(n: IndParam) -> Indicator:
    ...
```

#### COUNT

```python
def COUNT(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### COUNT

```python
def COUNT(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### COUNT

```python
def COUNT(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### COUNT

```python
def COUNT(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### COUNT

```python
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
```

#### COUNT

```python
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
```

#### CROSS

```python
def CROSS(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### CROSS

```python
def CROSS(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### CROSS

```python
def CROSS(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### CROSS

```python
def CROSS(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### CROSS

```python
def CROSS(arg0: float, arg1: Indicator) -> Indicator:
    ...
```

#### CROSS

```python
def CROSS(arg0: float, arg1: float) -> Indicator:
    """
    CROSS(x, y)
    
        交叉函数
    
        :param x: 变量或常量，判断交叉的第一条线
        :param y: 变量或常量，判断交叉的第二条线
        :rtype: Indicator
    """
```

#### CVAL

```python
def CVAL(value: float = 0.0, discard: int = 0) -> Indicator:
    ...
```

#### CVAL

```python
def CVAL(data: Indicator, value: float = 0.0, discard: int = 0) -> Indicator:
    """
    CVAL([data, value=0.0, discard=0])
    
        data 为 Indicator 实例，创建和 data 等长的常量指标，其值和为value，抛弃长度discard和data一样
    
        :param Indicator data: Indicator实例
        :param float value: 常数值
        :param int discard: 抛弃数量
        :rtype: Indicator
    """
```

#### CVAL

```python
def CVAL(data: Indicator, value: float = 0.0, discard: int = 0) -> Indicator:
    """
    CVAL([data, value=0.0, discard=0])
    
        data 为 Indicator 实例，创建和 data 等长的常量指标，其值和为value，抛弃长度discard和data一样
    
        :param Indicator data: Indicator实例
        :param float value: 常数值
        :param int discard: 抛弃数量
        :rtype: Indicator
    """
```

#### CYCLE

```python
def CYCLE(adjust_cycle: int = 1, adjust_mode: str = 'query', delay_to_trading_day: bool = True) -> Indicator:
    ...
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

#### C_AMO

```python
def C_AMO(arg0: KData) -> Indicator:
    ...
```

#### C_AMO

```python
def C_AMO() -> Indicator:
    """
    AMO([data])
    
        获取成交金额，包装KData的成交金额成Indicator
        
        :param data: 输入数据（KData 或 Indicator）
        :rtype: Indicator
    """
```

#### C_CLOSE

```python
def C_CLOSE(arg0: KData) -> Indicator:
    ...
```

#### C_CLOSE

```python
def C_CLOSE() -> Indicator:
    """
    CLOSE([data])
    
        获取收盘价，包装KData的收盘价成Indicator
    
        :param data: 输入数据（KData 或 Indicator）
        :rtype: Indicator
    """
```

#### C_HIGH

```python
def C_HIGH(arg0: KData) -> Indicator:
    ...
```

#### C_HIGH

```python
def C_HIGH() -> Indicator:
    """
    HIGH([data])
    
        获取最高价，包装KData的最高价成Indicator
    
        :param data: 输入数据（KData 或 Indicator） 
        :rtype: Indicator
    """
```

#### C_KDATA

```python
def C_KDATA(arg0: KData) -> Indicator:
    ...
```

#### C_KDATA

```python
def C_KDATA() -> Indicator:
    """
    KDATA([data])
    
        包装KData成Indicator，用于其他指标计算
    
        :param data: KData 或 具有6个返回结果的Indicator（如KDATA生成的Indicator）
        :rtype: Indicator
    """
```

#### C_LOW

```python
def C_LOW(arg0: KData) -> Indicator:
    ...
```

#### C_LOW

```python
def C_LOW() -> Indicator:
    """
    LOW([data])
    
        获取最低价，包装KData的最低价成Indicator
    
        :param data: 输入数据（KData 或 Indicator） 
        :rtype: Indicator
    """
```

#### C_OPEN

```python
def C_OPEN(arg0: KData) -> Indicator:
    ...
```

#### C_OPEN

```python
def C_OPEN() -> Indicator:
    """
    OPEN([data])
    
        获取开盘价，包装KData的开盘价成Indicator
    
        :param data: 输入数据（KData 或 Indicator） 
        :rtype: Indicator
    """
```

#### C_VOL

```python
def C_VOL(arg0: KData) -> Indicator:
    ...
```

#### C_VOL

```python
def C_VOL() -> Indicator:
    """
    VOL([data])
    
        获取成交量，包装KData的成交量成Indicator
    
        :param data: 输入数据（KData 或 Indicator）
        :rtype: Indicator
    """
```

#### DATE

```python
def DATE() -> Indicator:
    ...
```

#### DATE

```python
def DATE(arg0: KData) -> Indicator:
    """
    DATE([data])
    
        取得该周期从1900以来的年月日。用法: DATE 例如函数返回1000101，表示2000年1月1日。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### DAY

```python
def DAY() -> Indicator:
    ...
```

#### DAY

```python
def DAY(arg0: KData) -> Indicator:
    """
    DAY([data])
    
        取得该周期的日期。用法: DAY 函数返回有效值范围为(1-31)。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### DECLINE

```python
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
```

#### DEVSQ

```python
def DEVSQ(n: int = 10) -> Indicator:
    ...
```

#### DEVSQ

```python
def DEVSQ(n: IndParam) -> Indicator:
    ...
```

#### DEVSQ

```python
def DEVSQ(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### DEVSQ

```python
def DEVSQ(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### DEVSQ

```python
def DEVSQ(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### DEVSQ

```python
def DEVSQ(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### DEVSQ

```python
def DEVSQ(data: Indicator, n: int = 10) -> Indicator:
    """
    DEVSQ([data, n=10])
    
        数据偏差平方和，求X的N日数据偏差平方和
    
        :param Indicator data: 输入数据
        :param int|Indicator n: 时间窗口
        :rtype: Indicator
    """
```

#### DEVSQ

```python
def DEVSQ(data: Indicator, n: int = 10) -> Indicator:
    """
    DEVSQ([data, n=10])
    
        数据偏差平方和，求X的N日数据偏差平方和
    
        :param Indicator data: 输入数据
        :param int|Indicator n: 时间窗口
        :rtype: Indicator
    """
```

#### DIFF

```python
def DIFF() -> Indicator:
    ...
```

#### DIFF

```python
def DIFF(arg0: Indicator) -> Indicator:
    """
    DIFF([data])
    
        差分指标，即data[i] - data[i-1]
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### DISCARD

```python
def DISCARD(discard: int) -> Indicator:
    ...
```

#### DISCARD

```python
def DISCARD(ind: Indicator, discard: int) -> Indicator:
    """
    DISCARD(data, discard)
        
        以指标公式的方式设置指标结果的丢弃数据量。
    
        :param Indicator data: 指标
        :param int discard: 丢弃数据量
        :rtype: Indicator
    """
```

#### DISCARD

```python
def DISCARD(ind: Indicator, discard: int) -> Indicator:
    """
    DISCARD(data, discard)
        
        以指标公式的方式设置指标结果的丢弃数据量。
    
        :param Indicator data: 指标
        :param int discard: 丢弃数据量
        :rtype: Indicator
    """
```

#### DMA

```python
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
```

#### DMA

```python
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
```

#### DMA

```python
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
```

#### DOWNNDAY

```python
def DOWNNDAY(data: Indicator, n: int = 3) -> Indicator:
    ...
```

#### DOWNNDAY

```python
def DOWNNDAY(data: Indicator, n: int = 3) -> Indicator:
    ...
```

#### DOWNNDAY

```python
def DOWNNDAY(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### DOWNNDAY

```python
def DOWNNDAY(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### DOWNNDAY

```python
def DOWNNDAY(data: Indicator, n: Indicator) -> Indicator:
    """
    DOWNNDAY(data[, n=3])
    
        连跌周期数, DOWNNDAY(CLOSE,M)表示连涨M个周期
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### DOWNNDAY

```python
def DOWNNDAY(data: Indicator, n: Indicator) -> Indicator:
    """
    DOWNNDAY(data[, n=3])
    
        连跌周期数, DOWNNDAY(CLOSE,M)表示连涨M个周期
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### DROPNA

```python
def DROPNA() -> Indicator:
    ...
```

#### DROPNA

```python
def DROPNA(arg0: Indicator) -> Indicator:
    """
    DROPNA([data])
    
        删除 nan 值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### EMA

```python
def EMA(n: int = 22) -> Indicator:
    ...
```

#### EMA

```python
def EMA(n: IndParam) -> Indicator:
    ...
```

#### EMA

```python
def EMA(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### EMA

```python
def EMA(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### EMA

```python
def EMA(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### EMA

```python
def EMA(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### EMA

```python
def EMA(data: Indicator, n: int = 22) -> Indicator:
    """
    EMA([data, n=22])
    
        指数移动平均线(Exponential Moving Average)
    
        :param data: 输入数据
        :param int|Indicator|IndParam n n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
```

#### EMA

```python
def EMA(data: Indicator, n: int = 22) -> Indicator:
    """
    EMA([data, n=22])
    
        指数移动平均线(Exponential Moving Average)
    
        :param data: 输入数据
        :param int|Indicator|IndParam n n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
```

#### EVERY

```python
def EVERY(n: int = 20) -> Indicator:
    ...
```

#### EVERY

```python
def EVERY(n: IndParam) -> Indicator:
    ...
```

#### EVERY

```python
def EVERY(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### EVERY

```python
def EVERY(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### EVERY

```python
def EVERY(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### EVERY

```python
def EVERY(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### EVERY

```python
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
```

#### EVERY

```python
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
```

#### EV_Bool

```python
def EV_Bool(ind: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_Bool(ind, market='SH')
    
        布尔信号指标市场环境
    
        :param Indicator ind: bool类型的指标，指标中相应位置>0则代表市场有效，否则无效
        :param str market: 指定的市场，用于获取相应的交易日历
    """
```

#### EV_TwoLine

```python
def EV_TwoLine(fast: Indicator, slow: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_TwoLine(fast, slow[, market = 'SH'])
    
        快慢线判断策略，市场指数的快线大于慢线时，市场有效，否则无效。
    
        :param Indicator fast: 快线指标
        :param Indicator slow: 慢线指标
        :param string market: 市场名称
    """
```

#### EV_TwoLine

```python
def EV_TwoLine(fast: Indicator, slow: Indicator, market: str = 'SH') -> EnvironmentBase:
    """
    EV_TwoLine(fast, slow[, market = 'SH'])
    
        快慢线判断策略，市场指数的快线大于慢线时，市场有效，否则无效。
    
        :param Indicator fast: 快线指标
        :param Indicator slow: 慢线指标
        :param string market: 市场名称
    """
```

#### EXIST

```python
def EXIST(n: int = 20) -> Indicator:
    ...
```

#### EXIST

```python
def EXIST(n: IndParam) -> Indicator:
    ...
```

#### EXIST

```python
def EXIST(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### EXIST

```python
def EXIST(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### EXIST

```python
def EXIST(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### EXIST

```python
def EXIST(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### EXIST

```python
def EXIST(data: Indicator, n: int = 20) -> Indicator:
    """
    EXIST([data, n=20])
    
        存在, EXIST(X,N) 表示条件X在N周期有存在
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
```

#### EXIST

```python
def EXIST(data: Indicator, n: int = 20) -> Indicator:
    """
    EXIST([data, n=20])
    
        存在, EXIST(X,N) 表示条件X在N周期有存在
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 计算均值的周期窗口，必须为大于0的整数 
        :rtype: Indicator
    """
```

#### EXP

```python
def EXP() -> Indicator:
    ...
```

#### EXP

```python
def EXP(arg0: float) -> Indicator:
    ...
```

#### EXP

```python
def EXP(arg0: Indicator) -> Indicator:
    """
    EXP([data])
    
        EXP(X)为e的X次幂
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### FILTER

```python
def FILTER(n: int = 5) -> Indicator:
    ...
```

#### FILTER

```python
def FILTER(n: IndParam) -> Indicator:
    ...
```

#### FILTER

```python
def FILTER(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### FILTER

```python
def FILTER(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### FILTER

```python
def FILTER(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### FILTER

```python
def FILTER(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### FILTER

```python
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
```

#### FILTER

```python
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
```

#### FINANCE

```python
def FINANCE(ix: int) -> Indicator:
    ...
```

#### FINANCE

```python
def FINANCE(name: str) -> Indicator:
    ...
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

#### FLOOR

```python
def FLOOR() -> Indicator:
    ...
```

#### FLOOR

```python
def FLOOR(arg0: Indicator) -> Indicator:
    ...
```

#### FLOOR

```python
def FLOOR(arg0: float) -> Indicator:
    """
    FLOOR([data])
    
        向下舍入(向数值减小方向舍入)取整
    
        用法：FLOOR(A)返回沿A数值减小方向最接近的整数
    
        例如：FLOOR(12.3)求得12
    
        :param data: 输入数据
        :rtype: Indicator
    """
```

#### HHV

```python
def HHV(n: int = 20) -> Indicator:
    ...
```

#### HHV

```python
def HHV(n: IndParam) -> Indicator:
    ...
```

#### HHV

```python
def HHV(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### HHV

```python
def HHV(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### HHV

```python
def HHV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### HHV

```python
def HHV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### HHV

```python
def HHV(data: Indicator, n: int = 20) -> Indicator:
    """
    HHV([data, n=20])
    
        N日内最高价，N=0则从第一个有效值开始。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
```

#### HHV

```python
def HHV(data: Indicator, n: int = 20) -> Indicator:
    """
    HHV([data, n=20])
    
        N日内最高价，N=0则从第一个有效值开始。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
```

#### HHVBARS

```python
def HHVBARS(n: int = 20) -> Indicator:
    ...
```

#### HHVBARS

```python
def HHVBARS(n: IndParam) -> Indicator:
    ...
```

#### HHVBARS

```python
def HHVBARS(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### HHVBARS

```python
def HHVBARS(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### HHVBARS

```python
def HHVBARS(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### HHVBARS

```python
def HHVBARS(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### HHVBARS

```python
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
```

#### HHVBARS

```python
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
```

#### HOUR

```python
def HOUR() -> Indicator:
    ...
```

#### HOUR

```python
def HOUR(arg0: KData) -> Indicator:
    """
    HOUR([data])
    
        取得该周期的小时数。用法：HOUR 函数返回有效值范围为(0-23)，对于日线及更长的分析周期值为0。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### HSL

```python
def HSL() -> Indicator:
    ...
```

#### HSL

```python
def HSL(arg0: KData) -> Indicator:
    """
    HSL(kdata)
    
        获取换手率, 乘以 100 才是百分比，等于 VOL(k) / CAPITAL(k) * 0.01
    
        :param KData kdata: k线数据
        :rtype: Indicator
    """
```

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

#### IF

```python
def IF(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: float, arg2: Indicator) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: float, arg2: Indicator) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### IF

```python
def IF(arg0: Indicator, arg1: Indicator, arg2: float) -> Indicator:
    ...
```

#### IF

```python
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
```

#### IF

```python
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
```

#### INBLOCK

```python
def INBLOCK(category: str, name: str) -> Indicator:
    ...
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
def INDEXA(fill_null: bool = True) -> Indicator:
    ...
```

#### INDEXA

```python
def INDEXA(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXA([kdata])
        
        返回对应的大盘成交金额,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXADV

```python
def INDEXADV() -> Indicator:
    ...
```

#### INDEXADV

```python
def INDEXADV(arg0: Query) -> Indicator:
    """
    INDEXADV([query])
        
        通达信 880005 大盘上涨家数, 可能无法盘中更新!
    """
```

#### INDEXC

```python
def INDEXC(fill_null: bool = True) -> Indicator:
    ...
```

#### INDEXC

```python
def INDEXC(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXC([kdata])
        
        返回对应的大盘收盘价,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INDEXDEC

```python
def INDEXDEC() -> Indicator:
    ...
```

#### INDEXDEC

```python
def INDEXDEC(arg0: Query) -> Indicator:
    """
    INDEXDEC([query])
        
        通达信 880005 大盘下跌家数, 可能无法盘中更新!
    """
```

#### INDEXH

```python
def INDEXH(fill_null: bool = True) -> Indicator:
    ...
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
def INDEXL(fill_null: bool = True) -> Indicator:
    ...
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
def INDEXO(fill_null: bool = True) -> Indicator:
    ...
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
def INDEXV(fill_null: bool = True) -> Indicator:
    ...
```

#### INDEXV

```python
def INDEXV(kdata: KData, fill_null: bool = True) -> Indicator:
    """
    INDEXV([kdata])
        
        返回对应的大盘成交量,分别是上证指数,深证成指,科创50,创业板指
    """
```

#### INSUM

```python
def INSUM(block: Block, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
```

#### INSUM

```python
def INSUM(block: Block, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
```

#### INSUM

```python
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
```

#### INSUM

```python
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
```

#### INSUM

```python
def INSUM(stks: typing.Sequence, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
```

#### INSUM

```python
def INSUM(stks: typing.Sequence, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
```

#### INSUM

```python
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
```

#### INSUM

```python
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
```

#### INTPART

```python
def INTPART() -> Indicator:
    ...
```

#### INTPART

```python
def INTPART(arg0: Indicator) -> Indicator:
    ...
```

#### INTPART

```python
def INTPART(arg0: float) -> Indicator:
    """
    INTPART([data])
    
        取整(绝对值减小取整，即取得数据的整数部分)
    
        :param data: 输入数据
        :rtype: Indicator
    """
```

#### IR

```python
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
```

#### IR

```python
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
```

#### IR

```python
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
```

#### ISINF

```python
def ISINF() -> Indicator:
    ...
```

#### ISINF

```python
def ISINF(ind: Indicator) -> Indicator:
    """
    ISINF(ind)
    
        判断指标是否为正无穷大 (+inf) 值，若为 +inf 值, 则返回1, 否则返回0。如判断负无穷大, 使用 ISINFA。
    
        :param Indicator ind: 指定指标
        :rtype: Indicator
    """
```

#### ISINFA

```python
def ISINFA() -> Indicator:
    ...
```

#### ISINFA

```python
def ISINFA(ind: Indicator) -> Indicator:
    """
    ISINFA(ind)
    
        判断指标是否为负无穷大 (-inf) 值，若为 -inf 值, 则返回1, 否则返回0。如判断正无穷大, 使用 ISINF。
    
        :param Indicator ind: 指定指标
        :rtype: Indicator
    """
```

#### ISLASTBAR

```python
def ISLASTBAR() -> Indicator:
    ...
```

#### ISLASTBAR

```python
def ISLASTBAR(data: KData) -> Indicator:
    ...
```

#### ISLASTBAR

```python
def ISLASTBAR(data: Indicator) -> Indicator:
    """
    ISLASTBAR(ind)
    
        判断当前数据是否为最后一个数据，若为最后一个数据，则返回1，否则返回0.
    
        :param Indicator|KData data: 指定指标
        :rtype: Indicator
    """
```

#### ISNA

```python
def ISNA(ignore_discard: bool = False) -> Indicator:
    ...
```

#### ISNA

```python
def ISNA(ind: Indicator, ignore_discard: bool = False) -> Indicator:
    """
    ISNA(ind[, ignore_discard=False])
    
        判断指标是否为 nan 值，若为 nan 值, 则返回1, 否则返回0.
    
        :param Indicator ind: 指定指标
        :param bool ignore_discard: 忽略指标丢弃数据
    """
```

#### ISNA

```python
def ISNA(ind: Indicator, ignore_discard: bool = False) -> Indicator:
    """
    ISNA(ind[, ignore_discard=False])
    
        判断指标是否为 nan 值，若为 nan 值, 则返回1, 否则返回0.
    
        :param Indicator ind: 指定指标
        :param bool ignore_discard: 忽略指标丢弃数据
    """
```

#### JUMPDOWN

```python
def JUMPDOWN() -> Indicator:
    ...
```

#### JUMPDOWN

```python
def JUMPDOWN(arg0: Indicator) -> Indicator:
    """
    JUMPDOWN([ind])
        
        边缘跳变，从大于0.0，跳变到 <= 0.0
    
        :param Indicator ind: 指标
        :rtype: Indicator
    """
```

#### JUMPUP

```python
def JUMPUP() -> Indicator:
    ...
```

#### JUMPUP

```python
def JUMPUP(arg0: Indicator) -> Indicator:
    """
    JUMPUP([ind])
        
        边缘跳变，从小于等于0.0，跳变到 > 0.0
        
        :param Indicator ind: 指标
        :rtype: Indicator
    """
```

#### KALMAN

```python
def KALMAN(q: float = 0.01, r: float = 0.1) -> Indicator:
    ...
```

#### KALMAN

```python
def KALMAN(ind: Indicator, q: float = 0.01, r: float = 0.1) -> Indicator:
    """
    KALMAN(ind, [q=0.01], [r=0.1])
    
        Kalman滤波器, 用于平滑指标, 可设置平滑系数q和r, 默认q=0.01, r=0.1
    
        :param Indicator ind: 指标
        :param float q: 平滑系数
        :param float r: 噪声系数
        :rtype: Indicator
    """
```

#### KALMAN

```python
def KALMAN(ind: Indicator, q: float = 0.01, r: float = 0.1) -> Indicator:
    """
    KALMAN(ind, [q=0.01], [r=0.1])
    
        Kalman滤波器, 用于平滑指标, 可设置平滑系数q和r, 默认q=0.01, r=0.1
    
        :param Indicator ind: 指标
        :param float q: 平滑系数
        :param float r: 噪声系数
        :rtype: Indicator
    """
```

#### KDATA_PART

```python
def KDATA_PART(data: KData, kpart: str) -> Indicator:
    ...
```

#### KDATA_PART

```python
def KDATA_PART(kpart: str) -> Indicator:
    """
    KDATA_PART([data, kpart])
    
        根据字符串选择返回指标KDATA/OPEN/HIGH/LOW/CLOSE/AMO/VOL，如:KDATA_PART("CLOSE")等同于CLOSE()
    
        :param data: 输入数据（KData 或 Indicator） 
        :param string kpart: KDATA|OPEN|HIGH|LOW|CLOSE|AMO|VOL
        :rtype: Indicator
    """
```

#### LAST

```python
def LAST(m: int = 10, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(m: int, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(m: IndParam, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(m: IndParam, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: int = 10, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: int = 10, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: int, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: int, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: IndParam, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: IndParam, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: IndParam, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: IndParam, n: IndParam) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: int, n: Indicator) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: int, n: Indicator) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: Indicator, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: Indicator, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
def LAST(data: Indicator, m: Indicator, n: int = 5) -> Indicator:
    ...
```

#### LAST

```python
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
```

#### LAST

```python
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
```

#### LAST

```python
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
```

#### LASTVALUE

```python
def LASTVALUE(ignore_discard: bool = False) -> Indicator:
    ...
```

#### LASTVALUE

```python
def LASTVALUE(ind: Indicator, ignore_discard: bool = False) -> Indicator:
    """
    LASTVALUE(ind, [ignore_discard=False])
    
        等同于通达信CONST指标。取输入指标最后值为常数, 即结果中所有值均为输入指标的最后值, 谨慎使用。含未来函数, 谨慎使用。
    
        :param Indicator ind: 指标
        :param bool ignore_discard: 忽略指标丢弃数据
        :rtype: Indicator
    """
```

#### LASTVALUE

```python
def LASTVALUE(ind: Indicator, ignore_discard: bool = False) -> Indicator:
    """
    LASTVALUE(ind, [ignore_discard=False])
    
        等同于通达信CONST指标。取输入指标最后值为常数, 即结果中所有值均为输入指标的最后值, 谨慎使用。含未来函数, 谨慎使用。
    
        :param Indicator ind: 指标
        :param bool ignore_discard: 忽略指标丢弃数据
        :rtype: Indicator
    """
```

#### LIUTONGPAN

```python
def LIUTONGPAN() -> Indicator:
    ...
```

#### LIUTONGPAN

```python
def LIUTONGPAN(arg0: KData) -> Indicator:
    """
    LIUTONGPAN(kdata)
    
       获取流通盘（单位：万股），同 CAPITAL
    
       :param KData kdata: k线数据
       :rtype: Indicator
    """
```

#### LLV

```python
def LLV(n: int = 20) -> Indicator:
    ...
```

#### LLV

```python
def LLV(n: IndParam) -> Indicator:
    ...
```

#### LLV

```python
def LLV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### LLV

```python
def LLV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### LLV

```python
def LLV(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LLV

```python
def LLV(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LLV

```python
def LLV(data: Indicator, n: int = 20) -> Indicator:
    """
    LLV([data, n=20])
    
        N日内最低价，N=0则从第一个有效值开始。
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
```

#### LLV

```python
def LLV(data: Indicator, n: int = 20) -> Indicator:
    """
    LLV([data, n=20])
    
        N日内最低价，N=0则从第一个有效值开始。
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: N日时间窗口
        :rtype: Indicator
    """
```

#### LLVBARS

```python
def LLVBARS(n: int = 20) -> Indicator:
    ...
```

#### LLVBARS

```python
def LLVBARS(n: IndParam) -> Indicator:
    ...
```

#### LLVBARS

```python
def LLVBARS(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### LLVBARS

```python
def LLVBARS(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### LLVBARS

```python
def LLVBARS(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LLVBARS

```python
def LLVBARS(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LLVBARS

```python
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
```

#### LLVBARS

```python
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
```

#### LN

```python
def LN() -> Indicator:
    ...
```

#### LN

```python
def LN(arg0: float) -> Indicator:
    ...
```

#### LN

```python
def LN(arg0: Indicator) -> Indicator:
    """
    LN([data])
    
        求自然对数, LN(X)以e为底的对数
    
        :param data: 输入数据
        :rtype: Indicator
    """
```

#### LOG

```python
def LOG() -> Indicator:
    ...
```

#### LOG

```python
def LOG(arg0: float) -> Indicator:
    ...
```

#### LOG

```python
def LOG(arg0: Indicator) -> Indicator:
    """
    LOG([data])
    
        以10为底的对数
    
        :param data: 输入数据
        :rtype: Indicator
    """
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: Indicator, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: Indicator, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: Indicator, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: float, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: float, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: float, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: Indicator, b: float, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: float, b: Indicator, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: float, b: Indicator, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: float, b: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: float, b: Indicator, n: Indicator) -> Indicator:
    ...
```

#### LONGCROSS

```python
def LONGCROSS(a: float, b: float, n: int = 3) -> Indicator:
    ...
```

#### LONGCROSS

```python
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
```

#### MA

```python
def MA(n: int = 22) -> Indicator:
    ...
```

#### MA

```python
def MA(n: IndParam) -> Indicator:
    ...
```

#### MA

```python
def MA(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### MA

```python
def MA(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### MA

```python
def MA(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### MA

```python
def MA(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### MA

```python
def MA(data: Indicator, n: int = 22) -> Indicator:
    """
    MA([data, n=22])
    
        简单移动平均
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### MA

```python
def MA(data: Indicator, n: int = 22) -> Indicator:
    """
    MA([data, n=22])
    
        简单移动平均
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### MACD

```python
def MACD(n1: int = 12, n2: int = 26, n3: int = 9) -> Indicator:
    ...
```

#### MACD

```python
def MACD(n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
```

#### MACD

```python
def MACD(data: Indicator, n1: int = 12, n2: int = 26, n3: int = 9) -> Indicator:
    ...
```

#### MACD

```python
def MACD(data: Indicator, n1: int = 12, n2: int = 26, n3: int = 9) -> Indicator:
    ...
```

#### MACD

```python
def MACD(data: Indicator, n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
```

#### MACD

```python
def MACD(data: Indicator, n1: IndParam, n2: IndParam, n3: IndParam) -> Indicator:
    ...
```

#### MACD

```python
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
```

#### MACD

```python
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
```

#### MACD

```python
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
```

#### MACD

```python
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
```

#### MAX

```python
def MAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### MAX

```python
def MAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### MAX

```python
def MAX(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### MAX

```python
def MAX(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### MAX

```python
def MAX(arg0: float, arg1: Indicator) -> Indicator:
    """
    MAX(ind1, ind2)
    
        求最大值, MAX(A,B)返回A和B中的较大值。
    
        :param Indicator ind1: A
        :param Indicator ind2: B
        :rtype: Indicator
    """
```

#### MDD

```python
def MDD() -> Indicator:
    ...
```

#### MDD

```python
def MDD(arg0: Indicator) -> Indicator:
    """
    MDD([data])
        
        当前价格相对历史最高值的回撤百分比，通常用于计算最大回撤
    """
```

#### MIN

```python
def MIN(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### MIN

```python
def MIN(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### MIN

```python
def MIN(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### MIN

```python
def MIN(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### MIN

```python
def MIN(arg0: float, arg1: Indicator) -> Indicator:
    """
    MIN(ind1, ind2)
    
        求最小值, MIN(A,B)返回A和B中的较小值。
    
        :param Indicator ind1: A
        :param Indicator ind2: B
        :rtype: Indicator
    """
```

#### MINUTE

```python
def MINUTE() -> Indicator:
    ...
```

#### MINUTE

```python
def MINUTE(arg0: KData) -> Indicator:
    """
    MINUTE([data])
    
        取得该周期的分钟数。用法：MINUTE 函数返回有效值范围为(0-59)，对于日线及更长的分析周期值为0。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### MOD

```python
def MOD(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### MOD

```python
def MOD(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### MOD

```python
def MOD(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### MOD

```python
def MOD(arg0: Indicator, arg1: float) -> Indicator:
    ...
```

#### MOD

```python
def MOD(arg0: float, arg1: Indicator) -> Indicator:
    ...
```

#### MOD

```python
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
```

#### MONTH

```python
def MONTH() -> Indicator:
    ...
```

#### MONTH

```python
def MONTH(arg0: KData) -> Indicator:
    """
    MONTH([data])
    
        取得该周期的月份。用法: MONTH 函数返回有效值范围为(1-12)。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### MRR

```python
def MRR() -> Indicator:
    ...
```

#### MRR

```python
def MRR(arg0: Indicator) -> Indicator:
    """
    MRR([data])
        
        当前价格相对历史最低值的盈利百分比，可用于计算历史最高盈利比例
    """
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: int = 3) -> Indicator:
    ...
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: int = 3) -> Indicator:
    ...
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: int = 3) -> Indicator:
    ...
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: int) -> Indicator:
    ...
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: int) -> Indicator:
    ...
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: int) -> Indicator:
    ...
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: IndParam) -> Indicator:
    """
    NDAY(x, y[, n=3])
    
        连大, NDAY(X,Y,N)表示条件X>Y持续存在N个周期
    
        :param Indicator x:
        :param Indicator y:
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: IndParam) -> Indicator:
    """
    NDAY(x, y[, n=3])
    
        连大, NDAY(X,Y,N)表示条件X>Y持续存在N个周期
    
        :param Indicator x:
        :param Indicator y:
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### NDAY

```python
def NDAY(x: Indicator, y: Indicator, n: IndParam) -> Indicator:
    """
    NDAY(x, y[, n=3])
    
        连大, NDAY(X,Y,N)表示条件X>Y持续存在N个周期
    
        :param Indicator x:
        :param Indicator y:
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### NOT

```python
def NOT() -> Indicator:
    ...
```

#### NOT

```python
def NOT(arg0: Indicator) -> Indicator:
    """
    NOT([data])
    
        求逻辑非。NOT(X)返回非X,即当X=0时返回1，否则返回0。
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### POS

```python
def POS(block: Block, query: Query, sg: ...) -> Indicator:
    ...
```

#### POW

```python
def POW(n: int) -> Indicator:
    ...
```

#### POW

```python
def POW(n: IndParam) -> Indicator:
    ...
```

#### POW

```python
def POW(data: Indicator, n: int) -> Indicator:
    ...
```

#### POW

```python
def POW(data: Indicator, n: int) -> Indicator:
    ...
```

#### POW

```python
def POW(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### POW

```python
def POW(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### POW

```python
def POW(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### POW

```python
def POW(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### POW

```python
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
```

#### PRICELIST

```python
def PRICELIST(data: typing.Any, result_index: int = 0, discard: int = 0, align_dates: typing.Any = None) -> Indicator:
    ...
```

#### RECOVER_BACKWARD

```python
def RECOVER_BACKWARD() -> Indicator:
    ...
```

#### RECOVER_BACKWARD

```python
def RECOVER_BACKWARD(arg0: Indicator) -> Indicator:
    ...
```

#### RECOVER_BACKWARD

```python
def RECOVER_BACKWARD(arg0: KData) -> Indicator:
    """
    RECOVER_BACKWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行后向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
```

#### RECOVER_EQUAL_BACKWARD

```python
def RECOVER_EQUAL_BACKWARD() -> Indicator:
    ...
```

#### RECOVER_EQUAL_BACKWARD

```python
def RECOVER_EQUAL_BACKWARD(arg0: Indicator) -> Indicator:
    ...
```

#### RECOVER_EQUAL_BACKWARD

```python
def RECOVER_EQUAL_BACKWARD(arg0: KData) -> Indicator:
    """
    RECOVER_EQUAL_BACKWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行等比后向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
```

#### RECOVER_EQUAL_FORWARD

```python
def RECOVER_EQUAL_FORWARD() -> Indicator:
    ...
```

#### RECOVER_EQUAL_FORWARD

```python
def RECOVER_EQUAL_FORWARD(arg0: Indicator) -> Indicator:
    ...
```

#### RECOVER_EQUAL_FORWARD

```python
def RECOVER_EQUAL_FORWARD(arg0: KData) -> Indicator:
    """
    RECOVER_EQUAL_FORWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行等比前向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
```

#### RECOVER_FORWARD

```python
def RECOVER_FORWARD() -> Indicator:
    ...
```

#### RECOVER_FORWARD

```python
def RECOVER_FORWARD(arg0: Indicator) -> Indicator:
    ...
```

#### RECOVER_FORWARD

```python
def RECOVER_FORWARD(arg0: KData) -> Indicator:
    """
    RECOVER_FORWARD([data])
        
        对输入的指标数据 (CLOSE|OPEN|HIGH|LOW) 进行前向复权
    
        :param Indicator|KData data: 只接受 CLOSE|OPEN|HIGH|LOW 指标，或 KData（此时默认使用 KData 的收盘价）
        :rtype: Indicator
    """
```

#### REF

```python
def REF(n: int) -> Indicator:
    ...
```

#### REF

```python
def REF(n: IndParam) -> Indicator:
    ...
```

#### REF

```python
def REF(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### REF

```python
def REF(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### REF

```python
def REF(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### REF

```python
def REF(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### REF

```python
def REF(data: Indicator, n: int) -> Indicator:
    """
    REF([data, n])
    
        向前引用 （即右移），引用若干周期前的数据。
    
        用法：REF(X，A)　引用A周期前的X值。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 引用n周期前的值，即右移n位
        :rtype: Indicator
    """
```

#### REF

```python
def REF(data: Indicator, n: int) -> Indicator:
    """
    REF([data, n])
    
        向前引用 （即右移），引用若干周期前的数据。
    
        用法：REF(X，A)　引用A周期前的X值。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 引用n周期前的值，即右移n位
        :rtype: Indicator
    """
```

#### REPLACE

```python
def REPLACE(old_value: float = ..., new_value: float = 0.0, ignore_discard: bool = False) -> Indicator:
    ...
```

#### REPLACE

```python
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
```

#### REPLACE

```python
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
```

#### RESULT

```python
def RESULT(arg0: int) -> Indicator:
    ...
```

#### RESULT

```python
def RESULT(data: Indicator, result_ix: int) -> Indicator:
    """
    RESULT(data, result_ix)
              
        以公式指标的方式返回指定指标中的指定结果集
    
        :param Indicator data: 指定的指标
        :param int result_ix: 指定的结果集
    """
```

#### RESULT

```python
def RESULT(data: Indicator, result_ix: int) -> Indicator:
    """
    RESULT(data, result_ix)
              
        以公式指标的方式返回指定指标中的指定结果集
    
        :param Indicator data: 指定的指标
        :param int result_ix: 指定的结果集
    """
```

#### REVERSE

```python
def REVERSE() -> Indicator:
    ...
```

#### REVERSE

```python
def REVERSE(arg0: Indicator) -> Indicator:
    ...
```

#### REVERSE

```python
def REVERSE(arg0: float) -> Indicator:
    """
    REVERSE([data])
    
        求相反数，REVERSE(X)返回-X
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### ROC

```python
def ROC(n: int = 10) -> Indicator:
    ...
```

#### ROC

```python
def ROC(n: IndParam) -> Indicator:
    ...
```

#### ROC

```python
def ROC(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROC

```python
def ROC(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROC

```python
def ROC(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROC

```python
def ROC(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROC

```python
def ROC(data: Indicator, n: int = 10) -> Indicator:
    """
    ROC([data, n=10])
    
        变动率指标: ((price / prevPrice)-1)*100
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
```

#### ROC

```python
def ROC(data: Indicator, n: int = 10) -> Indicator:
    """
    ROC([data, n=10])
    
        变动率指标: ((price / prevPrice)-1)*100
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
```

#### ROCP

```python
def ROCP(n: int = 10) -> Indicator:
    ...
```

#### ROCP

```python
def ROCP(n: IndParam) -> Indicator:
    ...
```

#### ROCP

```python
def ROCP(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROCP

```python
def ROCP(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROCP

```python
def ROCP(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROCP

```python
def ROCP(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROCP

```python
def ROCP(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCP([data, n=10])
    
        变动率指标: (price - prevPrice) / prevPrice
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
```

#### ROCP

```python
def ROCP(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCP([data, n=10])
    
        变动率指标: (price - prevPrice) / prevPrice
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
```

#### ROCR

```python
def ROCR(n: int = 10) -> Indicator:
    ...
```

#### ROCR

```python
def ROCR(n: IndParam) -> Indicator:
    ...
```

#### ROCR

```python
def ROCR(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROCR

```python
def ROCR(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROCR

```python
def ROCR(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROCR

```python
def ROCR(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROCR

```python
def ROCR(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCR([data, n=10])
    
        变动率指标: (price / prevPrice)
    
        :param data: 输入数据
        :param int n|Indicator|IndParam: 时间窗口
        :rtype: Indicator
    """
```

#### ROCR

```python
def ROCR(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCR([data, n=10])
    
        变动率指标: (price / prevPrice)
    
        :param data: 输入数据
        :param int n|Indicator|IndParam: 时间窗口
        :rtype: Indicator
    """
```

#### ROCR100

```python
def ROCR100(n: int = 10) -> Indicator:
    ...
```

#### ROCR100

```python
def ROCR100(n: IndParam) -> Indicator:
    ...
```

#### ROCR100

```python
def ROCR100(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROCR100

```python
def ROCR100(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### ROCR100

```python
def ROCR100(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROCR100

```python
def ROCR100(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### ROCR100

```python
def ROCR100(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCR100([data, n=10])
    
        变动率指标: (price / prevPrice) * 100
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### ROCR100

```python
def ROCR100(data: Indicator, n: int = 10) -> Indicator:
    """
    ROCR100([data, n=10])
    
        变动率指标: (price / prevPrice) * 100
    
        :param data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### ROUND

```python
def ROUND(ndigits: int = 2) -> Indicator:
    ...
```

#### ROUND

```python
def ROUND(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
```

#### ROUND

```python
def ROUND(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
```

#### ROUND

```python
def ROUND(data: float, ndigits: int = 2) -> Indicator:
    """
    ROUND([data, ndigits=2])
    
        四舍五入
    
        :param data: 输入数据
        :param int ndigits: 保留的小数点后位数
        :rtype: Indicator
    """
```

#### ROUNDDOWN

```python
def ROUNDDOWN(ndigits: int = 2) -> Indicator:
    ...
```

#### ROUNDDOWN

```python
def ROUNDDOWN(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
```

#### ROUNDDOWN

```python
def ROUNDDOWN(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
```

#### ROUNDDOWN

```python
def ROUNDDOWN(data: float, ndigits: int = 2) -> Indicator:
    """
    ROUND([data, ndigits=2])
    
        四舍五入
    
        :param data: 输入数据
        :param int ndigits: 保留的小数点后位数
        :rtype: Indicator
    """
```

#### ROUNDUP

```python
def ROUNDUP(ndigits: int = 2) -> Indicator:
    ...
```

#### ROUNDUP

```python
def ROUNDUP(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
```

#### ROUNDUP

```python
def ROUNDUP(data: Indicator, ndigits: int = 2) -> Indicator:
    ...
```

#### ROUNDUP

```python
def ROUNDUP(data: float, ndigits: int = 2) -> Indicator:
    """
    ROUNDUP([data, ndigits=2])
    
        向上截取，如10.1截取后为11
    
        :param data: 输入数据
        :param int ndigits: 保留的小数点后位数
        :rtype: Indicator
    """
```

#### RSI

```python
def RSI(n: int = 14) -> Indicator:
    ...
```

#### RSI

```python
def RSI(data: Indicator, n: int = 14) -> Indicator:
    """
    RSI([data, n=14])
    
        相对强弱指数
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### RSI

```python
def RSI(data: Indicator, n: int = 14) -> Indicator:
    """
    RSI([data, n=14])
    
        相对强弱指数
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### SAFTYLOSS

```python
def SAFTYLOSS(n1: int = 10, n2: int = 3, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: int = 10, n2: int = 3, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: int = 10, n2: int = 3, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: IndParam, n2: IndParam, p: IndParam) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: Indicator, n2: Indicator, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: Indicator, n2: Indicator, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: Indicator, n2: Indicator, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
def SAFTYLOSS(data: Indicator, n1: Indicator, n2: Indicator, p: float = 2.0) -> Indicator:
    ...
```

#### SAFTYLOSS

```python
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
```

#### SAFTYLOSS

```python
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
```

#### SAFTYLOSS

```python
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
```

#### SAFTYLOSS

```python
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
```

#### SGN

```python
def SGN() -> Indicator:
    ...
```

#### SGN

```python
def SGN(arg0: float) -> Indicator:
    ...
```

#### SGN

```python
def SGN(arg0: Indicator) -> Indicator:
    """
    SGN([data])
    
        求符号值, SGN(X)，当 X>0, X=0, X<0分别返回 1, 0, -1。
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### SG_Band

```python
def SG_Band(ind: Indicator, lower: Indicator, upper: Indicator) -> SignalBase:
    ...
```

#### SG_Band

```python
def SG_Band(ind: Indicator, lower: Indicator, upper: Indicator) -> SignalBase:
    ...
```

#### SG_Band

```python
def SG_Band(ind: Indicator, lower: float, upper: float) -> SignalBase:
    """
    SG_Band(ind, lower, upper)
              
        指标区间指示器, 当指标超过上轨时，买入；
        当指标低于下轨时，卖出。::
    
            SG_Band(MA(C, n=10), 100, 200)
            SG_Band(CLOSE, MA(LOW), MA(HIGH))
    """
```

#### SG_Bool

```python
def SG_Bool(buy: Indicator, sell: Indicator, alternate: bool = True) -> SignalBase:
    """
    SG_Bool(buy, sell)
    
        布尔信号指示器，使用运算结果为类似bool数组的Indicator分别作为买入、卖出指示。
    
        :param Indicator buy: 买入指示（结果Indicator中相应位置>0则代表买入）
        :param Indicator sell: 卖出指示（结果Indicator中相应位置>0则代表卖出）
        :param bool alternate: 是否交替买入卖出，默认为True
        :return: 信号指示器
    """
```

#### SG_Bool

```python
def SG_Bool(buy: Indicator, sell: Indicator, alternate: bool = True) -> SignalBase:
    """
    SG_Bool(buy, sell)
    
        布尔信号指示器，使用运算结果为类似bool数组的Indicator分别作为买入、卖出指示。
    
        :param Indicator buy: 买入指示（结果Indicator中相应位置>0则代表买入）
        :param Indicator sell: 卖出指示（结果Indicator中相应位置>0则代表卖出）
        :param bool alternate: 是否交替买入卖出，默认为True
        :return: 信号指示器
    """
```

#### SG_Cross

```python
def SG_Cross(fast: Indicator, slow: Indicator) -> SignalBase:
    """
    SG_Cross(fast, slow)
    
        双线交叉指示器，当快线从下向上穿越慢线时，买入；当快线从上向下穿越慢线时，卖出。如：5日MA上穿10日MA时买入，5日MA线下穿MA10日线时卖出:: 
    
            SG_Cross(MA(C, n=10), MA(C, n=30))
    
        :param Indicator fast: 快线
        :param Indicator slow: 慢线
        :return: 信号指示器
    """
```

#### SG_CrossGold

```python
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
```

#### SG_Flex

```python
def SG_Flex(op: Indicator, slow_n: int) -> SignalBase:
    """
    SG_Flex(ind, slow_n)
    
        使用自身的EMA(slow_n)作为慢线，自身作为快线，快线向上穿越慢线买入，快线向下穿越慢线卖出。
    
        :param Indicator ind:
        :param int slow_n: 慢线EMA周期
        :return: 信号指示器
    """
```

#### SG_OneSide

```python
def SG_OneSide(ind: Indicator, is_buy: bool) -> SignalBase:
    """
    SG_OneSide(ind, is_buy)
              
        根据输入指标构建单边信号（单纯的只包含买入或卖出信号），如果指标值大于0，则加入信号。也可以使用 SG_Buy 或 SG_Sell 函数。
        
        :param Indicator ind: 输入指标
        :param bool is_buy: 构建的是买入信号，否则为卖出信号
        :return: 信号指示器
    """
```

#### SG_Single

```python
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
```

#### SG_Single2

```python
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
```

#### SIN

```python
def SIN() -> Indicator:
    ...
```

#### SIN

```python
def SIN(arg0: Indicator) -> Indicator:
    ...
```

#### SIN

```python
def SIN(arg0: float) -> Indicator:
    """
    SIN([data])
    
        正弦值
    
        :param Indicator data: 输入数据
        :rtype: Indicator
    """
```

#### SLICE

```python
def SLICE(data: list[float], start: int, end: int) -> Indicator:
    ...
```

#### SLICE

```python
def SLICE(start: int, end: int, result_index: int = 0) -> Indicator:
    ...
```

#### SLICE

```python
def SLICE(data: Indicator, start: int, end: int, result_index: int = 0) -> Indicator:
    """
    SLICE(data, start, end, result_index=0)
    
        获取某指标中指定范围 [start, end) 的数据，生成新的指标
    
        :param Indicator|PriceList data: 输入数据
        :param int start: 起始位置
        :param int end: 终止位置（不包含本身）
        :param int result_index: 原输入数据中的结果集
    """
```

#### SLICE

```python
def SLICE(data: Indicator, start: int, end: int, result_index: int = 0) -> Indicator:
    """
    SLICE(data, start, end, result_index=0)
    
        获取某指标中指定范围 [start, end) 的数据，生成新的指标
    
        :param Indicator|PriceList data: 输入数据
        :param int start: 起始位置
        :param int end: 终止位置（不包含本身）
        :param int result_index: 原输入数据中的结果集
    """
```

#### SLOPE

```python
def SLOPE(n: int = 22) -> Indicator:
    ...
```

#### SLOPE

```python
def SLOPE(n: IndParam) -> Indicator:
    ...
```

#### SLOPE

```python
def SLOPE(data: Indicator, n: int = 22) -> Indicator:
    ...
```

#### SLOPE

```python
def SLOPE(data: Indicator, n: int = 22) -> Indicator:
    ...
```

#### SLOPE

```python
def SLOPE(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### SLOPE

```python
def SLOPE(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### SLOPE

```python
def SLOPE(data: Indicator, n: Indicator) -> Indicator:
    """
    SLOPE([data, n=22])
    
        计算线性回归斜率，N支持变量
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### SLOPE

```python
def SLOPE(data: Indicator, n: Indicator) -> Indicator:
    """
    SLOPE([data, n=22])
    
        计算线性回归斜率，N支持变量
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### SMA

```python
def SMA(n: int = 22, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(n: int, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(n: IndParam, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(n: IndParam, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: int = 22, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: int = 22, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: int, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: int, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: IndParam, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: IndParam, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: IndParam, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: IndParam, m: IndParam) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: int, m: Indicator) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: int, m: Indicator) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: Indicator, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: Indicator, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
def SMA(data: Indicator, n: Indicator, m: float = 2.0) -> Indicator:
    ...
```

#### SMA

```python
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
```

#### SMA

```python
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
```

#### SMA

```python
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
```

#### SPEARMAN

```python
def SPEARMAN(ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    ...
```

#### SPEARMAN

```python
def SPEARMAN(ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    ...
```

#### SPEARMAN

```python
def SPEARMAN(ind: Indicator, ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    """
    SPEARMAN(ind, ref_ind[, n=0, fill_null=True])
    
        Spearman 相关系数。与 SPEARMAN(ref_ind, n)(ind) 等效。
    
        :param Indicator ind: 输入参数1
        :param Indicator ref_ind: 输入参数2
        :param int n: 滚动窗口(大于2 或 等于0)，等于0时，代表 n 实际使用 ind 的长度
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
    """
```

#### SPEARMAN

```python
def SPEARMAN(ind: Indicator, ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    """
    SPEARMAN(ind, ref_ind[, n=0, fill_null=True])
    
        Spearman 相关系数。与 SPEARMAN(ref_ind, n)(ind) 等效。
    
        :param Indicator ind: 输入参数1
        :param Indicator ref_ind: 输入参数2
        :param int n: 滚动窗口(大于2 或 等于0)，等于0时，代表 n 实际使用 ind 的长度
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
    """
```

#### SPEARMAN

```python
def SPEARMAN(ind: Indicator, ref_ind: Indicator, n: int = 0, fill_null: bool = True) -> Indicator:
    """
    SPEARMAN(ind, ref_ind[, n=0, fill_null=True])
    
        Spearman 相关系数。与 SPEARMAN(ref_ind, n)(ind) 等效。
    
        :param Indicator ind: 输入参数1
        :param Indicator ref_ind: 输入参数2
        :param int n: 滚动窗口(大于2 或 等于0)，等于0时，代表 n 实际使用 ind 的长度
        :param bool fill_null: 缺失数据使用 nan 填充; 否则使用小于对应日期且最接近对应日期的数据
    """
```

#### SQRT

```python
def SQRT() -> Indicator:
    ...
```

#### SQRT

```python
def SQRT(arg0: Indicator) -> Indicator:
    ...
```

#### SQRT

```python
def SQRT(arg0: float) -> Indicator:
    """
    SQRT([data])
    
        开平方
    
        用法：SQRT(X)为X的平方根
    
        例如：SQRT(CLOSE)收盘价的平方根
    
        :param data: 输入数据
        :rtype: Indicator
    """
```

#### STDEV

```python
def STDEV(n: int = 10) -> Indicator:
    ...
```

#### STDEV

```python
def STDEV(n: IndParam) -> Indicator:
    ...
```

#### STDEV

```python
def STDEV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### STDEV

```python
def STDEV(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### STDEV

```python
def STDEV(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### STDEV

```python
def STDEV(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### STDEV

```python
def STDEV(data: Indicator, n: int = 10) -> Indicator:
    """
    STDEV([data, n=10])
    
        计算N周期内样本标准差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### STDEV

```python
def STDEV(data: Indicator, n: int = 10) -> Indicator:
    """
    STDEV([data, n=10])
    
        计算N周期内样本标准差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### STDP

```python
def STDP(n: int = 10) -> Indicator:
    ...
```

#### STDP

```python
def STDP(n: IndParam) -> Indicator:
    ...
```

#### STDP

```python
def STDP(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### STDP

```python
def STDP(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### STDP

```python
def STDP(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### STDP

```python
def STDP(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### STDP

```python
def STDP(data: Indicator, n: int = 10) -> Indicator:
    """
    STDP([data, n=10])
    
        总体标准差，STDP(X,N)为X的N日总体标准差
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
```

#### STDP

```python
def STDP(data: Indicator, n: int = 10) -> Indicator:
    """
    STDP([data, n=10])
    
        总体标准差，STDP(X,N)为X的N日总体标准差
    
        :param data: 输入数据
        :param int n: 时间窗口
        :rtype: Indicator
    """
```

#### SUM

```python
def SUM(n: int = 20) -> Indicator:
    ...
```

#### SUM

```python
def SUM(n: IndParam) -> Indicator:
    ...
```

#### SUM

```python
def SUM(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### SUM

```python
def SUM(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### SUM

```python
def SUM(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### SUM

```python
def SUM(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### SUM

```python
def SUM(data: Indicator, n: int = 20) -> Indicator:
    """
    SUM([data, n=20])
    
        求总和。SUM(X,N),统计N周期中X的总和,N=0则从第一个有效值开始。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### SUM

```python
def SUM(data: Indicator, n: int = 20) -> Indicator:
    """
    SUM([data, n=20])
    
        求总和。SUM(X,N),统计N周期中X的总和,N=0则从第一个有效值开始。
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### SUMBARS

```python
def SUMBARS(a: float) -> Indicator:
    ...
```

#### SUMBARS

```python
def SUMBARS(a: IndParam) -> Indicator:
    ...
```

#### SUMBARS

```python
def SUMBARS(data: Indicator, a: IndParam) -> Indicator:
    ...
```

#### SUMBARS

```python
def SUMBARS(data: Indicator, a: IndParam) -> Indicator:
    ...
```

#### SUMBARS

```python
def SUMBARS(data: Indicator, a: Indicator) -> Indicator:
    ...
```

#### SUMBARS

```python
def SUMBARS(data: Indicator, a: Indicator) -> Indicator:
    ...
```

#### SUMBARS

```python
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
```

#### SUMBARS

```python
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
```

#### TAN

```python
def TAN() -> Indicator:
    ...
```

#### TAN

```python
def TAN(arg0: Indicator) -> Indicator:
    ...
```

#### TAN

```python
def TAN(arg0: float) -> Indicator:
    """
    TAN([data])
    
        正切值
    
        :param Indicator data: 输入数据
        :rtype: Indicato
    """
```

#### TA_ACCBANDS

```python
def TA_ACCBANDS(n: int = 20) -> Indicator:
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

#### TA_ACOS

```python
def TA_ACOS() -> Indicator:
    ...
```

#### TA_ACOS

```python
def TA_ACOS(arg0: Indicator) -> Indicator:
    ...
```

#### TA_ACOS

```python
def TA_ACOS(arg0: float) -> Indicator:
    """
    TA_ACOS - Vector Trigonometric ACos
    """
```

#### TA_AD

```python
def TA_AD() -> Indicator:
    ...
```

#### TA_AD

```python
def TA_AD(data: KData) -> Indicator:
    """
    TA_AD - Chaikin A/D Line
    """
```

#### TA_ADD

```python
def TA_ADD(fill_null: bool = True) -> Indicator:
    ...
```

#### TA_ADD

```python
def TA_ADD(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_ADD - Vector Arithmetic Add
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_ADD

```python
def TA_ADD(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_ADD - Vector Arithmetic Add
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_ADD

```python
def TA_ADD(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_ADD - Vector Arithmetic Add
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_ADOSC

```python
def TA_ADOSC(fast_n: int = 3, slow_n: int = 10) -> Indicator:
    ...
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
def TA_ADX(n: int = 14) -> Indicator:
    ...
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
def TA_ADXR(n: int = 14) -> Indicator:
    ...
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

#### TA_APO

```python
def TA_APO(fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    ...
```

#### TA_APO

```python
def TA_APO(data: Indicator, fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    """
    TA_APO - Absolute Price Oscillator
    
    :param Indicator data: input data
    :param int fast_n: Number of period for the fast MA (From 2 to 100000)
    :param int slow_n: Number of period for the slow MA (From 2 to 100000)    
    :param int matype: Type of Moving Average
    """
```

#### TA_APO

```python
def TA_APO(data: Indicator, fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    """
    TA_APO - Absolute Price Oscillator
    
    :param Indicator data: input data
    :param int fast_n: Number of period for the fast MA (From 2 to 100000)
    :param int slow_n: Number of period for the slow MA (From 2 to 100000)    
    :param int matype: Type of Moving Average
    """
```

#### TA_AROON

```python
def TA_AROON(n: int = 14) -> Indicator:
    ...
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
def TA_AROONOSC(n: int = 14) -> Indicator:
    ...
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

#### TA_ASIN

```python
def TA_ASIN() -> Indicator:
    ...
```

#### TA_ASIN

```python
def TA_ASIN(arg0: Indicator) -> Indicator:
    ...
```

#### TA_ASIN

```python
def TA_ASIN(arg0: float) -> Indicator:
    """
    TA_ASIN - Vector Trigonometric ASin
    """
```

#### TA_ATAN

```python
def TA_ATAN() -> Indicator:
    ...
```

#### TA_ATAN

```python
def TA_ATAN(arg0: Indicator) -> Indicator:
    ...
```

#### TA_ATAN

```python
def TA_ATAN(arg0: float) -> Indicator:
    """
    TA_ATAN - Vector Trigonometric ATan
    """
```

#### TA_ATR

```python
def TA_ATR(n: int = 14) -> Indicator:
    ...
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

#### TA_AVGDEV

```python
def TA_AVGDEV(n: int = 14) -> Indicator:
    ...
```

#### TA_AVGDEV

```python
def TA_AVGDEV(arg0: IndParam) -> Indicator:
    ...
```

#### TA_AVGDEV

```python
def TA_AVGDEV(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_AVGDEV

```python
def TA_AVGDEV(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_AVGDEV

```python
def TA_AVGDEV(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_AVGDEV

```python
def TA_AVGDEV(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_AVGDEV

```python
def TA_AVGDEV(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_AVGDEV - Average Deviation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_AVGDEV

```python
def TA_AVGDEV(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_AVGDEV - Average Deviation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_AVGPRICE

```python
def TA_AVGPRICE() -> Indicator:
    ...
```

#### TA_AVGPRICE

```python
def TA_AVGPRICE(data: KData) -> Indicator:
    """
    TA_AVGPRICE - Average Price
    """
```

#### TA_BBANDS

```python
def TA_BBANDS(n: int = 5, nbdevup: float = 2.0, nbdevdn: float = 2.0, matype: int = 0) -> Indicator:
    ...
```

#### TA_BBANDS

```python
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
```

#### TA_BBANDS

```python
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
```

#### TA_BETA

```python
def TA_BETA(n: int = 5, fill_null: bool = True) -> Indicator:
    ...
```

#### TA_BETA

```python
def TA_BETA(ind1: Indicator, ind2: Indicator, n: int = 5, fill_null: bool = True) -> Indicator:
    """
    TA_BETA - Beta
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
```

#### TA_BETA

```python
def TA_BETA(ind1: Indicator, ind2: Indicator, n: int = 5, fill_null: bool = True) -> Indicator:
    """
    TA_BETA - Beta
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
```

#### TA_BETA

```python
def TA_BETA(ind1: Indicator, ind2: Indicator, n: int = 5, fill_null: bool = True) -> Indicator:
    """
    TA_BETA - Beta
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
```

#### TA_BOP

```python
def TA_BOP() -> Indicator:
    ...
```

#### TA_BOP

```python
def TA_BOP(data: KData) -> Indicator:
    """
    TA_BOP - Balance Of Power
    """
```

#### TA_CCI

```python
def TA_CCI(n: int = 14) -> Indicator:
    ...
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

#### TA_CDL2CROWS

```python
def TA_CDL2CROWS() -> Indicator:
    ...
```

#### TA_CDL2CROWS

```python
def TA_CDL2CROWS(data: KData) -> Indicator:
    """
    TA_CDL2CROWS - Two Crows
    """
```

#### TA_CDL3BLACKCROWS

```python
def TA_CDL3BLACKCROWS() -> Indicator:
    ...
```

#### TA_CDL3BLACKCROWS

```python
def TA_CDL3BLACKCROWS(data: KData) -> Indicator:
    """
    TA_CDL3BLACKCROWS - Three Black Crows
    """
```

#### TA_CDL3INSIDE

```python
def TA_CDL3INSIDE() -> Indicator:
    ...
```

#### TA_CDL3INSIDE

```python
def TA_CDL3INSIDE(data: KData) -> Indicator:
    """
    TA_CDL3INSIDE - Three Inside Up/Down
    """
```

#### TA_CDL3LINESTRIKE

```python
def TA_CDL3LINESTRIKE() -> Indicator:
    ...
```

#### TA_CDL3LINESTRIKE

```python
def TA_CDL3LINESTRIKE(data: KData) -> Indicator:
    """
    TA_CDL3LINESTRIKE - Three-Line Strike
    """
```

#### TA_CDL3OUTSIDE

```python
def TA_CDL3OUTSIDE() -> Indicator:
    ...
```

#### TA_CDL3OUTSIDE

```python
def TA_CDL3OUTSIDE(data: KData) -> Indicator:
    """
    TA_CDL3OUTSIDE - Three Outside Up/Down
    """
```

#### TA_CDL3STARSINSOUTH

```python
def TA_CDL3STARSINSOUTH() -> Indicator:
    ...
```

#### TA_CDL3STARSINSOUTH

```python
def TA_CDL3STARSINSOUTH(data: KData) -> Indicator:
    """
    TA_CDL3STARSINSOUTH - Three Stars In The South
    """
```

#### TA_CDL3WHITESOLDIERS

```python
def TA_CDL3WHITESOLDIERS() -> Indicator:
    ...
```

#### TA_CDL3WHITESOLDIERS

```python
def TA_CDL3WHITESOLDIERS(data: KData) -> Indicator:
    """
    TA_CDL3WHITESOLDIERS - Three Advancing White Soldiers
    """
```

#### TA_CDLABANDONEDBABY

```python
def TA_CDLABANDONEDBABY(penetration: float = 0.3) -> Indicator:
    ...
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

#### TA_CDLADVANCEBLOCK

```python
def TA_CDLADVANCEBLOCK() -> Indicator:
    ...
```

#### TA_CDLADVANCEBLOCK

```python
def TA_CDLADVANCEBLOCK(data: KData) -> Indicator:
    """
    TA_CDLADVANCEBLOCK - Advance Block
    """
```

#### TA_CDLBELTHOLD

```python
def TA_CDLBELTHOLD() -> Indicator:
    ...
```

#### TA_CDLBELTHOLD

```python
def TA_CDLBELTHOLD(data: KData) -> Indicator:
    """
    TA_CDLBELTHOLD - Belt-hold
    """
```

#### TA_CDLBREAKAWAY

```python
def TA_CDLBREAKAWAY() -> Indicator:
    ...
```

#### TA_CDLBREAKAWAY

```python
def TA_CDLBREAKAWAY(data: KData) -> Indicator:
    """
    TA_CDLBREAKAWAY - Breakaway
    """
```

#### TA_CDLCLOSINGMARUBOZU

```python
def TA_CDLCLOSINGMARUBOZU() -> Indicator:
    ...
```

#### TA_CDLCLOSINGMARUBOZU

```python
def TA_CDLCLOSINGMARUBOZU(data: KData) -> Indicator:
    """
    TA_CDLCLOSINGMARUBOZU - Closing Marubozu
    """
```

#### TA_CDLCONCEALBABYSWALL

```python
def TA_CDLCONCEALBABYSWALL() -> Indicator:
    ...
```

#### TA_CDLCONCEALBABYSWALL

```python
def TA_CDLCONCEALBABYSWALL(data: KData) -> Indicator:
    """
    TA_CDLCONCEALBABYSWALL - Concealing Baby Swallow
    """
```

#### TA_CDLCOUNTERATTACK

```python
def TA_CDLCOUNTERATTACK() -> Indicator:
    ...
```

#### TA_CDLCOUNTERATTACK

```python
def TA_CDLCOUNTERATTACK(data: KData) -> Indicator:
    """
    TA_CDLCOUNTERATTACK - Counterattack
    """
```

#### TA_CDLDARKCLOUDCOVER

```python
def TA_CDLDARKCLOUDCOVER(penetration: float = 0.5) -> Indicator:
    ...
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

#### TA_CDLDOJI

```python
def TA_CDLDOJI() -> Indicator:
    ...
```

#### TA_CDLDOJI

```python
def TA_CDLDOJI(data: KData) -> Indicator:
    """
    TA_CDLDOJI - Doji
    """
```

#### TA_CDLDOJISTAR

```python
def TA_CDLDOJISTAR() -> Indicator:
    ...
```

#### TA_CDLDOJISTAR

```python
def TA_CDLDOJISTAR(data: KData) -> Indicator:
    """
    TA_CDLDOJISTAR - Doji Star
    """
```

#### TA_CDLDRAGONFLYDOJI

```python
def TA_CDLDRAGONFLYDOJI() -> Indicator:
    ...
```

#### TA_CDLDRAGONFLYDOJI

```python
def TA_CDLDRAGONFLYDOJI(data: KData) -> Indicator:
    """
    TA_CDLDRAGONFLYDOJI - Dragonfly Doji
    """
```

#### TA_CDLENGULFING

```python
def TA_CDLENGULFING() -> Indicator:
    ...
```

#### TA_CDLENGULFING

```python
def TA_CDLENGULFING(data: KData) -> Indicator:
    """
    TA_CDLENGULFING - Engulfing Pattern
    """
```

#### TA_CDLEVENINGDOJISTAR

```python
def TA_CDLEVENINGDOJISTAR(penetration: float = 0.3) -> Indicator:
    ...
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
def TA_CDLEVENINGSTAR(penetration: float = 0.3) -> Indicator:
    ...
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

#### TA_CDLGAPSIDESIDEWHITE

```python
def TA_CDLGAPSIDESIDEWHITE() -> Indicator:
    ...
```

#### TA_CDLGAPSIDESIDEWHITE

```python
def TA_CDLGAPSIDESIDEWHITE(data: KData) -> Indicator:
    """
    TA_CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    """
```

#### TA_CDLGRAVESTONEDOJI

```python
def TA_CDLGRAVESTONEDOJI() -> Indicator:
    ...
```

#### TA_CDLGRAVESTONEDOJI

```python
def TA_CDLGRAVESTONEDOJI(data: KData) -> Indicator:
    """
    TA_CDLGRAVESTONEDOJI - Gravestone Doji
    """
```

#### TA_CDLHAMMER

```python
def TA_CDLHAMMER() -> Indicator:
    ...
```

#### TA_CDLHAMMER

```python
def TA_CDLHAMMER(data: KData) -> Indicator:
    """
    TA_CDLHAMMER - Hammer
    """
```

#### TA_CDLHANGINGMAN

```python
def TA_CDLHANGINGMAN() -> Indicator:
    ...
```

#### TA_CDLHANGINGMAN

```python
def TA_CDLHANGINGMAN(data: KData) -> Indicator:
    """
    TA_CDLHANGINGMAN - Hanging Man
    """
```

#### TA_CDLHARAMI

```python
def TA_CDLHARAMI() -> Indicator:
    ...
```

#### TA_CDLHARAMI

```python
def TA_CDLHARAMI(data: KData) -> Indicator:
    """
    TA_CDLHARAMI - Harami Pattern
    """
```

#### TA_CDLHARAMICROSS

```python
def TA_CDLHARAMICROSS() -> Indicator:
    ...
```

#### TA_CDLHARAMICROSS

```python
def TA_CDLHARAMICROSS(data: KData) -> Indicator:
    """
    TA_CDLHARAMICROSS - Harami Cross Pattern
    """
```

#### TA_CDLHIGHWAVE

```python
def TA_CDLHIGHWAVE() -> Indicator:
    ...
```

#### TA_CDLHIGHWAVE

```python
def TA_CDLHIGHWAVE(data: KData) -> Indicator:
    """
    TA_CDLHIGHWAVE - High-Wave Candle
    """
```

#### TA_CDLHIKKAKE

```python
def TA_CDLHIKKAKE() -> Indicator:
    ...
```

#### TA_CDLHIKKAKE

```python
def TA_CDLHIKKAKE(data: KData) -> Indicator:
    """
    TA_CDLHIKKAKE - Hikkake Pattern
    """
```

#### TA_CDLHIKKAKEMOD

```python
def TA_CDLHIKKAKEMOD() -> Indicator:
    ...
```

#### TA_CDLHIKKAKEMOD

```python
def TA_CDLHIKKAKEMOD(data: KData) -> Indicator:
    """
    TA_CDLHIKKAKEMOD - Modified Hikkake Pattern
    """
```

#### TA_CDLHOMINGPIGEON

```python
def TA_CDLHOMINGPIGEON() -> Indicator:
    ...
```

#### TA_CDLHOMINGPIGEON

```python
def TA_CDLHOMINGPIGEON(data: KData) -> Indicator:
    """
    TA_CDLHOMINGPIGEON - Homing Pigeon
    """
```

#### TA_CDLIDENTICAL3CROWS

```python
def TA_CDLIDENTICAL3CROWS() -> Indicator:
    ...
```

#### TA_CDLIDENTICAL3CROWS

```python
def TA_CDLIDENTICAL3CROWS(data: KData) -> Indicator:
    """
    TA_CDLIDENTICAL3CROWS - Identical Three Crows
    """
```

#### TA_CDLINNECK

```python
def TA_CDLINNECK() -> Indicator:
    ...
```

#### TA_CDLINNECK

```python
def TA_CDLINNECK(data: KData) -> Indicator:
    """
    TA_CDLINNECK - In-Neck Pattern
    """
```

#### TA_CDLINVERTEDHAMMER

```python
def TA_CDLINVERTEDHAMMER() -> Indicator:
    ...
```

#### TA_CDLINVERTEDHAMMER

```python
def TA_CDLINVERTEDHAMMER(data: KData) -> Indicator:
    """
    TA_CDLINVERTEDHAMMER - Inverted Hammer
    """
```

#### TA_CDLKICKING

```python
def TA_CDLKICKING() -> Indicator:
    ...
```

#### TA_CDLKICKING

```python
def TA_CDLKICKING(data: KData) -> Indicator:
    """
    TA_CDLKICKING - Kicking
    """
```

#### TA_CDLKICKINGBYLENGTH

```python
def TA_CDLKICKINGBYLENGTH() -> Indicator:
    ...
```

#### TA_CDLKICKINGBYLENGTH

```python
def TA_CDLKICKINGBYLENGTH(data: KData) -> Indicator:
    """
    TA_CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    """
```

#### TA_CDLLADDERBOTTOM

```python
def TA_CDLLADDERBOTTOM() -> Indicator:
    ...
```

#### TA_CDLLADDERBOTTOM

```python
def TA_CDLLADDERBOTTOM(data: KData) -> Indicator:
    """
    TA_CDLLADDERBOTTOM - Ladder Bottom
    """
```

#### TA_CDLLONGLEGGEDDOJI

```python
def TA_CDLLONGLEGGEDDOJI() -> Indicator:
    ...
```

#### TA_CDLLONGLEGGEDDOJI

```python
def TA_CDLLONGLEGGEDDOJI(data: KData) -> Indicator:
    """
    TA_CDLLONGLEGGEDDOJI - Long Legged Doji
    """
```

#### TA_CDLLONGLINE

```python
def TA_CDLLONGLINE() -> Indicator:
    ...
```

#### TA_CDLLONGLINE

```python
def TA_CDLLONGLINE(data: KData) -> Indicator:
    """
    TA_CDLLONGLINE - Long Line Candle
    """
```

#### TA_CDLMARUBOZU

```python
def TA_CDLMARUBOZU() -> Indicator:
    ...
```

#### TA_CDLMARUBOZU

```python
def TA_CDLMARUBOZU(data: KData) -> Indicator:
    """
    TA_CDLMARUBOZU - Marubozu
    """
```

#### TA_CDLMATCHINGLOW

```python
def TA_CDLMATCHINGLOW() -> Indicator:
    ...
```

#### TA_CDLMATCHINGLOW

```python
def TA_CDLMATCHINGLOW(data: KData) -> Indicator:
    """
    TA_CDLMATCHINGLOW - Matching Low
    """
```

#### TA_CDLMATHOLD

```python
def TA_CDLMATHOLD(penetration: float = 0.5) -> Indicator:
    ...
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
def TA_CDLMORNINGDOJISTAR(penetration: float = 0.3) -> Indicator:
    ...
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
def TA_CDLMORNINGSTAR(penetration: float = 0.3) -> Indicator:
    ...
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

#### TA_CDLONNECK

```python
def TA_CDLONNECK() -> Indicator:
    ...
```

#### TA_CDLONNECK

```python
def TA_CDLONNECK(data: KData) -> Indicator:
    """
    TA_CDLONNECK - On-Neck Pattern
    """
```

#### TA_CDLPIERCING

```python
def TA_CDLPIERCING() -> Indicator:
    ...
```

#### TA_CDLPIERCING

```python
def TA_CDLPIERCING(data: KData) -> Indicator:
    """
    TA_CDLPIERCING - Piercing Pattern
    """
```

#### TA_CDLRICKSHAWMAN

```python
def TA_CDLRICKSHAWMAN() -> Indicator:
    ...
```

#### TA_CDLRICKSHAWMAN

```python
def TA_CDLRICKSHAWMAN(data: KData) -> Indicator:
    """
    TA_CDLRICKSHAWMAN - Rickshaw Man
    """
```

#### TA_CDLRISEFALL3METHODS

```python
def TA_CDLRISEFALL3METHODS() -> Indicator:
    ...
```

#### TA_CDLRISEFALL3METHODS

```python
def TA_CDLRISEFALL3METHODS(data: KData) -> Indicator:
    """
    TA_CDLRISEFALL3METHODS - Rising/Falling Three Methods
    """
```

#### TA_CDLSEPARATINGLINES

```python
def TA_CDLSEPARATINGLINES() -> Indicator:
    ...
```

#### TA_CDLSEPARATINGLINES

```python
def TA_CDLSEPARATINGLINES(data: KData) -> Indicator:
    """
    TA_CDLSEPARATINGLINES - Separating Lines
    """
```

#### TA_CDLSHOOTINGSTAR

```python
def TA_CDLSHOOTINGSTAR() -> Indicator:
    ...
```

#### TA_CDLSHOOTINGSTAR

```python
def TA_CDLSHOOTINGSTAR(data: KData) -> Indicator:
    """
    TA_CDLSHOOTINGSTAR - Shooting Star
    """
```

#### TA_CDLSHORTLINE

```python
def TA_CDLSHORTLINE() -> Indicator:
    ...
```

#### TA_CDLSHORTLINE

```python
def TA_CDLSHORTLINE(data: KData) -> Indicator:
    """
    TA_CDLSHORTLINE - Short Line Candle
    """
```

#### TA_CDLSPINNINGTOP

```python
def TA_CDLSPINNINGTOP() -> Indicator:
    ...
```

#### TA_CDLSPINNINGTOP

```python
def TA_CDLSPINNINGTOP(data: KData) -> Indicator:
    """
    TA_CDLSPINNINGTOP - Spinning Top
    """
```

#### TA_CDLSTALLEDPATTERN

```python
def TA_CDLSTALLEDPATTERN() -> Indicator:
    ...
```

#### TA_CDLSTALLEDPATTERN

```python
def TA_CDLSTALLEDPATTERN(data: KData) -> Indicator:
    """
    TA_CDLSTALLEDPATTERN - Stalled Pattern
    """
```

#### TA_CDLSTICKSANDWICH

```python
def TA_CDLSTICKSANDWICH() -> Indicator:
    ...
```

#### TA_CDLSTICKSANDWICH

```python
def TA_CDLSTICKSANDWICH(data: KData) -> Indicator:
    """
    TA_CDLSTICKSANDWICH - Stick Sandwich
    """
```

#### TA_CDLTAKURI

```python
def TA_CDLTAKURI() -> Indicator:
    ...
```

#### TA_CDLTAKURI

```python
def TA_CDLTAKURI(data: KData) -> Indicator:
    """
    TA_CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
    """
```

#### TA_CDLTASUKIGAP

```python
def TA_CDLTASUKIGAP() -> Indicator:
    ...
```

#### TA_CDLTASUKIGAP

```python
def TA_CDLTASUKIGAP(data: KData) -> Indicator:
    """
    TA_CDLTASUKIGAP - Tasuki Gap
    """
```

#### TA_CDLTHRUSTING

```python
def TA_CDLTHRUSTING() -> Indicator:
    ...
```

#### TA_CDLTHRUSTING

```python
def TA_CDLTHRUSTING(data: KData) -> Indicator:
    """
    TA_CDLTHRUSTING - Thrusting Pattern
    """
```

#### TA_CDLTRISTAR

```python
def TA_CDLTRISTAR() -> Indicator:
    ...
```

#### TA_CDLTRISTAR

```python
def TA_CDLTRISTAR(data: KData) -> Indicator:
    """
    TA_CDLTRISTAR - Tristar Pattern
    """
```

#### TA_CDLUNIQUE3RIVER

```python
def TA_CDLUNIQUE3RIVER() -> Indicator:
    ...
```

#### TA_CDLUNIQUE3RIVER

```python
def TA_CDLUNIQUE3RIVER(data: KData) -> Indicator:
    """
    TA_CDLUNIQUE3RIVER - Unique 3 River
    """
```

#### TA_CDLUPSIDEGAP2CROWS

```python
def TA_CDLUPSIDEGAP2CROWS() -> Indicator:
    ...
```

#### TA_CDLUPSIDEGAP2CROWS

```python
def TA_CDLUPSIDEGAP2CROWS(data: KData) -> Indicator:
    """
    TA_CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    """
```

#### TA_CDLXSIDEGAP3METHODS

```python
def TA_CDLXSIDEGAP3METHODS() -> Indicator:
    ...
```

#### TA_CDLXSIDEGAP3METHODS

```python
def TA_CDLXSIDEGAP3METHODS(data: KData) -> Indicator:
    """
    TA_CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    """
```

#### TA_CEIL

```python
def TA_CEIL() -> Indicator:
    ...
```

#### TA_CEIL

```python
def TA_CEIL(arg0: Indicator) -> Indicator:
    ...
```

#### TA_CEIL

```python
def TA_CEIL(arg0: float) -> Indicator:
    """
    TA_CEIL - Vector Ceil
    """
```

#### TA_CMO

```python
def TA_CMO(n: int = 14) -> Indicator:
    ...
```

#### TA_CMO

```python
def TA_CMO(arg0: IndParam) -> Indicator:
    ...
```

#### TA_CMO

```python
def TA_CMO(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_CMO

```python
def TA_CMO(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_CMO

```python
def TA_CMO(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_CMO

```python
def TA_CMO(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_CMO

```python
def TA_CMO(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_CMO - Chande Momentum Oscillator
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_CMO

```python
def TA_CMO(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_CMO - Chande Momentum Oscillator
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_CORREL

```python
def TA_CORREL(n: int = 30, fill_null: bool = True) -> Indicator:
    ...
```

#### TA_CORREL

```python
def TA_CORREL(ind1: Indicator, ind2: Indicator, n: int = 30, fill_null: bool = True) -> Indicator:
    """
    TA_CORREL - Pearson's Correlation Coefficient (r)
        
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
```

#### TA_CORREL

```python
def TA_CORREL(ind1: Indicator, ind2: Indicator, n: int = 30, fill_null: bool = True) -> Indicator:
    """
    TA_CORREL - Pearson's Correlation Coefficient (r)
        
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
```

#### TA_CORREL

```python
def TA_CORREL(ind1: Indicator, ind2: Indicator, n: int = 30, fill_null: bool = True) -> Indicator:
    """
    TA_CORREL - Pearson's Correlation Coefficient (r)
        
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    :param int n: Number of periode (From 1 to 100000)
    """
```

#### TA_COS

```python
def TA_COS() -> Indicator:
    ...
```

#### TA_COS

```python
def TA_COS(arg0: Indicator) -> Indicator:
    ...
```

#### TA_COS

```python
def TA_COS(arg0: float) -> Indicator:
    """
    TA_COS - Vector Trigonometric Cos
    """
```

#### TA_COSH

```python
def TA_COSH() -> Indicator:
    ...
```

#### TA_COSH

```python
def TA_COSH(arg0: Indicator) -> Indicator:
    ...
```

#### TA_COSH

```python
def TA_COSH(arg0: float) -> Indicator:
    """
    TA_COSH - Vector Trigonometric Cosh
    """
```

#### TA_DEMA

```python
def TA_DEMA(n: int = 30) -> Indicator:
    ...
```

#### TA_DEMA

```python
def TA_DEMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_DEMA

```python
def TA_DEMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_DEMA

```python
def TA_DEMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_DEMA

```python
def TA_DEMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_DEMA

```python
def TA_DEMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_DEMA

```python
def TA_DEMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_DEMA - Double Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_DEMA

```python
def TA_DEMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_DEMA - Double Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_DIV

```python
def TA_DIV(fill_null: bool = True) -> Indicator:
    ...
```

#### TA_DIV

```python
def TA_DIV(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_DIV - Vector Arithmetic Div
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_DIV

```python
def TA_DIV(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_DIV - Vector Arithmetic Div
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_DIV

```python
def TA_DIV(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_DIV - Vector Arithmetic Div
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_DX

```python
def TA_DX(n: int = 14) -> Indicator:
    ...
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

#### TA_EMA

```python
def TA_EMA(n: int = 30) -> Indicator:
    ...
```

#### TA_EMA

```python
def TA_EMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_EMA

```python
def TA_EMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_EMA

```python
def TA_EMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_EMA

```python
def TA_EMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_EMA

```python
def TA_EMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_EMA

```python
def TA_EMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_EMA - Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_EMA

```python
def TA_EMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_EMA - Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_EXP

```python
def TA_EXP() -> Indicator:
    ...
```

#### TA_EXP

```python
def TA_EXP(arg0: Indicator) -> Indicator:
    ...
```

#### TA_EXP

```python
def TA_EXP(arg0: float) -> Indicator:
    """
    TA_EXP - Vector Arithmetic Exp
    """
```

#### TA_FLOOR

```python
def TA_FLOOR() -> Indicator:
    ...
```

#### TA_FLOOR

```python
def TA_FLOOR(arg0: Indicator) -> Indicator:
    ...
```

#### TA_FLOOR

```python
def TA_FLOOR(arg0: float) -> Indicator:
    """
    TA_FLOOR - Vector Floor
    """
```

#### TA_HT_DCPERIOD

```python
def TA_HT_DCPERIOD() -> Indicator:
    ...
```

#### TA_HT_DCPERIOD

```python
def TA_HT_DCPERIOD(arg0: Indicator) -> Indicator:
    ...
```

#### TA_HT_DCPERIOD

```python
def TA_HT_DCPERIOD(arg0: float) -> Indicator:
    """
    TA_HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period
    """
```

#### TA_HT_DCPHASE

```python
def TA_HT_DCPHASE() -> Indicator:
    ...
```

#### TA_HT_DCPHASE

```python
def TA_HT_DCPHASE(arg0: Indicator) -> Indicator:
    ...
```

#### TA_HT_DCPHASE

```python
def TA_HT_DCPHASE(arg0: float) -> Indicator:
    """
    TA_HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase
    """
```

#### TA_HT_PHASOR

```python
def TA_HT_PHASOR() -> Indicator:
    ...
```

#### TA_HT_PHASOR

```python
def TA_HT_PHASOR(arg0: Indicator) -> Indicator:
    ...
```

#### TA_HT_PHASOR

```python
def TA_HT_PHASOR(arg0: float) -> Indicator:
    """
    TA_HT_PHASOR - Hilbert Transform - Phasor Components
    
    :return: result(0) - outInPhase
             result(1) - outQuadrature
    """
```

#### TA_HT_SINE

```python
def TA_HT_SINE() -> Indicator:
    ...
```

#### TA_HT_SINE

```python
def TA_HT_SINE(arg0: Indicator) -> Indicator:
    ...
```

#### TA_HT_SINE

```python
def TA_HT_SINE(arg0: float) -> Indicator:
    """
    TA_HT_SINE - Hilbert Transform - SineWave
    :return: result(0) - outSine
             result(1) - outLeadSine
    """
```

#### TA_HT_TRENDLINE

```python
def TA_HT_TRENDLINE() -> Indicator:
    ...
```

#### TA_HT_TRENDLINE

```python
def TA_HT_TRENDLINE(arg0: Indicator) -> Indicator:
    ...
```

#### TA_HT_TRENDLINE

```python
def TA_HT_TRENDLINE(arg0: float) -> Indicator:
    """
    TA_HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    """
```

#### TA_HT_TRENDMODE

```python
def TA_HT_TRENDMODE() -> Indicator:
    ...
```

#### TA_HT_TRENDMODE

```python
def TA_HT_TRENDMODE(arg0: Indicator) -> Indicator:
    ...
```

#### TA_HT_TRENDMODE

```python
def TA_HT_TRENDMODE(arg0: float) -> Indicator:
    """
    TA_HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode
    """
```

#### TA_IMI

```python
def TA_IMI(n: int = 14) -> Indicator:
    ...
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

#### TA_KAMA

```python
def TA_KAMA(n: int = 30) -> Indicator:
    ...
```

#### TA_KAMA

```python
def TA_KAMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_KAMA

```python
def TA_KAMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_KAMA

```python
def TA_KAMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_KAMA

```python
def TA_KAMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_KAMA

```python
def TA_KAMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_KAMA

```python
def TA_KAMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_KAMA - Kaufman Adaptive Moving Average
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_KAMA

```python
def TA_KAMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_KAMA - Kaufman Adaptive Moving Average
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG

```python
def TA_LINEARREG(n: int = 14) -> Indicator:
    ...
```

#### TA_LINEARREG

```python
def TA_LINEARREG(arg0: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG

```python
def TA_LINEARREG(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG

```python
def TA_LINEARREG(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG

```python
def TA_LINEARREG(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG

```python
def TA_LINEARREG(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG

```python
def TA_LINEARREG(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG - Linear Regression
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG

```python
def TA_LINEARREG(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG - Linear Regression
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(n: int = 14) -> Indicator:
    ...
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(arg0: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_ANGLE - Linear Regression Angle
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG_ANGLE

```python
def TA_LINEARREG_ANGLE(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_ANGLE - Linear Regression Angle
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(n: int = 14) -> Indicator:
    ...
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(arg0: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_INTERCEPT - Linear Regression Intercept
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG_INTERCEPT

```python
def TA_LINEARREG_INTERCEPT(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_INTERCEPT - Linear Regression Intercept
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(n: int = 14) -> Indicator:
    ...
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(arg0: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_SLOPE - Linear Regression Slope
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LINEARREG_SLOPE

```python
def TA_LINEARREG_SLOPE(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_LINEARREG_SLOPE - Linear Regression Slope
    
    :param KData data: input KData
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_LN

```python
def TA_LN() -> Indicator:
    ...
```

#### TA_LN

```python
def TA_LN(arg0: Indicator) -> Indicator:
    ...
```

#### TA_LN

```python
def TA_LN(arg0: float) -> Indicator:
    """
    TA_LN - Vector Log Natural
    """
```

#### TA_LOG10

```python
def TA_LOG10() -> Indicator:
    ...
```

#### TA_LOG10

```python
def TA_LOG10(arg0: Indicator) -> Indicator:
    ...
```

#### TA_LOG10

```python
def TA_LOG10(arg0: float) -> Indicator:
    """
    TA_LOG10 - Vector Log10
    """
```

#### TA_MA

```python
def TA_MA(n: int = 30, matype: int = 0) -> Indicator:
    ...
```

#### TA_MA

```python
def TA_MA(data: Indicator, n: int = 30, matype: int = 0) -> Indicator:
    """
    TA_MA - Moving average
    
    :param Indicator data: input data
    :param int n: Number of periode (From 1 to 100000)
    :param int matype: Type of Moving Average
    """
```

#### TA_MA

```python
def TA_MA(data: Indicator, n: int = 30, matype: int = 0) -> Indicator:
    """
    TA_MA - Moving average
    
    :param Indicator data: input data
    :param int n: Number of periode (From 1 to 100000)
    :param int matype: Type of Moving Average
    """
```

#### TA_MACD

```python
def TA_MACD(fast_n: int = 12, slow_n: int = 26, signal_n: int = 9) -> Indicator:
    ...
```

#### TA_MACD

```python
def TA_MACD(data: Indicator, fast_n: int = 30, slow_n: int = 26, signal_n: int = 9) -> Indicator:
    """
    TA_MACD - Moving Average Convergence/Divergence
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int signal_n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    """
```

#### TA_MACD

```python
def TA_MACD(data: Indicator, fast_n: int = 30, slow_n: int = 26, signal_n: int = 9) -> Indicator:
    """
    TA_MACD - Moving Average Convergence/Divergence
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int signal_n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    """
```

#### TA_MACDEXT

```python
def TA_MACDEXT(fast_n: int = 12, slow_n: int = 26, signal_n: int = 9, fast_matype: int = 0, slow_matype: int = 0, signal_matype: int = 0) -> Indicator:
    ...
```

#### TA_MACDEXT

```python
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
```

#### TA_MACDEXT

```python
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
```

#### TA_MACDFIX

```python
def TA_MACDFIX(n: int = 9) -> Indicator:
    ...
```

#### TA_MACDFIX

```python
def TA_MACDFIX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MACDFIX

```python
def TA_MACDFIX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MACDFIX

```python
def TA_MACDFIX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MACDFIX

```python
def TA_MACDFIX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MACDFIX

```python
def TA_MACDFIX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MACDFIX

```python
def TA_MACDFIX(data: Indicator, n: int = 9) -> Indicator:
    """
    TA_MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    
    :param Indicator data: input data
    :param int n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    :return: result(0) - outMACD
             result(1) - outMACDSignal
             result(2) - outMACDHist
    """
```

#### TA_MACDFIX

```python
def TA_MACDFIX(data: Indicator, n: int = 9) -> Indicator:
    """
    TA_MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    
    :param Indicator data: input data
    :param int n: Smoothing for the signal line (nb of period) (From 1 to 100000)
    :return: result(0) - outMACD
             result(1) - outMACDSignal
             result(2) - outMACDHist
    """
```

#### TA_MAMA

```python
def TA_MAMA(fast_limit: float = 0.5, slow_limit: float = 0.05) -> Indicator:
    ...
```

#### TA_MAMA

```python
def TA_MAMA(data: Indicator, fast_limit: float = 0.5, slow_limit: float = 0.05) -> Indicator:
    """
    TA_MAMA - MESA Adaptive Moving Average
    
    :param Indicator data: input data
    :param float fast_limit: Fast limit (From 0.01 to 0.99)
    :param float slow_limit: Slow limit (From 0.01 to 0.99)
    """
```

#### TA_MAMA

```python
def TA_MAMA(data: Indicator, fast_limit: float = 0.5, slow_limit: float = 0.05) -> Indicator:
    """
    TA_MAMA - MESA Adaptive Moving Average
    
    :param Indicator data: input data
    :param float fast_limit: Fast limit (From 0.01 to 0.99)
    :param float slow_limit: Slow limit (From 0.01 to 0.99)
    """
```

#### TA_MAVP

```python
def TA_MAVP(ref_ind: Indicator, min_n: int = 2, max_n: int = 30, matype: int = 0, fill_null: bool = True) -> Indicator:
    ...
```

#### TA_MAVP

```python
def TA_MAVP(ref_ind: Indicator, min_n: int = 2, max_n: int = 30, matype: int = 0, fill_null: bool = True) -> Indicator:
    ...
```

#### TA_MAVP

```python
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
```

#### TA_MAVP

```python
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
```

#### TA_MAVP

```python
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
```

#### TA_MAX

```python
def TA_MAX(n: int = 30) -> Indicator:
    ...
```

#### TA_MAX

```python
def TA_MAX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MAX

```python
def TA_MAX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MAX

```python
def TA_MAX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MAX

```python
def TA_MAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MAX

```python
def TA_MAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MAX

```python
def TA_MAX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MAX - Highest value over a specified period
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MAX

```python
def TA_MAX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MAX - Highest value over a specified period
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(n: int = 30) -> Indicator:
    ...
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MAXINDEX - Index of highest value over a specified period
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MAXINDEX

```python
def TA_MAXINDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MAXINDEX - Index of highest value over a specified period
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MEDPRICE

```python
def TA_MEDPRICE() -> Indicator:
    ...
```

#### TA_MEDPRICE

```python
def TA_MEDPRICE(data: KData) -> Indicator:
    """
    TA_MEDPRICE - Median Price
    """
```

#### TA_MFI

```python
def TA_MFI(n: int = 14) -> Indicator:
    ...
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

#### TA_MIDPOINT

```python
def TA_MIDPOINT(n: int = 14) -> Indicator:
    ...
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_MIDPOINT - MidPoint over period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MIDPOINT

```python
def TA_MIDPOINT(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_MIDPOINT - MidPoint over period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MIDPRICE

```python
def TA_MIDPRICE(n: int = 14) -> Indicator:
    ...
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

#### TA_MIN

```python
def TA_MIN(n: int = 30) -> Indicator:
    ...
```

#### TA_MIN

```python
def TA_MIN(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MIN

```python
def TA_MIN(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MIN

```python
def TA_MIN(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MIN

```python
def TA_MIN(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MIN

```python
def TA_MIN(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MIN

```python
def TA_MIN(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MIN - Lowest value over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MIN

```python
def TA_MIN(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MIN - Lowest value over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MININDEX

```python
def TA_MININDEX(n: int = 30) -> Indicator:
    ...
```

#### TA_MININDEX

```python
def TA_MININDEX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MININDEX

```python
def TA_MININDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MININDEX

```python
def TA_MININDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MININDEX

```python
def TA_MININDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MININDEX

```python
def TA_MININDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MININDEX

```python
def TA_MININDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MININDEX - Index of lowest value over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MININDEX

```python
def TA_MININDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MININDEX - Index of lowest value over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_MINMAX

```python
def TA_MINMAX(n: int = 30) -> Indicator:
    ...
```

#### TA_MINMAX

```python
def TA_MINMAX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MINMAX

```python
def TA_MINMAX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MINMAX

```python
def TA_MINMAX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MINMAX

```python
def TA_MINMAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MINMAX

```python
def TA_MINMAX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MINMAX

```python
def TA_MINMAX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MINMAX - Lowest and highest values over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - outMin
             result(1) - outMax
    """
```

#### TA_MINMAX

```python
def TA_MINMAX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MINMAX - Lowest and highest values over a specified period
    
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - outMin
             result(1) - outMax
    """
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(n: int = 30) -> Indicator:
    ...
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MINMAXINDEX - Indexes of lowest and highest values over a specified period
        
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - outMinIdx
             result(1) - outMaxIdx
    """
```

#### TA_MINMAXINDEX

```python
def TA_MINMAXINDEX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_MINMAXINDEX - Indexes of lowest and highest values over a specified period
        
    :param Indicator data: input
    :param int n: Number of period (From 2 to 100000)
    :return: result(0) - outMinIdx
             result(1) - outMaxIdx
    """
```

#### TA_MINUS_DI

```python
def TA_MINUS_DI(n: int = 14) -> Indicator:
    ...
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
def TA_MINUS_DM(n: int = 14) -> Indicator:
    ...
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

#### TA_MOM

```python
def TA_MOM(n: int = 10) -> Indicator:
    ...
```

#### TA_MOM

```python
def TA_MOM(arg0: IndParam) -> Indicator:
    ...
```

#### TA_MOM

```python
def TA_MOM(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MOM

```python
def TA_MOM(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_MOM

```python
def TA_MOM(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MOM

```python
def TA_MOM(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_MOM

```python
def TA_MOM(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_MOM - Momentum
        
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_MOM

```python
def TA_MOM(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_MOM - Momentum
        
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_MULT

```python
def TA_MULT(fill_null: bool = True) -> Indicator:
    ...
```

#### TA_MULT

```python
def TA_MULT(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_MULT - Vector Arithmetic Mult
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_MULT

```python
def TA_MULT(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_MULT - Vector Arithmetic Mult
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_MULT

```python
def TA_MULT(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_MULT - Vector Arithmetic Mult
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_NATR

```python
def TA_NATR(n: int = 14) -> Indicator:
    ...
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

#### TA_OBV

```python
def TA_OBV() -> Indicator:
    ...
```

#### TA_OBV

```python
def TA_OBV(data: KData) -> Indicator:
    """
    TA_OBV - On Balance Volume
    """
```

#### TA_PLUS_DI

```python
def TA_PLUS_DI(n: int = 14) -> Indicator:
    ...
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
def TA_PLUS_DM(n: int = 14) -> Indicator:
    ...
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

#### TA_PPO

```python
def TA_PPO(fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    ...
```

#### TA_PPO

```python
def TA_PPO(data: Indicator, fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    """
    TA_PPO - Percentage Price Oscillator
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int matype: Type of Moving Average
    """
```

#### TA_PPO

```python
def TA_PPO(data: Indicator, fast_n: int = 12, slow_n: int = 26, matype: int = 0) -> Indicator:
    """
    TA_PPO - Percentage Price Oscillator
    
    :param Indicator data: input data
    :param int fast_n: Number of periode for fast MA (From 2 to 100000)
    :param int slow_n: Number of periode for slow MA (From 2 to 100000)
    :param int matype: Type of Moving Average
    """
```

#### TA_ROC

```python
def TA_ROC(n: int = 10) -> Indicator:
    ...
```

#### TA_ROC

```python
def TA_ROC(arg0: IndParam) -> Indicator:
    ...
```

#### TA_ROC

```python
def TA_ROC(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROC

```python
def TA_ROC(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROC

```python
def TA_ROC(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROC

```python
def TA_ROC(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROC

```python
def TA_ROC(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROC - Rate of change : ((price/prevPrice)-1)*100
        
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROC

```python
def TA_ROC(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROC - Rate of change : ((price/prevPrice)-1)*100
        
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROCP

```python
def TA_ROCP(n: int = 10) -> Indicator:
    ...
```

#### TA_ROCP

```python
def TA_ROCP(arg0: IndParam) -> Indicator:
    ...
```

#### TA_ROCP

```python
def TA_ROCP(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROCP

```python
def TA_ROCP(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROCP

```python
def TA_ROCP(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROCP

```python
def TA_ROCP(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROCP

```python
def TA_ROCP(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROCP

```python
def TA_ROCP(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROCR

```python
def TA_ROCR(n: int = 10) -> Indicator:
    ...
```

#### TA_ROCR

```python
def TA_ROCR(arg0: IndParam) -> Indicator:
    ...
```

#### TA_ROCR

```python
def TA_ROCR(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROCR

```python
def TA_ROCR(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROCR

```python
def TA_ROCR(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROCR

```python
def TA_ROCR(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROCR

```python
def TA_ROCR(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCR - Rate of change ratio: (price/prevPrice)
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROCR

```python
def TA_ROCR(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCR - Rate of change ratio: (price/prevPrice)
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROCR100

```python
def TA_ROCR100(n: int = 10) -> Indicator:
    ...
```

#### TA_ROCR100

```python
def TA_ROCR100(arg0: IndParam) -> Indicator:
    ...
```

#### TA_ROCR100

```python
def TA_ROCR100(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROCR100

```python
def TA_ROCR100(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_ROCR100

```python
def TA_ROCR100(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROCR100

```python
def TA_ROCR100(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_ROCR100

```python
def TA_ROCR100(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_ROCR100

```python
def TA_ROCR100(data: Indicator, n: int = 10) -> Indicator:
    """
    TA_ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_RSI

```python
def TA_RSI(n: int = 14) -> Indicator:
    ...
```

#### TA_RSI

```python
def TA_RSI(arg0: IndParam) -> Indicator:
    ...
```

#### TA_RSI

```python
def TA_RSI(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_RSI

```python
def TA_RSI(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_RSI

```python
def TA_RSI(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_RSI

```python
def TA_RSI(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_RSI

```python
def TA_RSI(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_RSI - Relative Strength Index
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_RSI

```python
def TA_RSI(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_RSI - Relative Strength Index
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_SAR

```python
def TA_SAR(acceleration: float = 0.02, maximum: float = 0.2) -> Indicator:
    ...
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
def TA_SAREXT(startvalue: float = 0.0, offsetonreverse: float = 0.0, accelerationinitlong: float = 0.02, accelerationlong: float = 0.02, accelerationmaxlong: float = 0.2, accelerationinitshort: float = 0.02, accelerationshort: float = 0.02, accelerationmaxshort: float = 0.2) -> Indicator:
    ...
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

#### TA_SIN

```python
def TA_SIN() -> Indicator:
    ...
```

#### TA_SIN

```python
def TA_SIN(arg0: Indicator) -> Indicator:
    ...
```

#### TA_SIN

```python
def TA_SIN(arg0: float) -> Indicator:
    """
    TA_SIN - Vector Trigonometric Sin
    """
```

#### TA_SINH

```python
def TA_SINH() -> Indicator:
    ...
```

#### TA_SINH

```python
def TA_SINH(arg0: Indicator) -> Indicator:
    ...
```

#### TA_SINH

```python
def TA_SINH(arg0: float) -> Indicator:
    """
    TA_SINH - Vector Trigonometric Sinh
    """
```

#### TA_SMA

```python
def TA_SMA(n: int = 30) -> Indicator:
    ...
```

#### TA_SMA

```python
def TA_SMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_SMA

```python
def TA_SMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_SMA

```python
def TA_SMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_SMA

```python
def TA_SMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_SMA

```python
def TA_SMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_SMA

```python
def TA_SMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_SMA - Simple Moving Average
        
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_SMA

```python
def TA_SMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_SMA - Simple Moving Average
        
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_SQRT

```python
def TA_SQRT() -> Indicator:
    ...
```

#### TA_SQRT

```python
def TA_SQRT(arg0: Indicator) -> Indicator:
    ...
```

#### TA_SQRT

```python
def TA_SQRT(arg0: float) -> Indicator:
    """
    TA_SQRT - Vector Square Root
    """
```

#### TA_STDDEV

```python
def TA_STDDEV(n: int = 5, nbdev: float = 1.0) -> Indicator:
    ...
```

#### TA_STDDEV

```python
def TA_STDDEV(data: Indicator, n: int = 5, nbdev: float = 1.0) -> Indicator:
    """
    TA_STDDEV - Standard Deviation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param float nbdev: Nb of deviations
    """
```

#### TA_STDDEV

```python
def TA_STDDEV(data: Indicator, n: int = 5, nbdev: float = 1.0) -> Indicator:
    """
    TA_STDDEV - Standard Deviation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param float nbdev: Nb of deviations
    """
```

#### TA_STOCH

```python
def TA_STOCH(fastk_n: int = 5, slowk_n: int = 3, slowk_matype: int = 0, slowd_n: int = 3, slowd_matype: int = 0) -> Indicator:
    ...
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
def TA_STOCHF(fastk_n: int = 5, fastd_n: int = 3, fastd_matype: int = 0) -> Indicator:
    ...
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

#### TA_STOCHRSI

```python
def TA_STOCHRSI(n: int = 14, fastk_n: int = 5, fastd_n: int = 3, matype: int = 0) -> Indicator:
    ...
```

#### TA_STOCHRSI

```python
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
```

#### TA_STOCHRSI

```python
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
```

#### TA_SUB

```python
def TA_SUB(fill_null: bool = True) -> Indicator:
    ...
```

#### TA_SUB

```python
def TA_SUB(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_SUB - Vector Arithmetic Subtraction
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_SUB

```python
def TA_SUB(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_SUB - Vector Arithmetic Subtraction
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_SUB

```python
def TA_SUB(ind1: Indicator, ind2: Indicator, fill_null: bool = True) -> Indicator:
    """
    TA_SUB - Vector Arithmetic Subtraction
    
    :param Indicator ind1: input1
    :param Indicator ind2: input2
    """
```

#### TA_SUM

```python
def TA_SUM(n: int = 30) -> Indicator:
    ...
```

#### TA_SUM

```python
def TA_SUM(arg0: IndParam) -> Indicator:
    ...
```

#### TA_SUM

```python
def TA_SUM(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_SUM

```python
def TA_SUM(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_SUM

```python
def TA_SUM(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_SUM

```python
def TA_SUM(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_SUM

```python
def TA_SUM(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_SUM - Summation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_SUM

```python
def TA_SUM(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_SUM - Summation
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_T3

```python
def TA_T3(n: int = 5, vfactor: float = 0.7) -> Indicator:
    ...
```

#### TA_T3

```python
def TA_T3(data: Indicator, n: int = 5, vfactor: float = 0.7) -> Indicator:
    """
    TA_T3 - Triple Exponential Moving Average (T3)
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param float vfactor: Volume Factor (From 0 to 1)
    """
```

#### TA_T3

```python
def TA_T3(data: Indicator, n: int = 5, vfactor: float = 0.7) -> Indicator:
    """
    TA_T3 - Triple Exponential Moving Average (T3)
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    :param float vfactor: Volume Factor (From 0 to 1)
    """
```

#### TA_TAN

```python
def TA_TAN() -> Indicator:
    ...
```

#### TA_TAN

```python
def TA_TAN(arg0: Indicator) -> Indicator:
    ...
```

#### TA_TAN

```python
def TA_TAN(arg0: float) -> Indicator:
    """
    TA_TAN - Vector Trigonometric Tan
    """
```

#### TA_TANH

```python
def TA_TANH() -> Indicator:
    ...
```

#### TA_TANH

```python
def TA_TANH(arg0: Indicator) -> Indicator:
    ...
```

#### TA_TANH

```python
def TA_TANH(arg0: float) -> Indicator:
    """
    TA_TANH - Vector Trigonometric Tanh
    """
```

#### TA_TEMA

```python
def TA_TEMA(n: int = 30) -> Indicator:
    ...
```

#### TA_TEMA

```python
def TA_TEMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_TEMA

```python
def TA_TEMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TEMA

```python
def TA_TEMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TEMA

```python
def TA_TEMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TEMA

```python
def TA_TEMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TEMA

```python
def TA_TEMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TEMA - Triple Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_TEMA

```python
def TA_TEMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TEMA - Triple Exponential Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_TRANGE

```python
def TA_TRANGE() -> Indicator:
    ...
```

#### TA_TRANGE

```python
def TA_TRANGE(data: KData) -> Indicator:
    """
    TA_TRANGE - True Range
    """
```

#### TA_TRIMA

```python
def TA_TRIMA(n: int = 30) -> Indicator:
    ...
```

#### TA_TRIMA

```python
def TA_TRIMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_TRIMA

```python
def TA_TRIMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TRIMA

```python
def TA_TRIMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TRIMA

```python
def TA_TRIMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TRIMA

```python
def TA_TRIMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TRIMA

```python
def TA_TRIMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TRIMA - Triangular Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_TRIMA

```python
def TA_TRIMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TRIMA - Triangular Moving Average
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_TRIX

```python
def TA_TRIX(n: int = 30) -> Indicator:
    ...
```

#### TA_TRIX

```python
def TA_TRIX(arg0: IndParam) -> Indicator:
    ...
```

#### TA_TRIX

```python
def TA_TRIX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TRIX

```python
def TA_TRIX(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TRIX

```python
def TA_TRIX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TRIX

```python
def TA_TRIX(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TRIX

```python
def TA_TRIX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_TRIX

```python
def TA_TRIX(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    """
```

#### TA_TSF

```python
def TA_TSF(n: int = 14) -> Indicator:
    ...
```

#### TA_TSF

```python
def TA_TSF(arg0: IndParam) -> Indicator:
    ...
```

#### TA_TSF

```python
def TA_TSF(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TSF

```python
def TA_TSF(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_TSF

```python
def TA_TSF(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TSF

```python
def TA_TSF(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_TSF

```python
def TA_TSF(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_TSF - Time Series Forecast
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_TSF

```python
def TA_TSF(data: Indicator, n: int = 14) -> Indicator:
    """
    TA_TSF - Time Series Forecast
    
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_TYPPRICE

```python
def TA_TYPPRICE() -> Indicator:
    ...
```

#### TA_TYPPRICE

```python
def TA_TYPPRICE(data: KData) -> Indicator:
    """
    TA_TYPPRICE - Typical Price
    """
```

#### TA_ULTOSC

```python
def TA_ULTOSC(n1: int = 7, n2: int = 14, n3: int = 28) -> Indicator:
    ...
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

#### TA_VAR

```python
def TA_VAR(n: int = 5, nbdev: float = 1.0) -> Indicator:
    ...
```

#### TA_VAR

```python
def TA_VAR(data: Indicator, n: int = 5, nbdev: float = 1.0) -> Indicator:
    """
    TA_VAR - Variance
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    :param float nbdev: Nb of deviations
    """
```

#### TA_VAR

```python
def TA_VAR(data: Indicator, n: int = 5, nbdev: float = 1.0) -> Indicator:
    """
    TA_VAR - Variance
    
    :param Indicator data: input data
    :param int n: Number of period (From 1 to 100000)
    :param float nbdev: Nb of deviations
    """
```

#### TA_WCLPRICE

```python
def TA_WCLPRICE() -> Indicator:
    ...
```

#### TA_WCLPRICE

```python
def TA_WCLPRICE(data: KData) -> Indicator:
    """
    TA_WCLPRICE - Weighted Close Price
    """
```

#### TA_WILLR

```python
def TA_WILLR(n: int = 14) -> Indicator:
    ...
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

#### TA_WMA

```python
def TA_WMA(n: int = 30) -> Indicator:
    ...
```

#### TA_WMA

```python
def TA_WMA(arg0: IndParam) -> Indicator:
    ...
```

#### TA_WMA

```python
def TA_WMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_WMA

```python
def TA_WMA(arg0: Indicator, arg1: IndParam) -> Indicator:
    ...
```

#### TA_WMA

```python
def TA_WMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_WMA

```python
def TA_WMA(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### TA_WMA

```python
def TA_WMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_WMA - Weighted Moving Average
        
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TA_WMA

```python
def TA_WMA(data: Indicator, n: int = 30) -> Indicator:
    """
    TA_WMA - Weighted Moving Average
        
    :param Indicator data: input data
    :param int n: Number of period (From 2 to 100000)
    """
```

#### TIME

```python
def TIME() -> Indicator:
    ...
```

#### TIME

```python
def TIME(arg0: KData) -> Indicator:
    """
    TIME([data])
    
        取得该周期的时分秒。用法: TIME 函数返回有效值范围为(000000-235959)。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### TIMELINE

```python
def TIMELINE() -> Indicator:
    ...
```

#### TIMELINE

```python
def TIMELINE(arg0: KData) -> Indicator:
    """
    TIMELINE([k])
    
        分时价格数据
    
        :param KData k: 上下文
        :rtype: Indicator
    """
```

#### TIMELINEVOL

```python
def TIMELINEVOL() -> Indicator:
    ...
```

#### TIMELINEVOL

```python
def TIMELINEVOL(arg0: KData) -> Indicator:
    """
    TIMELINEVOL([k])
    
        分时成交量数据
    
        :param KData k: 上下文
        :rtype: Indicator
    """
```

#### TR

```python
def TR() -> Indicator:
    ...
```

#### TR

```python
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
```

#### TURNOVER

```python
def TURNOVER(n: int = 1) -> Indicator:
    ...
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

#### UPNDAY

```python
def UPNDAY(data: Indicator, n: int = 3) -> Indicator:
    ...
```

#### UPNDAY

```python
def UPNDAY(data: Indicator, n: int = 3) -> Indicator:
    ...
```

#### UPNDAY

```python
def UPNDAY(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### UPNDAY

```python
def UPNDAY(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### UPNDAY

```python
def UPNDAY(data: Indicator, n: Indicator) -> Indicator:
    """
    UPNDAY(data[, n=3])
    
        连涨周期数, UPNDAY(CLOSE,M)表示连涨M个周期
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### UPNDAY

```python
def UPNDAY(data: Indicator, n: Indicator) -> Indicator:
    """
    UPNDAY(data[, n=3])
    
        连涨周期数, UPNDAY(CLOSE,M)表示连涨M个周期
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### VAR

```python
def VAR(n: int = 10) -> Indicator:
    ...
```

#### VAR

```python
def VAR(n: IndParam) -> Indicator:
    ...
```

#### VAR

```python
def VAR(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### VAR

```python
def VAR(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### VAR

```python
def VAR(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### VAR

```python
def VAR(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### VAR

```python
def VAR(data: Indicator, n: int = 10) -> Indicator:
    """
    VAR([data, n=10])
    
        估算样本方差, VAR(X,N)为X的N日估算样本方差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### VAR

```python
def VAR(data: Indicator, n: int = 10) -> Indicator:
    """
    VAR([data, n=10])
    
        估算样本方差, VAR(X,N)为X的N日估算样本方差
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### VARP

```python
def VARP(n: int = 10) -> Indicator:
    ...
```

#### VARP

```python
def VARP(n: IndParam) -> Indicator:
    ...
```

#### VARP

```python
def VARP(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### VARP

```python
def VARP(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### VARP

```python
def VARP(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### VARP

```python
def VARP(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### VARP

```python
def VARP(data: Indicator, n: int = 10) -> Indicator:
    """
    VARP([data, n=10])
    
        总体样本方差, VARP(X,N)为X的N日总体样本方差
    
        :param Indicator data: 输入数据
        :param int n|Indicator|IndParam: 时间窗口
        :rtype: Indicator
    """
```

#### VARP

```python
def VARP(data: Indicator, n: int = 10) -> Indicator:
    """
    VARP([data, n=10])
    
        总体样本方差, VARP(X,N)为X的N日总体样本方差
    
        :param Indicator data: 输入数据
        :param int n|Indicator|IndParam: 时间窗口
        :rtype: Indicator
    """
```

#### VIGOR

```python
def VIGOR(kdata: KData, n: int = 2) -> Indicator:
    ...
```

#### VIGOR

```python
def VIGOR(n: int = 2) -> Indicator:
    """
    VIGOR([kdata, n=2])
    
        亚历山大.艾尔德力度指数 [BOOK2]_
    
        计算公式：（收盘价今－收盘价昨）＊成交量今
    
        :param KData data: 输入数据
        :param int n: EMA平滑窗口
        :rtype: Indicator
    """
```

#### WEAVE

```python
def WEAVE(arg0: typing.Sequence) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
def WEAVE(arg0: Indicator, arg1: Indicator, arg2: Indicator, arg3: Indicator, arg4: Indicator) -> Indicator:
    ...
```

#### WEAVE

```python
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
```

#### WEAVE

```python
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
```

#### WEAVE

```python
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
```

#### WEAVE

```python
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
```

#### WEAVE

```python
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
```

#### WEAVE

```python
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
```

#### WEEK

```python
def WEEK() -> Indicator:
    ...
```

#### WEEK

```python
def WEEK(arg0: KData) -> Indicator:
    """
    WEEK([data])
    
        取得该周期的星期数。用法：WEEK 函数返回有效值范围为(0-6)，0表示星期天。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### WINNER

```python
def WINNER() -> Indicator:
    ...
```

#### WINNER

```python
def WINNER(arg0: Indicator) -> Indicator:
    ...
```

#### WINNER

```python
def WINNER(arg0: float) -> Indicator:
    """
    WINNER([ind])
        
        获利盘比例
        用法: WINNER(CLOSE)　表示以当前收市价卖出的获利盘比例。
        例如: 返回0.1表示10%获利盘;WINNER(10.5)表示10.5元价格的获利盘比例
        该函数仅对日线分析周期有效，且仅对存在流通盘权息数据的证券有效，对指数、基金等无效。
    """
```

#### WMA

```python
def WMA(n: int = 22) -> Indicator:
    ...
```

#### WMA

```python
def WMA(n: IndParam) -> Indicator:
    ...
```

#### WMA

```python
def WMA(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### WMA

```python
def WMA(data: Indicator, n: IndParam) -> Indicator:
    ...
```

#### WMA

```python
def WMA(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### WMA

```python
def WMA(data: Indicator, n: Indicator) -> Indicator:
    ...
```

#### WMA

```python
def WMA(data: Indicator, n: int = 22) -> Indicator:
    """
    WMA([data, n=22])
    
        加权移动平均，算法:Yn=(1*X1+2*X2+...+n*Xn)/(1+2+...+n)
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### WMA

```python
def WMA(data: Indicator, n: int = 22) -> Indicator:
    """
    WMA([data, n=22])
    
        加权移动平均，算法:Yn=(1*X1+2*X2+...+n*Xn)/(1+2+...+n)
    
        :param Indicator data: 输入数据
        :param int|Indicator|IndParam n: 时间窗口
        :rtype: Indicator
    """
```

#### YEAR

```python
def YEAR() -> Indicator:
    ...
```

#### YEAR

```python
def YEAR(arg0: KData) -> Indicator:
    """
    YEAR([data])
    
        取得该周期的年份。
    
        :param data: 输入数据 KData
        :rtype: Indicator
    """
```

#### ZHBOND10

```python
def ZHBOND10(default_val: float = 0.4) -> Indicator:
    ...
```

#### ZHBOND10

```python
def ZHBOND10(data: DatetimeList, default_val: float = 0.4) -> Indicator:
    ...
```

#### ZHBOND10

```python
def ZHBOND10(data: KData, default_val: float = 0.4) -> Indicator:
    ...
```

#### ZHBOND10

```python
def ZHBOND10(data: Indicator, default_val: float = 0.4) -> Indicator:
    """
    ZHBOND10([data, defaut_val])
    
        获取10年期中国国债收益率
    
        :param DatetimeList|KDate|Indicator data: 输入的日期参考，优先使用上下文中的日期
        :param float default_val: 如果输入的日期早于已有国债数据的最早记录，则使用此默认值
    """
```

#### ZHBOND10

```python
def ZHBOND10(data: Indicator, default_val: float = 0.4) -> Indicator:
    """
    ZHBOND10([data, defaut_val])
    
        获取10年期中国国债收益率
    
        :param DatetimeList|KDate|Indicator data: 输入的日期参考，优先使用上下文中的日期
        :param float default_val: 如果输入的日期早于已有国债数据的最早记录，则使用此默认值
    """
```

#### ZONGGUBEN

```python
def ZONGGUBEN() -> Indicator:
    ...
```

#### ZONGGUBEN

```python
def ZONGGUBEN(arg0: KData) -> Indicator:
    """
    ZONGGUBEN(kdata)
    
       获取总股本（单位：万股）
    
       :param KData kdata: k线数据
       :rtype: Indicator
    """
```

#### ZSCORE

```python
def ZSCORE(out_extreme: bool = False, nsigma: float = 3.0, recursive: bool = False) -> Indicator:
    ...
```

#### ZSCORE

```python
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
```

#### ZSCORE

```python
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
```

