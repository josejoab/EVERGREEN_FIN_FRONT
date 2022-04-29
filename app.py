from flask import *
from flask_cors import CORS, cross_origin
import requests
import json


app=Flask(__name__)

host = " https://evergreen-finance-back.herokuapp.com/eveergreen/fin/cost/"

#index
@app.route("/")
def index():
    return render_template("index.html")

#create
@app.route("/create")
def create():
    return render_template("create.html")

#save
@app.route("/save",methods=["POST"])
def save():
    
    name = request.form['name']
    price = int(request.form['price'])
    
    url = host + "create-cost"
    datos = {"name" : name,
                "price" : price}  

    respuesta = requests.post(url, json=datos)
    
    # Ahora decodificamos la respuesta como json
    data_cost = respuesta.json()
    print("La respuesta del servidor es:")
    print(data_cost)

    return redirect("/get_costs")

#gets
@app.route("/get_costs")
def get_costs():
    url = host + "get-costs"
    respuesta = requests.get(url)
    data_costs = respuesta.json()

    print("respuesta gets")
    print(data_costs)

    return render_template("get_costs.html.jinja", costs=data_costs["body"])

#gets
@cross_origin
@app.route("/get_cost/<id>",  methods=['GET'])
def get_cost(id):
    url = host + "get-cost/" + id
    respuesta = requests.get(url)
    data_cost = respuesta.json()

    print("id: "+id)
    print("url: "+url)
    print("respuesta get")
    print(data_cost)

    return render_template("update.html.jinja", cost=data_cost["body"][0])

#update
@app.route("/update",methods=["POST"])
def update():
    
    name = request.form['name']
    price = int(request.form['price'])
    id = request.form['key']
    
    url = host + "update-cost/"+id
    datos = {"name" : name,
                "price" : price}  

    respuesta = requests.put(url, json=datos)
    
    # Ahora decodificamos la respuesta como json
    data_cost = respuesta.json()
    print("La respuesta del servidor es:")
    print(data_cost)

    return redirect("/get_costs")

#gets
@cross_origin
@app.route("/delete_cost/<id>",  methods=['GET'])
def delete_cost(id):
    url = host + "delete-cost/" + id
    respuesta = requests.delete(url)
    data_cost = respuesta.json()

    print("id: "+id)
    print("url: "+url)
    print("respuesta get")
    print(data_cost)

    return redirect("/get_costs")


if __name__ == "__main__":
    app.run(debug=True)