from postgres_db import get_postgres_db
import os

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

postgres_db = get_postgres_db(POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD)


def test_postgres():
    cursor = postgres_db.cursor()
    cursor.execute("""
        SELECT * FROM final_project.job LIMIT 25
    """)
    jobs = cursor.fetchall()
    for job in jobs:
        print(job)


if __name__ == '__main__':
    test_postgres()