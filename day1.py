import numpy

# 題目:
# 1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a = numpy.arange(0, 21)
# print(a)
# 2.呈上題，將以上數列取出偶數。
b = a[::2]
# print(b)
# 3.呈1題，將數列取出3的倍數。
c = a[::3]
# print(c)
