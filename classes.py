import pymongo

def start_client():
    client = pymongo.MongoClient("localhost", 27017)
    return client

class Usuario:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

    def cadastrar(self):
        client = start_client()
        db = client["database"]
        usuarios = db["usuarios"]
        data = {"nome": self.user, "senha": self.passw}
        usuarios.insert_one(data)
        client.close()

    def autenticar(self, usuario,senha):
        client = start_client()
        db = client["database"]
        usuarios = db["usuarios"]
        user = usuarios.find_one({"nome": usuario})

        if user and user["senha"] == senha:
            client.close
            return True
        else:
            client.close
            return False

class Alunos(Usuario):
    def __init__(self):
        self.nome = self.user
        
        client = start_client()
        db = client["database"]
        alunos = db["alunos"]
        data = {"nome": self.nome}
        alunos.insert_one(data)
        client.close()

    def inserir_nota(self, avaliacao, nota):
        client = start_client()
        db = client["database"]
        alunos = db["alunos"]
        filtro = {"nome": self.nome}
        data = { "$set": { avaliacao: nota } }
        alunos.update_one(filtro, data)
        client.close()