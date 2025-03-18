## BlockInfoDriver

```python
class BlockInfoDriver:
    """
    板块数据驱动基类
        
        子类接口：
            - _init(self) (必须)
            _ getBlock(self, category, name) （必须）
            _ _getBlockList(self, category=None) （必须）
        
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, arg0: str) -> None:
        """
        初始化
        
            :param str name: 驱动名称
        """
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def _init(self) -> bool:
        """
        【子类接口（必须）】驱动初始化
        """
    def getBlock(self, category: str, name: str) -> Block:
        """
        【子类接口（必须）】获取指定板块
        
            :param str category: 指定的板块分类
            :param str name: 板块名称
        """
    def get_param(self, arg0: str) -> any:
        """
        获取指定参数
        """
    def have_param(self, arg0: str) -> bool:
        """
        指定参数是否存在
        """
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        设置指定参数
        """
    @property
    def name(self) -> str:
        """
        驱动名称
        """
```

