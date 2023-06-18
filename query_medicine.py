# -*- coding: utf-8 -*-

"""
Module implementing query_medicine_Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

import dataClass
from Ui_login import Ui_Dialog
from query_abstract import query_abstract_Dialog


class query_medicine_Dialog(query_abstract_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(query_medicine_Dialog, self).__init__(
            database_name="medicine",
            table_title=['pharmacy_id', 'medicine_id', 'medicine_name'
                , 'medicine_category', 'medicine_price', 'medicine_stock']
            , parent=parent)
        # self.setupUi(self) #记得注释掉这句

    def get_where_conditions(self):
        pk_1 = self.plainTextEdit.toPlainText()
        pk_2 = self.plainTextEdit_2.toPlainText()
        pk_values = [pk_1, pk_2]
        pk_names = dataClass.primary_key_dict[self.database_name]

        where_conditions = [f"{pk_names[i]}='{pk_values[i]}'" for i in range(len(pk_values))]
        if pk_1 == pk_2 == "":
            where_conditions = "1=1"
        return where_conditions
