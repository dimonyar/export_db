import excel
import sql_query
import variables
from txt import file_output

export_import = int(input("Press 1 if want export data SQL to xlsx and txt \n or"
                          " \n Press 2 for import xlsx to SQL :\n"))

if export_import == 1:
    goods = sql_query.goods()
    excel.good(path=variables.path, file=variables.xlsfile, goods=goods)
elif export_import == 2:
    sql_query.delete_table('Barcode')
    sql_query.delete_table('Good')
    sql_query.insert_into('Good')
    sql_query.insert_into('Barcode')


# file_output(path=variables.path, file=variables.txtfile, goods=goods)




