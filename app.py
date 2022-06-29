
import numpy as np
import pickle
from flask import Flask,render_template,request

model1=pickle.load(open(r'E:\SOFTWARE\DT_proj\artifacts\model.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    data=np.zeros(4)
    data[0]=request.form['Outlook']
    data[1]=request.form['Temperature']
    data[2]=request.form['Humidity']
    data[3]=request.form['Windy']
    result=model1.predict([data])
    if result[0]==1:
        res="Play"
    else:
        res="Don't Play"
    return render_template('index.html',pred=res)
    

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)