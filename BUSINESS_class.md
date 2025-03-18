## BUSINESS

```python
class BUSINESS:
    """
    Members:
    
      INIT
    
      BUY
    
      SELL
    
      BUY_SHORT
    
      SELL_SHORT
    
      GIFT
    
      BONUS
    
      CHECKIN
    
      CHECKOUT
    
      CHECKIN_STOCK
    
      CHECKOUT_STOCK
    
      BORROW_CASH
    
      RETURN_CASH
    
      BORROW_STOCK
    
      RETURN_STOCK
    
      INVALID
    """
    BONUS: typing.ClassVar[BUSINESS]  # value = <BUSINESS.BONUS: 4>
    BORROW_CASH: typing.ClassVar[BUSINESS]  # value = <BUSINESS.BORROW_CASH: 9>
    BORROW_STOCK: typing.ClassVar[BUSINESS]  # value = <BUSINESS.BORROW_STOCK: 11>
    BUY: typing.ClassVar[BUSINESS]  # value = <BUSINESS.BUY: 1>
    BUY_SHORT: typing.ClassVar[BUSINESS]  # value = <BUSINESS.BUY_SHORT: 14>
    CHECKIN: typing.ClassVar[BUSINESS]  # value = <BUSINESS.CHECKIN: 5>
    CHECKIN_STOCK: typing.ClassVar[BUSINESS]  # value = <BUSINESS.CHECKIN_STOCK: 7>
    CHECKOUT: typing.ClassVar[BUSINESS]  # value = <BUSINESS.CHECKOUT: 6>
    CHECKOUT_STOCK: typing.ClassVar[BUSINESS]  # value = <BUSINESS.CHECKOUT_STOCK: 8>
    GIFT: typing.ClassVar[BUSINESS]  # value = <BUSINESS.GIFT: 3>
    INIT: typing.ClassVar[BUSINESS]  # value = <BUSINESS.INIT: 0>
    INVALID: typing.ClassVar[BUSINESS]  # value = <BUSINESS.INVALID: 15>
    RETURN_CASH: typing.ClassVar[BUSINESS]  # value = <BUSINESS.RETURN_CASH: 10>
    RETURN_STOCK: typing.ClassVar[BUSINESS]  # value = <BUSINESS.RETURN_STOCK: 12>
    SELL: typing.ClassVar[BUSINESS]  # value = <BUSINESS.SELL: 2>
    SELL_SHORT: typing.ClassVar[BUSINESS]  # value = <BUSINESS.SELL_SHORT: 13>
    __members__: typing.ClassVar[dict[str, BUSINESS]]  # value = {'INIT': <BUSINESS.INIT: 0>, 'BUY': <BUSINESS.BUY: 1>, 'SELL': <BUSINESS.SELL: 2>, 'BUY_SHORT': <BUSINESS.BUY_SHORT: 14>, 'SELL_SHORT': <BUSINESS.SELL_SHORT: 13>, 'GIFT': <BUSINESS.GIFT: 3>, 'BONUS': <BUSINESS.BONUS: 4>, 'CHECKIN': <BUSINESS.CHECKIN: 5>, 'CHECKOUT': <BUSINESS.CHECKOUT: 6>, 'CHECKIN_STOCK': <BUSINESS.CHECKIN_STOCK: 7>, 'CHECKOUT_STOCK': <BUSINESS.CHECKOUT_STOCK: 8>, 'BORROW_CASH': <BUSINESS.BORROW_CASH: 9>, 'RETURN_CASH': <BUSINESS.RETURN_CASH: 10>, 'BORROW_STOCK': <BUSINESS.BORROW_STOCK: 11>, 'RETURN_STOCK': <BUSINESS.RETURN_STOCK: 12>, 'INVALID': <BUSINESS.INVALID: 15>}
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

