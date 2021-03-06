from settings import server, port, user, password, database
from sqlalchemy import Column, ForeignKeyConstraint, DateTime, String, BigInteger, Float, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.mssql import IMAGE, UNIQUEIDENTIFIER, SMALLINT, BIT, DATETIME2
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
    Updated = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)
    Field_1 = Column(String(100), nullable=True)
    Field_2 = Column(String(100), nullable=True)
    Barcode = relationship("Barcode")
    PriceAndRemains = relationship("PriceAndRemains")
    DocDetails = relationship('DocDetails')


class Barcode(Base):
    __tablename__ = 'Barcode'

    BarcodeName = Column(String(127), primary_key=True, unique=True, nullable=False)
    id = Column(BigInteger, autoincrement=True)
    GoodF = Column(String(30), ForeignKey('Good.GoodF'), nullable=False)
    Code = Column(String(30), nullable=False)
    Count = Column(Float, nullable=False)
    Field_1 = Column(String(255), nullable=True)
    Field_2 = Column(String(255), nullable=True)
    Field_3 = Column(String(100), nullable=True)
    Field_4 = Column(String(100), nullable=True)
    Updated = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)
    BarcodeImages = relationship("BarcodeImages")


class BarcodeImages(Base):
    __tablename__ = 'BarcodeImages'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    BarcodeName = Column(String(127), ForeignKey('Barcode.BarcodeName'), nullable=False)
    Image = Column(IMAGE, nullable=False)
    MainImage = Column(Boolean, nullable=False)
    Updated = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)


class Partners(Base):
    __tablename__ = 'Partners'

    id = Column(BigInteger, autoincrement=True)
    PartnerF = Column(String(50), primary_key=True, nullable=False)
    NamePartner = Column(String(50), nullable=False)
    Deleted = Column(BIT, nullable=False)
    Field_1 = Column(String(50), nullable=True)
    Field_2 = Column(String(50), nullable=True)
    Discount = Column(Float, nullable=False)
    Updated = Column(BIT, nullable=False)
    DocHead = relationship("DocHead")


class User(Base):
    __tablename__ = 'User'

    id = Column(BigInteger, autoincrement=True)
    UserF = Column(BigInteger, primary_key=True, nullable=False)
    Login = Column(String(20), nullable=False)
    Name = Column(String(50), nullable=False)
    Password = Column(String(200), nullable=False)
    Updated = Column(BIT, nullable=False)
    Field_1 = Column(String(50), nullable=True)
    Field_2 = Column(String(20), nullable=True)
    Deleted = Column(BIT, nullable=False)
    DocDetails = relationship('DocDetails')


class Stores(Base):
    __tablename__ = 'Stores'

    id = Column(BigInteger, autoincrement=True)
    StoreF = Column(String(50), primary_key=True, nullable=False)
    NameStore = Column(String(50), nullable=False)
    Deleted = Column(BIT, nullable=False)
    Field_1 = Column(String(100), nullable=True)
    Field_2 = Column(String(50), nullable=True)
    Updated = Column(BIT, nullable=False)
    PriceAndRemains = relationship("PriceAndRemains")
    DocHead = relationship("DocHead")


class Cell(Base):
    __tablename__ = 'Cell'

    id = Column(BigInteger, autoincrement=True)
    CellF = Column(BigInteger, primary_key=True, nullable=False)
    BarcodeCell = Column(String(127), nullable=False)
    Name = Column(String(30), nullable=True)
    Deleted = Column(BIT, nullable=False)
    Updated = Column(BIT, nullable=False)
    ScanHistory = relationship('ScanHistory')
    DocDetails = relationship('DocDetails')


class PriceAndRemains(Base):
    __tablename__ = 'PriceAndRemains'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    GoodF = Column(String(30), ForeignKey('Good.GoodF'), nullable=False)
    StoreF = Column(String(50), ForeignKey('Stores.StoreF'), nullable=False)
    Price = Column(Float, nullable=False)
    Remain = Column(Float, nullable=False)
    Field_1 = Column(String(50), nullable=True)
    Field_2 = Column(String(50), nullable=True)
    Updated = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)


class SalesReceipts(Base):
    __tablename__ = 'SalesReceipts'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    NameDocu = Column(String(50), nullable=False)
    DocHeadF = Column(UNIQUEIDENTIFIER, nullable=False)
    CashierName = Column(String(50), nullable=False)
    NamePartner = Column(String(50), nullable=True)
    FixReceiptDate = Column(DateTime, nullable=False)
    FactoryNumberDevice = Column(String(50), nullable=True)
    FiscNumberDevice = Column(String(50), nullable=True)
    DocType = Column(SMALLINT, nullable=False)
    NumberChange = Column(Integer, nullable=False)
    FiscNumberReceipt = Column(String(50), nullable=True)
    SerialNumberDevice = Column(String(50), nullable=False)
    OrdinalNumberDocuChange = Column(Integer, nullable=False)
    FormPayment = Column(String(50), nullable=True)
    GoodF = Column(String(30), nullable=False)
    GoodName = Column(String(300), nullable=False)
    Discount = Column(Float, nullable=False)
    StoreF = Column(String(50), nullable=True)
    UnitPriceDiscount = Column(Float, nullable=False)
    colProduct = Column(Float, nullable=False)
    PositionAmount = Column(Float, nullable=False)
    PositionDiscount = Column(Float, nullable=False)
    CheckAmount = Column(Float, nullable=False)
    CheckDiscount = Column(Float, nullable=False)
    TotalSumm = Column(Float, nullable=False)
    ClientSumm = Column(Float, nullable=False)
    Delivery = Column(Float, nullable=False)
    Field_1 = Column(String(100), nullable=True)
    Field_2 = Column(String(50), nullable=True)
    Field_3 = Column(String(20), nullable=True)
    Field_4 = Column(String(20), nullable=True)
    Updated = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)


