from neo4j import GraphDatabase as gd
import neo4j.exceptions
import psycopg2 as pg
from sklearn.cluster import KMeans
import numpy as np

postgres_conn = None

def query_1():
    '''
    1. User inputs a country, city, sector, and then their order of importance 1-7 for each of the following:
        - opportunities_ranking
        - comp_benefits_ranking
        - culture_values_ranking
        - senior_management_ranking
        - worklife_balance_ranking
        - ceo_approval_ranking
        - company_outlook_ranking

    2. Values of the user's preferences comes from the frontend, with which we construct a pseudo-review node.

    3. We then use the cosine similarity algorithm to find the most 10 most similar reviews to the pseudo-review.

    4. We then return the top 10 jobs associated with those reviews.
    '''

    # Configure Neo4J Connection
    driver = gd.driver("neo4j+s34a20161.databases.neo4j.io:7687", auth=("neo4j", "hello"))
    try:
        driver.verify_connectivity()
    except neo4j.exceptions.ServiceUnavailable:
        print('Connection to Neo4j database failed. Please try again.')
        exit()

    # Neo4J similarity construction
    neo_similarity_query = """
        WITH $job_review_preferences AS job_review_preferences
        MATCH (r:Review)
        WITH r, job_review_preferences
            [
                r.opportunities_ranking,
                r.comp_benefits_ranking,
                r.culture_values_ranking,
                r.senior_management_ranking,
                r.worklife_balance_ranking,
                r.ceo_approval_ranking,
                r.company_outlook_ranking
            ] AS job_review_rankings
        WITH r, gds.similarity.cosine(job_review_preferences, job_review_rankings) AS similarity
        RETURN r.review_id AS reviewId, similarity AS cosineSimilarity
        ORDER BY similarity DESC
        LIMIT 10
        """
    
    postgres_job_info_query = """
        SELECT j.job_title, c.company_name
        """

    with driver.session() as session:
        cluster_reviews()

        # Grab relevant jobs with user scores
        demo_job_review_preferences = [3, 5, 7, 2, 1, 6, 4]
        result = session.run(neo_similarity_query, job_review_preferences=demo_job_review_preferences)
        jobs = [job for job in result]

        # Grab relevant job info from PostgreSQL

    try:
            # Configure PostgreSQL connection
        postgres_conn = pg.connect(
            host="s-l112.engr.uiowa.edu",
            port=5432,
            database="mdb_student18",
            user='mdb_student18',
            password='finalproject2023')
        cur = postgres_conn.cursor()

    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if postgres_conn is not None:
            postgres_conn.close()
    return

def cluster_reviews(song_features, num_clusters=3):
    # Cluster the songs
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(song_features)
    centroids = kmeans.cluster_centers_
    return centroids

'''
2. [Neo4J] We will cluster companies around countries/cities, and allow the user to query a city or company and return the other
companies in the cluster. Hoping to add a feature that allows the user to search for certain keywords in employee reviews as well.
'''
def query_2():
    return

query_1()