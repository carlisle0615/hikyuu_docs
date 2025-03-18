## Query

```python
class Query:
    """
    K线数据查询条件
    """
```

## 相关方法

#### IC

```python
def IC(ind: Indicator, stks: typing.Any, query: Query, ref_stk: Stock, n: int = 1, spearman: bool = True) -> Indicator:
    """
    IC(ind, stks, query, ref_stk[, n=1])
    
        计算指定的因子相对于参考证券的 IC （实际为 RankIC）
        
        :param Indicator ind: 输入因子
        :param sequence(stock)|Block stks 证券组合
        :param Query query: 查询条件
        :param Stock ref_stk: 参照证券，通常使用 sh000300 沪深300
        :param int n: 时间窗口
        :param bool spearman: 使用 spearman 相关系数，否则为 pearson
    """
```

#### ICIR

```python
def ICIR(ind: Indicator, stks: typing.Any, query: Query, ref_stk: Stock, n: int = 1, rolling_n: int = 120, spearman: bool = True) -> Indicator:
    """
    ICIR(ind, stks, query, ref_stk[, n=1, rolling_n=120])
    
        计算 IC 因子 IR = IC的多周期均值/IC的标准方差
    
        :param Indicator ind: 输入因子
        :param sequence(stock)|Block stks 证券组合
        :param Query query: 查询条件
        :param Stock ref_stk: 参照证券，通常使用 sh000300 沪深300
        :param int n: 计算IC时对应的 n 日收益率
        :param int rolling_n: 滚动周期
        :param bool spearman: 使用 spearman 相关系数，否则为 pearson
    """
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

#### INSUM

```python
def INSUM(stks: typing.Sequence, query: Query, ind: Indicator, mode: int, fill_null: bool = True) -> Indicator:
    """
    INSUM(stks, query, ind, mode[, fill_null=True])
    
        返回板块各成分该指标相应输出按计算类型得到的计算值.计算类型:0-累加,1-平均数,2-最大值,3-最小值.
    
        :param Sequence stks: stock list
        :param Query query: 指定范围
        :param Indicator ind: 指定指标
        :param int mode: 计算类型:0-累加,1-平均数,2-最大值,3-最小值.
        :param bool fill_null: 日期对齐时缺失数据填充 nan 值。
        :rtype: Indicator
    """
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

#### POS

```python
def POS(block: Block, query: Query, sg: ...) -> Indicator:
    ...
```

#### crt_pf_strategy

```python
def crt_pf_strategy(pf: Portfolio, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, name: str = 'PFStrategy', other_brokers: list[OrderBrokerBase] = [], config: str = '') -> Strategy:
    ...
```

#### crt_sys_strategy

```python
def crt_sys_strategy(sys: System, stk_market_code: str, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: str = [], name: list[OrderBrokerBase] = 'SYSStrategy', config: str = '') -> Strategy:
    ...
```

#### find_optimal_system

```python
def find_optimal_system(sys_list: list[System], stock: Stock, query: Query, sort_key: str = '', sort_mode: int = 0) -> tuple[float, System]:
    ...
```

#### find_optimal_system_multi

```python
def find_optimal_system_multi(sys_list: list[System], stock: Stock, query: Query, sort_key: str = '', sort_mode: int = 0) -> tuple[float, System]:
    ...
```

#### inner_analysis_sys_list

```python
def inner_analysis_sys_list(arg0: typing.Any, arg1: Query, arg2: System) -> dict:
    ...
```

#### inner_combinate_ind_analysis

```python
def inner_combinate_ind_analysis(arg0: Stock, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
    ...
```

#### inner_combinate_ind_analysis_with_block

```python
def inner_combinate_ind_analysis_with_block(arg0: Block, arg1: Query, arg2: TradeManager, arg3: System, arg4: typing.Sequence, arg5: typing.Sequence, arg6: int) -> dict:
    ...
```

#### run_in_strategy

```python
def run_in_strategy(sys: System, stock: Stock, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: list[OrderBrokerBase] = []) -> None:
    """
    run_in_strategy(sys, stk, query, broker, costfunc, [other_brokers=[]])
              
        在策略运行时中执行系统交易 SYS
        目前仅支持 buy_delay| sell_delay 均为 false 的系统，即 close 时执行交易
     
        :param sys: 交易系统
        :param stk: 交易对象
        :param query: 查询条件
        :param broker: 订单代理（专用与和账户资产同步的订单代理）
        :param costfunc: 成本函数
        :param other_brokers: 其他的订单代理
    """
```

#### run_in_strategy

```python
def run_in_strategy(pf: Portfolio, query: Query, broker: OrderBrokerBase, cost_func: TradeCostBase, other_brokers: list[OrderBrokerBase] = []) -> None:
    """
    run_in_strategy(pf, query, adjust_cycle, broker, costfunc, [other_brokers=[]])
              
        在策略运行时中执行组合策略 PF
        目前仅支持 buy_delay| sell_delay 均为 false 的系统，即 close 时执行交易
    
        :param Portfolio pf: 资产组合
        :param Query query: 查询条件
        :param broker: 订单代理（专用与和账户资产同步的订单代理）
        :param costfunc: 成本函数
        :param other_brokers: 其他的订单代理
    """
```

