from better_partial import partial as better_partial, _
from functools import partial as worse_partial

'''
Consider a standard function of several variables 
'''

def f(a,b,c,d,e):
  return a,b,c,d,e

'''
Suppose we want produce a new function that fixes the value of `c`. With better_partial we can do this:
'''
better_g1 = better_partial(f)(..., c=3)
print(better_g1(1, 2, 4, 5))  # --> (1,2,3,4,5)
'''
Or we could do this
'''
better_g2 = better_partial(f)(_, _, 3, _, _)
print(better_g2(1, 2, 4, 5))  # --> (1,2,3,4,5) 
'''
How would we do this with functools.partial? Like this?
'''
worse_g = worse_partial(f, c=3)
print(worse_g(1, 2, 4, 5))  # --> TypeError f() got multiple values for argument 'c'
'''
functools.partial is doing the following: 
  (1) feed 1, 2, 4, 5 into f as positional arguments for a, b, c, d
  (2) supply c=3 as a kwarg, but wait, c was already provided by the positional arguments
  (3) TypeError
  
To be clear, I'm not saying this is a bug. 
I just want to be able to arbitraryily partially apply my functions which,
to my knowledge, functools.partial doesn't allow.
'''