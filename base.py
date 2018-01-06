# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

number = input('请输入你的分数:')
a = int(number)
if a > 60:
    print('恭喜你，及格')
else:
    print('很抱歉，不及格')

# 转移符
print('I\'m ok.')
print('I\'m learning\nPython')
print(r'\\\t\\')  # 不转义
print(r'''hello, \n
world''')

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量名全部大写
# 字符串以Unicode编码，类型是str，在网络中以byte传输;
#!/usr/bin/env python3：
# -*- coding: utf-8 -*-：按utf-8读取
# ord：获取字符串的整数表示
print(ord('A'))
# chr：编码转换为对应的字符
print(chr(66))
# len：包含多少个字符
print(len('ABC'))
print(len('中文'.encode('utf-8')))
# 格式化。
# 1. %d：整数；%f：浮点数；%s：字符串；%x：十六进制整数
print('%2d-%02d' % (3, 1))
# 2. format
print('Hello, {0}, 成绩提升了{1}%'.format('小张',17.23))

# list：有序集合
