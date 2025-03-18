## TimeDelta

```python
class TimeDelta:
    """
    时间时长，用于时间计算。可通过以下方式构建：
    
        - 通过 datetime.timedelta 构建。TimdeDelta(timedelta实例)
        - TimeDelta(days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0)
    
            - -99999999 <= days <= 99999999
            - -100000 <= hours <= 100000
            - -100000 <= minutes <= 100000
            - -8639900 <= seconds <= 8639900
            - -86399000000 <= milliseconds <= 86399000000
            - -86399000000 <= microseconds <= 86399000000
    
        以上参数限制，主要为防止求总微秒数时可能出现溢出的情况。如只使用一个参数不希望存在上述限制时，可使用快捷函数：
        Days, Hours, Minutes, Seconds, Milliseconds, Microseconds
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def max() -> TimeDelta:
        """
        max()
        
            支持的最大时长
        
            :return: TimeDelta(99999999, 23, 59, 59, 999, 999)
        """
    @staticmethod
    def max_ticks() -> int:
        """
        max_ticks()
        
            支持的最大 ticks （即微秒数）
        
            :rtype: int
        """
    @staticmethod
    def min() -> TimeDelta:
        """
        min()
        
            支持的最小时长
        
            :return: TimeDelta(-99999999, 0, 0, 0, 0, 0)
        """
    @staticmethod
    def min_ticks() -> int:
        """
        min_ticks()
        
            支持的最小 ticks （即微秒数）
        
            :rtype: int
        """
    @staticmethod
    def resolution() -> TimeDelta:
        """
        resolution()
        
            支持的最小精度
                
            :return: TimeDelta(0, 0, 0, 0, 0, 1)
        """
    def __abs__(self) -> TimeDelta:
        ...
    def __add__(self, td):
        """
        可和 TimeDelta, datetime.timedelta, Datetime执行相加操作
        """
    def __eq__(self, arg0: TimeDelta) -> bool:
        ...
    def __floordiv__(self, arg0: float) -> TimeDelta:
        ...
    def __ge__(self, arg0: TimeDelta) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    def __gt__(self, arg0: TimeDelta) -> bool:
        ...
    def __hash__(self):
        ...
    def __init__(self, *args, **kwargs):
        """
        
            可通过以下方式构建：
        
            - 通过 datetime.timedelta 构建。TimdeDelta(timedelta实例)
            - TimeDelta(days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0)
        
                - -99999999 <= days <= 99999999
                - -100000 <= hours <= 100000
                - -100000 <= minutes <= 100000
                - -8639900 <= seconds <= 8639900
                - -86399000000 <= milliseconds <= 86399000000
                - -86399000000 <= microseconds <= 86399000000
            
        """
    def __le__(self, arg0: TimeDelta) -> bool:
        ...
    def __lt__(self, arg0: TimeDelta) -> bool:
        ...
    def __mod__(self, arg0: TimeDelta) -> TimeDelta:
        ...
    def __mul__(self, arg0: float) -> TimeDelta:
        ...
    def __ne__(self, arg0: TimeDelta) -> bool:
        ...
    def __neg__(self) -> TimeDelta:
        ...
    def __pos__(self) -> TimeDelta:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: float) -> TimeDelta:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __sub__(self, td):
        """
        可减去TimeDelta, datetime.timedelta
        """
    @typing.overload
    def __truediv__(self, arg0: TimeDelta) -> float:
        ...
    @typing.overload
    def __truediv__(self, arg0: float) -> TimeDelta:
        ...
    def from_ticks(self: int) -> TimeDelta:
        """
        from_ticks(ticks)
        
            使用 ticks（即微秒数） 值创建
        
            :param int ticks: 微秒数
            :rtype: TimeDelta
        """
    def isNegative(self) -> bool:
        """
        isNegative(self)
        
            是否为负时长
        
            :rtype: bool
        """
    def timedelta(self):
        """
         转化为 datetime.timedelta 
        """
    def total_days(self) -> float:
        """
        total_days(self)
        
            获取带小数的总天数
        
            :rtype: float
        """
    def total_hours(self) -> float:
        """
        total_hours(self)
        
            获取带小数的总小时数
        
            :rtype: float
        """
    def total_milliseconds(self) -> float:
        """
        total_milliseconds(self)
        
            获取带小数的总毫秒数
        
            :rtype: float
        """
    def total_minutes(self) -> float:
        """
        total_minutes(self)
        
            获取带小数的总分钟数
        
            :rtype: float
        """
    def total_seconds(self) -> float:
        """
        total_seconds(self)
        
            获取带小数的总秒数
        
            :rtype: float
        """
    @property
    def days(self) -> int:
        """
        天数 [-99999999, 99999999]
        """
    @property
    def hours(self) -> int:
        """
        小时数 [0, 23]
        """
    @property
    def microseconds(self) -> int:
        """
        微秒数 [0, 999]
        """
    @property
    def milliseconds(self) -> int:
        """
        毫秒数 [0, 999]
        """
    @property
    def minutes(self) -> int:
        """
        分钟数 [0, 59]
        """
    @property
    def seconds(self) -> int:
        """
        秒数 [0, 59]
        """
    @property
    def ticks(self) -> int:
        """
        同总微秒数
        """
```

## 相关方法

### 与TimeDelta相关的方法

#### Days

```python
def Days(arg0: int) -> TimeDelta:
    """
    Days(days)
    
          TimeDelta 快捷创建函数
    
          :param int days: 天数 [-99999999, 99999999]
          :rtype: TimeDelta
    """
```

#### Hours

```python
def Hours(arg0: int) -> TimeDelta:
    """
    Hours(hours)
    
          TimeDelta 快捷创建函数
    
          :param int hours: 小时数
          :rtype: TimeDelta
    """
```

#### Microseconds

```python
def Microseconds(arg0: int) -> TimeDelta:
    """
    Microseconds(microsecs)
    
          TimeDelta 快捷创建函数
    
          :param int microsecs: 微秒数
          :rtype: TimeDelta
    """
```

#### Milliseconds

```python
def Milliseconds(arg0: int) -> TimeDelta:
    """
    Milliseconds(milliseconds)
    
          TimeDelta 快捷创建函数
    
          :param int milliseconds: 毫秒数
          :rtype: TimeDelta
    """
```

#### Minutes

```python
def Minutes(arg0: int) -> TimeDelta:
    """
    Minutes(mins)
    
          TimeDelta 快捷创建函数
    
          :param int mins: 分钟数
          :rtype: TimeDelta
    """
```

#### Seconds

```python
def Seconds(arg0: int) -> TimeDelta:
    """
    Seconds(secs)
    
          TimeDelta 快捷创建函数
    
          :param int secs: 秒数
          :rtype: TimeDelta
    """
```

