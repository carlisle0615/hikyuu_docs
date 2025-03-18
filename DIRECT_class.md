## DIRECT

```python
class DIRECT:
    """
    Members:
    
      BUY
    
      SELL
    
      AUCTION
    """
    AUCTION: typing.ClassVar[DIRECT]  # value = <DIRECT.AUCTION: 2>
    BUY: typing.ClassVar[DIRECT]  # value = <DIRECT.BUY: 0>
    SELL: typing.ClassVar[DIRECT]  # value = <DIRECT.SELL: 1>
    __members__: typing.ClassVar[dict[str, DIRECT]]  # value = {'BUY': <DIRECT.BUY: 0>, 'SELL': <DIRECT.SELL: 1>, 'AUCTION': <DIRECT.AUCTION: 2>}
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

