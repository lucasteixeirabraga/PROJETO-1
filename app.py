from flask import Flask, render_template

app= Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")


@app.route("/contato")
def contatos():
    return render_template("contato.html")


