#_*_ coding:utf-8 _*_
'''
Created on 2014年11月18日

@author: huang_yun
'''
import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))           
    return (all_athletes)

def get_from_store(file_list):
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_and_store):' + str(ioerr))           
    return (all_athletes)


if __name__ == '__main__':
    files = ['james2.txt','julie2.txt','mikey2.txt']
    print(put_to_store(files))
    print(get_from_store('athletes.pickle'))