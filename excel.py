import settings
import sql_query
import pandas as pd
from progress.bar import IncrementalBar


def good(path, file, goods):
    s = sql_query.goods_columns(server=settings.server, port=settings.port, database=settings.database,
                                user=settings.user,
                                password=settings.password)

    keys = s.split(', ')

    bar = IncrementalBar('generate dict for xlsx', max=len(goods) * len(keys))
    values = []
    for i in range(len(keys)):
        lst = []
        for row in goods:
            bar.next()
            lst.append(row[i])
        values.append(lst)
    # values = [[row[i] for row in goods] for i in range(len(keys))]

    df = pd.DataFrame(dict(zip(keys, values)))
    full_path = path + file
    df.to_excel(str(full_path), sheet_name='goods', index=False)
    print("\ncompleted")
