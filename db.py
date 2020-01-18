
'''#  sql 搜尋'''
import sqlite3
conn = sqlite3.connect ('sTock.db')
from flask import render_template

# df.to_sql("todo",conn, if_exists="replace")

'''
SQL 搜尋
'''
k =[]
cursor = conn.execute('select 股票,代號,股價淨值比,殖利率,本益比 from todo')
rows = cursor.fetchall()# 顯示全部

#轉至  分成 index 跟 item 兩個項目        
def search_enumera(s):
        
        for index, item in enumerate(rows):
        
            if item[1] == s:

                print(item)

                return item





# b =new_dict.get(a)
# print(b)
        # s= dct.tuple.select('台泥')
#         print(s)

# a = new_dict.values['1102']
# a =new_dict
# print(pd.DataFrame(a))



    
# print(value)



# a= new_dict

conn.close
