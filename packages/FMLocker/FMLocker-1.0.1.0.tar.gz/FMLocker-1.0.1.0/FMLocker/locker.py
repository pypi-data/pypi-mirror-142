# -*- coding: utf-8 -*-
# @Time    : 2022-03-02 19:32
# @Author  : Huang.XiaoGang
# @File    : MySQLocker.py
# @Software: PyCharm
import time
import datetime
import _thread
import threading
from collections import namedtuple
import MySQLdb


def get_connection(host, port, username, password, db):
    conn = MySQLdb.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        db=db,
    )
    return conn


class MySQLocker(object):
    _instance_lock = threading.Lock()
    InnoDBSql = """
        CREATE TABLE IF NOT EXISTS `forest_locker` (
          `locker_name` varchar(255) NOT NULL,
          `value` varchar(255) DEFAULT NULL,
          PRIMARY KEY (`locker_name`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    MemoryDBSql = """
        CREATE TABLE IF NOT EXISTS `forest_locker`  (
          `locker_name` varchar(100) NOT NULL,
          `value` varchar(255) NULL,
          PRIMARY KEY (`locker_name`)
        ) ENGINE = MEMORY DEFAULT CHARSET=utf8mb4;
    """

    def __init__(self, host, port, username, password, db, is_use_memory_table=True,
                 table_stucture=None):
        """
        table_stucture: 表结构 {'table_name': '', 'lock_field_name': '', 'value_field_name': ''}
        """
        self.conn = get_connection(host, port, username, password, db)
        self.is_use_memory_table = is_use_memory_table
        self.table_stucture = table_stucture
        self.create_locker_table()
        self.lockers = {}
        self.is_have_locker = False
        self.locker = threading.Lock()
        _thread.start_new_thread(self.heartbeat, ())

    def __new__(cls, *args, **kwargs):
        if not hasattr(MySQLocker, "_instance"):
            with MySQLocker._instance_lock:
                if not hasattr(MySQLocker, "_instance"):
                    MySQLocker._instance = object.__new__(cls)
        return MySQLocker._instance

    def create_locker_table(self):
        if self.is_use_memory_table:
            with self.conn.cursor() as cursor:
                cursor.execute(self.MemoryDBSql)
                self.conn.commit()
        self.table_stucture = {
            'table_name': 'forest_locker',
            'lock_field_name': 'locker_name',
            'value_field_name': 'value'
        }

    def heartbeat(self):
        while True:
            self.locker.acquire()
            try:
                cursor = self.conn.cursor()
                if self.is_have_locker:
                    for key in self.lockers.keys():
                        timestamp = str(int(time.time() * 1000))
                        sql = "update {} set {} = '{}' where {} = '{}' and {} = '{}'".format(
                            self.table_stucture['table_name'],
                            self.table_stucture['value_field_name'],
                            timestamp,
                            self.table_stucture['lock_field_name'],
                            key,
                            self.table_stucture['value_field_name'],
                            self.lockers[key]
                        )
                        cursor.execute(sql)
                else:
                    num = cursor.execute('select now()')
                    cursor.fetchone()
                self.conn.commit()
            except:
                self.conn.close()
            finally:
                self.locker.release()
            time.sleep(0.2)

    def renewal_locker(self, lock_name):
        self.locker.acquire()
        try:
            if not self.is_have_locker:
                return
            cursor = self.conn.cursor()
            timestamp = str(int(time.time() * 1000))
            sql = "update {} set {} = '{}' where {} = '{}' and {} = '{}'".format(
                self.table_stucture['table_name'],
                self.table_stucture['value_field_name'],
                timestamp,
                self.table_stucture['lock_field_name'],
                lock_name,
                self.table_stucture['value_field_name'],
                self.lockers[lock_name],
            )
            num = cursor.execute(sql)
            self.conn.commit()
            self.lockers[lock_name] = timestamp
            return num > 0
        except:
            self.conn.rollback()
        finally:
            self.locker.release()

    def _get_locker_by_timeout(self, lock_name, timeout):
        start_time = time.time()
        result = False
        while (time.time() - start_time) < timeout:
            timestamp = str(int(time.time() * 1000))
            cursor = self.conn.cursor()
            self.locker.acquire()
            try:
                # 获取locker
                try:
                    cursor.execute("insert into {} ({}, {}) values ('{}', '{}')"
                                   .format(self.table_stucture['table_name'],
                                           self.table_stucture['lock_field_name'],
                                           self.table_stucture['value_field_name'],
                                           lock_name, timestamp))
                    self.conn.commit()
                    self.lockers[lock_name] = {'timestamp': timestamp}
                    self.is_have_locker = True
                    result = True
                    break
                except:
                    self.conn.rollback()
                # 检查上次锁时间
                try:
                    sql = f"select {self.table_stucture['value_field_name']} from {self.table_stucture['table_name']}" \
                          f" where {self.table_stucture['lock_field_name']} = '{lock_name}'"
                    cursor.execute(sql)
                    lock_value = int(time.time() * 1000)
                    last_value = int(cursor.fetchone())
                    if (last_value - lock_value) > 2000:
                        timestamp = str(int(time.time() * 1000))
                        sql = f"update {self.table_stucture['table_name']} set {self.table_stucture['lock_field_name']}" \
                              f" = {timestamp} where {self.table_stucture['lock_field_name']} = '{lock_name}' and " \
                              f"{self.table_stucture['value_field_name']} = {last_value}"
                        num = cursor.execute(sql)
                        self.conn.commit()
                        if num > 0:
                            self.lockers[lock_name] = {'timestamp': timestamp}
                            self.is_have_locker = True
                            result = True
                            break
                except:
                    self.conn.rollback()
            finally:
                self.locker.release()
            time.sleep(0.2)
        return result

    def _get_locker_try_once(self, lock_name):
        self.locker.acquire()
        try:
            cursor = self.conn.cursor()
            timestamp = str(int(time.time() * 1000))
            sql = "insert into {} ({}, {}) values ('{}', '{}')".format(self.table_stucture['table_name'],
                                                                       self.table_stucture['lock_field_name'],
                                                                       self.table_stucture['value_field_name'],
                                                                       lock_name, timestamp)
            num = cursor.execute(sql)
            self.conn.commit()
            if num > 0:
                self.lockers[lock_name] = {'timestamp': timestamp}
                self.is_have_locker = True
                return True
        except:
            self.conn.rollback()
            return False

    def get_locker(self, lock_name, timeout=0):
        if timeout > 0:
            return self._get_locker_by_timeout(lock_name, timeout)
        else:
            return self._get_locker_try_once(lock_name)

    def release_locker(self, lock_name):
        self.locker.acquire()
        try:
            cursor = self.conn.cursor()
            timestamp = self.lockers.get(lock_name)
            if timestamp:
                sql = f"delete from {self.table_stucture['table_name']} where {self.table_stucture['lock_field_name']}" \
                      f" = '{lock_name}' and {self.table_stucture['value_field_name']} = '{timestamp}'"
                self.lockers.pop(lock_name)
            else:
                sql = f"delete from {self.table_stucture['table_name']} where {self.table_stucture['lock_field_name']}" \
                      f" = '{lock_name}'"
            num = cursor.execute(sql)
            self.is_have_locker = len(self.lockers.keys()) > 0
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.locker.release()
        return num > 0
