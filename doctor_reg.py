# -*- coding: utf-8 -*-

"""
Module implementing doctor_reg_Dialog.
"""
import re

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox

import dataClass
import dbop
from Ui_doctor_reg import Ui_Dialog


def check_password(password):
    """
    检查密码
    1.长度大于等于8
    2.仅由字母数字下划线构成
    3.小写字母，大写字母，数字至少各一
    :param password: 待检查的密码
    :return: 是否通过检查
    """
    if len(password) < 8:
        return False

    if not re.match(r'^[A-Za-z0-9_]+$', password):
        return False

    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    return has_lowercase and has_uppercase and has_digit


class doctor_reg_Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(doctor_reg_Dialog, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_regit_3_clicked(self):
        """
        注册按钮
        """
        _input = self.get_input()
        if self.check_input(_input):
            res = self.insert(_input)
            if res:
                QMessageBox.information(self, "提示", "注册成功")
            else:
                QMessageBox.information(self, "提示", "注册失败，请检查您的ID是否填写正确")

    def get_input(self):
        """
        提取输入
        :return: 字典，用于获得各个框中的输入
        """

        return {
            'id': self.lineEdit_id_3.text(),
            'name': self.lineEdit_id_4.text(),
            'psw': self.lineEdit_pwd_5.text(),
            'rep_psw': self.lineEdit_pwd_6.text()
        }

    def check_input(self, input):
        """
        检查输入合法性，包括密码重复检查以及密码强壮性检查
        :return: 成功与否
        """
        if not all(value != '' for value in input.values()):
            QMessageBox.warning(self, "警告", "请填写完整信息！")
        elif not check_password(input['psw']):
            QMessageBox.warning(self, "警告", "密码至少包含八个字符，由数字，字母和下划线构成，且包含数字和大小写字母！")
        elif input['psw'] != input['rep_psw']:
            QMessageBox.warning(self, "警告", "两次密码不一致！")
        else:
            return True
        return False

    def insert(self, input):
        """
        插入数据库
        """
        doctor = dataClass.doctor_data(doctor_id=input['id'], doctor_name=input['name'])
        ret1 = dbop.insert_into_table('doctor', doctor, True)

        doctor_account = dataClass.doctor_accounts_data(doctor_id=input['id'],
                                                        password=dbop.pwdEncryption(input['psw']))
        ret2 = dbop.insert_into_table('doctor_accounts', doctor_account, True)
        print(ret1, ret2)
        return ret1 is None and ret2 is None
