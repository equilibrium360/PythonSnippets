import sqlite3
from sqlite3 import Error
import time
import datetime

def get_new_record_key():
    epoch_time = int(time.time())
    return str(epoch_time)

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def insert_perm_deploymt_record(dbconn, params_dict):
    """fdgfgf
      dfgdfgf
      dsfg sdf"""

    insert_sql = """INSERT INTO MLE_PERM_DEPLOYMT_AUDIT (RECORD_KEY,
                                                  PERM_FILE_NAME, 
                                                  PERM_FILE_TYPE, 
                                                  DEPLOYMT_START_TIME, 
                                                  PERM_DEPLOYMT_STATUS) VALUES (?, ?, ?, ?, ? )"""

    val = (params_dict['record_key'],
           params_dict['perm_file_name'],
           params_dict['perm_file_type'],
           params_dict['deploymt_start_time'],
           params_dict['perm_deploymt_status']
           )
    dbcursor = dbconn.cursor()

    dbcursor.execute(insert_sql, val)
    dbconn.commit()
    dbcursor.close()


    print(dbcursor.rowcount, "record inserted.")

def update_perm_deploymt_record(dbconn, params_dict):

    update_query = """ UPDATE MLE_PERM_DEPLOYMT_AUDIT set DEPLOYMT_END_TIME = ?  ,  PERM_DEPLOYMT_STATUS = ? WHERE record_key = ? """


    dbcursor = dbconn.cursor()

    val = (params_dict['deploymt_end_time'],
           params_dict['perm_deploymt_status'],
           params_dict['record_key']
          )
    dbcursor.execute(update_query, val)

    dbconn.commit()
    dbcursor.close()


    print(dbcursor.rowcount, "record updated.")



if __name__ == '__main__':

    record_key = get_new_record_key()

    conn = create_connection("/Users/UNIVERSE/PycharmProjects/PythonSnippets/database/sqlite/sqliteDB/audit.db")
    start_time = datetime.datetime.now()
    perm_deploy_start_dict = {
        'record_key': record_key,
        'perm_file_name': 'userRoles.json',
        'perm_file_type': 'user_roles',
        'deploymt_start_time': datetime.datetime.now(),
        'perm_deploymt_status': 'started'

    }
    insert_perm_deploymt_record(conn, perm_deploy_start_dict)

    perm_deploy_end_dict = {
        'record_key': record_key,
        'deploymt_end_time': str(datetime.datetime.now()),
        'perm_deploymt_status': 'success'

    }
    update_perm_deploymt_record(conn, perm_deploy_end_dict)
    conn.close()
