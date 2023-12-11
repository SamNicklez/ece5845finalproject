from neo4j import GraphDatabase
import neo4j.exceptions

def get_neo4j_db(uri, user, password):
    return GraphDatabase.driver(
        uri=uri,
        auth=(user, password)
    )

def get_similar_jobs(driver, country, city, sector, ranks):
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

    neo_similarity_query = """
    WITH $job_review_preferences AS job_review_preferences
    MATCH (r:Review)-[:REVIEW_FOR]->(j:Job)
    WHERE j.country = $country AND j.city = $city AND j.sector = $sector
    WITH r, job_review_preferences,
        [
            r.opportunities_rank,
            r.comp_benefits_rank,
            r.culture_values_rank,
            r.senior_management_rank,
            r.worklife_balance_rank,
            r.ceo_approval_rank,
            r.company_outlook_rank
        ] AS job_review_ranks
    WITH r, gds.similarity.cosine(job_review_preferences, job_review_ranks) AS similarity
    RETURN r.review_id AS reviewId, similarity AS cosineSimilarity
    ORDER BY similarity DESC
    LIMIT 10
    """

    # switch this to use the driver parameter in the function
    with driver.session() as session:
        # Grab relevant jobs with user scores
        result = session.run(neo_similarity_query, job_review_preferences=ranks, country=country, city=city, sector=sector)
        reviews = [review for review in result]
        print(reviews)
    review_ids = []
    for review in reviews:
        review_ids.append(review["reviewId"])
        # print(review["cosineSimilarity"])

    return review_ids

def get_companies_in_cluster(driver, company_id):
    '''
    1. User inputs a country and city.

    2. We compute the top 5 companies in that city with the best average review score and most reviews. Return that list to the user.

    3. User then clicks on a company from the list of 5. The company_id is passed to the backend.

    4. We return all companies in the same cluster as the one with that company_id. User can see the whole list.
    '''
    driver = get_neo4j_db("neo4j://localhost:7687", "neo4j", "hello")
    with driver.session() as session:
        # Return all companies in the same cluster as the one with that company_id
        result = session.run("MATCH (c:Company {company_id: $company_id}), (c2:Company) WHERE c.kmeans = c2.kmeans RETURN c2.company_id AS company_id LIMIT 20", company_id=company_id)
        companies = [company for company in result]
        company_ids = []
        for company in companies:
            company_ids.append(company["company_id"])
    return company_ids

# print(get_similar_jobs(None, "United States", "New York, NY", "Information Technology", [3, 5, 7, 2, 1, 6, 4]))
print(get_companies_in_cluster(None, 18))

'''
MATCH (c:Company)
WITH [c.benefits_rating] AS swag, c
SET c.br_graph = swag
RETURN count(c)

CALL gds.graph.project(
    'company_graph',
    {
        Company: {
            properties: 'br_graph'
        }
    },
    '*'
)

CALL gds.kmeans.write.estimate('company_graph', {
    writeProperty: 'br_graph',
    nodeProperty: 'benefits_rating'
})
YIELD nodeCount, bytesMin, bytesMax, requiredMemory

CALL gds.kmeans.write('company_graph', {
    writeProperty: 'kmeans',
    nodeProperty: 'br_graph',
    k: 3,
    randomSeed: 42
})
YIELD nodePropertiesWritten

CALL gds.graph.drop('company_graph')
'''