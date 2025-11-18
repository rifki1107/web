from flask import Flask

app = flask(__name__)

@app.route ("/")
def hello world ():
    return "<p>hello world</p>"