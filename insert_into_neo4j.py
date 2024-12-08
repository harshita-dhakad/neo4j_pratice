from neo4j import GraphDatabase
import utils as userdb
from log import logger

# Connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "Ritik@123"

def read_table(table_name: str) -> str :
    logger.info("read_table function fect data from the databse")
    return f"SELECT * FROM {table_name} ;"

def read_table_details(table_name: str) -> str :
  logger.info("read_table_details function generally read the structure of table")
  return  f"""
    SELECT column_name
    FROM information_schema.columns 
    WHERE table_name = '{table_name}';
    """

table_data = []
table_str = [] 


def db_data_covert_into_neo4j_format(table_name: str) -> str :
    logger.info("in db_data_convert_into_neo4j_format function that provide cyper query")
    try :
        userdb.cursor.execute(read_table(table_name))
        table_data = userdb.cursor.fetchall()
        logger.info("data has been fected from the databse")
        userdb.cursor.execute(read_table_details(table_name))
        table_str = userdb.cursor.fetchall()
        logger.info("table structure info has been read by the database")
    except Exception as err :
        logger.info(f'unable to read table, we found err -> {err}')

    table_str = list(map(lambda x: x[0], table_str))
    table = "CREATE"

    for i in table_data:
        combined = list(map(lambda x, y: (x, y), table_str, i))
        combined_dict = dict(combined)
        table += f"(:{table_name.upper()} {combined_dict} \n),"

    for i in table_str :
        table = table.rstrip(',').replace(f"'{i}'", f"{i}")
    
    return table


def insert_data_into_neo4j(table_name: str)  :
    logger.info("In 'insert_data_into_neo4j' function for data insertion into the Neo4j database.")
    try:
    # Using a context manager for the driver
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            logger.info("first read the database from databse and formate into cyper language")
            table = db_data_covert_into_neo4j_format(table_name)
            def create_person_node(table: str, pro: list):
                with driver.session() as session:
                    session.run(table)
        # Create a Person node
            create_person_node(table, table_str)
        return "data insert into neo4j sucessfull"
    except Exception as err:
        logger.info(f"Error: {err}")
        exit()
