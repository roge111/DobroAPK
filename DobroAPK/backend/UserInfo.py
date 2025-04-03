
"""
    Класс UserIfo  используется для работы с информацией о пользователе.
    insert_user_in_data_table - метод, который добавляет информацию в таблицу user_info
    update_user - метод, который обновляет данные пользователя
    

"""
class UserInfo:
    def __init__(self, db_manager):
        self.db = db_manager
      
    def _check_login(self, login: str):
        users = self.db.query_database("SELECT login FROM users;")
        return any(user[0].lower() == login.lower() for user in users)
    
    def _check_null(self, column, id, value):
        if len(value) == 0:
            return self.db.query_database(
                f"select {column} from users_info where id={id};"
            )[0][0]
        return value
    def insert_user_in_data_table(self, id, login):
        self.db.query_database(
            f"INSERT INTO users_info (id) VALUES ({id});", reg=True
        )
        self.db.query_database(
            f"UPDATE users_info SET login='{login}' WHERE id={id};", reg=True
        )
      
    def update_user(self, id, lfp="", login = "", info="", contacts="", hobbi=""):
        if len(login) == 0:
            login = self._check_null("login", id, login)
        else:
            if self._check_login(login):
                return False, "Данный логин уже существует"
        lfp = self._check_null("lfp", id, lfp)
        info = self._check_null("info", id, info)
        contacts = self._check_null("contacts", id, contacts)
        hobbi = self._check_null("hobbi", id, hobbi)
    
       


        self.db.query_database(
            f"UPDATE users_info SET lfp='{lfp}', login='{login}', info='{info}', contacts='{contacts}',hobbi='{hobbi}' WHERE id='{id}';", reg=True
        )
        return True, "ОК"
