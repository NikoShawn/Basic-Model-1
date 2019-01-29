# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:43:54 2019

@author: admin
"""

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

# pyexcel_xls 以 OrderedDict 结构处理数据
from collections import OrderedDict
 
from pyexcel_xls import get_data
from pyexcel_xls import save_data
 
 
def read_xls_file():
    xls_data = get_data(r"C:\Users\admin\Desktop\D01.xlsx")
    print("Get data type:", type(xls_data))
    for sheet_n in xls_data.keys():
        print(sheet_n, ":", xls_data[sheet_n])
 
 
if __name__ == '__main__':
    read_xls_file()

y = np.random.standard_normal((1000,2))
c = np.random.randint(0,10,len(y))
plt.scatter(y[:,0],y[:,1],c=c,marker='o')   # 必須使用 plt.scatter 不能使用plt.plot
plt.colorbar()
plt.title('Position Plot',size=20)
plt.grid(True)

plt.xlabel('1st',size=20)
plt.ylabel('2 nd',size=20)

plt.show()