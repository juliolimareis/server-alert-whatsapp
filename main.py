import sys
import os
import json
import argparse

sys.path.insert(0, 'libs')

import requests

def getJson(dir):
    """
    Lê o conteúdo de um arquivo JSON em um diretório especificado.

    Parâmetros:
    diretorio (str): Caminho para o diretório onde o arquivo JSON está localizado.

    Retorna:
    dict: Conteúdo do arquivo JSON.
    """
    if not os.path.isfile(dir):
        raise FileNotFoundError(f"O arquivo {dir} não foi encontrado.")

    with open(dir, 'r', encoding='utf-8') as file:
        app = json.load(file)

    return app

def send_message(body: dict):
  base_url = CONFIG['zApiUrl']
  headers = {
    'Client-Token': CONFIG['clientToken'],
    'Content-Type': 'application/json'
  }

  url = f"{base_url}/send-text"
  return requests.post(url, json=body, headers=headers)

def verify_service(app):
    url = app['url']
    response = requests.get(url)
    
    if response.status_code == 200:
      send_message({'phone': CONFIG['phone'], 'message': f"✅ Service *{app['name']}*"}) 
    else:
      send_message({'phone': CONFIG['phone'], 'message': f"❌ Service *{app['name']}* status code: {response.status_code}"}) 

def start():
  # if(datetime.datetime.now().hour in CONFIG['hours']):
  for app in CONFIG['apps']:
    verify_service(app)

parser = argparse.ArgumentParser(description="Config json")
parser.add_argument('--path_json_config', type=str, required=True, help="json config")
args = parser.parse_args()

CONFIG = getJson(args.path_json_config)

start()



      