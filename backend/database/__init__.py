"""
Configurations setup for this package
"""

import sys
from typing import Dict, Any
from pathlib import Path
from dotenv import dotenv_values


"""
The configurations should only be imported by this.
It contains information:
    to connect to the database
"""
class Config():

    try:
        # Values are loaded as dict
        config: Dict[str, Any] = dotenv_values(".env")
        # _ in front of variable name for weak proctection 
        _sql_name = str(config["SQL_DATABASE_NAME"])
        _sql_user = str(config["SQL_USER_NAME"])
        _sql_password = str(config["SQL_PASSWORD"])
        _sql_host = str(config["SQL_HOST"])
        _sql_port = str(config["SQL_PORT"])

    except KeyError as err:
        print("Error from ", __name__," in", __file__, ": Could not find key ", err, file=sys.stderr)
        sys.exit(1)


    """
    Returns(string) database name for SQL database
    """
    @classmethod
    def sql_dbname(cls) -> str:
        return cls._sql_name

    """
    Returns(string) username for SQL database
    """
    @classmethod
    def sql_user(cls) -> str:
        return cls._sql_user

    """
    Returns(string) password for SQL database
    """
    @classmethod
    def sql_password(cls) -> str:
        return cls._sql_password

    """
    Returns(string) host for SQL database
    """
    @classmethod
    def sql_host(cls) -> str:
        return cls._sql_host

    """
    Returns(string) port for SQL database
    """
    @classmethod
    def sql_port(cls) -> str:
        return cls._sql_port



