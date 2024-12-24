import pandas as pd
from py2neo import Graph, Node
import utils as userdb
from log import logger
import json

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Ritik@123"))

def db_data_covert_into_neo4j_format(table_name: str)  :
    logger.info("in db_data_convert_into_neo4j_format function that provide cyper query")
    try :
        logger.info("table structure info has been read by the database")
        userdb.cursor.execute(f'SELECT * FROM {table_name};')
        table_data = userdb.cursor.fetchall()
        column_names = [desc[0] for desc in userdb.cursor.description]
        df = pd.DataFrame(table_data, columns=column_names)
        df.drop(['created_at', 'last_modify_on'], axis=1, inplace=True)
        json_form = df.to_json(orient='records')
        json_form = json.loads(json_form)
        logger.info("data has been fected from the databse")
    except Exception as err :
        logger.info(f'unable to read table, we found err -> {err}')   
    return json_form


def insert_data_into_neo4j(table_name: str)  :
    table_label = table_name[0].upper() + table_name[1:].lower()
    logger.info("In 'insert_data_into_neo4j' function for data insertion into the Neo4j database.")
    table = db_data_covert_into_neo4j_format(table_name)
    
    for emp in table:
    # Create a node with the label "Employee" and properties
        employee_node = Node(table_label,**emp)
        graph.merge(employee_node, table_label, "id")  # merge ensures no duplicates based on 'id'

print("Employee nodes created successfully!")
