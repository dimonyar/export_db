from sqlclasstable import Good, Barcode, Partners, User, Stores, PriceAndRemains, ScanHistory, DocHead, DocDetails, \
    SalesReceipts
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import server, port, user, password, database
from epochtime import tact_to_data, data_to_tact
from hashmd5 import str2hash

app = Flask(__name__)

engine = create_engine(f'mssql+pymssql://{user}:{password}@{server}:{port}/{database}', echo=False)

session = sessionmaker(bind=engine)
s = session()


@app.route('/')
def start():
    goods = '/goods/'
    stores = '/stores/'
    users = '/user/'
    partners = '/partners/'
    dochead = '/dochead/'
    html = f'''
            <ul>
              <li><a href="{goods}">{goods}</a></li>
              <li><a href="{stores}">{stores}</a></li>
              <li><a href="{users}">{users}</a></li>
              <li><a href="{partners}">{partners}</a></li>
            </ul>
            <ul>
              <li><a href="{dochead}">{dochead}</a></li>
            </ul>
            '''
    return html


@app.route('/goods/')
def goods():
    result = s.query(Good.GoodF, Good.Name, Good.Unit, Good.Price)
    html = '<table border="1">' \
           '<col width="50" valign="top align="right">' \
           '<col width="500" valign="top" align="left">' \
           '<col width="50" valign="top" align="center">' \
           '<col width="100" valign="top" align="right">'
    for row in result:
        html += '<tr><td>' + row[0] + '</td><td>' + row[1] + '</td><td>' + row[2] + '</td><td>' + str(
            int(row[3])) + '</td></tr>'
    html += '</table>'

    return html


@app.route('/stores/')
def stores():
    result = s.query(Stores.StoreF, Stores.NameStore)
    html = '<table border="1">' \
           '<col width="50" valign="top align="left">' \
           '<col width="300" valign="top" align="left">'
    for row in result:
        html += '<tr><td>' + row[0] + '</td><td>' + row[1] + '</td></tr>'
    html += '</table>'

    return html


@app.route('/user/')
def user():
    result = s.query(User.UserF, User.Name, User.Login, User.Password)
    html = '<table border="1">' \
           '<col width="50" valign="top align="left">' \
           '<col width="300" valign="top" align="left">' \
           '<col width="300" valign="top" align="left">' \
           '<col width="300" valign="top" align="left">'
    for row in result:
        user_f = str(row[0])
        name = row[1]
        login = row[2]
        pw = row[3]
        if user_f == '-1':
            continue
        html += '<tr><td>' + user_f + '</td><td width="auto">' + name + '</td><td width="auto">' \
                + login + '</td><td>' + pw + '</td></tr>'
    html += '</table>'

    return html


@app.route('/partners/')
def partners():
    result = s.query(Partners.PartnerF, Partners.NamePartner, Partners.Discount).order_by(Partners.NamePartner)
    html = '<table border="1">' \
           '<col width="50" valign="top align="left">' \
           '<col width="500" valign="top" align="left">' \
           '<col width="50" valign="top" align="left">'
    for row in result:
        html += f'<tr><td>{row.PartnerF}</td><td>{row.NamePartner}</td><td width="auto">{str(row.Discount)}</td></tr>'
    html += '</table>'

    return html


@app.route('/dochead/')
def dochead():
    result = s.query(DocHead.DocType, DocHead.Comment, Partners.NamePartner, DocHead.CreateDate, DocHead.DocStatus,
                     Stores.NameStore).join(Partners).join(Stores)
    html = '<table border="1">' \
           '<col width="50" valign="top align="left">' \
           '<col width="500" valign="top" align="left">' \
           '<col width="100" valign="top" align="left">' \
           '<col width="100" valign="top" align="left">' \
           '<col width="100" valign="top" align="left">'
    typ = {1: 'приходный', 2: 'расходный', 3: 'инвентаризация', 4: 'перемещение', 5: 'списание', 6: 'возврат',
           7: 'сбор штрихкодов', 8: 'сбор штрихкодов с характеристиками'}
    for row in result:
        html += f'<tr><td>{typ[row.DocType]}</td><td>{row.Comment}</td><td>{row.NamePartner}</td><td>{tact_to_data(row.CreateDate)}</td><td>{str(row.DocStatus)}</td><td>{row.NameStore}</td></tr> '
    html += '</table>'

    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
