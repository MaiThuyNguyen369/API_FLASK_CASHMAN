from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [{" Description ":" Salary", " Amount ":" 5000"}]

@app.route("/incomes")
def get_incomes():
  return jsonify(incomes)

@app.route("/incomes", methods=["POST"])
def add_incomes():
  incomes.append(request.get_json())
  return "",  204