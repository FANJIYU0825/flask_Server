import requests
import datetime
import pandas as pd
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot
import os,shutil
import twstock
import sqlite3




#stock_no = '2337'
# stock_no = str(input('\n查詢股票收盤價歷史線圖\n\n請輸入上公司股票代號 : '))
def path(stock_no):

    if stock_no.isdigit():
    
        stock_csv = 'templates' + '\\' + stock_no + '.csv'
        stock_html = stock_no + '.html'
        d_stock_html = 'templates' +'\\' + stock_no + '.html'
        stock_id = stock_no + '.TW'
        filepath = 'templates'+ '\\' + stock_no +'_2y.csv'


        now = int(datetime.datetime.now().timestamp())+86400
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
# requests.post : get url & 傳送參數
        response = requests.post(url)
    
#產生2年歷史股價csv資料檔
        if not os.path.exists("data"):
            os.mkdir("data")
    
        with open(stock_csv,'w') as f:
            f.writelines(response.text)
  
            f.close()   
            data = pd.read_csv(stock_csv)
            df = pd.DataFrame(data)
            # conn = sqlite3.connect ('sTock.db')
            # df.to_sql("todo",conn, if_exists="replace")
            try:
                
                # 將今日str日期,倒推2年前

                today= str(datetime.date.today())

                date_str = str(int(today[0:4])-2) + today[4:8] + '01'
                #print(date_str)
                
                df1 = df.loc[df["Date"] >= date_str ]
#print('寫csv檔')
                df1.to_csv(filepath,encoding='big5',index=False)


#繪製個股歷史股價圖html檔
                pdstock = pd.read_csv(filepath, encoding='big5')  #以pandas讀取檔案

                real = twstock.realtime.get(stock_no) # 取得股票中文名稱
                if real['success']:  #如果讀取成功  
                    stock_name = real['info']['name']    
                else:
                    print('錯誤：' + real['rtmessage'])  
                stock_title = stock_name +'('+stock_no+')' + ' 近2年股價收盤歷史線圖'
                data = [Scatter(x=pdstock['Date'], y=pdstock['Close'], name='Close')]
                plot({"data": data, "layout": Layout(title=stock_title)},auto_open= False)
    
                shutil.copy('temp-plot.html',d_stock_html)    
                print('\n目前股價：',real['realtime']['latest_trade_price'])   
                print('\n查詢成功 ! 請查看 {} 歷史股價線圖' .format(stock_name)) 

                #   os.rename('temp-plot.html',stock_html)
                #   shutil.move(stock_html,d_stock_html)
    
            except:
                print('股票代號輸入錯誤  !!')     

    else:
        print('股票代號須為數字 !!')

