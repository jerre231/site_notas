from flask import *
import pandas as pd
from classes import *

app = Flask(__name__)

admin = {
    'admin': 123
}

@app.route("/")
def redirect_to_login():
    return redirect(url_for("login"))

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
    nome = request.form.get("nome")
    numero = request.form.get("numero")
    opc = request.form.get("opc")

    if opc == "insert":
        pass
    elif opc == "remove":
        pass
    
    return redirect(url_for("imprimir"))

@app.route("/imprimir")
def imprimir():
    '''
    df = pd.read_csv('data.txt', delimiter=':', header=None, names=['Nome', 'Número'])  
    tabela_html = df.to_html(classes='table table-striped', index=False)
    
    return render_template("home.html", tabela_html=tabela_html)
    '''
    return render_template("home.html")

@app.route("/pagina_de_cadastro", methods=["GET", "POST"])                             
def pagina_de_cadastro():
    if request.method == "POST":
        email = request.form.get("email_cadastro")
        password = request.form.get("pass_cadastro")
        user_temp = Usuario(email, password)
        user_temp.cadastrar()

    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run()