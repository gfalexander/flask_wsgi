class User():
    __id: int
    __name: str
    __password: str
    __email: str
    __created_at: float

    def __init__(self, id, name, password, email, created_at) -> None:
        self.__id = id
        self.__name = name
        self.__password = password
        self.__email = email
        self.__created_at = created_at
    
    
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
    
    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at
    
    
    