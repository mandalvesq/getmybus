from flask import Flask
from flask import redirect, request
import json
import requests

app = Flask(__name__)
url = 'http://api.olhovivo.sptrans.com.br/v2.1'
apikey = 'e10365af8aed9e34e765e828fe573e6d1961c02fe2a4d3fb7e55e1fcxxxxxxx'
session = requests.session()
stop_id = 340015329
bus_id = 8000
head = {'Authorization': 'token {}'.format(apikey)}

@app.route('/home')

def auth():
    response = session.post(url + '/Login/Autenticar?token={}'.format(apikey), timeout=3)
    print(response)

def home():
    return redirect("http://mandalvesq.github.io")




#@app.route('/Previsao?codigoParada=<string:cod_>&codigoLinha=<string:cod_>', methods=['GET'])
def get_previsao(stop_id, bus_id):
    result = session.get(url + '/Previsao?codigoParada={}&codigoLinha={}'.format(stop_id, bus_id))
    print(result)
    return result

if __name__ == "__main__":
    auth()