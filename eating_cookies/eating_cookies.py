#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


"""
Understand:

I need to find an algorithm to determine how many different ways 
there are to sum the numbers 1, 2, or 3 to equal a number

n = 1
1

n = 2
1, 1
2

n = 3
1, 1, 1
1, 2
2, 1
3

n=4
1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2
1, 3
3, 1

n=5
1, 1, 1, 1, 1
1, 1, 1, 2
1, 1, 2, 1
1, 2, 1, 1
2, 1, 1, 1
1, 2, 2
2, 1, 2
2, 2, 1
1, 1, 3
1, 3, 1
3, 1, 1
2, 3
3, 2
"""