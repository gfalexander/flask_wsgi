from sqlite3.dbapi2 import Connection

from billing.db import get_db
from billing.models.user.dto import UserMapper


class UserRepository():
    __db: Connection
    __ai: int

    def __init__(self) -> None:
        self.__db = get_db()
        
        test_increment = self.__db.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1").fetchall()
        if len(test_increment) == 0:
            self.__ai = 1
        else:
            self.__ai = test_increment[0][0] + 1


    def save(self, user):
        
        try:
            self.__db.execute(
                'INSERT INTO users (id, name, password, email) VALUES (?, ?, ?, ?)',
                (self.__ai, user.name, user.password, user.email)
            )
            self.__db.commit()

            id, name, password, email, created_at = self.__db.execute(
                'SELECT id, name, password, email, created_at FROM users WHERE id = ?',
                (self.__ai,)
            ).fetchone()

            dict_user = {
                'id': id,
                'name': name,
                'password': password,
                'email': email,
                'created_at': created_at
            }

            saved_user = UserMapper.toModel(dict_user)
                        
            return saved_user
        except self.__db.IntegrityError:
            return None