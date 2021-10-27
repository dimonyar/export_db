import settings
import variables
import sql_query
import pandas as pd
from progress.bar import IncrementalBar


def good(path, file, goods):
    s = sql_query.goods_columns()

    keys = s.split(', ')

    bar = IncrementalBar('generate dict for xlsx', max=len(goods) * len(keys))
    value = []
    for i in range(len(keys)):
        lst = []
        for row in goods:
            bar.next()
            lst.append(row[i])
        value.append(lst)
    # values = [[row[i] for row in goods] for i in range(len(keys))]

    df = pd.DataFrame(dict(zip(keys, value)))
    full_path = path + file
    df.to_excel(str(full_path), sheet_name='Good', index=False)
    print("\ncompleted")


def columns(table: str):
    full_path = variables.path + variables.xlsfile
    if table == 'Barcode':
        sheet_name = 'Good'
    else:
        sheet_name = table
    df = pd.read_excel(full_path, sheet_name=sheet_name)
    return ', '.join([i for i in df.columns.tolist() if i.split('.')[0] == table])


def values(table: str):
    full_path = variables.path + variables.xlsfile
    df = pd.read_excel(full_path, dtype=object).replace({True: 1, False: 0})
    lst = df.values.tolist()
    index_columns = [i for i in range(len(df.columns.tolist())) if df.columns.tolist()[i].split('.')[0] == table]
    value = []
    bar = IncrementalBar('generate insert query', max=len(lst))
    columns_name = columns(table)
    for row in lst:
        val = []
        for i in range(len(row)):
            if i in index_columns:
                if isinstance(row[i], str):
                    val.append(str(row[i]).replace("'", "’"))
                else:
                    val.append(row[i])
        if 'INSERT INTO ' + table + '(' + columns_name + ') VALUES' + str(tuple(val)) not in value:
            bar.next()
            value.append('INSERT INTO ' + table + '(' + columns_name + ') VALUES' + str(tuple(val)))
        else:
            continue
    return '; '.join(value).replace('nan', 'NULL')
