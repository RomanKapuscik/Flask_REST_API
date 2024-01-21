from flask import Flask, jsonify, request
from algorytmy import find_name_json, find_name_list, find_name_set, buble_sort, liczby_losowe

app = Flask(__name__)


@app.route("/")
def witajSwiecie():
    return "Hello, World!"


@app.route("/json")
def find_json():
    return find_name_json('Julian')


@app.route("/list")
def find_list():
    return find_name_list('Julian')


@app.route("/set")
def find_set():
    return find_name_set('Julian')


@app.route("/buble_sort_100")
def buble_sort_100():
    return list(buble_sort(liczby_losowe))

# @app.route("/dane", methods=['POST'])
# def loadJson():
#     content_type = request.headers.get('Content-Type')
#
#     if (content_type == 'application/json'):
#         mojeDane = request.get_json()
#
#         return mojeDane['mail']


app.run()
