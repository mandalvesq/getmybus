from flask import Flask
from flask import redirect, request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return redirect("http://mandalvesq.github.io")

@app.route('/linhas/BuscarBus/<string:cod_>', methods=['GET')
def get_buss():
    data = request.json
