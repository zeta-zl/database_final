import hashlib
from typing import TypeVar

import dbClass
import sharedata
from dataClass import dataClass, primary_key_dict

data_T = TypeVar('data_T', bound=dataClass)
quotation = "'"


def findPatient(usr, pwd):
    """
    查找用户
    """
    db = sharedata.getValue('dbObj')
    sql = "select * from `patient` where patient_id=%(usr)s"
    params = {"usr": quotation + usr + quotation}
    result = db.query(sql, params)
    if result:
        return result
    else:
        return "no_user"


def check_login(database_name, id, psw):
    """
    判断账户名和密码是否匹配
    :param database_name: 数据库名
    :param id: id值
    :param psw: 密码，未加密
    :return: 是否匹配
    """
    where_clause = "%s_id = %s" % (database_name.split('_')[0], id)
    _psw = select_from_table(database_name, where_clause)
    return pwdEncryption(psw) == _psw[0][1]


def pwdEncryption(pwd):
    """
    密码加密
    """
    # 创建SHA-256哈希对象
    sha256_hash = hashlib.sha256()
    # 将密码编码为字节流并更新哈希对象
    sha256_hash.update(pwd.encode('utf-8'))
    # 获取哈希值的十六进制表示
    hashed_password = sha256_hash.hexdigest()
    # 返回加密后的密码
    return hashed_password


def addPatient(usr, pwd, name, id, phone):
    """
    添加用户
    """
    db = sharedata.getValue('dbObj')
    sql = "insert into `patient` values(%(usr)s,%(name)s,%(id)s,%(phone)s,%(pwd)s)"
    params = {"usr": quotation + usr + quotation, "pwd": quotation + pwd + quotation,
              "name": quotation + name + quotation, "id": quotation + id + quotation,
              "phone": quotation + phone + quotation}
    result = db.execute(sql, params)
    return result


def insert_into_table(table_name, data_object: data_T, commit=False):
    """
    插入记录

    :param table_name: 要插入的表名
    :param data_object: 要插入的值，是dataClass的子类
    :param commit: 是否执行
    :return: 与execute相同

    """
    db = dbClass.dbClass()
    column_names = ','.join(data_object.to_dic().keys())
    placeholders = ','.join(['%s'] * len(data_object.to_dic()))

    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    params = tuple(data_object.to_dic().values())

    return db.execute(sql, params, commit)


def update_table(table_name, value: data_T, commit=False):
    """
    更新记录

    :param table_name: 要更新的表名
    :param value: 要更新的值，是dataClass的子类
    :param commit: 是否执行
    :return: 与execute相同

    """
    db = dbClass.dbClass()
    primary_keys = primary_key_dict[table_name]
    column_value_pairs = ','.join([f"{column}=%s" for column in value.to_dic().keys()])

    where_clause = ' AND '.join([f"{column}=%s" for column in primary_keys])
    params = tuple(value.to_dic().values()) + tuple(value.to_dic()[key] for key in primary_keys)

    sql = f"UPDATE {table_name} SET {column_value_pairs} WHERE {where_clause}"
    db.execute(sql, params, commit)


def delete_from_table(table_name, value, commit=False):
    """
    删除记录

    :param table_name: 要删除的表名
    :param value: 包含主键值的对象，是dataClass的子类，或是WHERE条件列表，每个元素为一个条件字符串
    :param commit: 是否执行
    :return: 与execute相同

    """

    db = dbClass.dbClass()
    if isinstance(value, dataClass):
        primary_keys = primary_key_dict[table_name]  # List of primary key names
        where_clause = ' AND '.join([f"{column}=%s" for column in primary_keys])
        params = tuple(value.to_dic()[key] for key in primary_keys)

        sql = f"DELETE FROM {table_name} WHERE {where_clause}"
        db.execute(sql, params, commit)
    else:
        if isinstance(value, str):
            value = [value]

        where_clause = ' AND '.join(value)

        sql = f"DELETE FROM {table_name} WHERE {where_clause}"
        db.execute(sql, commit=commit)


def select_from_table(table_name, conditions):
    """
    查询记录

    :param table_name: 要查询的表名
    :param conditions: WHERE条件列表，每个元素为一个条件字符串
    :return: 查询结果

    """
    db = dbClass.dbClass()
    if isinstance(conditions, str):
        conditions = [conditions]
    where_clause = ' AND '.join(conditions)

    sql = f"SELECT * FROM {table_name} WHERE {where_clause}"
    result = db.query(sql)

    return result
