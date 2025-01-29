from flask import render_template, request, redirect, url_for, session
from forms import RegisterForm, LoginForm, BookForm  # Import forms
from models import User, Book
from app import app
from werkzeug.security import check_password_hash



@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        User.insert_user(form.username.data, form.password.data)
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        Book.insert_book(form.title.data, form.author.data, 2024)  # Example year
        return redirect(url_for("dashboard"))
    return render_template("add_book.html", form=form)


# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.get_user(username)
        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect(url_for("dashboard"))

        return "Invalid credentials!"

    return render_template("login.html")


# Dashboard Route
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        books = Book.get_all_books()  # Get books from database
        return render_template("dashboard.html", books=books)
    return redirect(url_for("login"))

@app.route("/books")
def books():
    all_books = Book.get_all_books()
    return render_template("books.html", books=all_books)

@app.route("/borrow/<book_id>", methods=["GET", "POST"])
def borrow_book(book_id):
    book = Book.get_book(book_id)
    if request.method == "POST":
        session["borrowed_books"].append(book_id)
        return redirect(url_for("dashboard"))

    return render_template("borrow_book.html", book=book)
