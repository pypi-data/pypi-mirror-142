
import mysql.connector
import pandas as pd
from pandas import DataFrame

# dir_path = os.path.dirname(sys.argv[0])
# os.chdir(dir_path)
'''tables = ['fruit_variety', 'project', 'project_plot', 'plot', 'customer','caliber']'''

# with open('config.json', "r", encoding='utf8') as json_file:
#     config = load(json_file)
#
# DB_SERVER = config['DB']['SERVER']
# DB_USER = config['DB']['USER']
# DB_PASSWORD = config['DB']['PASSWORD']
# DB_NAME = 'fruitspecdb_new'

def connect(db_server: str, db_user: str, db_password: str, db_name: str) -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(
        host=db_server,
        user=db_user,
        password=db_password,
        database=db_name)

def execute(SQL_command: str, params=()) -> None:
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute(SQL_command, params=params)
    mydb.commit()
    cursor.close()
    mydb.close()

def select(SQL_command: str, params=()) -> pd.DataFrame:
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute(SQL_command, params=params)
    df = DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
    mydb.close()
    return df