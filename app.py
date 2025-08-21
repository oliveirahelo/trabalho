from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados fictícios para nossa API
alunos = [
    {'id': 1, 'nome': 'henri', 'idade': 16},
    {'id': 2, 'nome': 'betina', 'idade': 18},
    {'id': 3, 'nome': 'Ana', 'idade': 15},
    {'id': 4, 'nome': 'breno', 'idade': 16},
    {'id': 5, 'nome': 'Heloisa', 'idade': 17}
]

# Rota inicial 
@app.route("/")
def home():
    return "API de alunos funcionando!"

# GET - Listar todos os alunos
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

# POST - Adicionar um novo aluno
@app.route("/alunos", methods=["POST"])
def adicionar_alunos():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify({"mensagem": "Aluno adicionado com sucesso!", "aluno": novo_aluno}), 201

# PUT - Atualizar dados de um aluno pelo ID
@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_alunos(id):
    for aluno in alunos:
        if aluno["id"] == id:
            dados = request.get_json()
            aluno.update(dados)
            return jsonify({"mensagem": "Aluno atualizado!", "aluno": aluno})
    return jsonify({"erro": "Aluno não encontrado!"}), 404

# DELETE - Remover aluno pelo ID
@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_alunos(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify({"mensagem": "Aluno removido com sucesso!"})
    return jsonify({"erro": "Aluno não encontrado!"}), 404

if __name__ == "__main__":
    app.run(debug=True)