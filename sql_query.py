import excel
import _mssql
import pymssql
import settings


def goods_columns():
    conn = pymssql.connect(
        server=settings.server,
        port=settings.port,
        database=settings.database,
        user=settings.user,
        password=settings.password,
        login_timeout=5,
        timeout=5)

    cursor = conn.cursor()
    query = ("""
                SELECT
                    *                 
                FROM
                    INFORMATION_SCHEMA.COLUMNS                 
                WHERE
                    TABLE_NAME = N'Barcode' 
                    OR TABLE_NAME = N'Good'
                """)

    cursor.execute(query)
    column = cursor.fetchall()
    conn.close()
    print('get a list of columns dbo.Barcode, dbo Good')
    return ', '.join([str(row[2] + '.' + row[3]) for row in column if row[3] != 'id'])


def goods():
    try:
        conn = pymssql.connect(
            server=settings.server,
            port=settings.port,
            database=settings.database,
            user=settings.user,
            password=settings.password,
            login_timeout=5,
            timeout=5)

        print("connection open")
        cursor = conn.cursor()
        query = ("""
                    SELECT
                        """ + goods_columns() + """                 
                    FROM
                        dbo.Barcode                 
                    JOIN
                        Good 
                        ON Barcode.GoodF = Good.GoodF                  
                    WHERE
                        Barcode.GoodF!=0
                    """)

        cursor.execute(query)
        print('get the values')
        good = cursor.fetchall()
        try:
            conn.close()
            print('connection close')
        except pymssql.Error:
            print("connection close failed")
        return good

    except pymssql.Error:
        print("connection failed")


def insert_into(table: str):
    try:
        conn = pymssql.connect(
            server=settings.server,
            port=settings.port,
            database=settings.database,
            user=settings.user,
            password=settings.password,
            login_timeout=5,
            timeout=5)

        cursor = conn.cursor()
        print("connection open")
        query = (excel.values(table))
        # print(query)
        cursor.execute(query)
        print('\n Insert values into')
        conn.commit()
        try:
            conn.close()
            print('connection close')
        except pymssql.Error:
            print("connection close failed")
    except pymssql.Error as e:
        print(e.__context__)


def delete_table(table: str):
    try:
        conn = pymssql.connect(
            server=settings.server,
            port=settings.port,
            database=settings.database,
            user=settings.user,
            password=settings.password,
            login_timeout=5,
            timeout=5)

        cursor = conn.cursor()
        print("connection open")
        query = ("""DELETE FROM """ + table)
        print(query)
        cursor.execute(query)
        print('Delete values from table', table)
        conn.commit()
        try:
            conn.close()
            print('connection close')
        except pymssql.Error:
            print("connection close failed")
    except pymssql.Error:
        print("connection failed")
