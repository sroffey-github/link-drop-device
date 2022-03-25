from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
import sys

msg = sys.argv[1]

app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QWidget()
grid_layout = QGridLayout()
labelA = QtWidgets.QLabel(mainWindow)
labelA.setText(msg)
mainWindow.setWindowTitle('Label Example')
mainWindow.setGeometry(1, 1, 300, 100)
grid_layout.addWidget(labelA, 1, 0, -1, 1)
topRightPoint = QApplication.desktop().availableGeometry().topRight()
mainWindow.move(topRightPoint)
mainWindow.show()
sys.exit(app.exec_())