import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from table_models import Base, GrntiBase, VuzBase, ExpositionBase


# """
# Пример добавления таблиц в БД
# """
#
# df = pd.read_excel('./data/vyst_mo.xlsx', index_col=0)
# df1 = pd.read_excel('./data/VUZ.xlsx', index_col=0)
# df2 = pd.read_excel('./data/grntirub.xlsx', index_col=0)
# df3 = pd.read_excel('./data/svod.xlsx', index_col=0)
# engine = create_engine('sqlite:///data_base.db')
#
# df.to_sql('vyst_mo', con=engine, if_exists='replace')
# df1.to_sql('VUZ', con=engine, if_exists='replace')
# df2.to_sql('grntirub', con=engine, if_exists='replace')
# df3.to_sql('svod', con=engine, if_exists='replace')
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from table_models import Base, GrntiBase, VuzBase  #, ExpositionBase  # Замени на имена твоих моделей


def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)


# Функция для загрузки данных из Excel в таблицу SQLAlchemy
def load_excel_to_table(file_path, model_class, session):
    data = pd.read_excel(file_path)
    records = data.to_dict(orient='records')
    print(records)
    session.bulk_insert_mappings(model_class, records)
    session.commit()


def fill_tables_from_excel():
    # Создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()

    # Заполнение таблиц
    load_excel_to_table('./data/grntirub.xlsx', GrntiBase, session)
    load_excel_to_table('./data/vuz.xlsx', VuzBase, session)
    load_excel_to_table('./data/vyst_mo.xlsx', ExpositionBase, session)

    # Закрываем сессию после завершения
    session.close()


# Создаем подключение к базе данных SQLite
engine = create_engine('sqlite:///database.db')


if __name__ == '__main__':
    create_db_and_tables()
    fill_tables_from_excel()
