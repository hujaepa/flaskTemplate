from flask import Flask

#INITIALIZE FLASK APP
def create_app():
    app = Flask(__name__)
    app.config["SECRECT_KEY"] = "c48skdBR8m"
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app