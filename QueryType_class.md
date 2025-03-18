## QueryType

```python
    class QueryType:
        """
        Members:
        
          INDEX : 按索引方式查询
        
          DATE : 按日期方式查询
        
          INVALID : 无效类型
        """
        DATE: typing.ClassVar[Query.QueryType]  # value = <QueryType.DATE: 1>
        INDEX: typing.ClassVar[Query.QueryType]  # value = <QueryType.INDEX: 0>
        INVALID: typing.ClassVar[Query.QueryType]  # value = <QueryType.INVALID: 2>
        __members__: typing.ClassVar[dict[str, Query.QueryType]]  # value = {'INDEX': <QueryType.INDEX: 0>, 'DATE': <QueryType.DATE: 1>, 'INVALID': <QueryType.INVALID: 2>}
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
```

