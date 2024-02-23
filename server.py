from flask import Flask,request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/random_number")
def random_number():
    minimum=request.args.get('min')
    maximum=request.args.get('max')
    if maximum is None:
        maximum=100
    if minimum is None:
        minimum=0
    
    return str(random.randint(int(minimum),int(maximum)))