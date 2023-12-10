from neo4j_db import get_neo4j_db
import os

NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USER = os.environ.get('NEO4J_USER')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')

neo4j_db = get_neo4j_db(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)


def test_neo4j():
    with neo4j_db.session() as session:
        result = session.run("""
            MATCH (n:review) RETURN n LIMIT 25;
        """)

        for record in result:
            print(record)


if __name__ == '__main__':
    test_neo4j()
