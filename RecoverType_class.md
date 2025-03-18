## RecoverType

```python
    class RecoverType:
        """
        Members:
        
          NO_RECOVER : 不复权
        
          FORWARD : 前向复权
        
          BACKWARD : 后向复权
        
          EQUAL_FORWARD : 等比前向复权
        
          EQUAL_BACKWARD : 等比后向复权
        
          INVALID : 无效类型
        """
        BACKWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.BACKWARD: 2>
        EQUAL_BACKWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.EQUAL_BACKWARD: 4>
        EQUAL_FORWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.EQUAL_FORWARD: 3>
        FORWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.FORWARD: 1>
        INVALID: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.INVALID: 5>
        NO_RECOVER: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.NO_RECOVER: 0>
        __members__: typing.ClassVar[dict[str, Query.RecoverType]]  # value = {'NO_RECOVER': <RecoverType.NO_RECOVER: 0>, 'FORWARD': <RecoverType.FORWARD: 1>, 'BACKWARD': <RecoverType.BACKWARD: 2>, 'EQUAL_FORWARD': <RecoverType.EQUAL_FORWARD: 3>, 'EQUAL_BACKWARD': <RecoverType.EQUAL_BACKWARD: 4>, 'INVALID': <RecoverType.INVALID: 5>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    BACKWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.BACKWARD: 2>
    DATE: typing.ClassVar[Query.QueryType]  # value = <QueryType.DATE: 1>
    DAY: typing.ClassVar[str] = 'DAY'
    EQUAL_BACKWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.EQUAL_BACKWARD: 4>
    EQUAL_FORWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.EQUAL_FORWARD: 3>
    FORWARD: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.FORWARD: 1>
    HALFYEAR: typing.ClassVar[str] = 'HALFYEAR'
    HOUR12: typing.ClassVar[str] = 'HOUR12'
    HOUR2: typing.ClassVar[str] = 'HOUR2'
    HOUR4: typing.ClassVar[str] = 'HOUR4'
    HOUR6: typing.ClassVar[str] = 'HOUR6'
    INDEX: typing.ClassVar[Query.QueryType]  # value = <QueryType.INDEX: 0>
    INVALID: typing.ClassVar[Query.QueryType]  # value = <QueryType.INVALID: 2>
    MIN: typing.ClassVar[str] = 'MIN'
    MIN15: typing.ClassVar[str] = 'MIN15'
    MIN3: typing.ClassVar[str] = 'MIN3'
    MIN30: typing.ClassVar[str] = 'MIN30'
    MIN5: typing.ClassVar[str] = 'MIN5'
    MIN60: typing.ClassVar[str] = 'MIN60'
    MONTH: typing.ClassVar[str] = 'MONTH'
    NO_RECOVER: typing.ClassVar[Query.RecoverType]  # value = <RecoverType.NO_RECOVER: 0>
    QUARTER: typing.ClassVar[str] = 'QUARTER'
    WEEK: typing.ClassVar[str] = 'WEEK'
    YEAR: typing.ClassVar[str] = 'YEAR'
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def get_all_ktype() -> list[str]:
        """
        获取所有KType
        """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self, start = 0, end = None, ktype = 'DAY', recover_type = ...):
        """
        
                构建按索引 [start, end) 方式获取K线数据条件。start，end应同为 int 或 同为 Datetime 类型。
        
                :param int|Datetime start: 起始索引位置或起始日期
                :param int|Datetime end: 结束索引位置或结束日期
                :param Query.KType ktype: K线数据类型（如日线、分钟线等）
                :param Query.RecoverType recover_type: 复权类型
                :return: 查询条件
                :rtype: KQuery
                
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def get_ktype_in_min(self: str) -> int:
        """
        获取ktype对应的分钟数
        """
    @property
    def end(self) -> int:
        """
        结束索引，当按日期查询方式创建时无效
        """
    @property
    def end_datetime(self) -> Datetime:
        """
        结束日期，当按索引查询方式创建时无效
        """
    @property
    def ktype(self) -> str:
        """
        查询的K线类型
        """
    @property
    def query_type(self) -> ...:
        """
        查询方式
        """
    @property
    def recover_type(self) -> ...:
        """
        复权类别
        """
    @property
    def start(self) -> int:
        """
        起始索引，当按日期查询方式创建时无效
        """
    @property
    def start_datetime(self) -> Datetime:
        """
        起始日期，当按索引查询方式创建时无效
        """
```

