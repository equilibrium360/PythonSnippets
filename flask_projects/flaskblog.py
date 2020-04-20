from flask import Flask, jsonify

app = Flask(__name__)


stores = [

    {
        'name': 'mac',
        'items': [
            {
                'name': 'item name',
                'price': 15.6
             }

        ]
    }

]

@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hello, World!saaas'


@app.route('/store', methods=['POST'])
def create_store():
    pass


# http://127.0.0.1/store/some_name
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name :
            return jsonify(store)
    return jsonify({'message': 'no store found'})


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'no store matched'})



app.run(debug=True)
