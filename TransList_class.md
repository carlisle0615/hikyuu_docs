## TransList

```python
class TransList:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def to_df(kdata):
        """
        转化为pandas的DataFrame
        """
    @staticmethod
    def to_np(data):
        """
        转化为numpy结构数组
        """
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: ...) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: TransList) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> TransList:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: int) -> ...:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: TransList) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None:
        ...
    def __iter__(self) -> typing.Iterator[...]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: TransList) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: ...) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TransList) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: ...) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: ...) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: TransList) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: int, x: ...) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> ...:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: int) -> ...:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: ...) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
```

