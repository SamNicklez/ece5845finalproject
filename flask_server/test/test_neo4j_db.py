from neo4j_db import get_neo4j_db

neo4j_db = get_neo4j_db()


def test_neo4j():
    with neo4j_db.session() as session:
        result = session.run("""
            MATCH (n:review) RETURN n LIMIT 25;
        """)

        for record in result:
            print(record)


if __name__ == '__main__':
    test_neo4j()
