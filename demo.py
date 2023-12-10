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
def postgres_query():
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

        # REQUESTS FOR FILTER DROPDOWNS
        # input -> none
        # output -> list of all options for each filter

        # demo selected values for full query
        selected_country = 'United States'
        selected_city = 'New York'
        selected_sector = 'Business Services'

        # country dropdown
        cur.execute("SELECT DISTINCT country FROM Job")
        countries_dropdown = cur.fetchall()

        #city dropdown (once country is selected)
        cur.execute("SELECT DISTINCT city FROM Job WHERE country = " + "'" + selected_country + "'")
        cities_dropdown = cur.fetchall()

        # sector dropdown
        cur.execute("SELECT DISTINCT sector FROM Company")
        sectors_dropdown = cur.fetchall()


        # input -> list of the 7 factors in order of greatest importance to least importance.
        # output -> list of tuples containing top 10 results. Gotta figure out how those are exactly formatted.
        #                - fields in the tuple: job_title, city, country, fifty_percentile_salary, company_name
        demo_list = ['opportunities_ranking', 'comp_benefits_ranking', 'culture_values_ranking', 'senior_management_ranking', 'worklife_balance_ranking', 'ceo_approval_ranking', 'company_outlook_ranking']
        # items in the list gotta look exactly like this otherwise the query will get goofed up.

        # The Big Query
        query = (
            'SELECT j.job_title, j.city, j.country, s.fifty_percentile_salary, c.name'
            'FROM Job j, Salary s, Company c, Review r '
            'WHERE j.salary_id = s.salary_id AND j.company_id = c.id ')
        
        # Adds filtering
        if selected_country:
            query += 'AND j.country = ' + "'" + selected_country + "' "
        if selected_city:
            query += 'AND j.city = ' + "'" + selected_city + "' "
        if selected_sector:
            query += 'AND c.sector = ' + "'" + selected_sector + "' "
        
        # Determines ordering based on user preferences
        query += 'ORDER BY '
        for i in range(len(demo_list)):
            query +=  'r.' + demo_list[i] + ', '
        query += 'r.overall_rating NULLS LAST LIMIT 10'

        # Executing the query + returning the data
        cur.execute(query)
        top_10_jobs = cur.fetchall()
        for job in top_10_jobs:
            print(job)
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

'''
2. [Neo4J] We will cluster companies around countries/cities, and allow the user to query a city or company and return the other
companies in the cluster. Hoping to add a feature that allows the user to search for certain keywords in employee reviews as well.
'''
def neo4j_query():
    driver = gd.driver("neo4j+s://34a20161.databases.neo4j.io:7687", auth=("neo4j", "sfIAsIHJ3vE49MOTEesIbizUlrCuMgUK0FvCmW-06L0"))
    try:
        driver.verify_connectivity()
    except neo4j.exceptions.ServiceUnavailable:
        print('Connection to Neo4j database failed. Please try again.')
        exit()
    with driver.session() as sesh:
        # NEO4J DATABASE WILL ALREADY BE CLUSTERED BY job.city. Now to query.

        # input -> city name
        # output -> list of 10 companies in the city with most reviews and highest average rating
        input_city = 'New York, NY'
        query = ('MATCH (r:review)-[rf:REVIEW_FOR]->(j:job)-[:AT_COMPANY]->(c:company) '
            'WHERE j.city=$input_city '
            'WITH c.company_id AS companyId, c.name AS companyName, COUNT(rf) AS numRating, AVG(r.overall_ranking) AS avgRating '
            'RETURN companyName, numRating, avgRating '
            'ORDER BY numRating DESC, avgRating DESC '
            'LIMIT 10;')
        result = sesh.run(query, input_city=input_city).data()
        # demo on how to process results
        for i in range(len(result)):
            print((str)(i+1) + ". " + result[i]['companyName'] + " with " + (str)(result[i]['numRating']) + " reviews and an average rating of " + (str)(result[i]['avgRating']))

    sesh.close()
    driver.close()

neo4j_query()