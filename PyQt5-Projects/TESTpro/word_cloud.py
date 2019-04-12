import sys
import jieba
import codecs
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
                            QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QIcon


class WordCloud(QWidget):
    def __init__(self, parent=None):
        super(WordCloud, self).__init__(parent)
        self.word_input = QTextEdit('在此输入文字')
        self.setWindowTitle('词云图生成器')
        self.setWindowIcon(QIcon('logo.ico'))
        self.resize(600, 600)
        layout = QVBoxLayout()
        btn_reset = QPushButton('重置')
        btn_reset.clicked.connect(lambda: self.reset_input())
        btn_converter = QPushButton('转换')
        btn_converter.clicked.connect(lambda: self.generate_img())
        layout.addWidget(self.word_input)
        layout.addWidget(btn_reset)
        layout.addWidget(btn_converter)
        self.setLayout(layout)

    def return_input(self):
        reply = QMessageBox.information(self, '当前输入', self.word_input.toPlainText(),
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def reset_input(self):
        self.word_input.setPlainText('')

    def generate_img(self):
        with open('轮子.txt', 'r', encoding="ANSI") as file:
            content = "".join(file.readlines())
        content_after = "".join(jieba.cut(content, cut_all=True))
        images = Image.open("heart_background.png")
        mask_images = np.array(images)
        wc = WordCloud(font_path="msyh.ttc", background_color="white", max_words=1000, max_font_size=500,
                       width=1500, height=1500, mask=mask_images).generate(content)
        plt.imshow(wc)
        wc.to_file('heart_of_love.png')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = WordCloud()
    obj.show()
    app.exec_()