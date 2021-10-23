import excel
import settings
import sql_query
import variables
from txt import file_output


connection_strings = settings.server, settings.port, settings.database, settings.user, settings.password

print(connection_strings)

goods = sql_query.goods(server=settings.server, port=settings.port, database=settings.database, user=settings.user,
                        password=settings.password)

file_output(path=variables.path, file=variables.txtfile, goods=goods)

excel.good(path=variables.path, file=variables.xlsfile, goods=goods)







