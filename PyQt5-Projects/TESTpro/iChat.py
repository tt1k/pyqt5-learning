import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, \
                            QPushButton, QLabel, QHBoxLayout, QTextEdit, \
                            QMessageBox
from PyQt5.QtGui import QIcon


class iChat(QWidget):
    def __init__(self, parent=None):
        super(iChat, self).__init__(parent)
        self.setWindowTitle('iChat')
        self.setWindowIcon(QIcon('logo.ico'))
        self.resize(600, 500)
        send_btn = QPushButton('发送')
        cancel_btn = QPushButton('取消')
        button_layout = QHBoxLayout()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(send_btn)
        window_label = QLabel()
        text_edit = QTextEdit()
        text_edit.setPlainText('在此输入文本')
        layout = QVBoxLayout()
        layout.addWidget(window_label)
        layout.addWidget(text_edit)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.show()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '退出', '确定退出程序？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.No:
            QCloseEvent.ignore()
        else:
            QCloseEvent.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = iChat()
    app.exec_()