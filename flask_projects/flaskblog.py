from flask import Flask

app = Flask(__name__)


stores = [

    {
        'name': 'My Wonderful store',
        'items': [
            {
                'name': 'item name',
                'price': 15.6
             }

        ]
    }

]

@app.route('/index')
def hello_world():
    return 'Hello, World!saaas'


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>', methods=['GET'])  # http://127.0.0.1/store/some_name
def get_store(name):
    pass


@app.route('/store', methods=['GET'])
def get_stores():
    pass


@app.route('/store/string:name/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/string:name/item', methods=['GET'])
def get_item_in_store(name):
    pass


app.run(debug=True)
