from flask_pymongo import PyMongo

mongo = PyMongo()  # Create a MongoDB instance

def init_db(app):
    """Initialize MongoDB with Flask App"""
    mongo.init_app(app)
