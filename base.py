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
classmattes = ['Michael','Bob','Tracy']
print(classmattes)
# 获取最后一个元素
print(classmattes[-1])
# append：list追加元素到末尾
# insert：插入到指定位置
# pop：删除list末尾的元素或pop(i)：删除指定位置的元素

# tuple【元组】：一旦初始化就不能修改，即每个元素的指向永远不变
classmattes = ('Michael','Bob','Tracy')
# 定义tuple时，元素就必须被确定下来

# 循环
# 1. for...in循环。range：生成一个整数序列
# 2. while
# 3. break：允许提前退出循环
# 4. continue：提前结束本轮循环，并直接开始下一轮循环