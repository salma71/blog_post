import glob
import time

start = time.time()

path = './csv_test-main/data/'
all_files = glob.glob(path + '*.csv')
cols = ['f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'target']

with open('merged.csv', 'w') as out:
    out.write('%s\n' % ','.join(cols))
    for filename in all_files:
        with open(filename) as f:
            for idx, line in enumerate(f):
                if idx > 0:
                    out.write(line)
end = time.time()
print(end - start)
