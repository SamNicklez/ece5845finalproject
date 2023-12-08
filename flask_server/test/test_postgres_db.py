from postgres_db import get_postgres_db


postgres_db = get_postgres_db()


def test_postgres():
    cursor = postgres_db.cursor()
    cursor.execute("SELECT * FROM final_project.job LIMIT 25")
    jobs = cursor.fetchall()
    for job in jobs:
        print(job)


if __name__ == '__main__':
    test_postgres()