from flask import Flask, request, render_template,url_for,request
from db import search_enumera
from fuct_scrw import path

app = Flask(__name__)



@app.route("/")#主頁面
def index():
    
    return render_template ('home_page.html' )


@app.route("/search_Page", methods=['GET', 'POST'])#搜尋網站
def search_Page():
    
    return render_template ('search_Page.html', )

    
@app.route('/everyD_recomend', methods=['GET', 'POST'])#每日推薦
def everyD_recomend():
    m={  '1' : '/stock_chart/2883',
        '2' : '/stock_chart/3706',
        '3' : '/stock_chart/2889',
        '4' : '/stock_chart/2890',
        '5' : '/stock_chart/2885',
        '6' : '/stock_chart/5519',
        '7' : '/stock_chart/2330',
        '8' : '/stock_chart/2317',
        '9' : '/stock_chart/1201'}
    
    return render_template('everD_test.html' , everyD = m )


@app.route("/search_result", methods=['GET', 'POST'])#查詢結果
def submit():
        if request.method == 'POST':
            a = request.form['email']
            a = int(a)
            if a == 2330:
                stock_no = a
                b = '2330none'
                c = '2330over'
                d = '2330fit'
                stock_no = str(stock_no)
                no = search_enumera(a)
                path(stock_no)
                keys = ['當前走勢', '過去走勢 1', '過去走勢 2','未來走勢']
                values = [f'/stock_chart/{a}', f'/stock_chart/{b}', f'/stock_chart/{c}',f'/stock_chart/{d}']
                data = dict(zip(keys, values))   
                return render_template ('search_result.html',data = data, a =a  ,no=no)

            else:
                stock_no = a
                no = search_enumera(a)
                stock_no = str(stock_no)
                keys = ['當前走勢', '過去走勢 1', '過去走勢 2','未來走勢']
                values = [f'/stock_chart/{a}', f'/stock_chart/{a}', f'/stock_chart/{a}',f'/stock_chart/{a}']
                data = dict(zip(keys, values))   
                
                return render_template ('search_result.html',data = data, a =a  ,no=no)

@app.route('/stock_chart/<value>')
def stock(value):

        return render_template(f'{value}.html')


if __name__ == '__main__':
    app.debug = True
    app.run()