# -*- coding:utf-8 -*-

a4 = ["a", "b", "c", "d"]

_3a4 = a4 * 3
print(_3a4)
# 压缩 打包为元组的列表
_3zip4 = zip(_3a4)
print(list(_3zip4))
# 与 zip 相反，可理解为解压
_3unzip4 = zip(*_3a4)
print(list(_3unzip4))

# 举例子，两个
a = [1, 2, 3]
b = [4, 5, 6]
zipped = zip(a, b)
print(list(zipped))
unzip = zip(*zip(a, b))
print(list(unzip))

# 举例子，三个
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
zipped = zip(a, b, c)
print(list(zipped))
unzip = zip(*zip(a, b, c))
print(list(unzip))