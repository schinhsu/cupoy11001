import pandas as pd

# 讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案
df = pd.read_csv('boston.csv')
df[['CHAS', 'NOX', 'RM']].to_excel('output.xlsx',index=False)
