import sys
import os
import pandas as pd
import pyodbc
import urllib
import sqlalchemy
sys.path.insert(0,os.getcwd())
import logging
import os
from ..token import GenToken
from ..constants import SharedConstants
from tenacity import retry, stop_after_attempt, wait_fixed, wait_random, retry_if_exception_type
import requests  as req
from ..patterns import Singleton
import traceback

__all__ = ['SqlOperation']

_sql_connection_string =  os.environ[SharedConstants.sql_connection_string]
params = urllib.parse.quote_plus(_sql_connection_string)

@retry(stop=stop_after_attempt(5), wait=wait_fixed(3) + wait_random(0, 2), retry=retry_if_exception_type(req.exceptions.InvalidSchema))
def get_db_connectionstring():
    '''
        Constructing connection string for pooling
    '''
    try:
        tokengen = GenToken()
        logging.info("token generated")
        engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        #engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, connect_args={'attrs_before': {SharedConstants.sql_copt_ss_access_token:tokengen.validation_token}}, pool_size=10, pool_recycle=600)
        logging.info("sqlalchemy engine created")
        return engine.connect().connection
    except:
        retmsg = 'Error - Error Info Exception occured while creating engine:' +  str(sys.exc_info()) + str(traceback.format_exc())
        logging.error(f"{retmsg}")
        logging.error("retrying again")
        raise(req.exceptions.InvalidSchema)

class SqlOperation(metaclass = Singleton):
    
    def __init__(self, connectionStringkey='SqlConnectionString'):
        """[summary]

        Args:
            connectionStringkey (str, optional): [description]. Defaults to 'SqlConnectionString'.
        """
    @retry(stop=stop_after_attempt(10), wait=wait_fixed(1), retry=retry_if_exception_type(pyodbc.OperationalError))
    def fetch_one(self,tsql:str, params= None)-> str:
        """[summary]

        Args:
            tsql (str): [sql query]

        Returns:
            list: [return list]
        """
        response = str({})
        try:
            logging.info("calling to database started")
            conn = connectionpool.connect()
            if conn.is_valid:
                logging.info("connection is opened")
                cursor =  conn.cursor()
                logging.info("cursor is opened")
                data = conn.execute(tsql,params)
                logging.info("stored procedure is executed")
                if data.description is not None:
                    response = data.fetchone()
                    logging.info("response from db received")
        except pyodbc.OperationalError:
            retmsg = 'Error - Error Info :' +  str(sys.exc_info()) + str(traceback.format_exc())
            logging.error(f"{retmsg}")
            raise(pyodbc.OperationalError)      
        except:
            retmsg = 'Error - Error Info :' +  str(sys.exc_info()) + str(traceback.format_exc())
            logging.error(f"{retmsg}")
            raise
        
        finally:
            if conn.is_valid:
                cursor.commit()
                logging.info("cursor is committed")
                cursor.close()
                logging.info("cursor is closed")
                conn.close()
                logging.info("connection is closed")
            else:
                logging.info("connection is not valid and retrying")
                raise(pyodbc.OperationalError)

        return response    
    
    def fetch_all(self,tsql:str, params= None)-> str:
        """[summary]

        Args:
            tsql (str): [sql query]

        Returns:
            list: [return list]
        """
        response = str({})
        try:
            conn = connectionpool.connect()
            data = conn.execute(tsql,params) 
            if data.description is not None:
                response = data.fetchall()
            
        except:
            retmsg = 'Error - Error Info :' +  str(sys.exc_info())
            logging.error(f"{retmsg}")
            raise
        
        finally:
            conn.close()

        return response  

    def exec_query(self,tsql:str)-> list:
        """[summary]

        Args:
            tsql (str): [sql query]

        Returns:
            list: [return list]
        """
        response = {}
        try:
            conn = connectionpool.connect()
            data = conn.execute(tsql)
            response = data.fetchall()
            
        except:
            retmsg = 'Error - Error Info :' +  str(sys.exc_info())
            logging.error(f"{retmsg}")
            raise

        return response  

connectionpool = sqlalchemy.pool.QueuePool(get_db_connectionstring, max_overflow=15, pool_size=5, recycle=600)