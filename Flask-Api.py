import pymysql
from flask import Flask, jsonify, request

app = Flask(__name__)

connection = pymysql.connect(user='root',
                            password='',
                            host='35.226.33.67',
                            database='customers')

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
    sql = "INSERT INTO customer_information(customerName, kontakt, telNumber, topic, note, file_path) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (customerName, kontakt, telNumber, topic, note, file_path)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-customerName', methods=['POST'])
def createUserCustomerName():
    data = request.json
    customerName = data['customerName']
    sql = "INSERT INTO customer_information(customerName) VALUES (%s)"
    val = (customerName)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-kontakt', methods=['POST'])
def createUserKontakt():
    data = request.json
    kontakt = data['kontakt']
    sql = "INSERT INTO customer_information(kontakt) VALUES (?)"
    val = (kontakt)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-telNumber', methods=['POST'])
def createUserTelNumber():
    data = request.json
    telNumber = data['telNumber']
    sql = "INSERT INTO customer_information(telNumber) VALUES (?)"
    val = (telNumber)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-topic', methods=['POST'])
def createUserTopic():
    data = request.json
    topic = data['topic']
    sql = "INSERT INTO customer_information(topic) VALUES (?)"
    val = (topic)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-note', methods=['POST'])
def createUserNote():
    data = request.json
    note = data['note']
    sql = "INSERT INTO customer_information(note) VALUES (?)"
    val = (note)
    try:
        cursor.execute(sql, val)
        connection.commit()
        return jsonify({'message': 'New user created!'}), 201
    except:
        return jsonify({'message': 'Failed to create user!'}), 500

@app.route('/api/v1/users-file_path', methods=['POST'])
def createUserFilePath():
    data = request.json
    file_path = data['file_path']
    sql = "INSERT INTO customer_information(file_path) VALUES (?)"
    val = (file_path)
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
    app.run(debug=True, port=5000)


