import psycopg2


 

#  Данный класс реализует все необходиы инструменты работы с базой данный. 
#  _connect - метод, который реализует подключение к БД
#  query_database - метод, который реализует запрос к БД
#  close - метод, который разрывает соединение с БД
class DataBaseManager:
    def __init__(self):
        self.connection = self._connect()

    def _connect(self):
        connect = psycopg2.connect(
            host="localhost",
            port=5178,
            dbname="postgres",
            user="postgres",
            password="Gb%v5oVA",
            client_encoding='utf-8'
        )
        return connect

    def query_database (self, query, params=None, fetch_one=False, reg=False):
        cursor = self.connection.cursor()
        cursor.execute(query)
        if not reg:
            result = cursor.fetchone() if fetch_one else cursor.fetchall()
            self.connection.commit()
            cursor.close()
            return result
        self.connection.commit()
        return 
    
    def close(self):
        self.connection.close()
