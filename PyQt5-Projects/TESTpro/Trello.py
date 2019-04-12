# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QListWidget, QMessageBox, \
                            QHBoxLayout, QPushButton, QDialog, QLineEdit, QMenu, QAction, QLabel
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
import qdarkstyle
import sys


class Trello(QMainWindow):
    def __init__(self, parent=None):
        super(Trello, self).__init__(parent)
        # 窗体设置
        self.setFixedSize(360, 600)
        # self.resize(300, 600)
        self.setWindowTitle("MyTrello")
        self.list = QListWidget()
        self.list.setFixedWidth(300)
        self.label = QLabel('What to Do')
        self.setWindowIcon(QIcon('trello_logo.ico'))

        # menuBar
        add_list = QAction(QIcon('trello_logo.ico'), 'Add List', self)
        add_list.triggered.connect(self.add_list_function)
        about_action = QAction(QIcon('trello_logo.ico'), 'About', self)
        about_action.triggered.connect(self.about_function)
        function_bar = self.menuBar()
        file = function_bar.addMenu('File')
        file.addAction(add_list)
        about = function_bar.addMenu('About')
        about.addAction(about_action)

        # button以及button布局
        btn_add = QPushButton('Add')
        btn_add.setFixedWidth(60)
        btn_add.clicked.connect(lambda: self.btn_add_function(self.list))
        btn_del = QPushButton('Del')
        btn_del.setFixedWidth(60)
        btn_del.clicked.connect(lambda: self.btn_del_function(self.list))
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_del)

        # 窗体布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list)
        layout.addLayout(btn_layout)
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(layout)
        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        # 设置右键删除
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction(QIcon('trello_logo.ico'), '|  删除')
        self.customContextMenuRequested.connect(lambda: self.show_context_menu())
        self.contextMenu.triggered[QAction].connect(lambda: self.right_hand_remove())

    # 显示右键目录
    def show_context_menu(self):
        items = self.list.selectedIndexes()
        if items:
          self.contextMenu.show()
          self.contextMenu.exec_(QCursor.pos())

    # 删除
    def right_hand_remove(self):
        cur = self.list.currentRow()
        self.list.removeItemWidget(self.list.takeItem(cur))

    # add button函数
    def btn_add_function(self, qlist):
        # dialog设置
        dialog = QDialog()
        dialog.setWindowIcon(QIcon('trello_logo.ico'))
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setWindowTitle('Add new task')
        dialog.setFixedSize(300, 120)
        # dialog控件设置
        line_edit = QLineEdit('Edit new task')
        dialog_btn = QPushButton('OK')
        dialog_btn.setFixedWidth(60)
        dialog_btn.clicked.connect(lambda: self.submit_new_task(line_edit, dialog, qlist))
        # dialog样式设置
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(dialog_btn)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(line_edit)
        dialog_layout.addLayout(btn_layout)
        dialog.setLayout(dialog_layout)
        dialog.exec_()

    # 删除选中item
    def btn_del_function(self, qlist):
        cur = qlist.currentRow()
        qlist.removeItemWidget(qlist.takeItem(cur))

    # 添加新的一行
    def submit_new_task(self, line_edit, dialog, qlist):
        qlist.addItem(line_edit.text())
        dialog.close()

    def submit_new_list(self, dialog):
        dialog.close()

    def add_list_function(self):
        # dialog设置
        dialog = QDialog()
        dialog.setWindowIcon(QIcon('trello_logo.ico'))
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setWindowTitle('Add New List')
        dialog.setFixedSize(300, 120)
        # dialog控件设置
        line_edit = QLineEdit('Edit New Name')
        dialog_btn = QPushButton('OK')
        dialog_btn.setFixedWidth(60)
        dialog_btn.clicked.connect(lambda: self.submit_new_list(dialog))
        # dialog样式设置
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(dialog_btn)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(line_edit)
        dialog_layout.addLayout(btn_layout)
        dialog.setLayout(dialog_layout)
        dialog.exec_()
        self.setFixedSize(self.width()+360, 600)
        # self.resize(self.width()+300, 600)
        btn_add = QPushButton('Add')
        btn_add.setFixedWidth(60)
        btn_add.clicked.connect(lambda: self.btn_add_function(new_list))
        btn_del = QPushButton('Del')
        btn_del.setFixedWidth(60)
        btn_del.clicked.connect(lambda: self.btn_del_function(new_list))
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_del)
        new_list = QListWidget()
        new_list.setFixedWidth(300)
        new_label = QLabel()
        new_label.setText(line_edit.text())
        new_layout = QVBoxLayout()
        new_layout.addWidget(new_label)
        new_layout.addWidget(new_list)
        new_layout.addLayout(btn_layout)
        self.main_layout.addLayout(new_layout)

    def return_new_list_name(self, line_edit):
        return line_edit.text()

    def about_function(self):
        QMessageBox.about(self, 'MyTrello', 'The Best Task Manager For U')

    def closeEvent(self, event):
        QMessageBox.about(self, 'MyTrello', 'Know What to Do Everyday')
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    run = Trello()
    run.show()
    sys.exit(app.exec_())
