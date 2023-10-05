import pymongo

def start_client():
    client = pymongo.MongoClient("localhost", 27017)
    return client

def calc_nota(p1, p2, nota_lista):
    media = sum(nota_lista)/len(nota_lista)
    med = ((p1 + p2)*(2/5))+((media)*0.2)
    return med

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

    def autenticar(self):
        client = start_client()
        db = client["database"]
        usuarios = db["usuarios"]
        user = usuarios.find_one({"nome": self.user})

        if user and user["senha"] == self.passw:
            client.close
            return True
        else:
            client.close
            return False

class Aluno(Usuario):
    def __init__(self, user):
        self.nome = user

        client = start_client()
        db = client["database"]
        alunos = db["alunos"]
        data = {"nome": self.nome}
        check = alunos.find_one(data)
        if not check:
            alunos.insert_one(data)
            client.close()
        else: pass

    def inserir_nota(self, avaliacao, nota):
        client = start_client()
        db = client["database"]
        alunos = db["alunos"]
        filtro = {"nome": self.nome}
        user = alunos.find_one(filtro)
        
        if user:
            data = { "$set": { avaliacao: nota } }
            alunos.update_one(filtro, data)
            client.close()

    def remover(self):                             #TODO: consertar, não está funcionando
        client = start_client()
        db = client["database"]
        alunos = db["alunos"]
        filtro = {"nome": self.nome}
        alunos.delete_many(filtro)