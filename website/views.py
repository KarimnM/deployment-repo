from flask import Blueprint, render_template, flash, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")









