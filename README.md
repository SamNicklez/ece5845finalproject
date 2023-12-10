# [ECE:5845 Modern Databases - Final Project](https://pitch.com/v/ECE5845-Final-Project-Presentation-nguzuq)
Samuel Nicklaus, Cole Arduser, Colin Hehn

### Potential Queries
a) We were hoping to recommend the user a type of tech job based on a few factors (salary, popular cities, etc.) using a sort of points system, such that salary is 33% of the determining factor of what we recommend, with maybe country of work and/or benefits weighed at the remaining percent. Should we opt for something more/less complex, or is this okay?

b) Something similar to point A, though we would recommend companies to the user given a city and various factors about the company & review data. Could potentially use text-search to find keywords in employee reviews and use those. Would this work?

### Query Feedback
For a), I would suggest that you allow the user to input the weights of the different factors (maybe a using a slider or just a textbox, of you could ask not important, somewhat important, very important and derive the weights from there), and returned a rank list of jobs. You can also allow the user to include some filters (such as limit results to a programming language or country).

For b), try to pose a query that you can execute in neo4j, maybe cluster the companies and allow the user to query one and return the other companies in the cluster.

### Final Query Descriptions

1. [PostgreSQL] Return the top 10 jobs based on a user's inputted preferences, some of our options being salary, location, benefits, and reviews (still unsure which will be available to the user at the moment). The user will be able to configure the importance of each of the preferences, such that the rank of jobs returned will be ordered using the 'weights' of each preference. We also plan to allow the user to filter the results by a specific preference (i.e only jobs in the Netherlands).
2. [Neo4J] Takes a city name as input (try "New York, NY" for demo) and returns a list of the top 10 companies with the most ratings, and highest average ratings given on Glassdoor with an employee in that city. The user can then select a company from the list (via pressing on that company row or however) and find all other companies in that Neo4J cluster.
   1. Might change that last part to find all jobs with a company in that cluster, but the definition of a cluster in Neo4J seems really unclear atm. Going to figure out early Sunday.
