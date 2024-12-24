import create_table
import insert_data
from insert_into_neo4j import insert_data_into_neo4j
import utils
from update_table import update_table
from log import logger


def main() :
    # logger.info("Process started.")
    nodes=["skill","employee","project","task","department","client"]
    # logger.info("Processing started for creating table from JSON file.")
    # create_table.create_table(utils.table_str_data)
    # logger.info("All the tables have been created.")
    # logger.info("Processing started for inserting data into tables.")
    # insert_data.insert_data_into_db()
    # logger.info('Data has been inserted into the tables.')
    # logger.info('Processing has  started for inserting data into Neo4j.')
    for i in nodes:
        insert_data_into_neo4j(i)
        logger.info(f'{i} tables of data have been loaded into Neo4j.')
    logger.info("All data has been inserted into the Neo4j database.")
    utils.cursor.close()
    utils.db_connection.close() 
    # update_table('employee', 'email' , "punit@gmail.com", 4)
    logger.info('process stoped')

if __name__ == "__main__":
    main()

