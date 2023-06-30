# -*- coding: utf-8 -*-

"""
Module implementing loginDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from Ui_login import Ui_Dialog
from db import dbop
from dbop import check_login
from doctor_reg import doctor_reg_Dialog
from mainWindow_onlypatient import MainWindow_onlypatient
from query_abstract import query_abstract_Dialog
from query_medicine import query_medicine_Dialog
from reg import regDialog


class loginDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(loginDialog, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_patientlogin_clicked(self):
        """
        点击病患登录按钮
        """
        username = self.lineEdit_id.text()
        pwd = self.lineEdit_pwd.text()
        if username == "" or pwd == "":
            QMessageBox.warning(self, "警告", "请填写用户名或者密码！")
        else:
            self.checkPatientPwd(username, pwd)

    @pyqtSlot()
    def on_pushButton_doctorlogin_clicked(self):
        """
        点击医生登录按钮
        """
        # temp = query_medicine_Dialog(self)
        # temp.exec()
        id = self.lineEdit_id.text()
        pwd = self.lineEdit_pwd.text()
        QMessageBox.information(self, "成功", f"{check_login('doctor_accounts', id, pwd)}")

    @pyqtSlot()
    def on_pushButton_patientreg_clicked(self):
        """
        点击病患注册按钮
        """
        patientreg = regDialog(self)
        patientreg.exec()

    @pyqtSlot()
    def on_pushButton_doctorreg_clicked(self):
        """
        点击医生注册按钮
        """
        doctorreg = doctor_reg_Dialog(self)
        doctorreg.exec()

    def checkPatientPwd(self, usr, pwd):
        """
        检查用户名和密码是否正确
        """
        find_user = dbop.findPatient(usr)
        if find_user == 'connect_error':
            QMessageBox.warning(self, "警告", "数据库连接失败！")
        elif find_user == 'execute_error':
            QMessageBox.warning(self, "警告", "数据库执行失败！")
        elif find_user == 'no_user':
            QMessageBox.warning(self, "警告", "用户名不存在！")
        else:
            if dbop.pwdEncryption(pwd) == find_user[0][1]:
                QMessageBox.information(self, "提示", "登录成功！")
                self.main = MainWindow_onlypatient()
                self.main.show()
                self.hide()
            else:
                QMessageBox.warning(self, "警告", "密码错误！")
