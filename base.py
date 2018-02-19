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
# 列表生成器：range()

# tuple【元组】：一旦初始化就不能修改，即每个元素的指向永远不变
classmattes = ('Michael','Bob','Tracy')
# 定义tuple时，元素就必须被确定下来

# 循环[迭代]
# 1. for...in循环。range：生成一个整数序列
# 2. while
# 3. break：允许提前退出循环
# 4. continue：提前结束本轮循环，并直接开始下一轮循环
# 5. 用切片代替
# 6. 可迭代对象：通过`isinstance()`判断一个对象是否是Iterable对象
# 7. 迭代器(Iterator)：被next()函数调用并不断返回下一个值的对象，可以使用isinstance()判断一个对象是否是Iterator对象
# 8. 生成器：一边循环一边计算的机制；包含yield变量即为generator; 调用next()的时候执行，遇到yield语句返回
# 8.1 Iterable类型：作用于for循环的对象，如list、dict、str等
# 8.2 Iterator类型：作用于next()函数的对象，一个惰性计算的序列；
# 8.3 for循环：通过不断调用next()函数实现的
g = (x * x for x in range(10))
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'