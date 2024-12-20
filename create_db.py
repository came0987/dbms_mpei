import pandas as pd
from sqlalchemy import MetaData, text

from connection import Session, engine
from table_models import Base, GrntiBase, VuzBase, VystMoBase, SvodBase#, GroupListBase


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
    with Session() as session:
        # Заполнение таблиц
        load_excel_to_table('./data/grntirub.xlsx', GrntiBase, session)
        load_excel_to_table('./data/vuz.xlsx', VuzBase, session)
        load_excel_to_table('./data/vyst_mo.xlsx', VystMoBase, session)

def create_svod():
    create_view = text(
        """
        SELECT 
            vyst_mo.codvuz,
            vuz.z2,
            vyst_mo.subject,
            vyst_mo.grnti,
            vuz.z1,
            vuz.z1full,
            vuz.region,
            vuz.city,
            vuz.status,
            vuz.obl,
            vuz.oblname,
            vuz.gr_ved,
            vuz.prof,
            vyst_mo.type,
            vyst_mo.regnumber,
            vyst_mo.bossname,
            vyst_mo.boss_position,
            vyst_mo.boss_academic_rank,
            vyst_mo.boss_scientific_degree,
            vyst_mo.exhitype,
            vyst_mo.vystavki,
            vyst_mo.exponat
        FROM 
            vyst_mo
        JOIN 
            vuz 
        ON 
            vyst_mo.codvuz = vuz.codvuz;
        """
    )

    with engine.connect() as conn:
        conn.execute(create_view)


def populate_svod():
    session = Session()
    vyst_records = session.query(VystMoBase).all()
    for vyst in vyst_records:
        vuz = session.query(VuzBase).filter_by(codvuz=vyst.codvuz).first()
        if vuz:
            # Извлекаем первые две цифры из grnti для поиска в таблице grnti_cod
            grnti_prefix = vyst.grnti[:2] if vyst.grnti else None
            rubrika = None
            if grnti_prefix:
                grnti_record = session.query(GrntiBase).filter_by(codrub=grnti_prefix).first()
                rubrika = grnti_record.rubrika if grnti_record else None

            # Создаем запись в SVOD
            new_svod = SvodBase(
                vyst_id=vyst.id,  # Связываем записи по id
                codvuz=vyst.codvuz,
                # id=vyst.id,  # Связываем записи по id
                z2=vuz.z2,
                subject=vyst.subject,
                grnti=vyst.grnti,
                rubrika=rubrika,  # Добавляем рубрику
                bossname=vyst.bossname,
                regnumber=vyst.regnumber,
                z1=vuz.z1,
                z1full=vuz.z1full,
                region=vuz.region,
                city=vuz.city,
                status=vuz.status,
                obl=vuz.obl,
                oblname=vuz.oblname,
                gr_ved=vuz.gr_ved,
                prof=vuz.prof,
                type=vyst.type,
                boss_position=vyst.boss_position,
                boss_academic_rank=vyst.boss_academic_rank,
                boss_scientific_degree=vyst.boss_scientific_degree,
                exhitype=vyst.exhitype,
                vystavki=vyst.vystavki,
                exponat=vyst.exponat
            )
            session.add(new_svod)
    session.commit()

def delete_tables(table_names: list):
    metadata = MetaData()
    metadata.reflect(bind=engine)

    for table_name in table_names:
        if table_name in metadata.tables:
            # Удаляем таблицу
            metadata.tables[table_name].drop(engine)
            print(f"Таблица {table_name} успешно удалена.")
        else:
            print(f"Таблица {table_name} не найдена в базе данных.")


# Заполняем таблицу SVOD
# populate_svod()

# Создаем подключение к базе данных SQLite
# engine = create_engine('sqlite:///database.db')


if __name__ == '__main__':
    delete_tables(["grntirub", "svod", "vuz", "vyst_mo", "grouplist"])
    create_db_and_tables()
    fill_tables_from_excel()
    populate_svod()
