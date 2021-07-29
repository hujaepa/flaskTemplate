
from flask import Blueprint
auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "<h3>Login</h3>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup")
def signup():
    return "<p>Sign up</p>"