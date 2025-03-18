## SystemPart

```python
class SystemPart:
    """
    系统关联部件（各自策略）枚举定义，用于修改相关部件参数
    
    Members:
    
      ENVIRONMENT : 外部环境
    
      CONDITION : 系统前提条件
    
      SIGNAL : 信号产生器
    
      STOPLOSS : 止损策略
    
      TAKEPROFIT : 止赢策略
    
      MONEYMANAGER : 资金管理策略
    
      PROFITGOAL : 盈利目标策略
    
      SLIPPAGE : 移滑价差算法
    
      ALLOCATEFUNDS : 资产分配算法
    
      INVALID : 无效系统部件
    
      EV : 外部环境
    
      CN : 系统前提条件
    
      SG : 信号产生器
    
      ST : 止损策略
    
      TP : 止赢策略
    
      MM : 资金管理策略
    
      PG : 盈利目标策略
    
      SP : 移滑价差算法
    
      AF : 资产分配算法
    """
    AF: typing.ClassVar[SystemPart]  # value = <SystemPart.ALLOCATEFUNDS: 8>
    ALLOCATEFUNDS: typing.ClassVar[SystemPart]  # value = <SystemPart.ALLOCATEFUNDS: 8>
    CN: typing.ClassVar[SystemPart]  # value = <SystemPart.CONDITION: 1>
    CONDITION: typing.ClassVar[SystemPart]  # value = <SystemPart.CONDITION: 1>
    ENVIRONMENT: typing.ClassVar[SystemPart]  # value = <SystemPart.ENVIRONMENT: 0>
    EV: typing.ClassVar[SystemPart]  # value = <SystemPart.ENVIRONMENT: 0>
    INVALID: typing.ClassVar[SystemPart]  # value = <SystemPart.INVALID: 10>
    MM: typing.ClassVar[SystemPart]  # value = <SystemPart.MONEYMANAGER: 5>
    MONEYMANAGER: typing.ClassVar[SystemPart]  # value = <SystemPart.MONEYMANAGER: 5>
    PG: typing.ClassVar[SystemPart]  # value = <SystemPart.PROFITGOAL: 6>
    PROFITGOAL: typing.ClassVar[SystemPart]  # value = <SystemPart.PROFITGOAL: 6>
    SG: typing.ClassVar[SystemPart]  # value = <SystemPart.SIGNAL: 2>
    SIGNAL: typing.ClassVar[SystemPart]  # value = <SystemPart.SIGNAL: 2>
    SLIPPAGE: typing.ClassVar[SystemPart]  # value = <SystemPart.SLIPPAGE: 7>
    SP: typing.ClassVar[SystemPart]  # value = <SystemPart.SLIPPAGE: 7>
    ST: typing.ClassVar[SystemPart]  # value = <SystemPart.STOPLOSS: 3>
    STOPLOSS: typing.ClassVar[SystemPart]  # value = <SystemPart.STOPLOSS: 3>
    TAKEPROFIT: typing.ClassVar[SystemPart]  # value = <SystemPart.TAKEPROFIT: 4>
    TP: typing.ClassVar[SystemPart]  # value = <SystemPart.TAKEPROFIT: 4>
    __members__: typing.ClassVar[dict[str, SystemPart]]  # value = {'ENVIRONMENT': <SystemPart.ENVIRONMENT: 0>, 'CONDITION': <SystemPart.CONDITION: 1>, 'SIGNAL': <SystemPart.SIGNAL: 2>, 'STOPLOSS': <SystemPart.STOPLOSS: 3>, 'TAKEPROFIT': <SystemPart.TAKEPROFIT: 4>, 'MONEYMANAGER': <SystemPart.MONEYMANAGER: 5>, 'PROFITGOAL': <SystemPart.PROFITGOAL: 6>, 'SLIPPAGE': <SystemPart.SLIPPAGE: 7>, 'ALLOCATEFUNDS': <SystemPart.ALLOCATEFUNDS: 8>, 'INVALID': <SystemPart.INVALID: 10>, 'EV': <SystemPart.ENVIRONMENT: 0>, 'CN': <SystemPart.CONDITION: 1>, 'SG': <SystemPart.SIGNAL: 2>, 'ST': <SystemPart.STOPLOSS: 3>, 'TP': <SystemPart.TAKEPROFIT: 4>, 'MM': <SystemPart.MONEYMANAGER: 5>, 'PG': <SystemPart.PROFITGOAL: 6>, 'SP': <SystemPart.SLIPPAGE: 7>, 'AF': <SystemPart.ALLOCATEFUNDS: 8>}
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

### 与SystemPart相关的方法

#### get_system_part_enum

```python
def get_system_part_enum(arg0: str) -> SystemPart:
    """
    get_system_part_enum(part_name)
    
         根据系统部件的字符串名称获取相应的枚举值
    
        :param str part_name: 系统部件的字符串名称，参见：:py:func:`getSystemPartName`
        :rtype: System.Part
    """
```

