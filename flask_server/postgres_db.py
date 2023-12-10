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
        SELECT
            j.id,
            j.job_title,
            j.sector,
            j.country,
            j.city,
            c.name,
            c.size,
            s.salary_type,
            s.ten_percentile_salary,
            s.ninety_percentile_salary,
            s.fifty_percentile_salary
        FROM
            final_project.job j
            JOIN final_project.company c ON j.company_id = c.id
            JOIN final_project.salary s ON j.salary_id = s.salary_id
        WHERE
            j.id = ANY(%s)
        """,
        (job_ids,)
    )
    jobs = cursor.fetchall()
    for job in jobs:
        print(job)
    return jobs
