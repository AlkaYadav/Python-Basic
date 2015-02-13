'''
rest.py
Making REST API with python
'''
from notes import itty
import time,os

@itty.get('/')
def welcome(request):
    return 'Hello'

@itty.get('/time')
def show_time(request):
    return time.ctime()

@itty.get('/show')
def show_files(request):
    files=os.listdir('/Users/alkyadav/Python/pyclass/notes')
    return str(files)

if __name__=='__main__':
    itty.run_itty(host='localhost',port=8080)

        
