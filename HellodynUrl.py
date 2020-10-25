# Flask: Morpheus Tutorials erster Teil

from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/")   # Hier wird die Indexseite (also Homepage) also Route eingetragen

def index():
    #die Zeile wird für die GEt/POST Dynamic ausge
    #return '<a href = ' + url_for("hello", name="Dödel") + '>Gruess Gott </a>' #Die url_for() Funktion gibt einen String zurück der der URl entspricht, die in 
    return '''
    <html>
        <body>

            <form action = "http://localhost:1337/login" method = "POST">
                <p>Name: </p>
                <p><input type = "text" name = "name" /> </p>
                <p><input type = "submit" value = "submit" /> </p>
            </form>

        </body>
    </html>
    '''

@app.route("/login", methods=['POST', 'GET']) #es gibt noch HEAD, PUT, DELETE
def login():
    name = ""
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    return "Hello" + name + "!"


@app.route("/hello/<string:name>")   

#auf der Unterseite wird ein Name als Parameter eingetragen. Der Name wird in der URL-Leiste auch benötigt um die Seite auszugeben
#   mit dem Statement "STRING" wird der Variablen ein Datentyp zugewiesen """

def hello(name):
    return "Hello " + name + "!"


@app.route("/addiere/<int:zahl>") # Versuch mit einer Zahl zur Berechnung, es geht auch z.B. float, path, 
def addiere(zahl):
    return str(zahl+zahl)  # ACHTUNG!! Ausgabe kann nur ein string, dct, tuple, Response instance, or WSGI callable sein 



@app.route("/add2/<int:z1>/<int:z2>") # so gehen auch mehrere Parameter
def add2(z1, z2):
    return str(z1+z2)



if __name__ == "__main__":
    app.run(port=1337, debug=True)
