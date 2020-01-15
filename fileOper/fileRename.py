#coding=utf-8
import os

path = './壁纸'
# 计算文件夹下文件数量生成list
i = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        i += 1
a = list(range(1, i + 1))

# 打乱list
import random
random.shuffle(a)

# 重命名
i = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        # 取后缀，名字按照2位前补零重命名
        (filename, extension) = os.path.splitext(file)
        filename = "{:0>2d}".format(a[i]) + extension
        i += 1
        os.rename(os.path.join(path, file), os.path.join(path, filename))
