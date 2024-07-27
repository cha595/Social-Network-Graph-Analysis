import pandas as pd
import time
import os

def get_saved_names(charlotteewhelan):
    return os.listdir('./users')

name_to_id = {}
id_to_name = {}

with open('./IG - Sheet1.csv', 'r') as ffile:
    for line in ffile.readlines():
        arr = line.split(',')
        name_to_id[arr[2]] = arr[1]
        id_to_name[arr[1]] = arr[2]

def clean(line):
    return line.strip()

def subtract(a, b):
    return list(set(a) - set(b))

if __name__ == '__main__':

    st = time.time()

    all_names = [f.strip() for f in open('./all_names.csv').readlines()]
    saved_names = get_saved_names()

    for name in saved_names:
        mutuals = []
        with open('users/'+name) as ff:
            for line in ff.readlines():
                if clean(line) in name_to_id.keys():
                    mutuals.append(clean(line))
        with open(f'./mutuals/{name}_mutual.csv','w') as ff:
            for m in mutuals:
                ff.write(m+'\n')

    ed = time.time()
    print(f'{ed-st}s - processed {len(saved_names)} users.')

    with open('./name_logs.log','w') as ff:
        ff.write('Names that doesn\'t exist in the followers (misspelled):\n')
        for n in subtract(saved_names, all_names):
            ff.write(n+'\n')
        ff.write(f'\nNames that are not crawled ({len(subtract(all_names,saved_names))}):\n')
        for n in subtract(all_names, saved_names):
            ff.write(n+'\n')
