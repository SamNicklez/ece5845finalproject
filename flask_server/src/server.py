from flask import Flask, request, jsonify

from neo4j_db import get_neo4j_db
from postgres_db import get_postgres_db

app = Flask(__name__)

postgres_db = get_postgres_db()
neo4j_db = get_neo4j_db()


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()