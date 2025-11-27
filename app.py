# pyhton venv .venv
# python -m pip install Flask
# Altera a interepreção para o .venv

from flask import Flask, jsonify, make_response, request
from json import loads, dumps

# Criando a variavel que receberá o servidor
servidor = Flask(__name__)

# Permite a leitura de outro arquivo
with open('bancodedados.txt', 'r') as arquivo:
    carros = loads(arquivo.read())  # Pega todo o texto do banco de dados


def persistir_carro(carro): # Persistindo o cadastro de um novo carro
    carros.append(carro)    # Cadastra no banco de dados
    # Permite editar outro arquivo
    with open('bancodedados.txt', 'w') as arquivo:  # Permite escrita no banco de dados
        arquivo.write(dumps(carros))    # Transforma a string em formato JSON

def persistir_lista_carros(carros): # Persistindo a listagem de todos os carros
    # Permite editar outro arquivo
    with open('bancodedados.txt', 'w') as arquivo:  # Permite escrita no banco de dados
        arquivo.write(dumps(carros))    # Transforma a string em formato JSON

# READ                   # http://localhost:5001/carros
@servidor.route('/carros', methods=['GET'])
def listar_carros(): # make_response para configurar o status (200 é o padrão)
    return make_response(jsonify(carros))  # Assegurar que será retornado uma lista json


# Detalhar               Convertendo (string) para (int)    # http://localhost:5001/carros/id
@servidor.route('/carros/<int:id_carro>', methods=['GET'])
def detalhar_carro(id_carro):   # id_carro recebe o ID mencionado na URL
    # Percorre toda a lista de carros
    for item in carros:
        # Compara o ID da procura na URL com o ID dos carros no código
        if item['id'] == id_carro:
            # Retorna os detalhes do carro se o ID encontrado
            return make_response(jsonify(item))
        
    # Status de erro se o ID não for encontrado
    return make_response(jsonify({'message': 'O carro não existe'}), 404)


# CREATE
'''
Use o parâmetro body json do Postman para cadastrar um novo carro
'''
                # http://localhost:5001/carros
@servidor.route('/carros', methods=['POST'])
def cadastrar_carro():
    body = request.get_json()   # Lê o json enviado na requisição
    persistir_carro(body)    # Adiciona o json à lista
    return make_response(body, 201) # Retorno de criação bem sucedida


# UPDATE                    http://localhost:5001/carros/id
@servidor.route('/carros/<int:id_carro>', methods=['PUT'])
def editar_carro(id_carro):
    body = dict(request.get_json()) # Body retornando em forma de dicionário
    for item in carros:
        if item['id'] == id_carro:  # Se o ID for encontrado, vai alterar os items abaixo
            item['marca'] = body['marca']
            item['modelo'] = body['modelo']
            item['ano'] = body['ano']
            item['cor'] = body['cor']
            persistir_lista_carros(carros) # Pegar a lista atualizada
            return make_response({}, 204)
    # Status de erro se o ID não for encontrado
    return make_response(jsonify({'message': 'O carro não existe'}), 404)


# DELETE                    http://localhost:5001/carros/id
@servidor.route('/carros/<int:id_carro>', methods=['DELETE'])
def excluir_carro(id_carro):
    for item in carros:
        if item['id'] == id_carro:  # Se o ID for encontrado, vai alterar os items abaixo
            carros.remove(item)
            persistir_lista_carros(carros)  # Pegar a lista atualizada
            return make_response({}, 204)
    # Status de erro se o ID não for encontrado
    return make_response(jsonify({'message': 'O carro não existe'}), 404)


# Alterando porta de saída padrão, nome do IP e ativando modo debug
servidor.run(port=5001, host='localhost', debug=True)
# Modo debug on: Possibilita alteraeções sem interromper o servidor




# Use no postman ou insomnia para testar requisições da URL http://localhost:5001/carros