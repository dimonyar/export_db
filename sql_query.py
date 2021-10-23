import pymssql


def goods_columns(server: str, port: str, database: str, user: str, password: str):
    conn = pymssql.connect(
        server=server,
        port=port,
        database=database,
        user=user,
        password=password,
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


def goods(server: str, port: str, database: str, user: str, password: str):
    try:
        conn = pymssql.connect(
            server=server,
            port=port,
            database=database,
            user=user,
            password=password,
            login_timeout=5,
            timeout=5)

        print("connection open")
        cursor = conn.cursor()
        query = ("""
                    SELECT
                        """ + goods_columns(server, port, database, user, password) + """                 
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
