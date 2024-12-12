from PySide6 import QtSql, QtWidgets
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/database.db', pool_pre_ping=True)
Session = sessionmaker(bind=engine)
metadata = MetaData()


class Data:
    db_connection = None  # Статическое свойство для хранения соединения

    @staticmethod
    def create_connection():
        if Data.db_connection is None:  # Создаем соединение, если оно еще не создано
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('database/database.db')
            if not db.open():
                QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                               "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
                return False
            Data.db_connection = db

            query = QtSql.QSqlQuery(db)
            if not query.exec("PRAGMA foreign_keys = ON;"):
                print(f"Failed to enable foreign key support: {query.lastError().text()}")
                return False

        return True

    @staticmethod
    def close_connection():
        if Data.db_connection is not None:
            Data.db_connection.close()
            QtSql.QSqlDatabase.removeDatabase('QSQLITE')
            Data.db_connection = None