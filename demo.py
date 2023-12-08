from neo4j import GraphDatabase as gd
import neo4j.exceptions
import psycopg2 as pg

# QUERY DEMO RUN

'''
1. [PostgreSQL] Return the top 10 jobs based on a user's inputted preferences, some of our options being salary, location, benefits,
and reviews (still unsure which will be available to the user at the moment). The user will be able to configure the importance
of each of the preferences, such that the rank of jobs returned will be ordered using the 'weights' of each preference.
We also plan to allow the user to filter the results by a specific preference (i.e only jobs in the Netherlands).
'''
conn = None
try:
    conn = pg.connect(
        host="s-l112.engr.uiowa.edu",
        port=5432,
        database="mdb_student18",
        # Probably should make this config instead, but it's fine for now
        user='mdb_student18',
        password='finalproject2023')
    cur = conn.cursor()


    # THE HOLY GRAIL
    query = (
        'SELECT j.job_title, j.city, j.country, s.fifty_percentile_salary, c.name '
        'FROM Job j, Salary s, Company c '
        'WHERE j.salary_id = s.salary_id AND j.company_id = c.id '
        'ORDER BY s.fifty_percentile_salary * 0.33 + j.country * 0.33 + c.size * 0.33 DESC '
        'LIMIT 10;'
    )

    cur.execute(query)
    top_10_jobs = cur.fetchall()
    for job in top_10_jobs:
        print(job)
except (Exception, pg.DatabaseError) as error:
    print(error)

    '''
    2. [Neo4J] We will cluster companies around countries/cities, and allow the user to query a city or company and return the other
    companies in the cluster. Hoping to add a feature that allows the user to search for certain keywords in employee reviews as well.
    '''
    driver = gd.driver("neo4j://localhost:7687", auth=("neo4j", "hello"))
    try:
        driver.verify_connectivity()
    except neo4j.exceptions.ServiceUnavailable:
        print('Connection to Neo4j database failed. Please try again.')
        exit()
    with driver.session() as sesh:
        def keyword():
            keyword = input("Please enter a keyword (or a few, separated by spaces): ")

            # THE HOLY GRAIL
            query = ("MATCH (u:User)-[r:RATED]->(m:Movie)-[:IN_GENRE]->(g:Genre) "
                     "WHERE ALL (keyword IN $keywordsList WHERE m.title CONTAINS keyword) "
                     "WITH m, g, AVG(r.rating) AS avgRating, CASE WHEN EXISTS((u:User {userID: $input_user})-[:RATED]->(m)) THEN true ELSE false END AS seenMovie, r.rating AS userRating "
                     "RETURN m.title AS movieTitle, g.name AS genre, avgRating AS averageRating, seenMovie AS seenMovie, userRating AS userRating;"
                    )

            result = sesh.run(query, input_user='1', keywordsList=keyword.split()).data()
            for i in range(len(result)):
                print((str)(i+1) + ". " + result[i]['field'])
            return
