import psycopg2
from log import logger
import json


try :
    logger.info("Reading JSON file to get data for table structure.")
    file = open('./config.json', 'r')
    table_str_data = json.loads(file.read())
except Exception as err :
    logger.error(f"Unable to read source file. Error: {err}")

try :
    logger.info("Attempting to stabilize connection with PostgreSQL database.")
    db_connection = psycopg2.connect(
        dbname = "pro1",
        user ='postgres',
        password = "mysecret",
        host="localhost",
        port="5432"

    )
    cursor = db_connection.cursor()
    logger.info("Connection stabilized with the database successfully.")
except  :
    logger.info(f"Unable to connect to the database. Error: {err}")
    exit()





