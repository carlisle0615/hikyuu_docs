## AllocateFundsBase

```python
class AllocateFundsBase:
    """
    资产分配算法基类, 子类接口：
    
    公共参数:
        
        - adjust_running_sys (bool|True): 是否调整之前已经持仓策略的持仓。不调整时，仅使用总账户当前剩余资金进行分配，否则将使用总市值进行分配
            注意: 无论是否调整已持仓策略，权重比例都是相对于总资产，不是针对剩余现金余额
                  仅针对剩余现金比例调整没有意义，即使分配由于交易成本原因可能也无法完成实际交易
            adjust_running_sys: True - 主动根据资产分配对已持仓策略进行增减仓
            adjust_running_sys: False - 不会根据当前分配权重对已持仓策略进行强制加减仓
        
        - auto_adjust_weight (bool|True): 自动调整权重，此时认为传入的权重为各证券的相互比例（详见ignore_zero_weight说明）。否则，以传入的权重为指定权重不做调整（此时传入的各个权重需要小于1）。
      
        - ignore_zero_weight (bool|False): 该参数在 auto_adjust_weight 时生效。是否过滤子类返回的比例权重列表中的 0 值（包含小于0）和 nan 值。
    
            如：子类返回权重比例列表 [6, 2, 0, 0, 0], 则
                - 过滤 0 值，则实际调整后的权重为 Xi / sum(Xi)：[6/8, 2/8]
                - 不过滤，m 设为非零元素个数，n为总元素个数，(Xi / Sum(Xi)) * (m / n)：
                     [(6/8)*(2/5), (2/8)*(2/5), 0, 0, 0]
                    即，保留分为5份后，仅在2份中保持相对比例
    
        - ignore_se_score_is_null (bool|False): 忽略选中系统列表中的系统得分为 null 的系统. 注意：某些SE（如SE_MultiFactor）本身可能也存在类似控制
        - ignore_se_score_lt_zero (bool|False): 忽略选中系统列表中的系统得分小于等于 0 的系统
        - reserve_percent (float|0.0): 保留不参与重分配的资产比例
        - trace (bool|False): 打印跟踪信息
    
    子类接口:
    
        - _allocateWeight : 【必须】子类资产分配调整实现
        - _clone : 【必须】克隆接口
        - _reset : 【可选】重载私有变量
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: AllocateFundsBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def _allocate_weight(self, date: Datetime, se_list: SystemWeightList) -> SystemWeightList:
        """
        _allocate_weight(self, date, se_list)
        
                【重载接口】子类分配权重接口，获取实际分配资产的系统实例及其权重
        
                :param Datetime date: 当前时间
                :param SystemList se_list: 当前选中的系统列表
                :return: 系统权重分配信息列表
                :rtype: SystemWeightList
        """
    def _reset(self) -> None:
        """
        子类复位操作实现
        """
    def clone(self) -> AllocateFundsBase:
        """
        克隆操作
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def reset(self) -> None:
        """
        复位操作
        """
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        set_param(self, name, value)
        
            设置参数
        
            :param str name: 参数名称
            :param value: 参数值
            :raises logic_error: Unsupported type! 不支持的参数类型
        """
    @property
    def name(self) -> str:
        """
        算法组件名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def query(self) -> Query:
        """
        设置或获取查询条件
        """
    @query.setter
    def query(self, arg1: Query) -> None:
        ...
    @property
    def tm(self) -> TradeManager:
        ...
```

## 相关方法

### 与AllocateFundsBase相关的方法

#### AF_EqualWeight

```python
def AF_EqualWeight() -> AllocateFundsBase:
    """
    AF_EqualWeight()
        
        等权重资产分配，对选中的资产进行等比例分配
    """
```

#### AF_FixedWeight

```python
def AF_FixedWeight(weight: float = 0.1) -> AllocateFundsBase:
    """
    AF_FixedWeight(weight)
        
        固定比例资产分配
    
        :param float weight:  指定的资产比例 [0, 1]
    """
```

#### AF_FixedWeightList

```python
def AF_FixedWeightList(weights: list[float]) -> AllocateFundsBase:
    """
    AF_FixedWeightList(weights)
        
        固定比例资产分配列表.
    
        :param float weights:  指定的资产比例列表
    """
```

#### AF_MultiFactor

```python
def AF_MultiFactor() -> AllocateFundsBase:
    """
    AF_MultiFactor()
          
        创建 MultiFactor 评分权重的资产分配算法实例, 即直接以SE返回的评分作为权重。
    """
```

