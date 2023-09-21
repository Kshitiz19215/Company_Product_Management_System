from flask import Flask, jsonify, request
from database import connect_to_database, close_database_connection
from datetime import timedelta

app=Flask(__name__)

@app.route('/company/update/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    conn , cursor = connect_to_database()
    data=request.get_json()

    company_name=data['company_name']
    company_address=data['company_address']
    company_country=data['company_country']

    query="SELECT * FROM company WHERE company_id = %s"
    cursor.execute(query, (company_id,))
    existing_company=cursor.fetchone()

    if not existing_company:
        return jsonify({'message':'Company not found'})
    
    if company_name:
        query="UPDATE company SET company_name = %s WHERE company_id = %s"
        cursor.execute(query,(company_name,company_id,))

    if company_address:
        query="UPDATE company SET company_address = %s WHERE company_id = %s"
        cursor.execute(query,(company_address,company_id,))

    if company_country:
        query="UPDATE company SET company_country = %s WHERE company_id = %s"
        cursor.execute(query,(company_country,company_id,))
    
    conn.commit()

    return jsonify({'message':'Company updated successfully'})
if __name__=='__main__':
    app.run(debug=True)