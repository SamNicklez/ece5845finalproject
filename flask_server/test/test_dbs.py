from test_neo4j_db import test_neo4j
from test_postgres_db import test_postgres


def test_dbs():
    test_postgres()
    test_neo4j()


if __name__ == '__main__':
    test_dbs()
