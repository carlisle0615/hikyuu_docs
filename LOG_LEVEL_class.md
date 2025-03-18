## LOG_LEVEL

```python
class LOG_LEVEL:
    """
    Members:
    
      DEBUG
    
      TRACE
    
      INFO
    
      WARN
    
      ERROR
    
      FATAL
    
      OFF
    """
    DEBUG: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.DEBUG: 1>
    ERROR: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.ERROR: 4>
    FATAL: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.FATAL: 5>
    INFO: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.INFO: 2>
    OFF: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.OFF: 6>
    TRACE: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.TRACE: 0>
    WARN: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.WARN: 3>
    __members__: typing.ClassVar[dict[str, LOG_LEVEL]]  # value = {'DEBUG': <LOG_LEVEL.DEBUG: 1>, 'TRACE': <LOG_LEVEL.TRACE: 0>, 'INFO': <LOG_LEVEL.INFO: 2>, 'WARN': <LOG_LEVEL.WARN: 3>, 'ERROR': <LOG_LEVEL.ERROR: 4>, 'FATAL': <LOG_LEVEL.FATAL: 5>, 'OFF': <LOG_LEVEL.OFF: 6>}
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

## 相关方法

### 与LOG_LEVEL相关的方法

#### get_log_level

```python
def get_log_level() -> LOG_LEVEL:
    """
    获取当前日志级别
    """
```

