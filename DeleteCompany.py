from flask import Flask, request, jsonify
from database import close_database_connection,connect_to_database
from datetime  import timedelta

app=Flask(__name__)

@app.route("/company/delete/<int:company_id>",methods=['DELETE'])
def delete_table(company_id):
    conn , cursor = connect_to_database()
    query="SELECT company_name , company_address , company_country FROM company WHERE company_id= %s"
    cursor.execute(query,(company_id,))
    existing_company=cursor.fetchone()

    if not existing_company:
        return jsonify({"message":"Company not found"})
    
    query1="DELETE FROM company WHERE company_id= %s"
    cursor.execute(query1,(company_id,))

    conn.commit()
    response={
        "message":"Company deleted successfully"
        }
    return response

if __name__=="__main__":
    app.run(debug=True)