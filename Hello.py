# Flask: Morpheus Tutorials erster Teil

from flask import Flask

app = Flask(__name__)

@app.route("/")   # Hier wird die Indexseite (also Homepage) also Route eingetragen

def index():
    return "Welcome to Flask"

@app.route("/hello")   #Hier wird eine Unterseite als Route eingetragen
def hello():
    return "Hello World!"



if __name__ == "__main__":
    app.run(port=1337, debug=True)
