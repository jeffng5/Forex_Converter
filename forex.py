from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import requests

app= Flask(__name__)
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug= DebugToolbarExtension(app)

#api call to get the exchange rates for countries
url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
assert response.status_code == 200
data = response.json()

#homepage route that displays globla currencies and form to input exchange info
@app.route('/')
def index():
    obj=list(data['rates'].keys())
    return render_template('forex.html', obj=obj)


#page that displays yield given entered info
@app.route('/show_rate', methods=['POST'])
def show_exchange():
    """ 
    converts one currency to another given amount 
    
    """
    
    obj= data['rates']
    assert type(obj)==dict
    # curr1=request.form['currency']
    # list_of_countries=[]
    # list_of_rates=[]
    # for x in enumerate(obj.keys()):
    #     list_of_countries.append(x)
    # for y in enumerate(obj.values()):
    #     list_of_rates.append(y)
    # for i in range(len(list_of_rates)):
    #     if list_of_rates[i][1]==curr1:
    #         print ('Well done')
    #     else:
    #         flash('There is no such currency!')

    
    curr= request.form['currency'] # currency convert from rate
    assert type(curr)==float
    into= request.form['change-currency'] # currency convert to rate
    assert type(into)==float
    amt= request.form['amount'] # amoubnt of currency you want exchanged
    assert type(amt)==float
    curr=obj.get(curr) #gets the value 
    into=obj.get(into) #gets the value
    thing= round(float(into/curr) * float(int(amt)), 2) #formula to convert the value
    assert type(thing) == float
    return render_template('forex1.html', thing=thing, curr=curr, into=into) # display currency yield
   
