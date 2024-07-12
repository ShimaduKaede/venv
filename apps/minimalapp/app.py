from flask import Flask

app=Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return "Hello,Flaskbook!" 


@app.route("/hello",methods=["POST"],endpoint="hello-endpoint")
def hello():
    return "Hello,World!"