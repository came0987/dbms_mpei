import uuid
from typing import Optional

from sqlalchemy import Integer, String, ForeignKey, CHAR, select, Column, Table, table, func, event
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedColumn, InstrumentedAttribute, relationship, \
    as_declarative, declared_attr
from sqlalchemy import and_, update, null

from connection import Session, engine, metadata, Data
# from main import ExponatDBMS


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

    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codvuz: Mapped[int] = mapped_column(Integer, primary_key=True,  nullable=False)
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

    # vysts = relationship("VystMoBase", back_populates="vuz", cascade="all")

    @classmethod
    def get_by_name(cls, codvuz: str):
        with Session() as session:
            statement = select(cls).where(and_(cls.codvuz == codvuz))
            db_object = session.scalars(statement).one()
        return db_object


class GrntiBase(Base):
    __tablename__ = 'grntirub'

    codrub: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, unique=True)
    rubrika: Mapped[str] = mapped_column(String(100), nullable=False)


class VystMoBase(Base):
    __tablename__ = 'vyst_mo'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codvuz: Mapped[int] = mapped_column(Integer, nullable=False)
    # codvuz: Mapped[int] = mapped_column(ForeignKey("vuz.codvuz", ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
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

    # vuz = relationship("VuzBase", back_populates="vysts", cascade='all')
    svod = relationship("SvodBase", back_populates="vyst", cascade='all')

    @classmethod
    def get_by_name_2(cls, codvuz: str, regnumber: str):
        with Session() as session:
            statement = select(cls).where(and_(cls.codvuz == codvuz, cls.regnumber == regnumber))
            db_object = session.scalars(statement).one()
        return db_object


class SvodBase(Base):
    __tablename__ = 'svod'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    codvuz = Column(Integer, primary_key=True)#, ForeignKey('vuz.codvuz', ondelete='CASCADE', onupdate='CASCADE'))
    z2 = Column(String)
    subject = Column(String)
    grnti = Column(String)
    rubrika = Column(String)  # Новый столбец для рубрики
    bossname = Column(String)
    regnumber = Column(Integer, primary_key=True)

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

    vyst_id = Column(Integer, ForeignKey('vyst_mo.id', ondelete='CASCADE', onupdate='CASCADE'))

    # Устанавливаем связи
    vyst = relationship("VystMoBase", back_populates="svod")

    # vuz = relationship("VuzBase", backref="svod")

    @classmethod
    def get_by_name_2(cls, codvuz: str, regnumber: str):
        with Session() as session:
            statement = select(cls).where(and_(cls.codvuz == codvuz, cls.regnumber == regnumber))
            db_object = session.scalars(statement).one()
        return db_object


@event.listens_for(VystMoBase, "after_insert")
def insert_svod_entry(mapper, connection, target):
    """
    Автоматически добавляет запись в svod при добавлении записи в vyst_mo.
    """
    # Получаем данные из таблицы VUZ
    # Data.close_connection()
    session = Session()

    vuz_data = connection.execute(
        VuzBase.__table__.select().where(VuzBase.codvuz == target.codvuz)
    ).fetchone()

    grnti_prefix = target.grnti[:2] if target.grnti else None
    rubrika = None
    if grnti_prefix:
        grnti_record = session.query(GrntiBase).filter_by(codrub=grnti_prefix).first()
        rubrika = grnti_record.rubrika if grnti_record else None

    if vuz_data:
        # Создаем запись в таблице Svod
        connection.execute(
            SvodBase.__table__.insert().values(
                vyst_id=target.id,
                codvuz=target.codvuz,
                z2=vuz_data.z2,
                subject=target.subject,
                grnti=target.grnti,
                rubrika=rubrika,  # Здесь вы можете указать любое значение для рубрики
                bossname=target.bossname,
                regnumber=target.regnumber,
                type=target.type,
                boss_position=target.boss_position,
                boss_academic_rank=target.boss_academic_rank,
                boss_scientific_degree=target.boss_scientific_degree,
                exhitype=target.exhitype,
                vystavki=target.vystavki,
                exponat=target.exponat,
                # Поля из VUZ
                z1=vuz_data.z1,
                z1full=vuz_data.z1full,
                region=vuz_data.region,
                city=vuz_data.city,
                status=vuz_data.status,
                obl=vuz_data.obl,
                oblname=vuz_data.oblname,
                gr_ved=vuz_data.gr_ved,
                prof=vuz_data.prof,
            )
        )

