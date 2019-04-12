import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton, \
                            QDesktopWidget, QMainWindow, QAction, qApp, QTextEdit, \
                            QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class MyMainWindow(QMainWindow):
    # 构造函数
    def __init__(self):
        super().__init__()
        self.tool_1 = self.addToolBar('工具_1')
        self.tool_2 = self.addToolBar('工具_2')
        self.tool_3 = self.addToolBar('工具_3')
        self.init_ui()

    # 初始化程序界面
    def init_ui(self):
        # 在窗口底部设置一个状态栏
        self.statusBar()
        self.statusBar().showMessage('This is a status bar')

        # 初始化窗口样式
        self.setWindowTitle('退学退课管理系统')
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(640, 360)

        # 设置my_exit_action用来退出程序
        my_exit_action = QAction(QIcon('logo.png'), '我的退出', self)
        # my_exit_action.setShortcut('Ctrl+Q')
        my_exit_action.setStatusTip('Click me to exit by your design')
        my_exit_action.triggered.connect(self.close)
        # 设置sys_exit_action用来退出程序
        sys_exit_action = QAction(QIcon('logo.png'), '系统退出', self)
        # sys_exit_action.setShortcut('Ctrl+Q')
        sys_exit_action.setStatusTip('Click me to exit by system design')
        sys_exit_action.triggered.connect(qApp.exit)
        # 设置nullAction什么都不做
        nullAction = QAction(QIcon('logo.png'), '空键', self)
        # nullAction.setShortcut('Ctrl+N')
        nullAction.setStatusTip('Click me to do nothing')
        # 设置quit退学按钮
        quit_action = QAction(QIcon('logo.png'), '一键退学', self)
        # quit_action .setShortcut('Ctrl+Z')
        quit_action.setStatusTip('Click me to quit NUAA')
        quit_action.triggered.connect(self.quit_school_msg)
        # 设置enroll按钮
        enroll_action = QAction(QIcon('logo.png'), '一键入学', self)
        # enroll_action .setShortcut('Ctrl+X')
        enroll_action.setStatusTip('Click me to enroll NUAA')
        enroll_action.triggered.connect(self.enroll_school_msg)
        # 设置quit_course按钮
        quit_course = QAction(QIcon('logo.png'), '一键退课', self)
        # enroll_action .setShortcut('Ctrl+X')
        quit_course.setStatusTip('Click me to quit course')
        quit_course.triggered.connect(self.quit_course_msg)

        # 设置退学按钮
        btn_1 = QPushButton('点我退学', self)
        btn_1.move(10, 65)
        btn_1.setToolTip('click me to quit school')
        btn_1.setStatusTip('click me to quit school')
        btn_1.clicked.connect(lambda: self.quit_school_msg())
        btn_1.resize(QPushButton.width(btn_1)+20, QPushButton.height(btn_1))
        # 设置退课按钮
        btn_2 = QPushButton('点我退课', self)
        btn_2.move(150, 65)
        btn_2.setToolTip('click me to quit course')
        btn_2.setStatusTip('click me to quit course')
        btn_2.clicked.connect(lambda: self.quit_course_msg())
        btn_2.resize(QPushButton.width(btn_2) + 20, QPushButton.height(btn_2))
        # 设置入学按钮
        btn_3 = QPushButton('点我入学', self)
        btn_3.move(10, 105)
        btn_3.setToolTip('click me to enroll school')
        btn_3.setStatusTip('click me to enroll school')
        btn_3.clicked.connect(lambda: self.enroll_school_msg())
        btn_3.resize(QPushButton.width(btn_3) + 20, QPushButton.height(btn_3))
        # 设置选课按钮
        btn_4 = QPushButton('点我选课', self)
        btn_4.move(150, 105)
        btn_4.setToolTip('click me to enroll course')
        btn_4.setStatusTip('click me to enroll course')
        btn_4.clicked.connect(lambda: self.enroll_course_msg())
        btn_4.resize(QPushButton.width(btn_4) + 20, QPushButton.height(btn_4))
        # 设置查询绩点按钮
        btn_5 = QPushButton('快速查询绩点', self)
        btn_5.move(10, 145)
        btn_5.setToolTip('click me to enroll course')
        btn_5.setStatusTip('click me to enroll course')
        btn_5.clicked.connect(lambda: self.check_score_msg())
        btn_5.resize(QPushButton.width(btn_5) + 50, QPushButton.height(btn_5))

        # 目录栏
        function_bar = self.menuBar()
        file = function_bar.addMenu('文件')
        file.addAction(my_exit_action)
        file.addAction(sys_exit_action)
        edit = function_bar.addMenu('编辑')
        edit.addAction(nullAction)
        quit = function_bar.addMenu('退学')
        quit.addAction(quit_action)
        enroll = function_bar.addMenu('入学')
        enroll.addAction(enroll_action)

        # 为工具栏绑定功能
        self.tool_1.addAction(nullAction)
        self.tool_2.addAction(nullAction)
        self.tool_3.addAction(nullAction)

        # 在程序中放一个输入文字的控件
        text_edit = QTextEdit()

        # 运行窗口
        self.show()

    # 重写程序退出函数
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出系统', "你想好了不退学了吗",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes: event.accept()
        else:
            event.ignore()

    def quit_school_msg(self):
        QMessageBox.information(self, "一键退学", "恭喜您已成功退学", QMessageBox.Yes)

    def enroll_school_msg(self):
        QMessageBox.information(self, "一键退学", "抱歉您入学失败", QMessageBox.Yes)

    def quit_course_msg(self):
        QMessageBox.information(self, "一键退课", "恭喜您已成功退课", QMessageBox.Yes)

    def enroll_course_msg(self):
        QMessageBox.information(self, "一键选课", "抱歉您选课失败", QMessageBox.Yes)

    def check_score_msg(self):
        QMessageBox.information(self, "快速查询绩点", "您的绩点2.0   \n抱歉保研失败", QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = MyMainWindow()
    sys.exit(app.exec_())
