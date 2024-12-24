import utils
from log import logger

//ritik yadav

def create_column(column_info: list) :
    logger.info("Structuring the columns provided.")
    col_str = " VARCHAR(150),".join(column_info) + " VARCHAR(150),"
    col_str += "created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,"
    col_str += "last_modify_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP"
    return col_str

def create_table_structure(table_info: list) -> str :
    logger.info("create_table_structure function create structure of table and return in one variable")
    table = ""
    for i in table_info :
       table += f"CREATE TABLE If NOT EXISTS {i["table_name"]}({create_column(i["columns"])});"
    return table


def create_table(table_structure_data: list) :
    logger.info("inter in the create_table function")
    try :
        utils.cursor.execute(create_table_structure(table_structure_data))
        utils.db_connection.commit()
    except Exception as err :
        logger.info(f'unable to create table, we found err -> {err}')
        exit()

