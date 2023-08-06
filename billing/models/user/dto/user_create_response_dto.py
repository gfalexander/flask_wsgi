class UserCreateResponseDto:
    __id: int
    __name: str
    __email: str

    def __init__(self, id, name, email) -> None:
        self.__id = id
        self.__name = name
        self.__email = email

    def __dict__(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email
        }

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email