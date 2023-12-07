from neo4j import GraphDatabase as gd
import neo4j.exceptions
import psycopg2 as pg

# Demo Neo4J server connection
driver = gd.driver("neo4j://localhost:7687", auth=("neo4j", "hello"))
try:
    driver.verify_connectivity()
except neo4j.exceptions.ServiceUnavailable:
    print('Connection to Neo4j database failed. Please try again.')
    exit()

with driver.session() as sesh:
    def keyword():
        keyword = input("Please enter a keyword (or a few, separated by spaces): ")
        query = ("MATCH (u:User)-[r:RATED]->(m:Movie)-[:IN_GENRE]->(g:Genre) "
                 "WHERE ALL (keyword IN $keywordsList WHERE m.title CONTAINS keyword) "
                 "WITH m, g, AVG(r.rating) AS avgRating, CASE WHEN EXISTS((u:User {userID: $input_user})-[:RATED]->(m)) THEN true ELSE false END AS seenMovie, r.rating AS userRating "
                 "RETURN m.title AS movieTitle, g.name AS genre, avgRating AS averageRating, seenMovie AS seenMovie, userRating AS userRating;"
                )

        result = sesh.run(query, input_user=user_id, keywordsList=keyword.split()).data()
        print('Listing movie titles containing keyword(s): ' + keyword + '.')
        for i in range(len(result)):
            print((str)(i+1) + ". " + result[i]['movieTitle'] + " (" + result[i]['genre'] + ", avg rating: " + (str)(result[i]['averageRating']) + ", seen: " + (str)(result[i]['seenMovie']) + ", your rating: " + (str)(result[i]['userRating']) + ")")
        return


# Demo PostgreSQL server connection
conn = None
try:
    file = open("credentials.txt")
    file_content = file.readlines()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = pg.connect(
        host="s-l112.engr.uiowa.edu",
        port=5432,
        database="mdb_student37",
        user=file_content[0],
        password=file_content[1])
		
    # create a cursor
    cur = conn.cursor()
    
    # execute a statement
    cur.execute('SELECT version();')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
except (Exception, pg.DatabaseError) as error:
    print(error)


# HOW OUR QUERIES LOOK IN PYTHON
