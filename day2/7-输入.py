# 作者: 王道 龙哥
# 2025年12月24日15时42分55秒
# xxx@qq.com
age = input('请输入你的年龄:')
print(type(age))
# int不可以转带小数点的字符串
new_age = int(float(age))
print(new_age + 10)
