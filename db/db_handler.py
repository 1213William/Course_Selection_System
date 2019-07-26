import os
import pickle
from conf import settings


def save(path, dic):
    p = os.path.join(path, f'{dic.name}.txt')
    with open(p, 'wb') as f:
        pickle.dump(dic, f)
        f.flush()


def select(path, file_name):
    p = os.path.join(path, f'{file_name}.txt')
    if os.path.exists(p):
        with open(p, 'rb') as f:
            return pickle.load(f)
    return None


def select_all(path):
    p = os.listdir(path)
    return p


if __name__ == '__main__':
    select_all('/Users/mac/Documents/NEW_CHOICE/db/school')
