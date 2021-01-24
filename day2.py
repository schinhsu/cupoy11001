import numpy

# 題目:

# 1.將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = numpy.array(range(30))
array = array1.reshape((5, 6), order='F')
print(array)
# 2.呈上題的array，找出被6除餘1的數的索引
b = numpy.where(array % 6 == 1)
print(b)
