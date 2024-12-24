import utils
from log import logger
 

def update_table(table_name: str, key: str, value: str, id: int)  :
    str_query = f"UPDATE {table_name} SET {key} = '{value}', last_modify_on = CURRENT_TIMESTAMP  WHERE id = '{id}' ;"
    try :
        utils.cursor.execute(str_query)
        utils.db_connection.commit()
        logger.info("table has been updated")
    except Exception as err :
        logger.info(f'unable to update table, we found err -> {err}')
        exit()






    