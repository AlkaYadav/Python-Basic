
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

if __name__=='__main__':
    create_dictionary()
