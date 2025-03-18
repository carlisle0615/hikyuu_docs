## Block

```python
class Block:
    """
    板块类，可视为证券的容器
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getitem__(self, arg0: str) -> Stock:
        """
        __getitem__(self, market_code)
        
            :param str market_code: 证券代码
            :return: Stock 实例
        """
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Block) -> None:
        ...
    def __iter__(self) -> typing.Iterator[Stock]:
        ...
    def __len__(self) -> int:
        """
        包含的证券数量
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def add(self, arg0: Stock) -> bool:
        """
        add(self, stock)
        
            加入指定的证券
        
            :param Stock stock: 待加入的证券
            :return: 是否成功加入
            :rtype: bool
        """
    @typing.overload
    def add(self, arg0: str) -> bool:
        """
        add(self, market_code)
        
            根据"市场简称证券代码"加入指定的证券
        
            :param str market_code: 市场简称证券代码
            :return: 是否成功加入
            :rtype: bool
        """
    @typing.overload
    def add(self, arg0: typing.Sequence) -> bool:
        """
        add(self, sequence)
        
            加入定的证券列表
        
            :param sequence stks: 全部由 Stock 组成的序列或全部由字符串市场简称证券代码组成的序列
            :return: True 全部成功 | False 存在失败
        """
    def clear(self) -> None:
        """
        移除包含的所有证券
        """
    def empty(self) -> bool:
        """
        empty(self)
            
            是否为空
        """
    def get_stock_list(self, filter: typing.Any = None) -> list[Stock]:
        """
        get_stock_list(self[, filter=None])
                
            获取证券列表
        
            :param func filter: 输入参数为 stock, 返回 True | False 的过滤函数
        """
    @typing.overload
    def remove(self, arg0: Stock) -> bool:
        """
        remove(self, stock)
        
            移除指定证券
        
            :param Stock stock: 指定的证券
            :return: 是否成功
            :rtype: bool
        """
    @typing.overload
    def remove(self, arg0: str) -> bool:
        """
        remove(market_code)
        
            移除指定证券
        
            :param str market_code: 市场简称证券代码
            :return: True 成功 | False 失败
            :rtype: bool
        """
    @property
    def category(self) -> str:
        """
        板块所属分类
        """
    @category.setter
    def category(self, arg1: str) -> None:
        ...
    @property
    def index_stock(self) -> Stock:
        """
        对应指数
        """
    @index_stock.setter
    def index_stock(self, arg1: Stock) -> None:
        ...
    @property
    def name(self) -> str:
        """
        板块名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
```

## 相关方法

### 与Block相关的方法

#### BLOCKSETNUM

```python
def BLOCKSETNUM(block: Block, query: Query) -> Indicator:
    """
    BLOCKSETNUM(block, query)
        
        横向统计（返回板块股个数）
    
        :param Block block: 待统计的板块
        :param Query query: 统计范围
    """
```

#### INSUM

```python
def INSUM(block: Block, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    ...
```

#### INSUM

```python
def INSUM(block: Block, query: Query, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    """
    INSUM(block, query, ind, mode[, fill_null=True])
    
        返回板块各成分该指标相应输出按计算类型得到的计算值.计算类型:0-累加,1-平均数,2-最大值,3-最小值.
    
        :param Block block: 指定板块
        :param Query query: 指定范围
        :param Indicator ind: 指定指标
        :param int mode: 计算类型:0-累加,1-平均数,2-最大值,3-最小值.
        :param bool fill_null: 日期对齐时缺失数据填充 nan 值。
        :rtype: Indicator
    """
```

#### POS

```python
def POS(block: Block, query: Query, sg: ...) -> Indicator:
    ...
```

#### get_block

```python
def get_block(arg0: str, arg1: str) -> Block:
    """
    get_block(category: str, name: str)
        
        获取预定义板块
    
        :param str category: 板块分类
        :param str name: 板块名称
        :rtype: Block
    """
```

#### inner_combinate_ind_analysis_with_block

```python
def inner_combinate_ind_analysis_with_block(arg0: Block, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
    ...
```

