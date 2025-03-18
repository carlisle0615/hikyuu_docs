## StockManager

```python
class StockManager:
    """
    证券信息管理类
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def instance() -> StockManager:
        """
        获取StockManager单例实例
        """
    def __getitem__(self, arg0: str) -> ...:
        """
        同 get_stock
        """
    def __iter__(self) -> typing.Iterator[...]:
        ...
    def __len__(self) -> int:
        """
        返回证券数量
        """
    def add_block(self, arg0: ...) -> None:
        """
        add_block(self, block)
              
            将独立的板块加入到数据库中， 板块通过 category+name 区分， 数据库中相同板块将被覆盖。注意，如果板块发生变化，需要调用 save_block 重新保存。
              
            :param Block block: 板块实例
        """
    def add_stock(self, arg0: ...) -> bool:
        """
        add_stock(self, stock)
              
            谨慎调用！！！仅供增加某些临时的外部 Stock
            @return True | False
        """
    def add_temp_csv_stock(self, code: str, day_filename: str, min_filename: str, tick: float = 0.01, tick_value: float = 0.01, precision: int = 2, min_trade_num: int = 1, max_trade_num: int = 1000000) -> ...:
        """
        add_temp_csv_stock(code, day_filename, min_filename[, tick=0.01, tick_value=0.01,
                precision=2, min_trade_num = 1, max_trade_num=1000000])
        
            从CSV文件（K线数据）增加临时的Stock，可用于只有CSV格式的K线数据时，进行临时测试。
        
            添加的 stock 对应的 market 为 "TMP", 如需通过 sm 获取，需加入 tmp，如：sm['tmp0001']
        
            CSV文件第一行为标题，需含有
            Datetime（或Date、日期）、OPEN（或开盘价）、HIGH（或最高价）、LOW（或最低价）、CLOSE（或收盘价）、AMOUNT（或成交金额）、VOLUME（或VOL、COUNT、成交量）。
        
            注意：请确保 csv 使用 utf8 格式存储，否则无法识别中文
        
            :param str code: 自行编号的证券代码，不能和已有的Stock相同，否则将返回Null<Stock>
            :param str day_filename: 日线CSV文件名
            :param str min_filename: 分钟线CSV文件名
            :param float tick: 最小跳动量，默认0.01
            :param float tick_value: 最小跳动量价值，默认0.01
            :param int precision: 价格精度，默认2
            :param int min_trade_num: 单笔最小交易量，默认1
            :param int max_trade_num: 单笔最大交易量，默认1000000
            :return: 加入的Stock
            :rtype: Stock
        """
    def datadir(self) -> str:
        """
        datadir(self) -> str
        
            获取财务数据存放路径
        """
    def get_base_info_parameter(self) -> ...:
        """
        获取当前基础信息驱动参数
        """
    def get_block(self, arg0: str, arg1: str) -> ...:
        """
        get_block(self, category, name)
        
            获取预定义的板块
        
            :param str category: 板块分类
            :param str name: 板块名称
            :return: 板块，如找不到返回空Block
            :rtype: Block
        """
    @typing.overload
    def get_block_list(self) -> list[...]:
        ...
    @typing.overload
    def get_block_list(self, arg0: str) -> list[...]:
        """
        get_block_list(self[, category])
        
            获取指定分类的板块列表
        
            :param str category: 板块分类
            :return: 板块列表
            :rtype: BlockList
        """
    def get_block_parameter(self) -> ...:
        """
        获取当前板块信息驱动参数
        """
    def get_context(self) -> StrategyContext:
        """
        获取当前上下文
        """
    def get_hikyuu_parameter(self) -> ...:
        """
        获取当前其他参数
        """
    def get_history_finance_all_fields(self) -> list:
        """
        get_history_finance_all_fields(self)
            获取所有历史财务信息字段及其索引
        """
    def get_history_finance_field_index(self, arg0: str) -> int:
        """
        get_history_finance_field_index(self, name)
            
            根据字段名称，获取历史财务信息相应字段索引
        """
    def get_history_finance_field_name(self, arg0: int) -> str:
        """
        get_history_finance_field_name(self, index)
                   
            根据字段索引，获取历史财务信息相应字段名
        """
    def get_kdata_parameter(self) -> ...:
        """
        获取当前K线数据驱动参数
        """
    def get_market_info(self, arg0: str) -> MarketInfo:
        """
        get_market_info(self, market)
        
            获取相应的市场信息
        
            :param string market: 指定的市场标识（市场简称）
            :return: 相应的市场信息，如果相应的市场信息不存在，则返回Null<MarketInfo>()
            :rtype: MarketInfo
        """
    def get_market_list(self) -> list[str]:
        """
        get_market_list(self)
        
            获取市场简称列表
        
            :rtype: StringList
        """
    def get_preload_parameter(self) -> ...:
        """
        获取当前预加载参数
        """
    def get_stock(self, arg0: str) -> ...:
        """
        get_stock(self, querystr)
        
            根据"市场简称证券代码"获取对应的证券实例
        
            :param str querystr: 格式：“市场简称证券代码”，如"sh000001"
            :return: 对应的证券实例，如果实例不存在，则Null<Stock>()，不抛出异常
            :rtype: Stock
        """
    def get_stock_list(self, filter: typing.Any = None) -> list[...]:
        """
        get_stock_list(self[, filter=None])
                
            获取证券列表
        
            :param func filter: 输入参数为 stock, 返回 True | False 的过滤函数
        """
    def get_stock_type_info(self, arg0: int) -> StockTypeInfo:
        """
        get_stock_type_info(self, stk_type)
        
            获取相应的证券类型详细信息
        
            :param int stk_type: 证券类型，参见： :py:data:`constant`
            :return: 对应的证券类型信息，如果不存在，则返回Null<StockTypeInfo>()
            :rtype: StockTypeInfo
        """
    def get_trading_calendar(self, query: ..., market: str = 'SH') -> DatetimeList:
        """
        get_trading_calendar(self, query[, market='SH'])
        
            获取指定市场的交易日日历
        
            :param KQuery query: Query查询条件
            :param str market: 市场简称
            :return: 日期列表
            :rtype: DatetimeList
        """
    def init(self, base_info_param: ..., block_param: ..., kdata_param: ..., preload_param: ..., hikyuu_param: ..., context: StrategyContext = ...) -> None:
        """
        init(self, base_info_param, block_param, kdata_param, preload_param, hikyuu_param, context)
                      
            初始化函数，必须在程序入口调用
            
            :param base_info_param 基础信息驱动参数
             param block_param 板块信息驱动参数
             param kdata_param K线数据驱动参数
             param preload_param 预加载参数
             param hikyuu_param 其他参数
             param StrategyContext context 策略上下文, 默认加载全部证券
        """
    def is_holiday(self, arg0: Datetime) -> bool:
        """
        is_holiday(self, d)
        
            判断日期是否为节假日
        
            :param Datetime d: 待判断的日期
        """
    def reload(self) -> None:
        """
        重新加载所有证券数据
        """
    @typing.overload
    def remove_block(self, category: str, name: str) -> None:
        ...
    @typing.overload
    def remove_block(self, block: ...) -> None:
        """
        remove_block(self, block)
                   
            从数据库中删除板块
            
            :param Block block: 板块实例
        """
    def remove_stock(self, arg0: str) -> None:
        """
        remove_stock(self, market_code)
            
            从 sm 中移除 market_code 代表的证券，谨慎使用！！！通常用于移除临时增加的外部 Stock
            
            :param str market_code: 证券市场标识
        """
    def remove_temp_csv_stock(self, arg0: str) -> None:
        """
        remove_temp_csv_stock(self, code)
        
            移除增加的临时Stock
        
            :param str code: 创建时自定义的编码
        """
    def save_block(self, arg0: ...) -> None:
        """
        save_block(self, block)
              
            保存发生变化后的板块保存至数据库
        
            :param Block block: 板块实例
        """
    def tmpdir(self) -> str:
        """
        tmpdir(self) -> str
        
            获取用于保存零时变量等的临时目录，如未配置则为当前目录 由m_config中的“tmpdir”指定
        """
    @property
    def data_ready(self) -> bool:
        """
        是否所有数据已准备就绪（加载完毕）
        """
```

