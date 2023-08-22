import sqlite3
from flask import Flask, jsonify, request
import mysql.connector
from google.cloud import storage

app = Flask(__name__)

connection = mysql.connector.connect(user = 'root', password = '123456',)
cursor = connection.cursor()


@app.route('/api/v1/users-post', methods=['POST'])
def createUser():
    data = request.json
    customerName = data['customerName']
    kontakt = data['kontakt']
    telNumber = data['telNumber']
    topic = data['topic']
    note = data['note']
    file_path = data['file_path']
    sql = "INSERT INTO customer_information(customerName, kontakt, telNumber, topic, note, file_path) VALUES (?, ?, ?, ?, ?, ?)"
    val = (customerName, kontakt, telNumber, topic, note, file_path)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-get', methods=['GET'])
def getUsers():
    cursor.execute("SELECT * FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/v1/users-customerName', methods=['GET'])
def getUsersCustomerName():
    cursor.execute("SELECT customerName FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)


@app.route('/api/v1/users-kontakt', methods=['GET'])
def getUsersKontakt():
    cursor.execute("SELECT kontakt FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/v1/users-telNumber', methods=['GET'])
def getUsersTelNumber():
    cursor.execute("SELECT telNumber FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/v1/users-topic', methods=['GET'])
def getUsersTopic():
    cursor.execute("SELECT topic FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/v1/users-note', methods=['GET'])
def getUsersNote():
    cursor.execute("SELECT note FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/v1/users-file_path', methods=['GET'])
def getUsersFilePath():
    cursor.execute("SELECT file_path FROM customer_information")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/api/v1/users/<id>', methods=['DELETE'])
def deleteUser(id):
    cursor.execute("DELETE FROM customer_information WHERE id = ?", (id,))
    connection.commit()
    return jsonify({'message': 'User deleted!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
