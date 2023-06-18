# -*- coding: utf-8 -*-

"""
Module implementing query_abstract_Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QTableWidgetItem

import dataClass
import dbop
from Ui_query_abstract import Ui_Dialog


class query_abstract_Dialog(QDialog, Ui_Dialog):
    """
    查询的窗口应该继承这个类
    传入数据库名与列名，重载get_where_conditions（默认有两个主键，选取条件为相等）
    并在新生成的类中删去 self.setupUi(self)，不需要为其它界面指定UI
    具体使用可参照query_medicine

    TODO：支持分页，美化前端，支持选取特殊列
    """

    def __init__(self, database_name="", table_title=None, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(query_abstract_Dialog, self).__init__(parent)
        self.setupUi(self)

        self.database_name = database_name
        self.table_title = table_title
        if self.database_name == "" or self.table_title is None:
            raise NotImplementedError("database_name与table_title应该被指定")
        self.tableWidget.setColumnCount(len(self.table_title))
        self.tableWidget.setHorizontalHeaderLabels(self.table_title)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

        print(self.database_name)
        items = dbop.select_from_table(self.database_name, "1=1")
        self.refreshtable(items)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """

        where_conditions = self.get_where_conditions()
        result = dbop.select_from_table(self.database_name, where_conditions)
        self.refreshtable(result)

    def refreshtable(self, items):
        """
        更新表格
        :param items: 新表格中的内容
        :return: 无
        """

        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()

        for item in items:

            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for index in range(len(item)):
                self.tableWidget.setItem(row, index, QTableWidgetItem(item[index]))

    def get_where_conditions(self):
        raise NotImplementedError("get_where_conditions() 需要被重载")
