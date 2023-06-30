import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog

import login
from db import sharedata

if __name__ == '__main__':
 
    QApp = QApplication(sys.argv)
    login = login.loginDialog()
    login.show()
    sys.exit(QApp.exec())