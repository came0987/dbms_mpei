import pandas as pd
import sqlite3
from sqlalchemy import create_engine

"""
Пример добавления таблиц в БД
"""

df = pd.read_excel('./data/vyst_mo.xlsx', index_col=0)
df1 = pd.read_excel('./data/VUZ.xlsx', index_col=0)
df2 = pd.read_excel('./data/grntirub.xlsx', index_col=0)
engine = create_engine('sqlite:///dbms.db')

df.to_sql('vyst_mo', con=engine, if_exists='replace')
df1.to_sql('VUZ', con=engine, if_exists='replace')
df2.to_sql('grntirub', con=engine, if_exists='replace')

