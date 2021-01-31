import numpy as np

# 1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
inverse_array1 = np.linalg.inv(array1)
result = array1 @ inverse_array1
print(result)
# 2. 運用上列array計算特徵值、特徵向量?
print(np.linalg.eig(array1))
# 3. 運用上列array計算SVD?
print(np.linalg.svd(array1))
