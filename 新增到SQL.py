#%% 讀進SQLite
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3

def ADD_SQL(csv_file, table_name, db_file):
    # 讀取 csv 檔案
    df = pd.read_csv(csv_file)

    # 創建 SQLite 連接
    conn = sqlite3.connect(db_file)

    # 將 DataFrame 寫入 SQLite 表格 index是SQL自己新增所以不要
    df.to_sql(table_name, conn, if_exists="replace", index = False)

    # 關閉 SQLite 連接
    conn.close()
# 呼叫ADD_SQL()
csv1 = "修正平均月薪.csv"
table_name1 = "月薪"
db = "就業勞動相關資料.sqlite"
ADD_SQL(csv1, table_name1, db)

csv2 = "月薪資上年同期增減率.csv"
table_name2 = "去年同期增減"
ADD_SQL(csv2, table_name2, db)

csv3 = "求才利用率.csv"
table_name3 = "求才利用率"
ADD_SQL(csv3, table_name3, db)

csv4 = "離職失業率.csv"
table_name4 = "離職失業率"
ADD_SQL(csv4, table_name4, db)

csv5 = "正常工時.csv"
table_name5 = "正常工時"
ADD_SQL(csv5, table_name5, db)

csv6 = "加班工時.csv"
table_name6 = "加班工時"
ADD_SQL(csv6, table_name6, db)