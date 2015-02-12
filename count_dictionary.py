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

if __name__=='__main__':
     print 'Simple counting'
     count()
     print 'Counting using Counter'
     count_using_Counter()


    
