import numpy as np

english_score = np.array([55, 89, 76, 65, 48, 70])
math_score = np.array([60, 85, 60, 68, np.nan, 60])
chinese_score = np.array([65, 90, 82, 72, 66, 77])

# 1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
print(np.mean(english_score), np.max(english_score), np.min(english_score), np.std(english_score))
print(np.nanmean(math_score), np.nanmax(math_score), np.nanmin(math_score), np.nanstd(math_score))
print(np.mean(chinese_score), np.max(chinese_score), np.min(chinese_score), np.std(chinese_score))
# 2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4] = 55
print(np.mean(math_score), np.max(math_score), np.min(math_score), np.std(math_score))
# 3. 用補考後資料找出與國文成績相關係數最高的學科?
more_related = "英文" if np.corrcoef(english_score, chinese_score)[1][0] > np.corrcoef(math_score, chinese_score)[1][
    0] else "數學"
print(more_related)
