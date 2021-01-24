import numpy

# 若是兩個陣列形狀不相同的話，遵循廣播規則，下面的例子可以正常運算。
a = numpy.arange(10)
b = 2
print(a * b)
c = numpy.random.randint(1, 10, 20).reshape(2, 10)
print(c)
print(a + c)
# 若沒有指定軸的話，則是回傳所有元素加總值
print(c.sum())
print(numpy.sum(c, axis=0))

# 歐拉常數 e
print(numpy.e)
print(numpy.exp(1))
# 可input array
print(numpy.exp(numpy.arange(5)))

# 對數 log
print(numpy.log10(numpy.array([1, 10, 100, 1000, 10000])))
print(numpy.log(9) / numpy.log(3))
# 若是 log(負數) 則會產生 nan 常數，NaN / NAN 為 nan (not a number) 的別名。
import warnings

warnings.filterwarnings('ignore')
print(numpy.log([-1, 1, 2]))

# 近似值
a = numpy.array([1.65, 1.55, -3.57, 2.0])
# 進行小數點第二位的 rounding
print(numpy.round(a, decimals=1))
print(numpy.round(a, decimals=0))
print(numpy.rint(a))
# 無條件捨去小數點
print(numpy.trunc(a))
print(numpy.floor(a))
print(numpy.ceil(a))
# 向0的方向取整數
print(numpy.fix(a))

# 絕對值
print(numpy.abs(a))
print(numpy.abs(1 + 2j))
