from database import Config 

from sqlalchemy import create_engine, text

"""
Class that wraps around sqlalchemy.
The interface (as in user interacts with) provides necessary methods for CRUD operations.
"""

class Database():
    
    def __init__(self, table):
        # URL credentials for Mysql database
        config = Config
        db_usr = config.sql_user()
        db_pswd = config.sql_password()
        db_host = config.sql_host()
        db_port = config.sql_port()
        db_name = config.sql_dbname()
        engine = create_engine(f"mysql://{db_usr}:{db_pswd}@{db_host}:{db_port}/{db_name}")
