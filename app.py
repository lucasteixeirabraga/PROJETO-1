from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lucasBRAGA99'
app.config['MYSQL_DB'] = 'desafio3'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
 
    return render_template("quemsomos.html")

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()

        return 'sucesso'
    return render_template('contato.html')

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM contato")
    if users > 0:
        userDetails = cur.fetchall()
        return render_template("users.html", userDetails=userDetails)
    return 'sem usuários'

if __name__ == '__main__':
    app.run(debug=True)










