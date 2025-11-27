# pyhton venv .venv
# python -m pip install Flask
# Altera a interepreção para o .venv

from flask import Flask, jsonify, make_response, request

# Criando a variavel que receberá o servidor
servidor = Flask(__name__)

# Dicionário = Objeto de carros
carros = [
    {
        'id': 1,
        'marca': 'Ford',
        'modelo': 'Ranger',
        'ano': 2020,
        'cor': 'Preto'
    },
    {
        'id': 2,
        'marca': 'Chevrolet',
        'modelo': 'Camaro',
        'ano': 2023,
        'cor': 'Prata'
    }
]


# Listar                   # http://localhost:5001/carros
@servidor.route('/carros', methods=['GET'])
def lista_carros(): # make_response para configurar o status (200 é o padrão)
    return make_response(jsonify(carros))  # Assegurar que será retornado uma lista json


# Detalhar               Convertendo (string) para (int)    # http://localhost:5001/carros/1
@servidor.route('/carros/<int:id_carro>', methods=['GET'])
def detalhe_carros(id_carro):   # id_carro recebe o ID mencionado na URL
    # Percorre toda a lista de carros
    for item in carros:
        # Compara o ID da procura na URL com o ID dos carros no código
        if item['id'] == id_carro:
            # Retorna os detalhes do carro se o ID encontrado
            return make_response(jsonify(item))
        
    # Status de erro se o ID não for encontrado
    return make_response(jsonify({'message': 'O carro não existe'}), 404)


# Cadastrar
'''
Use o parâmetro body json do Postman para cadastrar um novo carro
'''
@servidor.route('/carros', methods=['POST'])
def cadastro_carro():
    body = request.get_json()   # Lê o json enviado na requisição
    carros.append(body)    # Adiciona o json à lista
    return make_response(body, 201) # Retorno de criação bem sucedida


# Alterando porta de saída padrão, nome do IP e ativando modo debug
servidor.run(port=5001, host='localhost', debug=True)
# Modo debug on: Possibilita alteraeções sem interromper o servidor




# Use no postman ou insomnia para testar requisições da URL http://localhost:5001/carros