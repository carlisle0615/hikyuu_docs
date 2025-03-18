## KDataDriver

```python
class KDataDriver:
    """
    K线数据驱动基类
        
      子类接口:
        - _init(self)
        - getCount(self, market, code, ktype)
        - getKRecord(self, market, code, pos, ktype)
        - _loadKDate(self, market, code, ktype, startix, endix)
        - _getIndexRangeByDate(self, market, code, query)
        - _getTimeLineList(self, market, code, query)
        - _getTransList(self, market, code, query)
      
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def _init(self) -> bool:
        """
        【子类接口】初始化驱动
        """
    def canParallelLoad(self) -> bool:
        ...
    def clone(self) -> KDataDriver:
        ...
    def getCount(self, market: str, code: str, ktype: str) -> int:
        """
        【子类接口】获取K线记录数量
            
            :param str markt: 市场简称
            :param str code: 证券代码
            :param Query.KType ktype: K线类型
            :rtype int
        """
    def get_param(self, arg0: str) -> any:
        """
        获取指定参数的值
        """
    def have_param(self, arg0: str) -> bool:
        """
        指定参数是否存在
        """
    def isIndexFirst(self) -> bool:
        ...
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        设置参数
        """
    @property
    def name(self) -> str:
        """
        驱动名称
        """
```

