# 数据类转换
# hex()：把一个整数转换成十六进制表示的字符串；
# def：定义一个函数
def my_abs(x):
    # 类型检查
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-9))

# pass：定义一个什么事也不做的空函数.作为一个占位符
def nop():
    pass

# 返回多个值[tuple]
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)
print(x,y)

# 函数的参数
# 1. 位置参数
def power(x):
    return x * x
# 2. 默认参数
# 2.1 必选参数在前，默认参数在后
# 2.2 多个参数时，变化大的参数在前，变化小的参数在后
# 2.3 默认参数必须指向不变对象
def power(x,n=2):
    s = 1
    while n>0:
        n = n - 1
        s = s * x
    return s    

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

# 3. 可变参数，允许传入任意参数，包括0
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 4. 关键字参数：允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动转化为dict
extra ={'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)
