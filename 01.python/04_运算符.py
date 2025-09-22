# 1-02-8
"""
快捷键:
格式化代码：Ctrl + Alt + L
复制光标所在行：Ctrl + D
添加注释: Ctrl + /
"""
"""
算术运算符: + - * / // % **
赋值运算符: =
复合赋值运算符: += -= *= //= /= %= **=
比较运算符: == != > < >= <=
逻辑运算符: and or not
"""
# 算术运算符: + - * / //(取商) %(取余) **(幂运算)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
print('============================')
# 赋值运算符: =
a = 10
# 复合赋值运算符: += -= *= //= /= %= **=
a += 3
print(a) #13
a -= 3
print(a) #10
a *= 3
print(a) #30
a /= 3
print(a) #10.0
a //= 3
print(a) #3.3
a %= 3
print(a) #0.0
a **= 3
print(a) #0.0
print('============================')
# 比较运算符: == != > < >= <=
print(10 == 3) #False
print(10 != 3) #True
print(10 > 3) #True
print(10 < 3) #False
print(10 >= 3) #True
print(10 <= 3) #False
print('============================')
# 逻辑运算符: and(有假则假) or(有真则真) not(取反)
print(False or True) #True
print(False and True) #False
print(not False) #True