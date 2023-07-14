from flask import Flask, render_template, request
import pickle
import hashlib

app = Flask(__name__)
#load the model
# model = pickle.load(open('savedmodel.sav', 'rb'))
model = pickle.load(open('savedmodel.sav','rb'))
@app.route('/')
def home():
    result = ""
    # return render_template('index.html', **locals())
    return render_template('index.html',**locals())

@app.route('/predict', methods=['POST','GET'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length =float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]

    setosa = 'The flower is classified as Setosa'
    versicolor = 'The flower is classified as Versicolor'
    virginica = 'The flower is classified as Virginica'
    if result == 0:
        return render_template('index.html', setosa=setosa)
    elif result == 1:
        return render_template('index.html', versicolor=versicolor)
    else:
        return render_template('index.html', virginica=virginica) 
    

    # return render_template('index.html',**locals())
    # return render_template('index.html',**locals())


if __name__ == '__main__':
    app.run(debug=True)