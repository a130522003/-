# 修正千分位,問題
import pandas as pd
file = "平均月薪.csv"
dfwrong = pd.read_csv(file,thousands=(","))
dfwrong = dfwrong.set_index("x軸")
# # 取代,轉數字
# for col in dfwrong:
#     dfwrong[col] = dfwrong[col].str.replace(",", "").astype("int64")
outfile = "修正平均月薪.csv"
dfwrong.to_csv(outfile,sep = ",",index = True,header = True)

# print(dfwrong.info())  


