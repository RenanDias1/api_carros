import mysql.connector
from mysql.connector import Error


from flask import Flask, make_response, jsonify, request
from bd import Carros




app = Flask(__name__)

app.json.sort_keys = False


mydb = mysql.connector.connect(host="localhost",database="pycodebr", user="root", password="RENANcorrea@123")

@app.route('/carros', methods = ['GET'])
def get_carros():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM CARROS')
    my_carros = my_cursor.fetchall()

    carros = list()
    for carro in my_carros:
        carros.append(
            {
                'id':carro[0],
                'marca':carro[1],
                'modelo':carro[2],
                'ano':carro[3]
            }
        )

    return make_response(
        jsonify(
            message='Lista de Carros',
            Dados=carros
        )
    )

@app.route('/carros', methods =['POST'])
def create_carros():

    carro = request.json

    my_cursor = mydb.cursor()
    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', '{carro['ano']}')"
    my_cursor.execute(sql)
    mydb.commit()

    
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem='Carro Cadastrado com Sucesso',
            carro=carro
        )
    )


app.run()



