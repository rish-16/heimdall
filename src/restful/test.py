import requests
import json
from pprint import pprint

URL = "https://AskGPTSiri.rish-16.repl.co/prompt/"

data = {
    "prmpt": "hello this is a prompt"
}

res = requests.post(URL, json=data)
content = res.content
my_json = json.loads(content.decode('utf8').replace("'", '"'))

pprint (my_json["choices"][0]["text"])
