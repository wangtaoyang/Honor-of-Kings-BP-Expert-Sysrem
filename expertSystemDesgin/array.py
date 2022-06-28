#!/usr/bin/env python
# encoding: utf-8
'''
@Author  : pentiumCM
@Email   : 842679178@qq.com
@Software: PyCharm
@File    : __init__.py.py
@Time    : 2020/4/11 9:39
@desc	 : numpy计算矩阵的特征值，特征向量
'''

import numpy as np

mat = np.array([[1, 0.2, 0.5],
                [5, 1, 3],
                [2, 0.33, 1]])

eigenvalue, featurevector = np.linalg.eig(mat)

print("特征值：", eigenvalue)
print("特征向量：", featurevector)
