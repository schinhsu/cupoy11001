import pandas as pd

# 讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
df1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
df2 = pd.read_csv('STOCK_DAY_0050_202010.csv')
# 串聯
df = df1.append(df2)
# 找出open小於close的資料
print(df[df.open < df.close])