@event.listens_for(VystMoBase, "after_update")
def update_svod_from_vyst(mapper, connection, target):
    """
    Обновляет запись в таблице SvodBase при изменении данных в VystMoBase.
    """
    # Обновляем запись в таблице SvodBase
    # vuz_data = connection.execute(
    #     VuzBase.__table__.select().where(VuzBase.codvuz == target.codvuz)
    # ).fetchone()

    session = Session()

    grnti_prefix = target.grnti[:2] if target.grnti else None
    rubrika = None
    if grnti_prefix:
        grnti_record = session.query(GrntiBase).filter_by(codrub=grnti_prefix).first()
        rubrika = grnti_record.rubrika if grnti_record else None
    # if vuz_data:
    # Обновляем запись с учетом данных из VUZ
    connection.execute(
        SvodBase.__table__.update()
        .where(SvodBase.vyst_id == target.id)
        .values(
            codvuz=target.codvuz,
            subject=target.subject,
            grnti=target.grnti,
            rubrika=rubrika,
            bossname=target.bossname,
            regnumber=target.regnumber,
            type=target.type,
            boss_position=target.boss_position,
            boss_academic_rank=target.boss_academic_rank,
            boss_scientific_degree=target.boss_scientific_degree,
            exhitype=target.exhitype,
            vystavki=target.vystavki,
            exponat=target.exponat,
                # # Поля из VUZ
                # z1=vuz_data.z1,
                # z2=vuz_data.z2,
                # z1full=vuz_data.z1full,
                # region=vuz_data.region,
                # city=vuz_data.city,
                # status=vuz_data.status,
                # obl=vuz_data.obl,
                # oblname=vuz_data.oblname,
                # gr_ved=vuz_data.gr_ved,
                # prof=vuz_data.prof,
        )
    )

@event.listens_for(VuzBase, "after_update")
def update_svod_from_vuz(mapper, connection, target):
    """
    Обновляет записи в таблице SvodBase при изменении данных в таблице VuzBase.
    """
    # Обновляем записи в SvodBase, связанные через codvuz
    connection.execute(
        SvodBase.__table__.update()
        .where(SvodBase.codvuz == target.codvuz)
        .values(
            # Поля, которые обновляем из VuzBase
            z1=target.z1,
            z1full=target.z1full,
            region=target.region,
            city=target.city,
            status=target.status,
            obl=target.obl,
            oblname=target.oblname,
            gr_ved=target.gr_ved,
            prof=target.prof,
            z2=target.z2,  # Если z2 нужно обновлять
        )
    )

@event.listens_for(VuzBase, "after_delete")
def clear_svod_data_on_vuz_delete(mapper, connection, target):
    """
    Очищает информацию о записи из таблицы VUZ в таблице SVOD,
    оставляя значение в столбце codvuz.
    """
    # Очищаем все столбцы из VUZ в связанной таблице SVOD
    print(f"Deleting related data for VUZ codvuz={target.codvuz}")
    connection.execute(
        SvodBase.__table__.update()
        .where(SvodBase.codvuz == target.codvuz)
        .values(
            z1=null(),
            z1full=null(),
            z2=null(),
            region=null(),
            city=null(),
            status=null(),
            obl=null(),
            oblname=null(),
            gr_ved=null(),
            prof=null()
        )
    )


class GroupListBase(Base):
    __tablename__ = 'grouplist'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ui_table_name = Column(String)
    unique_regions = Column(String)
    unique_grnti = Column(String)
    record_count = Column(Integer)
    db_view_name = Column(String, unique=True)
    records_composite_keys = Column(String)

# def generate_uuid(mapper, connection, target):
#     target.db_table_name = f"table_{uuid.uuid4()}"
#
# # Привязываем событие к добавлению новой записи
# event.listen(GroupListBase, 'before_insert', generate_uuid)


