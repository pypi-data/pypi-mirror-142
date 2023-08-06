"""
这里定义的是一些常用常量
"""
from enum import Enum
from pytz import timezone

CHINA_TZ = timezone("Asia/Shanghai")

MAX_QUERY_SIZE: int = 5000
TS_DATE_FORMATE: str = '%Y%m%d'
MAX_QUERY_TIMES: int = 500

class TRADE_TIMES():
    TRADE_TIME_AM = ['09:30:00','11:30:00']
    TRADE_TIME_PM = ["13:00:00","15:00:00"]
    TRADE_TIME_AM_pre = ['09:25:00','11:31:00']
    TRADE_TIME_PM_pre = ["13:00:00","15:01:00"]

#print(TRADE_TIMES().TRADE_TIME_AM)

class REPORT_PERIODS():
    q1 = '0331'
    q2 = '0630'
    q3 = '0930'
    q4 = '1231'
    REPORT_PERIODS_DICT = { 'q1': '0331',
            'q2': '0630',
            'q3': '0930',
            'q4': '1231'}
    
class PERIODS():
    """stock trade period
    """
    PERIODS=[5,10,20,60,120,250]

class SWL_LEVEL():
    LEVEL =['L1','L2','L3']
    SWL_LEVEL = ['sw_l1','sw_l2','sw_l3']

class FREQUENCE():
    """查询的级别
    YEAR = 'year'  # 年bar
    QUARTER = 'quarter'  # 季度bar
    MONTH = 'month'  # 月bar
    WEEK = 'week'  # 周bar
    DAY = 'day'  # 日bar
    ONE_MIN = '1min'  # 1min bar
    FIVE_MIN = '5min'  # 5min bar
    FIFTEEN_MIN = '15min'  # 15min bar
    THIRTY_MIN = '30min'  # 30min bar
    HOUR = '60min'  # 60min bar
    SIXTY_MIN = '60min'  # 60min bar
    TICK = 'tick'  # transaction
    ASKBID = 'askbid'  # 上下五档/一档
    REALTIME_MIN = 'realtime_min' # 实时分钟线
    LATEST = 'latest'  # 当前bar/latest
    2019/08/06 @yutiansut
    """

    YEAR = 'year'  # 年bar
    QUARTER = 'quarter'  # 季度bar
    MONTH = 'month'  # 月bar
    WEEK = 'week'  # 周bar
    DAY = 'day'  # 日bar
    ONE_MIN = '1min'  # 1min bar
    FIVE_MIN = '5min'  # 5min bar
    FIFTEEN_MIN = '15min'  # 15min bar
    THIRTY_MIN = '30min'  # 30min bar
    HOUR = '60min'  # 60min bar
    SIXTY_MIN = '60min'  # 60min bar
    TICK = 'tick'  # transaction
    ASKBID = 'askbid'  # 上下五档/一档
    REALTIME_MIN = 'realtime_min'  # 实时分钟线
    LATEST = 'latest'  # 当前bar/latest
   


class MARKET_TYPE():
    """市场种类
    日线 尾数01
    分钟线 尾数02
    tick 尾数03
    市场:
    股票 0
    指数/基金 1
    期货 2
    港股 3
    美股 4
    比特币/加密货币市场 5
    """
    STOCK_CN = 'stock_cn'  # 中国A股
    STOCK_CN_B = 'stock_cn_b'  # 中国B股
    STOCK_CN_D = 'stock_cn_d'  # 中国D股 沪伦通
    STOCK_HK = 'stock_hk'  # 港股
    STOCK_US = 'stock_us'  # 美股
    FUTURE_CN = 'future_cn'  # 国内期货
    OPTION_CN = 'option_cn'  # 国内期权
    STOCKOPTION_CN = 'stockoption_cn'  # 个股期权
    # BITCOIN = 'bitcoin'  # 比特币
    CRYPTOCURRENCY = 'cryptocurrency'  # 加密货币(衍生货币)
    INDEX_CN = 'index_cn'  # 中国指数
    FUND_CN = 'fund_cn'   # 中国基金
    BOND_CN = 'bond_cn'  # 中国债券
    
