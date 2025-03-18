## Datetime

```python
class Datetime:
    """
    日期时间类（精确到微秒），通过以下方式构建：
        
        - 通过字符串：Datetime("2010-1-1 10:00:00")、Datetime("2001-1-1")、
                     Datetime("20010101")、Datetime("20010101T232359)
        - 通过 Python 的date：Datetime(date(2010,1,1))
        - 通过 Python 的datetime：Datetime(datetime(2010,1,1,10)
        - 通过 YYYYMMDDHHMMss 或 YYYYMMDDHHMM 或 YYYYMMDD 形式的整数：Datetime(201001011000)、Datetime(20010101)
        - Datetime(year, month, day, hour=0, minute=0, second=0, millisecond=0, microsecond=0)
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_hex(arg0: int) -> Datetime:
        """
        兼容oracle用后7个字节表示的datetime
        """
    @staticmethod
    def max() -> Datetime:
        """
        获取支持的最大日期, Datetime(9999, 12, 31)
        """
    @staticmethod
    def min() -> Datetime:
        """
        获取支持的最小日期, Datetime(1400, 1, 1)
        """
    @staticmethod
    def now() -> Datetime:
        """
        获取系统当前日期时间
        """
    @staticmethod
    def today() -> Datetime:
        """
        获取当前的日期
        """
    def __add__(self, td):
        """
        加上指定时长，时长对象可为 TimeDelta 或 datetime.timedelta 类型
        
            :param TimeDelta td: 时长
            :rtype: Datetime
            
        """
    def __eq__(self, arg0: Datetime) -> bool:
        ...
    def __ge__(self, arg0: Datetime) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    def __gt__(self, arg0: Datetime) -> bool:
        ...
    def __hash__(self):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Datetime) -> None:
        ...
    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0, millisecond: int = 0, microsecond: int = 0) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Any) -> None:
        ...
    def __le__(self, arg0: Datetime) -> bool:
        ...
    def __lt__(self, arg0: Datetime) -> bool:
        ...
    def __ne__(self, arg0: Datetime) -> bool:
        ...
    def __radd__(self, td):
        """
        加上指定时长，时长对象可为 TimeDelta 或 datetime.timedelta 类型
        
            :param TimeDelta td: 时长
            :rtype: Datetime
            
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __sub__(self, td):
        """
        减去指定的时长, 时长对象可为 TimeDelta 或 datetime.timedelta 类型
        
            :param TimeDelta td: 指定时长
            :rtype: Datetime
            
        """
    def date(self):
        """
        转化生成 python 的 date
        """
    def date_of_week(self, arg0: int) -> Datetime:
        """
            返回指定的本周中第几天的日期，周日为0天，周六为第6天
        
            :param int day: 指明本周的第几天，如小于则认为为第0天，如大于6则认为为第6天
        """
    def datetime(self):
        """
        转化生成 python 的 datetime
        """
    def day_of_week(self) -> int:
        """
        返回是一周中的第几天，周日为0，周一为1
        """
    def day_of_year(self) -> int:
        """
        返回一年中的第几天，1月1日为一年中的第1天
        """
    def endOfYear(self) -> Datetime:
        """
        返回年度结束日期
        """
    def end_of_day(self) -> Datetime:
        """
        返回当日 23点59分59秒
        """
    def end_of_halfyear(self) -> Datetime:
        """
        返回半年度结束日期
        """
    def end_of_month(self) -> Datetime:
        """
        返回月末最后一天日期
        """
    def end_of_quarter(self) -> Datetime:
        """
        返回季度结束日期
        """
    def end_of_week(self) -> Datetime:
        """
        返回周结束日期（周日）
        """
    def is_null(self) -> bool:
        """
        是否是Null值，等于 Datetime() 直接创建的对象
        """
    def next_day(self) -> Datetime:
        """
        返回下一自然日
        """
    def next_halfyear(self) -> Datetime:
        """
        返回下一半年度首日日期
        """
    def next_month(self) -> Datetime:
        """
        返回下月首日日期
        """
    def next_quarter(self) -> Datetime:
        """
        返回下一季度首日日期
        """
    def next_week(self) -> Datetime:
        """
        返回下周周一日期
        """
    def next_year(self) -> Datetime:
        """
        返回下一年度首日日期
        """
    def pre_day(self) -> Datetime:
        """
        返回前一自然日日期
        """
    def pre_halfyear(self) -> Datetime:
        """
        返回上一半年度首日日期
        """
    def pre_month(self) -> Datetime:
        """
        返回上月首日日期
        """
    def pre_quarter(self) -> Datetime:
        """
        返回上一季度首日日期
        """
    def pre_week(self) -> Datetime:
        """
        返回上周周一日期
        """
    def pre_year(self) -> Datetime:
        """
        返回上一年度首日日期
        """
    def start_of_day(self) -> Datetime:
        """
        返回当天 0点0分0秒
        """
    def start_of_halfyear(self) -> Datetime:
        """
        返回半年度起始日期
        """
    def start_of_month(self) -> Datetime:
        """
        返回月度起始日期
        """
    def start_of_quarter(self) -> Datetime:
        """
        返回季度起始日期
        """
    def start_of_week(self) -> Datetime:
        """
        返回周起始日期（周一）
        """
    def start_of_year(self) -> Datetime:
        """
        返回年度起始日期
        """
    @property
    def day(self) -> int:
        """
        日
        """
    @property
    def hex(self) -> int:
        """
        返回用后7个字节表示世纪、世纪年、月、日、时、分、秒的64位整数
        """
    @property
    def hour(self) -> int:
        """
        时
        """
    @property
    def microsecond(self) -> int:
        """
        微秒
        """
    @property
    def millisecond(self) -> int:
        """
        毫秒
        """
    @property
    def minute(self) -> int:
        """
        分
        """
    @property
    def month(self) -> int:
        """
        月
        """
    @property
    def number(self) -> int:
        """
        返回显示如 YYYYMMDDhhmm 的数字
        """
    @property
    def second(self) -> int:
        """
        秒
        """
    @property
    def ticks(self) -> int:
        """
        返回距离最小日期过去的微秒数
        """
    @property
    def year(self) -> int:
        """
        年
        """
    @property
    def ym(self) -> int:
        """
        返回显示如 YYYYMM 的数字
        """
    @property
    def ymd(self) -> int:
        """
        返回显示如 YYYYMMDD 的数字
        """
    @property
    def ymdh(self) -> int:
        """
        返回显示如 YYYYMMDDhh 的数字
        """
    @property
    def ymdhm(self) -> int:
        """
        返回显示如 YYYYMMDDhhmm 的数字
        """
    @property
    def ymdhms(self) -> int:
        """
        返回显示如 YYYYMMDDhhmms 的数字
        """
```

## 相关方法

#### get_date_range

```python
def get_date_range(start: Datetime, end: Datetime) -> DatetimeList:
    """
    get_date_range(start, end)
    
        获取指定 [start, end) 日期时间范围的自然日日历日期列表，仅支持到日
        为防止内存占用过大，end如果超出系统明日日期，则强制为系统明日日期。
        
        :param Datetime start: 起始日期
        :param Datetime end: 结束日期
        :rtype: DatetimeList
    """
```

