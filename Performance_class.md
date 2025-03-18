## Performance

```python
class Performance:
    """
    简单绩效统计
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def exist(arg0: str) -> bool:
        ...
    @staticmethod
    def to_df(per):
        """
        将 Performance 统计结果转换为 DataFrame 格式
        """
    def __getitem__(self, arg0: str) -> float:
        """
        按指标名称获取指标值，必须在运行 statistics 或 report 之后生效
                
                :param str name: 指标名称
                :rtype: float)
        """
    def __init__(self) -> None:
        ...
    def names(self) -> list[str]:
        """
        names(self)
              
              获取所有统计项名称
        """
    def report(self, tm: TradeManager, datetime: Datetime = ...) -> str:
        """
        report(self, tm[, datetime=Datetime.now()])
        
                简单的文本统计报告，用于直接输出打印
        
                :param TradeManager tm: 指定的交易管理实例
                :param Datetime datetime: 统计截止时刻
                :rtype: str
        """
    def reset(self) -> None:
        """
        reset(self)
        
                复位，清除已计算的结果
        """
    def statistics(self, tm: TradeManager, datetime: Datetime = ...) -> None:
        """
        statistics(self, tm[, datetime=Datetime.now()])
        
                根据交易记录，统计截至某一时刻的系统绩效, datetime必须大于等于lastDatetime
        
                :param TradeManager tm: 指定的交易管理实例
                :param Datetime datetime: 统计截止时刻
        """
    def values(self) -> list[float]:
        """
        values(self)
              
              获取所有统计项值，顺序与 names 相同
        """
```

