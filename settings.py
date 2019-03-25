from DBUtils.PooledDB import PooledDB, SharedDBConnection
import pymysql
class Config(object):
    SALT = b"123sdsdf"
    SECRET_KEY = 'kxcnvxcslsdmfl1234kxcm'
    MAX_CONTENT_LENGTH = 1024*1024*7
    TARGET_PATH = ''
    POOL = PooledDB(
        creator=pymysql,    #连接数据库模块
        maxconnections=6,   #链接池允许的最大链接数，0和None表示连接数
        mincached=2,        #初始化时，连接池中至少创建的空闲链接，0表示不连接
        maxcached=5,        #连接池中最多限制的链接，0和NONE表示不限制
        maxshared=3,        #链接池中最多共享的链接数量，0和None表示全部共享，PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
        blocking=True,      #连接池中如果没有可以链接后，是否阻塞等待。TRUE等待，FALSE不等待
        maxusage=None,      #一个链接最多被重复使用的次数，None表示无限制
        setsession=[],      #开始会话前执行的命令列表如：["set datestyle to ...", "set time zone ..."]
        ping=0,             # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        database='codingstatistic',
        charset='utf8'
    )