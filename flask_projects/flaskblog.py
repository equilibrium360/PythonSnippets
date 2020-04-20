from flask import Flask
app = Flask(__name__)

@app.route('/index')
def hello_world():
    return 'Hello, World!saaas'


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store', methods=['GET'])
def get_store():
    pass


app.run(debug=True)
