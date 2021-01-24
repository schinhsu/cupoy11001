import numpy

print(numpy.__version__)
# array() 函式，可將 Python list 或元組 (tuple) 的值建立為 NumPy array
a = [1, 2, 3, 4, 5]
b = (6, 7, 8, 9, 10)
np1 = numpy.array(a)
np2 = numpy.array(b)
# print(np1)
# print(np2)
# arange() 函式，產生的序列數字包含起始值但不包含結束值
c = numpy.arange(1, 6)
# print(c == a)
# linspace() 函式，產生的序列數字包含起始值且包含結束值，並可指定區間內要產生幾個元素
d = numpy.linspace(6, 10, 5)
# print(d == b)
# zeros()、ones() 函式，可以依照傳入的形狀引數，建立元素全為 0、全為 1 的陣列
e = numpy.zeros((2, 5))
f = numpy.ones((2, 5))
# print(e)
# print(f)
# empty() 函式則是不初始化陣列原始值，只給定指定形狀的陣列，初始元素值會隨機給定
g = numpy.empty((2, 5))
# print(g)
# 隨機產生陣列元素的函式
# rand()，[0, 1)
h = numpy.random.rand()
print(h)
i = numpy.random.rand(2, 4)
print(i)
# randn()，常態分布
j = numpy.random.randn()
print(j)
k = numpy.random.randn(2, 4)
print(k)
l = numpy.random.randn(3, 5) + 2.1
print(l)
# randint()，隨機整數
m = numpy.random.randint(4, high=10, size=10)
print(m)
