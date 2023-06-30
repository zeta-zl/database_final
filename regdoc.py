# -*- coding: utf-8 -*-

"""
Module implementing regdocDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox

from Ui_regdoc import Ui_Dialog
from db import dbop


class regdocDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(regdocDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_regdoc_pressed(self):
        """
        点击医生注册按钮
        """
        username = self.lineEdit_id.text()
        pwd = self.lineEdit_pwd.text()
        pwd_2 = self.lineEdit_pwd_2.text()
        name = self.lineEdit_name.text()
        title = self.comboBoxtitle.currentText()
        dept = self.lineEdit_dept.text()
        if username == "" or pwd == "" or pwd_2 == "" or name == "" or dept == "":
            QMessageBox.warning(self, "警告", "请填写完整信息！")
        elif pwd != pwd_2:
            QMessageBox.warning(self, "警告", "两次密码不一致！")
        elif self.checkpwd(pwd) == False:
            QMessageBox.warning(self, "警告", "密码至少包含八个字符，且包含数字和大小写字母！")
        else:
            encrypt_pwd = dbop.pwdEncryption(pwd)
            user_add_result = dbop.addDoctor(username, encrypt_pwd, name, title, dept)
            if user_add_result == "connect_error":
                QMessageBox.warning(self, "警告", "数据库连接失败！")
            elif user_add_result == "user_exist":
                QMessageBox.warning(self, "警告", "当前用户名已存在，请重新输入！")
            elif user_add_result == "excute_error":
                QMessageBox.warning(self, "警告", "数据库执行错误！")
            else:
                QMessageBox.information(self, "提示", "注册成功！")
                self.close()



    @pyqtSlot()
    def on_pushButton_cancel_pressed(self):
        """
        点击取消按钮
        """
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