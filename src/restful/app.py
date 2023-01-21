from flask import Flask, jsonify, request
from threading import Thread
import os
import openai

app = Flask('')

openai.api_key = os.getenv("OPENAI_API_KEY")

def answer(prmpt):
    # Load your API key from an environment variable or secret management service
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prmpt,
                                        temperature=0,
                                        max_tokens=256)
    return response["choices"][0]["text"]


@app.route('/')
def home():
    return "Hello, this is AskGPT!"

@app.route('/prompt/', methods=["POST"])
def prompt():
    return answer(request.json["prmpt"])

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()
