"""
将华氏温度转换为摄氏温度

Version: 1.0
Author: 成达
"""
f = float(input('清输入华氏温度'))
c = (f-32)/1.8
print('%.1f华氏温度 = %.1f摄氏温度'%(f,c))
print(f'{f:.1f}华氏温度 = {c:.1f}设施温度')