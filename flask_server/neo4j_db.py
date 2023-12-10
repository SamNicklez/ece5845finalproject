from neo4j import GraphDatabase


def get_neo4j_db(uri, user, password):
    return GraphDatabase.driver(
        uri=uri,
        auth=(user, password)
    )


def get_similar_jobs(tx, country, city, sector, ranks):
    return "TODO"
