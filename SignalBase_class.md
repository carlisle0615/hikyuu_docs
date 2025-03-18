## SignalBase

```python
class SignalBase:
    """
    信号指示器基类
        信号指示器负责产生买入、卖出信号。
    
    公共参数：
    
        - alternate (bool|True) ：买入和卖出信号是否交替出现。单线型的信号通常通过拐点、斜率等判断信号的产生，此种情况下可能出现连续出现买入信号或连续出现卖出信号的情况，此时可通过该参数控制买入、卖出信号是否交替出现。而双线交叉型的信号通常本身买入和卖出已经是交替出现，此时该参数无效。
    
    自定义的信号指示器接口：
    
        - _calculate : 【必须】子类计算接口
        - _clone : 【必须】克隆接口
        - _reset : 【可选】重载私有变量
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def plot(sg, new = True, axes = None, style = 1, kdata = None):
        """
        绘制买入/卖出信号
        
            :param SignalBase sg: 信号指示器
            :param new: 仅在未指定axes的情况下生效，当为True时，创建新的窗口对象并在其中进行绘制
            :param axes: 指定在那个轴对象中进行绘制
            :param style: 1 | 2 信号箭头绘制样式
            :param KData kdata: 指定的KData（即信号发生器的交易对象），
                               如该值为None，则认为该信号发生器已经指定了交易对象，
                               否则，使用该参数作为交易对象
            
        """
    @typing.overload
    def __add__(self, arg0: SignalBase) -> SignalBase:
        ...
    @typing.overload
    def __add__(self, arg0: float) -> SignalBase:
        ...
    def __and__(self, arg0: SignalBase) -> SignalBase:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: SignalBase) -> None:
        ...
    @typing.overload
    def __mul__(self, arg0: SignalBase) -> SignalBase:
        ...
    @typing.overload
    def __mul__(self, arg0: float) -> SignalBase:
        ...
    def __or__(self, arg0: SignalBase) -> SignalBase:
        ...
    def __radd__(self, arg0: float) -> SignalBase:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: float) -> SignalBase:
        ...
    def __rsub__(self, arg0: float) -> SignalBase:
        ...
    def __rtruediv__(self, arg0: float) -> SignalBase:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def __sub__(self, arg0: SignalBase) -> SignalBase:
        ...
    @typing.overload
    def __sub__(self, arg0: float) -> SignalBase:
        ...
    @typing.overload
    def __truediv__(self, arg0: SignalBase) -> SignalBase:
        ...
    @typing.overload
    def __truediv__(self, arg0: float) -> SignalBase:
        ...
    def _add_buy_signal(self, datetime: Datetime, value: float = 1.0) -> None:
        """
        _add_buy_signal(self, datetime)
        
            加入买入信号，在_calculate中调用
        
            :param Datetime datetime: 指示买入的日期
        """
    def _add_sell_signal(self, datetime: Datetime, value: float = -1.0) -> None:
        """
        _add_sell_signal(self, datetime)
        
            加入卖出信号，在_calculate中调用
        
            :param Datetime datetime: 指示卖出的日期
        """
    def _add_signal(self, datetime: Datetime, value: float) -> None:
        ...
    def _calculate(self, arg0: KData) -> None:
        """
        _calculate(self, kdata)
              
            【重载接口】子类计算接口
        """
    def _reset(self) -> None:
        """
        【重载接口】子类复位接口，复位内部私有变量
        """
    def clone(self) -> SignalBase:
        """
        克隆操作
        """
    def get_buy_signal(self) -> DatetimeList:
        """
        get_buy_signal(self)
        
            获取所有买入指示日期列表
            
            :rtype: DatetimeList
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_sell_signal(self) -> DatetimeList:
        """
        get_sell_signal(self)
        
            获取所有卖出指示日期列表
        
            :rtype: DatetimeList
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def next_time_should_buy(self) -> bool:
        """
        next_time_should_byu(self)
        
            下一时刻是否可以买入，相当于最后时刻是否指示买入
        """
    def next_time_should_sell(self) -> bool:
        """
        next_time_should_sell(self)
              
            下一时刻是否可以卖出，相当于最后时刻是否指示卖出
        """
    def reset(self) -> None:
        """
        复位操作
        """
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        set_param(self, name, value)
        
            设置参数
        
            :param str name: 参数名称
            :param value: 参数值
            :raises logic_error: Unsupported type! 不支持的参数类型
        """
    def should_buy(self, arg0: Datetime) -> bool:
        """
        should_buy(self, datetime)
        
            指定时刻是否可以买入
        
            :param Datetime datetime: 指定时刻
            :rtype: bool
        """
    def should_sell(self, arg0: Datetime) -> bool:
        """
        should_sell(self, datetime)
        
            指定时刻是否可以卖出
        
            :param Datetime datetime: 指定时刻
            :rtype: bool
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
    def to(self) -> KData:
        """
        设置或获取交易对象
        """
    @to.setter
    def to(self, arg1: KData) -> None:
        ...
```

## 相关方法

### 与SignalBase相关的方法

#### SG_Add

```python
def SG_Add(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
```

#### SG_Add

```python
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
```

#### SG_Add

```python
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
```

#### SG_Add

```python
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
```

#### SG_AllwaysBuy

```python
def SG_AllwaysBuy() -> SignalBase:
    """
    SG_AllwaysBuy()
        
        一个特殊的SG，持续每天发出买入信号，通常配合 PF 使用
    """
```

#### SG_And

```python
def SG_And(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
```

#### SG_And

```python
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
```

#### SG_And

```python
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
```

#### SG_And

```python
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

#### SG_Buy

```python
def SG_Buy(ind: Indicator) -> SignalBase:
    """
    SG_Buy(ind)
        
        生成单边买入信号
    
        :param Indicator ind: 输入指标
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

#### SG_Cycle

```python
def SG_Cycle() -> SignalBase:
    """
    SG_Cycle()
        
        一个特殊的SG，配合PF使用，以 PF 调仓周期为买入信号
    """
```

#### SG_Div

```python
def SG_Div(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
```

#### SG_Div

```python
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
```

#### SG_Div

```python
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
```

#### SG_Div

```python
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

#### SG_Mul

```python
def SG_Mul(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
```

#### SG_Mul

```python
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
```

#### SG_Mul

```python
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
```

#### SG_Mul

```python
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

#### SG_Or

```python
def SG_Or(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
```

#### SG_Or

```python
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
```

#### SG_Or

```python
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
```

#### SG_Or

```python
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
```

#### SG_Sell

```python
def SG_Sell(ind: Indicator) -> SignalBase:
    """
    SG_Sell(ind)
        
        生成单边卖出信号
    
        :param Indicator ind: 输入指标
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

#### SG_Sub

```python
def SG_Sub(sg_list: typing.Sequence, alternate: bool) -> SignalBase:
    ...
```

#### SG_Sub

```python
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
```

#### SG_Sub

```python
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
```

#### SG_Sub

```python
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
```

