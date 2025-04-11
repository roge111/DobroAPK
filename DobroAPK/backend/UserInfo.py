import os
from DataBaseManager import DataBaseManager
"""
    Класс UserIfo  используется для работы с информацией о пользователе.
    insert_user_in_data_table - метод, который добавляет информацию в таблицу user_info

"""
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'usersImage'

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
    
         #Проверка расширения
    def _allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS
    
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
    


    async def load_image_user(self, id, photo):
       # Проверка расширения файла
        if self._allowed_file(photo.filename):
            return {"message": "Неверный формат файла. Пожалуйста, загрузите изображение."}

        # Сохранение файла на сервере
        file_path = UPLOAD_FOLDER + '/' + photo.filename
        try:
            f = open(file_path, 'wb')
            f.write(await photo.read())
            message =  {"message": "Файл успешно загружен"}
        except Exception as e:
            message =  {"message": f"Ошибка при сохранении файла: {str(e)}, {file_path}, {os.getcwd()}"}

        
        self.db.query_database(
                f"INSERT INTO user_photo(id, link) VALUES ({id}, '{file_path}');", reg=True
        )

        return message

        
