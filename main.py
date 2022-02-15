from sqlclasstable import Good
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import server, port, user, password, database

app = Flask(__name__)

engine = create_engine(f'mssql+pymssql://{user}:{password}@{server}:{port}/{database}', echo=True)

session = sessionmaker(bind=engine)
s = session()

for row in s.query(Good.Name):
    print(row[0])

# @app.route('/')
# def requirements():
