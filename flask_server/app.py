from flask import Flask, request, jsonify

from neo4j_db import get_neo4j_db
from postgres_db import get_postgres_db
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Now you can use os.environ to get your environment variables
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USER = os.environ.get('NEO4J_USER')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')

app = Flask(__name__)

postgres_db = get_postgres_db(POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD)
neo4j_db = get_neo4j_db(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()