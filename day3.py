import numpy

# 題目:
# 運用投影片中的分貝公式回答下列問題。
# 1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
V1 = 20000
V0 = 20
ans1 = numpy.log10(V1 / V0) * 20
print(ans1)
# 2.30分貝的聲壓會是50分貝的幾倍?
V30 = numpy.power(10, 30 / 20)
V50 = numpy.power(10, 50 / 20)
ans2 = V30 / V50
print(ans2)
