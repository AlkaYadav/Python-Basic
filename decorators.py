'''
decorators.py
Create decorators to create a registry to add functions and
add_docstring to functions
'''

registry={}
def register(func):
    'to register functions'
    'identity function with side effect'
    'as it adds entry for function in registry'
    'decorators take func as arg and return func'
    registry[func.__name__]=func
    return func

def add_docstring(func):
    if func.__doc__ is None:
        func.__doc__='Unknown documentation'
    return func

def add_logging(func):
	def wrapper(x):
				print 'Called',func.__name__,'with ',x
				ans=func(x)
				print 'The answer is',ans
				wrapper.__name__=func.__name__
				return ans
	return wrapper
	
				
#######List of functions to register and add_doc####
@register    #like square=register(square)
@add_docstring
@add_logging
def square(x):
    return x ** x

@register
@add_docstring
def calculate(x):
    'Calculating some expensive work'
    import time
    time.sleep(1)
    print 'Done'
    return x+1

@register
@add_docstring    
def collatz(x):
	'Collatz conjecture:a simple example of halting problem'
	if x%2==0:
		return x//2
	return 3*x+1

if __name__ == '__main__':
    print 'Calling square'
    print 'Square of 5 is',square(5)
    print 'Registry',registry
    print 'Square doc is',square.__doc__
    print '================================'
    print 'Calling calculate'
    print 'calculate of 2 is',calculate(2)
    print 'Registry',registry
    print 'Square doc is',square.__doc__
    print '================================'
    print 'Calling collatz'
    print 'collatz of 8 is',collatz(8)
    print 'Registry',registry
    print 'Square doc is',square.__doc__
    print '================================'
