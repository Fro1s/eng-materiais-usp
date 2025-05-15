from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("about.html")

@app.route('/materiais/concreto')
def concreto():
    return render_template('materiais/concreto.html')

@app.route('/materiais/aco-inox')
def aco_inox():
    return render_template('materiais/aco_inox.html')

@app.route('/materiais/ferro-fundido')
def ferro_fundido():
    return render_template('materiais/ferro_fundido.html')

@app.route('/materiais/ferro-f22')
def ferro_f22():
    return render_template('materiais/ferro_f22.html')

@app.route('/materiais/folha-cana')
def folha_cana():
    return render_template('materiais/folha_cana.html')

if __name__ == "__main__":
    app.run(debug=True)