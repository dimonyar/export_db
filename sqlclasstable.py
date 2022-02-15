from settings import server, port, user, password, database
from flask import Flask
from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



engine = create_engine(f'mssql+pymssql://{user}:{password}@{server}:{port}/{database}', echo=True)

Base = declarative_base()


class Good(Base):
    __tablename__ = 'Good'

    id = Column(BigInteger, autoincrement=True)
    GoodF = Column(String(30), primary_key=True, nullable=False)
    Name = Column(String(300), nullable=False)
    Price = Column(Float, nullable=False)
    Unit = Column(String(20), nullable=False)
    Updated = Column(Boolean, nullable=False)
    Deleted = Column(Boolean, nullable=False)
    Field_1 = Column(String(100), nullable=True)
    Field_2 = Column(String(100), nullable=True)


Base.metadata.create_all(engine)

