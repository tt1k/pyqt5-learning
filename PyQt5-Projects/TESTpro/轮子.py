import jieba
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

with open('轮子.txt', 'r', encoding="ANSI") as file:
    content = "".join(file.readlines())
content_after = "".join(jieba.cut(content, cut_all=True))

# 添加的代码,把刚刚你保存好的图片用Image方法打开
# 然后用numpy转换了一下
images = Image.open("heart_background.png")
mask_images = np.array(images)

# 修改了一下wordCloud参数,就是把这些数据整理成一个形状
# 具体的形状会适应你的图片的
wc = WordCloud(font_path="msyh.ttc", background_color="white", max_words=1000, max_font_size=500,
               width=1500, height=1500, mask=mask_images).generate(content)
plt.imshow(wc)

# 生成词图
wc.to_file('heart_of_love.png')
