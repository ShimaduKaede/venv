from flask import Flask

app=Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return "Hello,Flaskbook!" 


@app.route("/hello/<name>",methods=["POST","GET"],endpoint="hello-endpoint")
def hello(name):
    return f"Hello,{name}!"