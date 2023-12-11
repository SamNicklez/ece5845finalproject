# [ECE:5845 Modern Databases - Final Project](https://pitch.com/v/ECE5845-Final-Project-Presentation-nguzuq)
Samuel Nicklaus, Cole Arduser, Colin Hehn

### Link to dataset [here.](https://www.kaggle.com/datasets/andresionek/data-jobs-listings-glassdoor/data)
Note that the dataset we used has been heavily modified to meet our needs. For the full data, please refer to the university phpadmin student18 account under the final_project schema

# Project README

## Overview

This project is a comprehensive application leveraging Python, Flask, Neo4j, and the Graph Data Science (GDS) library version 4.4.28. It is designed to utilize the powerful features of these technologies, offering a robust backend system with advanced data processing and graph database capabilities.

## Prerequisites

Before setting up the project, ensure that you have the following prerequisites installed on your system:

1. **Python:** Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Flask:** A lightweight WSGI web application framework in Python, used for building the web API. Install Flask via pip:
   
   ```bash
   pip install Flask
   ```

3. **Neo4j:** A highly scalable native graph database, which allows for efficient management and querying of connected data. Download and install Neo4j from [neo4j.com](https://neo4j.com/download/).

4. **Graph Data Science (GDS) Library 2.5.5:** A library for Neo4j, enabling advanced analytics and machine learning on graphs. Ensure that you are using GDS version 2.5.5, compatible with your Neo4j version. Refer to the [Neo4j GDS installation guide](https://neo4j.com/docs/graph-data-science/current/installation/) for detailed instructions.

## Setup and Installation

### Python and Flask Setup

Cole Finish

### Neo4j Setup
1. See the project directory for 'tjr_neo4j_server.dump'. This is a backup of the Neo4J server we used locally to provide recommendation data for our project.
2. See [this guide](https://neo4j.com/docs/desktop-manual/current/operations/create-from-dump/#:~:text=Once%20you%20have%20a%20dump,when%20creating%20a%20new%20DBMS.) for instructions on how to construct a new DBMS from a dump file. The instructions provided conduct it through the Neo4J Desktop application, but it can also be done through the command line.
3. Ensure that the Neo4J DB you created is version 4.4.28, and that the GDS library (version = 2.5.5) is installed and enabled.
4. Launch the Neo4J DBMS in the GUI, and ensure it is live before you run the Recommendation Engine application.

### Running the Client Application

#### Prerequisites

- [Node.js](https://nodejs.org/) (which comes with [npm](http://npmjs.com/))

#### Installation

1. navigate to the directory:

   ```bash
   cd client

2. To install the project dependencies, run the following command:
    
    ```bash
    npm install

### Running the Application

3. To start the development server, use the following command:

    ```bash
    npm run dev

