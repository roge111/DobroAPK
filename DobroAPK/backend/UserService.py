import psycopg2
import bcrypt
from DataBaseManager import DataBaseManager


# Данный класс реализует инструменты для работы с функциями для пользовтаеля. Принимает аргумент db_manager - это объект класса DataBaseManager
# _check_login - метод, который проверяет 
# register -  метод для регистрации пользователя в БД
# LogIn - метод для проверки существования пользователя и провекри правильности пароль

class UserService:
    def __init__(self, db_manager):
        self.db = db_manager
    
    def _check_login(self, login: str):
        users = self.db.query_database("SELECT login FROM users;")
        return any(user[0].lower() == login.lower() for user in users)


    def register(self, login, password):

        if self._check_login(login):
            return -1
        
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        last_id = self.db.query_database("SELECT MAX(id) FROM users;", fetch_one=True)[0] or 0
        print(last_id)
        new_id = last_id + 1

        self.db.query_database(
            f"INSERT INTO users (id, login, password) VALUES ({new_id}, '{login}', '{password_hash}');", reg=True)
        return new_id

    def login(self, login, password):
        stored_password = self.db.query_database(
            "SELECT password FROM users WHERE login = %s;",
            (login,), fetch_one=True
        )
        if not stored_password:
            return False

        return bcrypt.checkpw(
            password.encode('utf-8'),
            stored_password[0].encode('utf-8')
        )
    
    def insert_user_in_data_table(self, id):
        self.db.query_database(
            f"INSERT TO users_info (id, info, contacts) VALUES ({id});"
        )
    
    def update_info_user(self, id, info="", contacts=""):
        if len(info):
            self.db.query_database(
                f"UPDATE users_info SET info={info} WHERE id={id};"
            )
        else:
            self.db.query_database(
                f"UPDATE users_info SET contacts={contacts} WHERE id={id};"
            )




