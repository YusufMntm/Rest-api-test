import pymysql
from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/', methods=['GET'])
def getUserCustomerName():
    
    try:
        print("Working")
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)


