from flask import Flask
from flask import render_template,request,url_for,redirect

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


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complate",methods =["GET","POST"])
def contact_complate():
    if request.method=="POST":
        # メール送信
        
        # contactエンドポイントまでリダイレクト
        return redirect(url_for("contact_complate"))
    else:
        return render_template("contact_complate.html")