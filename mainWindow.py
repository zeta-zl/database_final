# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import time

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_mainWindow import Ui_MainWindow
from db import dbop
from guahao import guahaoDialog
import curuser


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.InitUi()
    
    @pyqtSlot()
    def on_actionguahao_2_triggered(self):
        """
        Slot documentation goes here.
        """
        guahao = guahaoDialog(self)
        self.setCentralWidget(guahao)
    
    @pyqtSlot()
    def on_actionquyao_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionadzhuyuanpat_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionjiaohao_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionkaiyao_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionzhuyuandoc_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    def InitUi(self):
        loginTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        currentuser = curuser.getcuruser()
        self.statusbar.showMessage("当前用户："+currentuser+"  |  登录时间："+loginTime)
        currentopt = curuser.getcurrentopt()
        if currentopt == "patient":
            self.menu_2.menuAction().setVisible(False)
        elif currentopt == "doctor":
            self.menu.menuAction().setVisible(False)