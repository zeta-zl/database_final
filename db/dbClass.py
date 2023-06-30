import pymysql
import logging
import os
import sys
from typing import TypeVar

# 加入日志
# 获取logger实例
logger = logging.getLogger("mylogger")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
# 文件日志
file_handler = logging.FileHandler(os.path.abspath('./log.txt'))
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class dbClass():
    def __init__(self):
        self.conn = None
        self.cur = None

    def __del__(self):
        try:
            # 关闭游标对象
            if self.cur is not None:
                self.cur.close()
        except:
            pass

        try:
            # 关闭数据库连接
            if self.conn is not None:
                self.conn.close()
        except:
            pass

    def init_db(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                                        , user='root'  # 用户名
                                        , passwd='zeta'  # 密码
                                        , port=3306  # 端口，默认为3306
                                        , charset='utf8'  # 字符编码
                                        )
            self.cur = self.conn.cursor()  # 生成游标对象

            sql = "CREATE DATABASE IF NOT EXISTS hospital"
            self.cur.execute(sql)
            return True
        except:
            logger.error("数据库连接失败")
            return False

    def connectdb(self):

        passwd = ""  # 在这里填写密码

        try:
            self.conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                                        , user='root'  # 用户名
                                        , passwd=passwd  # 密码
                                        , port=3306  # 端口，默认为3306
                                        , db='hospital'  # 数据库名称
                                        , charset='utf8'  # 字符编码
                                        )
            self.cur = self.conn.cursor()  # 生成游标对象
            return True
        except:

            assert passwd != "", "需要填写本地数据库密码"
            logger.error("数据库连接失败")
            return False

    def closedb(self):
        if self.cur and self.conn:
            self.cur.close()
            self.conn.close()
            return True

    def commit(self):
        self.conn.commit()

    def execute(self, sql, params=None, commit=False):
        '''
        执行sql语句
        :param sql: sql语句
        :param params: sql语句中的参数
        :param commit: 是否执行
        :return:
        '''
        res = self.connectdb()
        if res == False:
            logger.error("执行sql语句时，数据库连接失败")
            return "connect_error"
        try:
            if params:
                self.cur.execute(sql, params)
            else:
                self.cur.execute(sql)
            if commit:
                self.conn.commit()
        except Exception as e:
            print(e)
            print(self.cur.mogrify(sql, params))
            logger.error("数据库执行失败：" + sql)
            logger.error("参数：" + str(params))
            self.conn.rollback()
            self.closedb()
            return "execute_error"

    def query(self, sql, params=None):
        """
        查询
        :param sql: sql语句
        :param params: sql语句中的参数
        :return:
        """
        res = self.execute(sql, params)
        if res == "connect_error" or res == "execute_error":
            return res
        else:
            return self.cur.fetchall()
