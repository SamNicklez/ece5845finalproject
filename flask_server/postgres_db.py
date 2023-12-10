import psycopg2


def get_postgres_db(host, user, password):
    return psycopg2.connect(
        host=host,
        database=user,
        user=user,
        password=password
    )
