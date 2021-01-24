import numpy

# 透過 flatten() 與 ravel() 均可將多維陣列轉形為一維陣列
a = numpy.array([[0, 1, 2, 3],
                 [4, 5, 6, 7],
                 [8, 9, 10, 11]])
b = a.flatten()
b[3] = 12
print(b)
print(a)
# ravel() 建立的是原來陣列的 view，所以在 ravel() 回傳物件中做的元素值變更，將會影響原陣列的元素值。
b = a.ravel()
b[3] = 12
print(b)
print(a)
# flatten() 與 ravel() 引數 order 預設值為 C
# C 的意義是 C-style，展開時是以 row 為主的順序展開；
# 而 F 是 Fortran-style，展開時是以 column 為主的順序展開。
print(a.ravel(order='C'))
print(a.ravel(order='F'))
# np.reshape(a, new_shape) 或 a.reshape(new_shape, refcheck=True)
c = numpy.arange(15)
print(c.reshape((3, 5)))
print(numpy.reshape(c, (3, 5)))
print(c.reshape((3, 5)) == numpy.reshape(c, (3, 5)))
print(c.size)
# 若 reshape 後的陣列元素值改變，會影響原陣列對應的元素值也跟著改變。
d = c.reshape((3, 5))
d[0, 2] = 100
print(d)
print(c)
# np.resize(a, new_shape) 或 a.resize(new_shape, refcheck=True)
c.resize((4, 3), refcheck=False)
print(c)

# 3-dim array
e = numpy.array([[[1, 2, 3], [4, 5, 6],
                  [7, 8, 9], [10, 11, 12]],
                 [[1, 2, 3], [4, 5, 6],
                  [7, 8, 9], [10, 11, 12]]])
print(e.shape, e.size)
# a.sum(axis=0) 變化第一個維度加總
print(e.sum(axis=0))
print(e.sum(axis=1))

# 要增加軸數的話，可以使用 np.newaxis 物件
f = numpy.arange(12).reshape(2, 6)
print(f)
print(f[:, numpy.newaxis, :])
print('-----------------------------')
# concatenate() 進行陣列的合併時，須留意除了指定的軸之外 (預設為 axis 0)，其他軸的形狀必須完全相同
# 不增加維度
g = numpy.arange(10).reshape(5, 2)
h = numpy.arange(6).reshape(3, 2)
print(numpy.concatenate((g, h)))
# stack() 必須要所有陣列的形狀都一樣，增加維度
# stack(axis=1) (5*2)*2
# stack(axis=0) 2*(5*2)
i = numpy.arange(10).reshape(5, 2)
print((numpy.stack((g, i), axis=1)))
print((numpy.stack((g, i), axis=0)))
# hstack() 5*(2+2):水平軸，不增加維度
print(numpy.hstack((g, i)))
# vstack() (5+5)*2:垂直軸，不增加維度
print(numpy.vstack((g, i)))

# split
print('----------------------------------')
j = numpy.arange(10).reshape(5, 2)
print(j)
# 如果給定單一整數的話，那就會按照軸把陣列等分
print(numpy.split(j, 5))
# 如果給定一個 List 的整數值的話，就會按照區段去分割
# ary[:2]
# ary[2:3]
# ary[3:]
print(numpy.split(j, [2, 3]))
k = numpy.arange(30).reshape(5, 6)
print(numpy.hsplit(k, 3))
print(numpy.hsplit(k, [2, 3, 5]))
print(numpy.vsplit(k, [2, 4, 6]))

print('-----------------------------')
for row in k:
    print(k)
for entry in k.flat:
    print(entry)
print('-----------------------------')
l = numpy.random.randint(1, 20, 10)
print(l)
# 陣列中最大的元素值
print(numpy.amax(l))
# 陣列中最小的元素值
print(numpy.amin(l))
# 若設定 keepdims=True，結果會保留原陣列的維度來顯示。
m = l.reshape(2, 5)
print(m)
print(numpy.amax(m, keepdims=True))
print(m.max(axis=1))
# 若沒有指定軸的話，argmax() 與 argmin() 會回傳多維陣列展平後的索引。
print(numpy.argmax(m))
# # 列出各 row 的最大值索引, 分別為 [0, 0, 2, 1]
print(numpy.argmax(m, axis=1))
# where 回傳值為符合條件的元素索引
# 回傳的索引陣列要合併一起看
print(numpy.where(m > 10))
print(numpy.where(m > 10, "Y", "N"))
# nonzero 等同於 np.where(array != 0) 的語法

# sort() 回傳的是排序後的陣列
# argsort() 回傳的是排序後的陣列索引值
