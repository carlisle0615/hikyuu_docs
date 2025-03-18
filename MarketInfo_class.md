## MarketInfo

```python
class MarketInfo:
    """
    市场信息记录
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: Datetime, arg5: TimeDelta, arg6: TimeDelta, arg7: TimeDelta, arg8: TimeDelta) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def close_time1(self) -> TimeDelta:
        """
        闭市时间1
        """
    @property
    def close_time2(self) -> TimeDelta:
        """
        闭市时间2
        """
    @property
    def code(self) -> str:
        """
        该市场对应的主要指数代码，用于获取交易日历
        """
    @property
    def description(self) -> str:
        """
        描述说明
        """
    @property
    def last_datetime(self) -> Datetime:
        """
        该市场K线数据最后交易日期
        """
    @property
    def market(self) -> str:
        """
        市场标识（如：沪市“SH”, 深市“SZ”）
        """
    @property
    def name(self) -> str:
        """
        市场全称
        """
    @property
    def open_time1(self) -> TimeDelta:
        """
        开市时间1
        """
    @property
    def open_time2(self) -> TimeDelta:
        """
        开市时间2
        """
```

