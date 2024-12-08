import utils
from log import logger

def create_column(column_info: list) :
    logger.info("Structuring the columns provided.")
    return " VARCHAR(150),".join(column_info) + " VARCHAR(150)"

def create_table_structure(table_info: list) -> str :
    logger.info("create_table_structure function create structure of table and return in one variable")
    table = ""
    for i in table_info :
       logger.info(f'creating the structure of {i}')
       table += f"CREATE TABLE If NOT EXISTS {i["table_name"]}({create_column(i["columns"])});"
       logger.info(f'structure has been created of {i} table')
    logger.info('table structure is being returned')
    return table


def create_table(table_structure_data: list) :
    logger.info("inter in the create_table function")
    try :
        utils.cursor.execute(create_table_structure(table_structure_data))
        utils.db_connection.commit()
    except Exception as err :
        logger.info(f'unable to create table, we found err -> {err}')
        exit()

