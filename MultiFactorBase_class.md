## MultiFactorBase

```python
class MultiFactorBase:
    """
    市场环境判定策略基类
    
    自定义市场环境判定策略接口：
    
        - _calculate : 【必须】子类计算接口
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
    def __init__(self, arg0: MultiFactorBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    def __str__(self) -> str:
        ...
    def clone(self) -> MultiFactorBase:
        """
        克隆操作
        """
    def get_all_factors(self) -> list[Indicator]:
        """
        get_all_factors(self)
        
            获取所有证券合成后的因子列表
        
            :return: [factor1, factor2, ...] 顺序与参考证券顺序相同
        """
    def get_all_scores(self) -> list[ScoreRecordList]:
        """
        get_all_scores(self)
        
            获取所有日期的所有评分，长度与参考日期相同
        
            :return: ScoreRecordList
        """
    def get_all_src_factors(self) -> list[list[Indicator]]:
        ...
    def get_datetime_list(self) -> DatetimeList:
        """
        获取参考日期列表（由参考证券通过查询条件获得）
        """
    def get_factor(self, stock: Stock) -> Indicator:
        """
        get_factor(self, stock)
        
            获取指定证券合成后的新因子
        
            :param Stock stock: 指定证券
        """
    def get_ic(self, ndays: int = 0) -> Indicator:
        """
        get_ic(self[, ndays=0])
        
            获取合成因子的IC, 长度与参考日期同
        
            ndays 对于使用 IC/ICIR 加权的新因子，最好保持好 ic_n 一致，
            但对于等权计算的新因子，不一定非要使用 ic_n 计算。
            所以，ndays 增加了一个特殊值 0, 表示直接使用 ic_n 参数计算 IC
             
            :rtype: Indicator
        """
    def get_icir(self, ir_n: int, ic_n: int = 0) -> Indicator:
        """
        get_icir(self, ir_n[, ic_n=0])
        
            获取合成因子的 ICIR
        
            :param int ir_n: 计算 IR 的 n 窗口
            :param int ic_n: 计算 IC 的 n 窗口 (同 get_ic 中的 ndays)
        """
    def get_param(self, arg0: str) -> any:
        """
        get_param(self, name)
        
            获取指定的参数
        
            :param str name: 参数名称
            :return: 参数值
            :raises out_of_range: 无此参数
        """
    def get_ref_indicators(self) -> list[Indicator]:
        """
        获取创建时输入的原始因子列表
        """
    def get_ref_stock(self) -> Stock:
        """
        获取参考证券
        """
    def get_scores(self, date: Datetime, start: int = 0, end: typing.Any = None, filter: typing.Any = None) -> ScoreRecordList:
        """
        get_score(self, date[, start=0, end=Null])
        
            获取指定日期截面的所有因子值，已经降序排列，相当于各证券日期截面评分。
        
            :param Datetime date: 指定日期
            :param int start: 取当日排名开始
            :param int end: 取当日排名结束(不包含本身)
            :param function func: (ScoreRecord)->bool 或 (Datetime, ScoreRecord)->bool 为原型的可调用对象
            :rtype: ScoreRecordList
        """
    def get_stock_list(self) -> list[Stock]:
        """
        获取创建时指定的证券列表
        """
    def get_stock_list_num(self) -> int:
        """
        获取创建时指定的证券列表中证券数量
        """
    def have_param(self, arg0: str) -> bool:
        """
        是否存在指定参数
        """
    def set_param(self, arg0: str, arg1: any) -> None:
        """
        set_param(self, name, value)
        
            设置参数
        
            :param str name: 参数名称
            :param value: 参数值
            :raises logic_error: Unsupported type! 不支持的参数类型
        """
    def set_ref_indicators(self, arg0: list[Indicator]) -> None:
        """
        set_ref_indicators(self, inds)
              
            设置原始因子列表
            
            :param list inds: 新的原始因子列表
        """
    def set_ref_stock(self, arg0: Stock) -> None:
        """
        set_ref_stock(self, stk)
              
            设置参考证券
            
            :param Stock stk: 参考证券
        """
    def set_stock_list(self, arg0: list[Stock]) -> None:
        """
        set_stock_list(self, stks)
              
            设置计算范围指定的证券列表
            
            :param list stks: 新的待计算证券列表
        """
    @property
    def name(self) -> str:
        """
        名称
        """
    @name.setter
    def name(self, arg1: str) -> None:
        ...
    @property
    def query(self) -> Query:
        """
        查询条件
        """
    @query.setter
    def query(self, arg1: Query) -> None:
        ...
```

## 相关方法

### 与MultiFactorBase相关的方法

#### MF_EqualWeight

```python
def MF_EqualWeight() -> MultiFactorBase:
    ...
```

#### MF_EqualWeight

```python
def MF_EqualWeight(inds: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5])
    
        等权重合成因子
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
```

#### MF_ICIRWeight

```python
def MF_ICIRWeight() -> MultiFactorBase:
    ...
```

#### MF_ICIRWeight

```python
def MF_ICIRWeight(inds: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, ic_rolling_n: int = 120, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5, ic_rolling_n=120])
    
        滚动ICIR权重合成因子
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param int ic_rolling_n: IC 滚动周期
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
```

#### MF_ICWeight

```python
def MF_ICWeight() -> MultiFactorBase:
    ...
```

#### MF_ICWeight

```python
def MF_ICWeight(inds: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, ic_rolling_n: int = 120, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5, ic_rolling_n=120])
    
        滚动IC权重合成因子
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk:  (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param int ic_rolling_n: IC 滚动周期
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
```

#### MF_Weight

```python
def MF_Weight() -> MultiFactorBase:
    ...
```

#### MF_Weight

```python
def MF_Weight(inds: typing.Sequence, weights: typing.Sequence, stks: typing.Sequence, query: Query, ref_stk: typing.Any = None, ic_n: int = 5, spearman: bool = True) -> MultiFactorBase:
    """
    MF_EqualWeight(inds, stks, query, ref_stk[, ic_n=5])
    
        按指定权重合成因子 = ind1 * weight1 + ind2 * weight2 + ... + indn * weightn
    
        :param sequense(Indicator) inds: 原始因子列表
        :param sequense(float) weights: 权重列表(需和 inds 等长)
        :param sequense(stock) stks: 计算证券列表
        :param Query query: 日期范围
        :param Stock ref_stk: 参考证券 (未指定时，默认为 sh000300 沪深300)
        :param int ic_n: 默认 IC 对应的 N 日收益率
        :param bool spearman: 默认使用 spearman 计算相关系数，否则为 pearson
        :rtype: MultiFactorBase
    """
```

