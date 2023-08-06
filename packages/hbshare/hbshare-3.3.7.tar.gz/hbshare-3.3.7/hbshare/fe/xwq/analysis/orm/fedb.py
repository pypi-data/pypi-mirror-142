# -*- coding: utf-8 -*-

from hbshare.fe.xwq.analysis.orm.config import Config
from hbshare.fe.xwq.analysis.utils.file_reader import FileReader
from hbshare.fe.xwq.analysis.utils.logger_utils import LoggerUtils
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import sys
import time
import traceback
import warnings
warnings.filterwarnings('ignore', category=pymysql.Warning)


class FEDB:
    """
    不写成单例的好处，方便断开连接，省session的内存
    """
    def __init__(self):
        self.fedb_engine = None
        self.fedb_connection = None
        self.create_connection()

    def create_connection(self):
        db_properties = Config().get_db_properties()
        vaild = False
        while not vaild:
            try:
                # 若是连接sql server数据库，用pymssql代替pymysql
                self.fedb_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
                    'admin',
                    'mysql',
                    '192.168.223.152',
                    '3306',
                    'fe_temp_data'),
                                    connect_args={'charset': 'utf8'}, pool_recycle=360,
                                    pool_size=2, max_overflow=10, pool_timeout=360)
                # self.fedb_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
                #     FileReader.read_file_property(db_properties, 'fedb', 'user'),
                #     FileReader.read_file_property(db_properties, 'fedb', 'password'),
                #     FileReader.read_file_property(db_properties, 'fedb', 'host'),
                #     FileReader.read_file_property(db_properties, 'fedb', 'port'),
                #     FileReader.read_file_property(db_properties, 'fedb', 'database')),
                #                     encodings='utf8', connect_args={'charset': 'utf8'}, pool_recycle=360,
                #                     pool_size=2, max_overflow=10, pool_timeout=360)
                self.fedb_connection = self.fedb_engine.connect()
                vaild = True
            except Exception as e:
                self.close_connection()
                exc_type, exc_value, exc_trackback = sys.exc_info()
                LoggerUtils().get_logger().error(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
                LoggerUtils().get_logger().error('[FEDB] mysql connect error')
                time.sleep(5)
        return

    def get_df(self, sql):
        valid = False
        df = None
        while not valid:
            try:
                df = pd.read_sql_query(sql, self.fedb_engine)
                self.close_connection()
                valid = True
            except Exception as e:
                self.close_connection()
                self.create_connection()
                exc_type, exc_value, exc_trackback = sys.exc_info()
                LoggerUtils().get_logger().error(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
                LoggerUtils().get_logger().error('[FEDB] sql error:{0}'.format(sql))
                time.sleep(5)
        return df

    def close_connection(self):
        # 1) close connection
        try:
            if self.fedb_connection is not None:
                self.fedb_connection.close()
        except Exception as e:
            exc_type, exc_value, exc_trackback = sys.exc_info()
            LoggerUtils().get_logger().error(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
            LoggerUtils().get_logger().error('[FEDB] close connect error')
        # 2) dispose engine
        try:
            if self.fedb_engine is not None:
                self.fedb_engine.dispose()
        except Exception as e:
            exc_type, exc_value, exc_trackback = sys.exc_info()
            LoggerUtils().get_logger().error(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
            LoggerUtils().get_logger().error('[FEDB] dispose engine error')
        return

    def read_test(self):
        sql = 'SELECT * FROM bl_assets_pool;'
        df = self.get_df(sql)
        return df

if __name__ == '__main__':
    df = FEDB().read_test()
    print(df)

