# -*- coding: utf-8 -*-

"""
Module implementing regDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QMessageBox

from Ui_reg import Ui_Dialog
from db import dbop


class regDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(regDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_regit_clicked(self):
        """
        Slot documentation goes here.
        """
        username = self.lineEdit_id.text()
        pwd = self.lineEdit_pwd.text()
        pwd_2 = self.lineEdit_pwd_2.text()
        name = self.lineEdit_name.text()
        id = self.lineEdit_idcardid.text()
        phone = self.lineEdit_phonenumber.text()
        if username == "" or pwd == "" or pwd_2 == ""or name == "" or id == "" or phone == "":
            QMessageBox.warning(self,"警告","请填写完整信息！")
        elif pwd != pwd_2:
            QMessageBox.warning(self,"警告","两次密码不一致！")
        elif self.checkpwd(pwd) == False:
            QMessageBox.warning(self,"警告","密码至少包含八个字符，且包含数字和大小写字母！")
        else:
            encrypt_pwd = dbop.pwdEncryption(pwd)


    @pyqtSlot()
    def on_pushButton_cancel_clicked(self):
        '''
        点击取消按钮
        '''
        self.close()


    def checkpwd(self, pwd):
        '''
        检查密码是否有效
        1 位数大于8位
        2 包含数字和大写字母与小写字母
        '''
        if len(pwd) < 8:
            return False
        flag = 0
        for i in pwd:
            if i.islower():
                flag += 1
            elif i.isupper():
                flag += 1
            elif i.isdigit():
                flag += 1
            if flag == 3:
                return True
        return False