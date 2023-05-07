from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests

app= Flask(__name__)
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= True
debug= DebugToolbarExtension(app)

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

@app.route('/')
def index():
    obj=list(data['rates'].keys())
    # if request.method == "POST":
    #     thing=request.form['currency']
    return render_template('forex.html', obj=obj)


# obj=data['rates'].keys()
# obj = obj.get('EUR')


@app.route('/show_rate', methods=['POST'])
def show_exchange():
    obj= data['rates']
    curr= request.form['currency']
    into= request.form['change-currency']
    amt= request.form['amount']
    curr=obj.get(curr)
    into=obj.get(into)
    if str(curr) not in list(obj.keys()) or str(into) not in list(obj.keys()):
        flash('no such currency!')
    thing= round(float(into/curr) * float(int(amt)), 2)
    
    

    return render_template('forex1.html', thing=thing)
    