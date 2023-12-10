import psycopg2


def get_postgres_db(host, user, password):
    return psycopg2.connect(
        host=host,
        database=user,
        user=user,
        password=password
    )


def get_all_job_info(postgres_db, job_ids):
    cursor = postgres_db.cursor()
    cursor.execute(
        """
        SELECT *
        FROM final_project.job
        WHERE job_id = ANY(%s);
        """,
        (job_ids,)
    )
    jobs = cursor.fetchall()
    return jobs
