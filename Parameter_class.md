## Parameter

```python
class Parameter:
    """
    参数类，供需要命名参数设定的类使用，类似于 dict
    """
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __contains__(self, arg0: str) -> bool:
        ...
    def __eq__(self, arg0: Parameter) -> bool:
        ...
    def __getitem__(self, arg0: str) -> any:
        ...
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self):
        ...
    def __lt__(self, arg0: Parameter) -> bool:
        ...
    def __ne__(self, arg0: Parameter) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setitem__(self, arg0: str, arg1: any) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def get(self, arg0: str) -> any:
        ...
    def get_name_list(self) -> list[str]:
        """
        Get all the parameter names list
        """
    def get_name_value_list(self) -> str:
        """
        Return a string, like 'name1=val1,name2=val2,...'
        """
    def have(self, arg0: str) -> bool:
        """
        Return True if there is a parameter for the specified name.
        """
    def items(self):
        ...
    def keys(self):
        ...
    def set(self, arg0: str, arg1: any) -> None:
        ...
    def to_dict(self):
        """
        转化为 Python dict 对象
        """
    def type(self, arg0: str) -> str:
        """
        Get the type name of the specified parameter, return 'string' | 'int' | 'double' | 'bool' | 'Stock' | 'KQuery' | 'KData' | 'PriceList' | 'DatetimeList'
        """
```

