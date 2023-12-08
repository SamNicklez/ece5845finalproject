import os

from neo4j import GraphDatabase


def get_neo4j_db():
    return GraphDatabase.driver(
        uri=os.environ['NEO4J_URI'],
        auth=(
            os.environ['NEO4J_USER'],
            os.environ['NEO4J_PASSWORD']
        )
    )
