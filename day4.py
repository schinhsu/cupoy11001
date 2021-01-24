import numpy

# 題目:
english_score = numpy.array([55, 89, 76, 65, 48, 70])
math_score = numpy.array([60, 85, 60, 68, 55, 60])
chinese_score = numpy.array([65, 90, 82, 72, 66, 77])
# 上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，
# 舉例第一位同學英文55分、數學60分、國文65分，運用上列數據回答下列問題。
#
# #1.有多少學生英文成績比數學成績高?
compare = numpy.greater(english_score, math_score)
# ans1 = list(compare).count(False)
ans1 = numpy.sum(compare)
print(ans1)
# #2.是否全班同學最高分都是國文?
highest = numpy.logical_and(chinese_score > english_score, chinese_score > math_score)
ans2 = numpy.all(highest)
print(ans2)
