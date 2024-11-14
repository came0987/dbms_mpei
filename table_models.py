import uuid
from typing import Optional

from sqlalchemy import Integer, String, ForeignKey, CHAR, select, Column, Table, table, func, event
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedColumn, InstrumentedAttribute, relationship, \
    as_declarative, declared_attr
from sqlalchemy import and_

from connection import Session, engine, metadata, Data


class Base(DeclarativeBase):
    # @classmethod
    # def get_column_values(cls, column: MappedColumn):
    #     return select(cls).where(column)

    @classmethod
    def get_column_values(cls, column: InstrumentedAttribute):
        # Создаем запрос с использованием select()
        stmt = select(column)

        # Выполняем запрос и получаем значения с использованием нового синтаксиса
        with Session() as session:
            results = session.execute(stmt).scalars().all()

        return results

    @classmethod
    def get_by_name(cls, _id: int):
        with Session() as session:
            statement = select(cls).where(cls.id == _id)
            db_object = session.scalars(statement).one()
        return db_object


class VuzBase(Base):
    __tablename__ = 'vuz'

    # def get_column_values(self, column: MappedColumn):
    #     return select(self).where(self.z1 == f"{column.name}")

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codvuz: Mapped[int] = mapped_column(Integer, nullable=False)
    z1: Mapped[str] = mapped_column(String(100), nullable=False)
    z1full: Mapped[str] = mapped_column(String(200), nullable=False)
    z2: Mapped[str] = mapped_column(String(15), nullable=False)
    region: Mapped[str] = mapped_column(String(20), nullable=False)
    city: Mapped[str] = mapped_column(String(40), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    obl: Mapped[int] = mapped_column(Integer, nullable=False)
    oblname: Mapped[str] = mapped_column(String(50), nullable=False)
    gr_ved: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    prof: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)

    vysts = relationship("VystMoBase", back_populates="vuz", cascade="all, delete")

    @classmethod
    def get_by_name(cls, codvuz: str):
        with Session() as session:
            statement = select(cls).where(and_(cls.codvuz == codvuz))
            db_object = session.scalars(statement).one()
        return db_object


class GrntiBase(Base):
    __tablename__ = 'grnti'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codrub: Mapped[int] = mapped_column(Integer, nullable=False)
    rubrika: Mapped[str] = mapped_column(String(100), nullable=False)


class VystMoBase(Base):
    __tablename__ = 'vyst_mo'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codvuz: Mapped[int] = mapped_column(ForeignKey("vuz.codvuz"), nullable=False)
    type: Mapped[str] = mapped_column(String(5))
    regnumber: Mapped[str] = mapped_column(String(30), nullable=False)
    subject: Mapped[str] = mapped_column(String(150), nullable=False)
    grnti: Mapped[str] = mapped_column(String(30), nullable=False)
    bossname: Mapped[str] = mapped_column(String(50), nullable=False)
    boss_position: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # должность
    boss_academic_rank: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # ученое звание
    boss_scientific_degree: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # ученая степень
    exhitype: Mapped[str] = mapped_column(String(5), nullable=False)
    vystavki: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    exponat: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    vuz = relationship("VuzBase", back_populates="vysts")

    @classmethod
    def get_by_name_2(cls, codvuz: str, regnumber: str):
        with Session() as session:
            statement = select(cls).where(and_(cls.codvuz == codvuz, cls.regnumber == regnumber))
            db_object = session.scalars(statement).one()
        return db_object


class SvodBase(Base):
    __tablename__ = 'svod'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, ForeignKey('vyst_mo.id', ondelete='CASCADE'), primary_key=True)
    codvuz = Column(Integer, ForeignKey('vuz.codvuz', ondelete='CASCADE'))
    z2 = Column(String)
    subject = Column(String)
    grnti = Column(String)
    rubrika = Column(String)  # Новый столбец для рубрики
    bossname = Column(String)
    regnumber = Column(Integer)
    
    type = Column(String)
    boss_position = Column(String)
    boss_academic_rank = Column(String)
    boss_scientific_degree = Column(String)
    exhitype = Column(String)
    vystavki = Column(String)
    exponat = Column(String)

    # Поля из таблицы VUZ
    z1 = Column(String)
    z1full = Column(String)
    region = Column(String)
    city = Column(String)
    status = Column(String)
    obl = Column(String)
    oblname = Column(String)
    gr_ved = Column(String)
    prof = Column(String)

    # Устанавливаем связи
    vyst_mo = relationship("VystMoBase", backref="svod", cascade="all, delete")
    # vyst_mo = relationship(
    #     "VystMoBase",
    #     primaryjoin="SvodBase.codvuz == VystMoBase.codvuz",
    #     backref="svod",
    #     cascade="all, delete"
    # )
    vuz = relationship("VuzBase", backref="svod", cascade="all, delete")

