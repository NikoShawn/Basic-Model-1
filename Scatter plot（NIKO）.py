# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:16:40 2019

@author: admin
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]     #第一组数据

x2 = [1, 2, 3, 4]
y2 = [2, 3, 4, 5]    #第二组数据

n = 10
x3 = np.random.randint(0, 5, n)
y3 = np.random.randint(0, 5, n)   #使用随机数产生

plt.scatter(x1, y1, marker = 'x',color = 'red', s = 40 ,label = 'First')
#                   记号形状       颜色           点的大小    设置标签
plt.scatter(x2, y2, marker = '+', color = 'blue', s = 40, label = 'Second')
plt.scatter(x3, y3, marker = 'o', color = 'green', s = 40, label = 'Third')
plt.legend(loc = 'best')    # 设置 图例所在的位置 使用推荐位置

plt.show()  
