from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from db import init_db

app = Flask(__name__)


# Configurations
app.config.from_object(Config)

init_db(app)
mongo = PyMongo(app)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Register Route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        # Check if user exists
        existing_user = mongo.db.users.find_one({"username": username})
        if existing_user:
            return "User already exists!"

        mongo.db.users.insert_one({"username": username, "password": password})
        return redirect(url_for("login"))
    
    return render_template("register.html")

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = mongo.db.users.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect(url_for("dashboard"))

        return "Invalid credentials!"

    return render_template("login.html")

# Dashboard Route
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        books = mongo.db.books.find()
        return render_template("dashboard.html", books=books)
    return redirect(url_for("login"))

# Add Book Route
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book_data = {
            "title": request.form["title"],
            "author": request.form["author"],
            "year": request.form["year"]
        }
        mongo.db.books.insert_one(book_data)
        return redirect(url_for("dashboard"))

    return render_template("add_book.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
