'''
function_closure.py
Describes python function closures and cell contents working
A CLOSURE is a function object that remembers values in enclosing scopes
regardless of whether those scopes are still present in memory.
'''
def adder_factory(x):
    print 'Inside adder factory'
    def adder(y):
        print 'Inside closure'
        return x+y
    print 'Exiting adder factory'
    return adder

if __name__=='__main__':
    addition=adder_factory(4)
    print addition
    print 'Delete the reference to enclosing function'
    del adder_factory
    print 'Print func closure '
    print addition.func_closure
    print addition.func_closure[0].cell_contents
    print 'Calling the enclosed function'
    print addition(3)
    
    
    
