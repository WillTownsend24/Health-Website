from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Healthy Eating App is running!"