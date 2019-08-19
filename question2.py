from flask import Flask, request, jsonify

app = Flask(__name__)
dict= {
    "data": [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
        }

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({'sum': sum(dict['data'])})
