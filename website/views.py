#routes

from flask import Blueprint
# defining blueprint for routing in flask
views = Blueprint("views", __name__)

@views.route("/")
def home():
    return "<h1>Welcome</h1>"