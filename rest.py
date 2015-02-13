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
filelist_html_template="""
<html>
    <head>
        <title> File in notes folder</title>
    </head>
    <body>
        <h1>List of files in 'notes' folder</h1>
        <ul>
            %s
        </ul>
        </body>
        </html>
     
"""
listitem_html_template='<li>%s</li>'
@itty.get('/show')
def show_files(request):
    files=os.listdir('/Users/alkyadav/Python/pyclass/notes')
    query=request.GET
    fmt=query.get('format','json')
    if fmt == 'json':
        result=json.dumps(files)
        response=itty.Response(result,content_type='application/json')
    elif fmt == 'html':
        listitems=[]
        for filename in files:
            listitems.append(listitem_html_template%filename)
        response=filelist_html_template%''.join(listitems)
    else:
        response='Invalid ? format use json or html'%fmt
    return response    

@itty.get('/upper')
def show_upper(request):
    query=request.GET
    word=query.get('word','missing')
    return word.upper()
    
if __name__=='__main__':
    itty.run_itty(host='localhost',port=8080)

        
