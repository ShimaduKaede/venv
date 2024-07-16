from flask import Flask
from flask import render_template

app=Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return "Hello,Flaskbook!" 


@app.route("/hello/<name>",methods=["POST","GET"],endpoint="hello-endpoint")
def hello(name):
    return f"Hello,{name}!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)