from flask import Flask, render_template, request, flash, redirect, session, g, abort

app = Flask(__name__)

app.config["SECRET_KEY"] = "ihaveasecret"


@app.route("/")
def root():
    """Display's home page"""
    return render_template("homepage.html")


@app.route("/404")
def not_found():
    """Display's page to tell user that requested page is not found"""
    return render_template("404.html")
