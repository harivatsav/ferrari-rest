from flask import Flask,jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./cars.json').read())
data=jData["Cars"]

@app.route('/')
def cars_main():
    return render_template("index.html")

@app.route('/getcars/')
def cars_all():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getcars/<string:Year>/')
def cars(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/getcars/<string:Year>/<string:id>/')
def cars_id(Year='', id=''):
    car= []
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    for element in myList:
        if element["id"] == id:
            car.append(element)        
    result = jsonify(car)
    return render_template("index.html",items=car)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
