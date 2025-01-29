from db import mongo

class User:
    @staticmethod
    def insert_user(username, password):
        """Insert new user into MongoDB"""
        mongo.db.users.insert_one({"username": username, "password": password})

    @staticmethod
    def get_user(username):
        """Retrieve user by username"""
        return mongo.db.users.find_one({"username": username})


class Book:
    @staticmethod
    def insert_book(title, author, year):
        """Insert a new book into MongoDB"""
        mongo.db.books.insert_one({"title": title, "author": author, "year": year})

    @staticmethod
    def get_all_books():
        """Retrieve all books"""
        return mongo.db.books.find()

    @staticmethod
    def delete_book(book_id):
        """Delete a book by ID"""
        mongo.db.books.delete_one({"_id": book_id})