@as_declarative()
class DynamicTableBase(Base):
    # __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    vyst_id = Column(Integer, ForeignKey('vyst_mo.id', ondelete='CASCADE'))#, primary_key=True)
    codvuz = Column(Integer, ForeignKey('vuz.codvuz', ondelete='CASCADE'))
    z2 = Column(String)
    subject = Column(String)
    grnti = Column(String)
    rubrika = Column(String)  # Новый столбец для рубрики
    bossname = Column(String)
    regnumber = Column(Integer)

    type = Column(String)
    boss_position = Column(String)
    boss_academic_rank = Column(String)
    boss_scientific_degree = Column(String)
    exhitype = Column(String)
    vystavki = Column(String)
    exponat = Column(String)

    # Поля из таблицы VUZ
    z1 = Column(String)
    z1full = Column(String)
    region = Column(String)
    city = Column(String)
    status = Column(String)
    obl = Column(String)
    oblname = Column(String)
    gr_ved = Column(String)
    prof = Column(String)

    # vyst_mo = relationship("VystMoBase", backref="svod", cascade="all, delete")
    # vuz = relationship("VuzBase", backref="svod", cascade="all, delete")

    @declared_attr
    def vyst_mo(cls):
        return relationship("VystMoBase", backref="dynamic_svod", cascade="all, delete")

    @declared_attr
    def vuz(cls):
        return relationship("VuzBase", backref="dynamic_svod", cascade="all, delete")


class GroupListBase(Base):
    __tablename__ = 'grouplist'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    unique_fed_regions = Column(String)
    unique_grnti = Column(String)
    record_count = Column(Integer)
    ui_table_name = Column(String)
    db_table_name = Column(String, unique=True)

def generate_uuid(mapper, connection, target):
    target.db_table_name = f"table_{uuid.uuid4()}"

# Привязываем событие к добавлению новой записи
event.listen(GroupListBase, 'before_insert', generate_uuid)

def add_record_to_group_table(arg_list, bd_table_name: str):
    Data.close_connection()
    if bd_table_name in metadata.tables:
        # Динамически создаем класс ORM для существующей таблицы
        DynamicTableClass = type(bd_table_name, (DynamicTableBase,), {'__table__': metadata.tables[bd_table_name]})

    new_entry = DynamicTableClass(
    vyst_id = arg_list[0],
    codvuz = arg_list[1],
    z2 = arg_list[2],
    subject = arg_list[3],
    grnti = arg_list[4],
    rubrika = arg_list[5],  # Новый столбец для рубрики
    bossname = arg_list[6],
    regnumber = arg_list[7],

    type = arg_list[8],
    boss_position = arg_list[9],
    boss_academic_rank = arg_list[10],
    boss_scientific_degree = arg_list[11],
    exhitype = arg_list[12],
    vystavki = arg_list[13],
    exponat = arg_list[14],

    # Поля из таблицы VUZ
    z1 = arg_list[15],
    z1full = arg_list[16],
    region = arg_list[17],
    city = arg_list[18],
    status = arg_list[19],
    obl = arg_list[20],
    oblname = arg_list[21],
    gr_ved = arg_list[22],
    prof = arg_list[23],
    )

    with Session() as session:
        try:
            session.add(new_entry)
        except:
            session.rollback()
            raise
        else:
            session.commit()

    update_table_list(bd_table_name)

    Data.create_connection()

def get_dynamic_table(bd_table_name: str):
    if bd_table_name in metadata.tables:
        # Динамически создаем класс ORM для существующей таблицы
        DynamicTableClass: Table = type(bd_table_name, (DynamicTableBase,), {'__table__': metadata.tables[bd_table_name]})
        return DynamicTableClass
    return None

def update_table_list(bd_table_name: str):
    Data.close_connection()
    with Session as session:
        table = get_dynamic_table(bd_table_name)

        # Запрос уникальных значений столбцов и количества строк
        query = select([
            func.group_concat(func.distinct(table.c.region)).label('unique_fed_regions'),
            func.group_concat(func.distinct(table.c.grnti)).label('unique_grnti'),
            func.count().label('record_count')
        ])
        result = session.execute(query).fetchone()

        # Ищем или создаем запись в `table_list`
        table_list_entry = session.query(GroupListBase).filter_by(table_name=bd_table_name).first()
        # if not table_list_entry:
        #     table_list_entry = GroupListBase(table_name=bd_table_name)
        #     session.add(table_list_entry)

        # Обновляем значения в `table_list`
        table_list_entry.unique_names = result['unique_names']
        table_list_entry.unique_city = result['unique_city']
        table_list_entry.count = result['count']
        session.commit()
    Data.create_connection()

def create_dynamic_table(table_name):
    new_table = Table(
        table_name, metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
    # Column('id', Integer, ForeignKey('vyst_mo.id', ondelete='CASCADE'), primary_key=True),
    # Column('codvuz', Integer, ForeignKey('vuz.codvuz', ondelete='CASCADE')),
    Column('z2', String),
    Column('subject', String),
    Column('grnti', String),
    Column('rubrika', String), # Новый столбец для рубрики
    Column('bossname', String),
    Column('regnumber', Integer),

    Column('type', String),
    Column('boss_position', String),
    Column('boss_academic_rank',String),
    Column('boss_scientific_degree', String),
    Column('exhitype', String),
    Column('vystavki', String),
    Column('exponat', String),

    # Поля из таблицы VUZ
     Column('z1', String),
     Column('z1full', String),
     Column('region', String),
     Column('city', String),
     Column('status', String),
     Column('obl', String),
     Column('oblname', String),
     Column('gr_ved', String),
     Column('prof', String),
)
    metadata.create_all(engine)

    inherit_condition = DynamicTableBase.__table__.c.id == new_table.c.id
    if table_name in Base.metadata.tables:
        DynamicTable = Base.metadata.tables[table_name]
    else:
        DynamicTable = type(table_name, (DynamicTableBase,), {'__table__': new_table, '__mapper_args__': {'inherit_condition': inherit_condition}})
    return DynamicTable