from sqlclasstable import Good, Barcode, Partners, User, Stores, PriceAndRemains, ScanHistory, DocHead, DocDetails, SalesReceipts
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import server, port, user, password, database
from epochtime import tact_to_data, data_to_tact


app = Flask(__name__)

engine = create_engine(f'mssql+pymssql://{user}:{password}@{server}:{port}/{database}', echo=False)

session = sessionmaker(bind=engine)
s = session()



# @app.route('/')
# def requirements()
