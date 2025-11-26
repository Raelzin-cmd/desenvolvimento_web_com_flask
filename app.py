# pyhton venv .venv
# python -m pip install Flask
# Altera a interepreção para o .venv

from flask import Flask, jsonify, make_response

# Criando a variavel que receberá o servidor
servidor = Flask(__name__)

# Dicionário = Objeto de carros
carros = [
    {
        'marca': 'Ford',
        'modelo': 'Ranger',
        'ano': 2020,
        'cor': 'Preto'
    },
    {
        'marca': 'Chevolet',
        'modelo': 'Camaro',
        'ano': 2023,
        'cor': 'Prata'
    }
]

@servidor.route('/carros', methods=['GET'])
def lista_carros(): # make_response para configurar o status (200 é o padrão)
    return make_response(jsonify(carros))  # Assegurar que será retornado uma lista json     

# Alterando porta de saída padrão, nome do IP e ativando modo debug
servidor.run(port=5001, host='localhost', debug=True)
# Modo debug on: Possibilita alteraeções sem interromper o servidor




# URL para usar no postman ou navegador http://localhost:5001/carros