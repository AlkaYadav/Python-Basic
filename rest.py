'''
rest.py
Making REST API with python
'''
from notes import itty
import time,os,json

@itty.get('/')
def welcome(request):
    return 'Hello'

@itty.get('/time')
def show_time(request):
    return time.ctime()

@itty.get('/show')
def show_files(request):
    files=os.listdir('/Users/alkyadav/Python/pyclass/notes')
    result=json.dumps(files)
    itty.Response(result,content_type='application/json')
    return result

@itty.get('/upper')
def show_upper(request):
    query=request.GET
    word=query.get('word','missing')
    return word.upper()
    
if __name__=='__main__':
    itty.run_itty(host='localhost',port=8080)

        