class ScanHistory(Base):
    __tablename__ = 'ScanHistory'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    Bad_price = Column(BIT, nullable=False)
    Change_history = Column(BIT, nullable=False)
    Hend_enter = Column(BIT, nullable=False)
    Count = Column(Float, nullable=False)
    DocDetailsF = Column(UNIQUEIDENTIFIER, ForeignKey('DocDetails.DocDetailsF'), nullable=False)
    lastChanged = Column(DATETIME2, nullable=False)
    UserF = Column(BigInteger, nullable=False)
    Price_problem = Column(BIT, nullable=False)
    Comment = Column(String, nullable=True)
    UpdateFrom1C = Column(BIT, nullable=False)
    SerialNumberDevice = Column(String(20), nullable=False)
    CellF = Column(BigInteger, ForeignKey('Cell.CellF'), nullable=True)
    BarcodeName = Column(String(127), nullable=False)
    GoodF = Column(String(30), nullable=False)
    Expiration = Column(Float, nullable=False)
    Have_comment = Column(BIT, nullable=False)
    idPos = Column(UNIQUEIDENTIFIER, nullable=False)
    Field_1 = Column(String(100), nullable=True)
    Field_2 = Column(String(50), nullable=True)
    Field_3 = Column(String(20), nullable=True)
    Field_4 = Column(String(20), nullable=True)
    Deleted = Column(BIT, nullable=False)



class DocHead(Base):
    __tablename__ = 'DocHead'

    id = Column(BigInteger, autoincrement=True)
    Comment = Column(String(50), nullable=True)
    CreateDate = Column(BigInteger, nullable=False)
    DocStatus = Column(SMALLINT, nullable=False)
    PartnerF = Column(String(50), ForeignKey('Partners.PartnerF'), nullable=True)
    MainStoreF = Column(String(50), ForeignKey('Stores.StoreF'), nullable=True)
    AlternateStoreF = Column(String(50), nullable=True)
    DocType = Column(SMALLINT, nullable=True)
    UserF = Column(BigInteger, nullable=False)
    UpdatedFromTSD = Column(BIT, nullable=False)
    UpdateFrom1C = Column(BIT, nullable=False)
    DocHeadF = Column(UNIQUEIDENTIFIER, nullable=False, primary_key=True)
    BarcodeDocu = Column(String(50), nullable=True)
    Discount = Column(Float, nullable=False)
    Field_1 = Column(String(100), nullable=True)
    Field_2 = Column(String(100), nullable=True)
    Field_3 = Column(String(50), nullable=True)
    Field_4 = Column(String(30), nullable=True)
    Update = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)
    DocDetails = relationship('DocDetails')


class DocDetails(Base):
    __tablename__ = 'DocDetails'

    id = Column(BigInteger, autoincrement=True)
    DocHeadF = Column(UNIQUEIDENTIFIER, ForeignKey('DocHead.DocHeadF'), nullable=False)
    DocDetailsF = Column(UNIQUEIDENTIFIER, nullable=False, primary_key=True)
    Bad_price = Column(BIT, nullable=False)
    Price_problem = Column(BIT, nullable=False)
    CellF = Column(BigInteger, ForeignKey('Cell.CellF'), nullable=True)
    Change_history = Column(BIT, nullable=True)
    Count_Doc = Column(Float, nullable=False)
    Count_Real = Column(Float, nullable=False)
    CreateDate = Column(BigInteger, nullable=False)
    GoodF = Column(String(30), ForeignKey('Good.GoodF'), nullable=False)
    Hend_enter = Column(BIT, nullable=False)
    Price = Column(Float, nullable=True)
    UserF = Column(BigInteger, ForeignKey('User.UserF'), nullable=True)
    Expiration = Column(Float, nullable=False)
    Spec_comment = Column(String(300), nullable=True)
    UpdatedFromTSD = Column(BIT, nullable=False)
    UpdateFrom1C = Column(BIT, nullable=False)
    Field_1 = Column(String(300), nullable=True)
    Field_2 = Column(String(200), nullable=True)
    Field_3 = Column(String(100), nullable=True)
    Field_4 = Column(String(50), nullable=True)
    Update = Column(BIT, nullable=False)
    Deleted = Column(BIT, nullable=False)
    ScanHistory = relationship('ScanHistory')
