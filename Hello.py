# Flask: Morpheus Tutorials erster Teil

from flask import Flask

app = Flask(__name__)

@app.route("/")   # Hier wird die Indexseite (also Homepage) also Route eingetragen

def index():
    return "Welcome to Flask"

@app.route("/hello/<string:name>")   

#auf der Unterseite wird ein Name als Parameter eingetragen. Der Name wird in der URL-Leiste auch benötigt um die Seite auszugeben
#   mit dem Statement "STRING" wird der Variablen ein Datentyp zugewiesen """

def hello(name):
    return "Hello " + name + "!"


@app.route("/addiere/<int:zahl>") # Versuch mit einer Zahl zur Berechnung, es geht auch z.B. float, path, 
def addiere(zahl):
    return str(zahl+zahl)  # ACHTUNG!! Ausgabe kann nur ein string, dict, tuple, Response instance, or WSGI callable sein 



@app.route("/add2/<int:z1>/<int:z2>") # so gehen auch mehrere Parameter
def add2(z1, z2):
    return str(z1+z2)


if __name__ == "__main__":
    app.run(port=1337, debug=True)
