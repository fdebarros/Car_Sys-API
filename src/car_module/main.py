import mysql.connector
import http.client
from flask import Flask, jsonify, request


car_crud = mysql.connector.connect(
    host='$MysqlHost:3306',
    user='$User',
    password='$Pass',
    database='car_crud'
)
app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False

### GET FUNCTIONS ###
# LIST ALL
@app.route('/carros', methods=['GET'])
def get_cars():
    
    db_cursor = car_crud.cursor()
    db_cursor.execute('SELECT * FROM carros')
    cursor_return = db_cursor.fetchall()
    
    car_formatted = list()
    for car in cursor_return:
        car_formatted.append(
            {
                'id': car[0],
                'marca': car[1],
                'modelo': car[2],
                'ano': car [3]
            }
        )
    
    return jsonify(
        function_called='Lista geral de carros',
        carros=car_formatted)

# SEARCH BY ID
@app.route('/carros/<int:id_param>', methods=['GET'])
def get_cars_by_id(id_param):
    
    db_cursor = car_crud.cursor()
    db_cursor.execute('SELECT * FROM carros WHERE id = '+str(id_param))
    cursor_return = db_cursor.fetchall()
    
    car_formatted = list()
    for car in cursor_return:
        car_formatted.append(
            {
                'id': car[0],
                'marca': car[1],
                'modelo': car[2],
                'ano': car [3]
            }
        )
    return jsonify(car_formatted)

# SEARCH BY MODEL
@app.route('/carros/<string:model_param>', methods=['GET'])
def get_cars_by_model(model_param):
    
    db_cursor = car_crud.cursor()
    db_cursor.execute("SELECT * FROM carros WHERE modelo = '" +model_param+"'")
    cursor_return = db_cursor.fetchall()
    
    car_formatted = list()
    for car in cursor_return:
        car_formatted.append(
            {
                'id': car[0],
                'marca': car[1],
                'modelo': car[2],
                'ano': car [3]
            }
        )
    return jsonify(car_formatted)
    

### PUT FUNCTION ###

@app.route('/carros/<int:id_param>', methods=['PUT'])
def update_car(id_param):
    car_data = request.get_json()
    db_cursor = car_crud.cursor()
        
    sql_string = f"UPDATE carros SET marca='{car_data[0]}',  modelo = '{car_data[1]}', ano={car_data[2]} WHERE id = {id_param};"
    db_cursor.execute(sql_string)
    car_crud.commit()

    return http.client.responses[http.client.CREATED]
        
        
        
### POST FUNCTION ###
@app.route('/carros', methods=['POST'])
def insert_car():
    car_data = request.get_json()
    db_cursor = car_crud.cursor()
        
    sql_string = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{car_data[0]}', '{car_data[1]}', {car_data[2]});"
    db_cursor.execute(sql_string)
    car_crud.commit()

    return http.client.responses[http.client.CREATED]


### DELETE FUNCION ###

@app.route('/carros/<int:id_param>', methods=['DELETE'])
def delete_car(id_param):
    db_cursor = car_crud.cursor()   
        
    sql_string = f"DELETE FROM carros WHERE id = {id_param};"
    db_cursor.execute(sql_string)
    car_crud.commit()

    return http.client.responses[http.client.OK]

app.run(port=8080, host='localhost', debug=True)
