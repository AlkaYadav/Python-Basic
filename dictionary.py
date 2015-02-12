
#!/usr/bin/python

"""
dictionary.py
Various ways to create ,update ,delete dictionary
"""
def create_dictionary():
    '''
    1.Using {}
    '''
    d={'one':1,'two':2}
    print "Dictionary created :",d


    '''
    2.Using dict
    '''

    d=dict(one=1,two=2)
    print 'Dictionary created with dict:',d

    '''
    3.Using list of tuples
    '''
    d=dict([('hi',1),('hello',2),('bye',3)])
    print 'Dictionary created with list of tuples',d

    '''
    4.Dictionary From keys
    '''
    keys='zen alto hyundai lamborgini ferrari bmw mercedes'.split()
    d=dict.fromkeys(keys,"Default")
    print 'Dictionary created from keys',d
    return d

def update_dictionary(d):
    '''
    1.use setdefault
    '''
    print 'Original Dictionary:',sorted(d.items())
    print'Updatind Dictionary with setdeafult:'
    d.setdefault('new key1','new value1')
    print 'New Dictionary:',sorted(d.items())

    '''
    2.Using simple assignment
    '''
    print'Updatind Dictionary with simple assignment:'
    print 'Original Dictionary:',sorted(d.items())
    d['a']='value'
    print 'New Dictionary:',sorted(d.items()) 

    '''
    3.use get method
    '''
    print'Updatind Dictionary with get method:'
    print 'Original Dictionary:',sorted(d.items())
    print 'Return value of get:',d.get('b',None)
    print 'New Dictionary(Not updated!!):',sorted(d.items())

    '''
    4.use update method
    '''
    print'Updatind Dictionary with update method:'
    e={'a':1,'c':4,'y':7}
    print 'first dictionary:',sorted(d.items())
    print 'Another dictionary:',sorted(e.items())
    d.update(e)
    print 'New Dictionary after calling update:',sorted(d.items())

def del_dictionary(d):
    '''
    1.Using del method
    '''
    print 'Delete using del method for key "a"'
    print 'Original Dictionary:',sorted(d.items())
    del d['a']
    print 'Dictionary after deletion:',sorted(d.items())

    '''
    2.Using pop to avoid KeyError
    '''
    print 'Delete using pop method for key "h"'
    print 'Original Dictionary:',sorted(d.items())
    print'Delete:',d.pop('h','Value not present')
    print 'Dictionary after deletion:',sorted(d.items())


if __name__=='__main__':
    print 'Create new dictionary:'
    d=create_dictionary()
    print '================================='
    print 'Calling update method'
    print
    update_dictionary(d)
    print '=================================='
    print 'Calling delete'
    del_dictionary(d)
