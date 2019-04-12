import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton, \
                            QDesktopWidget, QMainWindow, QAction, qApp, QTextEdit, \
                            QLabel, QHBoxLayout, QVBoxLayout, QDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.Qt import QLineEdit, QTextEdit


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
        self.statusBar().showMessage('Designed by HR : status bar')
        self.setWindowTitle('Word Cloud Converter')
        self.setFixedSize(1200, 680)
        self.setWindowIcon(QIcon('../image/logo.ico'))
        # set actions
        file_action_1 = QAction(QIcon('logo.ico'), 'Open file', self)
        file_action_1.setStatusTip('Click me to Open File')
        file_action_1.triggered.connect(self.close)
        file_action_2 = QAction(QIcon('logo.ico'), 'Close file', self)
        file_action_2.setStatusTip('Click me to Close File')
        file_action_2.triggered.connect(self.close)
        info_action_1 = QAction(QIcon('logo.ico'), 'About me', self)
        info_action_1.setStatusTip('Click me to See Info')
        info_action_1.triggered.connect(self.show_info)
        # set menuBar
        menu_bar = self.menuBar()
        file = menu_bar.addMenu('File')
        file.addAction(file_action_1)
        file.addAction(file_action_2)
        info = menu_bar.addMenu('Info')
        info.addAction(info_action_1)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Close Project', "Sure to Close This ?", QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes: event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.statusBar().showMessage('U clicked Escape')
            self.close()
        if event.key() == Qt.Key_W:
            self.statusBar().showMessage('This is a Bonus Time')
            msg = QMessageBox.question(self, 'Bingo', 'U Found me!', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def show_info(self):
        QMessageBox.information(self, 'About me', 'Designed by HR', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MyMainWindow()
    app.exec_()
