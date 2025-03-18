## TradeRequest

```python
class TradeRequest:
    """
    交易请求记录。系统内部在实现延迟操作时登记的交易请求信息。暴露该结构的主要目的是用于
    在“delay”模式（延迟到下一个bar开盘时进行交易）的情况下，系统实际已知下一个Bar将要
    进行交易，此时可通过 System.getBuyTradeRequest() 、 System.getSellTradeRequest()
    来获知下一个BAR是否需要买入/卖出。主要用于提醒或打印下一个Bar需要进行操作。对于系统
    本身的运行没有影响。
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def business(self) -> BUSINESS:
        """
        交易业务类型，参见：:py:class:`hikyuu.trade_manage.BUSINESS`
        """
    @business.setter
    def business(self, arg0: BUSINESS) -> None:
        ...
    @property
    def count(self) -> int:
        """
        因操作失败，连续延迟的次数
        """
    @count.setter
    def count(self, arg0: int) -> None:
        ...
    @property
    def datetime(self) -> Datetime:
        """
        发出交易请求的时刻
        """
    @datetime.setter
    def datetime(self, arg0: Datetime) -> None:
        ...
    @property
    def part(self) -> SystemPart:
        """
        发出交易请求的来源，参见：:py:class:`System.Part`
        """
    @part.setter
    def part(self, arg0: SystemPart) -> None:
        ...
    @property
    def stoploss(self) -> float:
        """
        发出交易请求时刻的止损价
        """
    @stoploss.setter
    def stoploss(self, arg0: float) -> None:
        ...
    @property
    def valid(self) -> bool:
        """
        该交易请求记录是否有效（True | False）
        """
    @valid.setter
    def valid(self, arg0: bool) -> None:
        ...
```

