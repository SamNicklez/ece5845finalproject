# ece5845finalproject
Final Project for ECE:5845 Modern Databases

### Potential Queries
a) We were hoping to recommend the user a type of tech job based on a few factors (salary, popular cities, etc.) using a sort of points system, such that salary is 33% of the determining factor of what we recommend, with maybe country of work and/or benefits weighed at the remaining percent. Should we opt for something more/less complex, or is this okay?

b) Something similar to point A, though we would recommend companies to the user given a city and various factors about the company & review data. Could potentially use text-search to find keywords in employee reviews and use those. Would this work?

### Query Feedback
For a), I would suggest that you allow the user to input the weights of the different factors (maybe a using a slider or just a textbox, of you could ask not important, somewhat important, very important and derive the weights from there), and returned a rank list of jobs. You can also allow the user to include some filters (such as limit results to a programming language or country).

For b), try to pose a query that you can execute in neo4j, maybe cluster the companies and allow the user to query one and return the other companies in the cluster.

### Final Query Descriptions

1. [PostgreSQL] Return the top 10 jobs
2. [Neo4J] 