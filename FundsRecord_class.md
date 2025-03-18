## FundsRecord

```python
class FundsRecord:
    """
    当前资产情况记录
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __add__(self, arg0: FundsRecord) -> FundsRecord:
        ...
    def __getstate__(self) -> tuple:
        ...
    def __iadd__(self, arg0: FundsRecord) -> FundsRecord:
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
    def base_asset(self) -> float:
        """
        当前投入的资产价值（float）
        """
    @base_asset.setter
    def base_asset(self, arg0: float) -> None:
        ...
    @property
    def base_cash(self) -> float:
        """
        当前投入本金（float）
        """
    @base_cash.setter
    def base_cash(self, arg0: float) -> None:
        ...
    @property
    def borrow_asset(self) -> float:
        """
        当前借入证券资产价值（float）
        """
    @borrow_asset.setter
    def borrow_asset(self, arg0: float) -> None:
        ...
    @property
    def borrow_cash(self) -> float:
        """
        当前借入的资金（float），即负债
        """
    @borrow_cash.setter
    def borrow_cash(self, arg0: float) -> None:
        ...
    @property
    def cash(self) -> float:
        """
        当前现金（float）
        """
    @cash.setter
    def cash(self, arg0: float) -> None:
        ...
    @property
    def market_value(self) -> float:
        """
        当前多头市值（float）
        """
    @market_value.setter
    def market_value(self, arg0: float) -> None:
        ...
    @property
    def net_assets(self) -> float:
        """
        净资产
        """
    @property
    def profit(self) -> float:
        """
        当前收益
        """
    @property
    def short_market_value(self) -> float:
        """
        当前空头仓位市值（float）
        """
    @short_market_value.setter
    def short_market_value(self, arg0: float) -> None:
        ...
    @property
    def total_assets(self) -> float:
        """
        总资产
        """
    @property
    def total_base(self) -> float:
        """
        投入本值资产
        """
    @property
    def total_borrow(self) -> float:
        """
        总负债
        """
```

