from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

# create_app関数を作成する
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)
    # アプリのコンフィグ設定
    app.config.from_mapping(
        SECRET_KEY='2AZSMss3p5QPbcY2hBj',
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    # sqlalchemyとアプリを連携
    db.init_app(app)
    # migrateとアプリを連携
    Migrate(app,db)
    
    app.run(debug=True)
    
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    
    # register_blueprintメソッドを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud,url_prefix="/crud")
    
    
    return app