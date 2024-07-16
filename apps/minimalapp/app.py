from flask import Flask,flash
from flask import render_template,request,url_for,redirect
from email_validator import validate_email,EmailNotValidError


app=Flask(__name__)
    # SECRET_KEYを追加する
app.config['SECRET_KEY'] ="2AZSMss3p5QPbcY2hBsJ"

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
        # form属性を利用して値の取得
        username=request.form["username"]
        email=request.form["email"]
        description=request.form["description"]
        
        # 入力チェック
        is_valid=True
        if not username:
            flash("ユーザー名は必須です")
            is_valid=False
        
        if not email:
            flash("メールアドレスは必須です")
            is_valid=False
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid=False
            
        if not description:
            flash("お問い合わせ内容は必須です")
            is_valid=False
            
        if not is_valid:
            return redirect(url_for("contact"))
        # メール送信
        
        # contactエンドポイントまでリダイレクト
        flash("お問い合わせ内容はメールにて送信しました。お問い合わせありがとうございました。")
        return redirect(url_for("contact_complate"))
    else:
        return render_template("contact_complate.html")