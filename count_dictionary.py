'''
count_dictionary.py
Counting in dictionary
'''
from collections import Counter
def count():
    #Constructing dictionary with values as the no.
    #of occurences of the key in a list    
    colors = 'red green blue yellow purple red blue yellow red'.split()
    d={}
    for color in colors:
        d[color]=d.get(color,0)+1
    print 'Counted:',d    

def count_using_Counter():
    colors = 'red green blue yellow purple red blue yellow red'.split()
    print 'After counting using Counter',Counter(colors)
    print 'Printing most commons:',Counter(colors).most_common(2)

def create_new_dict_using_first_letter():
    '''
    Creates a dictionary with first letter of color as key and value
    is a set of colors starting with that first letter
    '''
    d={}
    colors='red green blue yellow purple red blue yellow red bluo'.split()
    print'Colors',colors
    for color in colors:
        (d.setdefault(color[0],set())).add(color)
        
    print 'Dictionary',d    

def count_default_dict():
    from collections import defaultdict
    '''defaultdict can be used to create trees using
       defaultdict(dict),every element will itself be a dictionary
    '''   
    #Specify set as default value
    #defaultdict doesn't give key error,it replaces with default value

    d=defaultdict(set)
    colors='red green blue yellow purple red blue yellow red bluo'.split()
    for color in colors:
        d[color[0]].add(color)
    print 'Dictionary created:',d
    print 'Another example of defaultdict'
    d=defaultdict(int)
    for color in colors:
          d[color]+=1
    print 'Dictionary created:',sorted(d.items())
    print 'Another example of defaultdict'
    d=defaultdict(lambda:-10)
    for color in colors:
        d[color]+=1
    print 'Dictionary created:',sorted(d.items())
    
      
if __name__=='__main__':
     print 'Simple counting'
     count()
     print 'Counting using Counter'
     count_using_Counter()
     print 'Creating something different'
     create_new_dict_using_first_letter()
     count_default_dict()

    
