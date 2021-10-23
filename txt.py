import os
from progress.bar import IncrementalBar


def file_output(path, file, goods):
    os.chdir(path)

    f = open(file, 'w')

    bar = IncrementalBar('write file', max=len(goods))

    for row in goods:
        bar.next()
        f.write(';'.join(str(i) for i in row) + '\n')

    bar.finish()
    f.close()
