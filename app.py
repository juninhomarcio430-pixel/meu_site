from flask import Flask

# inicializa o Flask
app = Flask(__name__)

# cria página inicial do site
@app.route("/")
def home():
    return "<h1>Parabéns Márcio Júnior! Meu site em Python está no ar!</h1>"

# rodar o servidor
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")