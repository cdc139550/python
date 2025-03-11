"""
输入半径计算圆的周长和面积

Version: 1.0
Author: 成达
"""
import math
r = float(input('输入半径'))
c = 2*math.pi*r
s = math.pi*r**2
print(f'周长:{c:2f}')
print(f'面积：{s:2f}')