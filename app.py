from flask import *
import pandas as pd
from classes import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email_login")
        password = request.form.get("pass_login")
        user_temp = Usuario(email, password)

        if user_temp.autenticar():
            return redirect(url_for("imprimir"))
        else:
            return redirect(url_for("login"))  

    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/box", methods=["GET", "POST"])
def box():
    try:
        nome = request.form.get("nome")
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))
        valor = request.form.get("valor")
        opc = request.form.get("opc")
        nota_lista_str = valor.split(",")
        nota_lista = [float(item) for item in nota_lista_str]
        aluno_temp = Aluno(nome)
    except:
        nome = request.form.get("nome")
        opc = request.form.get("opc")
        aluno_temp = Aluno(nome)
    if opc == "insert":
            if p1:
                aluno_temp.inserir_nota("P1", p1)
            if p2:
                aluno_temp.inserir_nota("P2", p2)
            if valor:
                for i, nota in enumerate(nota_lista):
                    numero = f"lista{i+1}"
                    aluno_temp.inserir_nota(numero, nota)
            media = calc_nota(p1, p2, nota_lista)
            aluno_temp.inserir_nota("media", media)
    elif opc == "remove":
        aluno_temp.remover()
    
    return redirect(url_for("imprimir"))

@app.route("/imprimir")
def imprimir():

    client = start_client()
    db = client["database"]
    alunos = db["alunos"]
    
    dados = list(alunos.find({}, {"_id": 0}))
    df = pd.DataFrame(dados)
    client.close
    
    #df = pd.read_csv('data.txt', delimiter=':', header=None, names=['Nome', 'Número'])  
    tabela_html = df.to_html(classes='table table-striped', index=False)
    
    return render_template("home.html", tabela_html=tabela_html)

@app.route("/pagina_de_cadastro", methods=["GET", "POST"])                             
def pagina_de_cadastro():
    if request.method == "POST":
        email = request.form.get("email_cadastro")
        password = request.form.get("pass_cadastro")
        user_temp = Usuario(email, password)
        user_temp.cadastrar()

    return render_template("cadastro.html")