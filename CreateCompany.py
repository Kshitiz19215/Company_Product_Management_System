from flask import Flask, jsonify, request
from database import connect_to_database, close_database_connection
from datetime import timedelta 
from collections import OrderedDict
from config import key
from hashlib import md5
from Helper import generate_token, isValidToken
import time as module_time

app = Flask(__name__)

@app.route('/company/create', methods=['POST'])
def create_company():
    reqToken = request.headers.get('reqToken')
    reqTimestamp = request.headers.get('reqTimestamp')

    validation = isValidToken(reqToken, reqTimestamp)
    
    if validation== False:
        return jsonify({'message': 'Invalid token'})
    
    conn, cursor = connect_to_database()

    data = request.get_json()

    company_name = data['company_name']
    company_address = data['company_address']
    company_country = data['company_country']

    query1 = "SELECT company_id FROM company WHERE company_name = %s AND company_address = %s AND company_country = %s"
    cursor.execute(query1, (company_name, company_address, company_country))
    company_exist = cursor.fetchone()

    if company_exist:
        return jsonify({'message': 'Company already exists.'})

    date = data['date']
    time = data['time']

    sql = "INSERT INTO company (company_name, company_address, company_country, date, time) VALUES (%s, %s, %s, %s, %s)"
    values = (data['company_name'], data['company_address'], data['company_country'], data['date'], data['time'])
    cursor.execute(sql, values)

    company_id = cursor.lastrowid

    query = "SELECT company_name, company_address, date, time, last_modified FROM company WHERE company_id = %s"
    cursor.execute(query, (company_id,))
    result = cursor.fetchone()

    response = OrderedDict([
        ('message', 'Company created successfully'),
        ('company_id', company_id),
        ('company_name', result[0]),
        ('company_address', result[1]),
        ('date', result[2].strftime('%Y-%m-%d')),
        ('time', str(result[3])),
        ('last_modified', str(result[4]))
    ])
    
    conn.commit()
    cursor.close()
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True )
