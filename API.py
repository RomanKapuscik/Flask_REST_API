from flask import Flask, jsonify, request
from algorytmy import find_name_json, find_name_list, find_name_set, buble_sort, liczby_losowe
from algorytmy_21012024 import find_friends_json, looking_for_things_with_friends, create_password

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


@app.route('/find_friends', methods=['GET'])
def find_friends():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')

    result = find_friends_json(name1, name2)

    return jsonify({'result': result})

@app.route('/find_things', methods=['GET'])
def find_things():
    name = request.args.get('name')
    items = request.args.getlist('items')

    result = looking_for_things_with_friends(name, items)

    return jsonify({'result': result})

@app.route('/create_password', methods=['GET'])
def create_password_api():
    num_of_car = int(request.args.get('number'))
    upper = bool(request.args.get('upper'))
    special = bool(request.args.get('special'))

    result = create_password(num_of_car, upper, special)

    return jsonify({'result': result})

# @app.route("/dane", methods=['POST'])
# def loadJson():
#     content_type = request.headers.get('Content-Type')
#
#     if (content_type == 'application/json'):
#         mojeDane = request.get_json()
#
#         return mojeDane['mail']


app.run()
