class UserCreateDto:

    __name: str
    __password: str
    __email: str

    def __init__(self, name, password, email) -> None:
        self.__name = name
        self.__password = password
        self.__email = email

    def __init__(self):
        self.__name = "name"
        self.__password = "password"
        self.__email = "email"

    def __dict__(self):
        return {
            'name': self.__name,
            'password': self.__password,
            'email': self.__email
        }

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email