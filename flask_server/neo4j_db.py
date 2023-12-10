from neo4j import GraphDatabase


def get_neo4j_db(uri, user, password):
    return GraphDatabase.driver(
        uri=uri,
        auth=(user, password)
    )
