from flask import Flask
app = Flask(__name__)

@app.route("/info")
def lwinfo():
   return "this is my information"

@app.route("/phone"):
    return "9547586955"

app.run(host="0.0.0.0")