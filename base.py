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
print(r'\\\t\\') # 不转义
print(r'''hello, \n
world''')

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量名全部大写
