from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__ (self) -> None:
        driver = 'mysql+pymysql'
        user = 'root'
        password = "Smiley%4075005"
        host = 'localhost'
        port = 3306
        database = 'clean_database'
        self.__connection_string = f"{driver}://{user}:{password}@{host}:{port}/{database}"
        self.__engine = self.__create_database_engine()
        self.session = None 

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
