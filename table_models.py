from typing import Optional

from sqlalchemy import Integer, String, ForeignKey, CHAR, select, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedColumn, InstrumentedAttribute

from connection import Session


class Base(DeclarativeBase):
    # @classmethod
    # def get_column_values(cls, column: MappedColumn):
    #     return select(cls).where(column)

    @classmethod
    def get_column_values(cls, session: Session, column: InstrumentedAttribute):
        # Создаем запрос с использованием select()
        stmt = select(column)

        # Выполняем запрос и получаем значения с использованием нового синтаксиса
        with session.begin():
            results = session.execute(stmt).scalars().all()

        return results


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


class GrntiBase(Base):
    __tablename__ = 'grnti'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codrub: Mapped[int] = mapped_column(Integer, nullable=False)
    rubrika: Mapped[str] = mapped_column(String(100), nullable=False)


class ExpositionBase(Base):
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
