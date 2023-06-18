import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import login

if __name__ == '__main__':
    for_test = 3333421
    QApp = QApplication(sys.argv)
    login = login.loginDialog()
    login.show()
    sys.exit(QApp.exec())
