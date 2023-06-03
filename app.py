from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__,template_folder='template')
model=pickle.load(open("Coba.pkl","rb"))

@app.route('/')
def home():
    return render_template('Predict.html')

@app.route('/predict',methods=["POST"])
def predict():
    LB=float(request.form['LB'])
    LT=float(request.form['LT'])
    KT=float(request.form['KT'])
    KM=float(request.form['KM'])
    GRS=float(request.form['GRS'])
    prediction = model.predict([[LB,LT,KT,KM,GRS]])
    output=round(prediction[0])

    return render_template("Predict.html",prediction_text="Rp.{}".format(output))

if __name__ == "__main__":
    app.run(debug=True)