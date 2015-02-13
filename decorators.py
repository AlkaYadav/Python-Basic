'''
decorators.py
Create decorators to create a registry to add functions and
add_docstring to functions
'''
import functools,random
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
	
#This func uses functools.wraps which manages to keep name of
#function,argument list correct to function calling

def memoize(maxsize=10):
    def decorator(func):
        'result caching wrapper'
        cache={}
        @functools.wraps(func)
        def wrapper(*args):  #**kwargs not available for dict
            if args in cache:
                return cache[args]
            result=func(*args)
            if len(cache)>=maxsize:
                del cache[random.choice(cache.keys())]
            cache[args]=result
            return result
        return wrapper
    return decorator
        
        
#######List of functions to register and add_doc####
@register    #like square=register(square)
@add_docstring
@add_logging
def square(x):
    return x ** x

@memoize(maxsize=3)
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
    print calculate(3)
    print calculate(4)
    print calculate(5)
    print '================================'
    print 'Calling collatz'
    print 'collatz of 8 is',collatz(8)
    print 'Registry',registry
    print 'Square doc is',square.__doc__
    print '================================'
