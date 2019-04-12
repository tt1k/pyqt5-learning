import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPalette, QPixmap
from PyQt5.QtCore import Qt


class MoveButton(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.btn_1 = QPushButton('超级棒！', self)
        self.btn_1.setGeometry(200, 550, 90, 30)
        self.btn_1.clicked.connect(lambda: self.ok_msg())
        self.btn_2 = QPushButton('一般般吧', self)
        self.btn_2.setGeometry(910, 550, 90, 30)
        self.btn_2.clicked.connect(lambda: self.switch())
        self.origin = self.btn_2.geometry().x()
        self.setFixedSize(1200, 680)
        self.setWindowTitle('灿哥加油')
        self.setWindowIcon(QIcon('logo.ico'))
        label1 = QLabel(self)
        label3 = QLabel(self)
        label1.setText("<h1>我就问你灿哥棒不棒！！！</h1>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label1.setGeometry(100, 100, 1000, label1.geometry().height())
        label3.setAlignment(Qt.AlignCenter)
        label3.setPixmap(QPixmap("./source.jpg"))
        label3.move(400, 150)

    def ok_msg(self):
        QMessageBox.information(self, '加油', '灿哥你是最棒的！！！', QMessageBox.Ok)
        app.quit()

    def closeEvent(self, event):
        event.ignore()

    def switch(self):
        if self.btn_2.geometry().x() == self.origin:
            self.btn_2.move(self.origin - 200, self.btn_2.geometry().y())
        else:
            self.btn_2.move(self.origin, self.btn_2.geometry().y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MoveButton()
    obj.show()
    app.exec()
