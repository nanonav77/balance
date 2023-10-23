import pymysql.cursors
import os
from dotenv import load_dotenv

class Database(object):

    def __init__(self):

        load_dotenv() ## CARGAMOS LAS VARIABLES DE ENTORNO QUE HACEN REFERENCIA A LA CONEXIÓN DE BASE DE DATOS

        self.host = os.getenv("HOST")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.database = os.getenv("DATABASE")
 
    def execute(self, query:str, parameters:list=[]):
        return self.__execute(query, parameters).rowcount
 
    def select_all(self, query:str, parameters:list=[]):
        cursor = self.__execute(query, parameters)
        return cursor.fetchall()
 
    def select_one(self, query:str, parameters:list=[]):
        cursor = self.__execute(query, parameters)
        return cursor.fetchone()
 
    def __execute(self, query:str, parameters:list=[]):
        try:
            with self.__openConnection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, parameters)
                    connection.commit()
                    return cursor
        except pymysql.Error as e:
           print(f"Error while executing query [{query}]: {str(e)}")
 
    def __openConnection(self):
        try:
            return pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        except pymysql.Error as e:
           print(f"Error while opening sql connection: {str(e)}")