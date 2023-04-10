"""
file name: app.py
Description: Uses Flask framework to access ChatGPT API via /get method. 
__copyright__ = "Copyright 2023, MartinYTech"
__author__=  Martin Yanev
__modified__= 09/04/2023
"""

from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = "<API_TOKEN>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userText,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    answer = response["choices"][0]["text"]
    return str(answer)


if __name__ == "__main__":
    app.run()
