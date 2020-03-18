#!/usr/bin/python

import argparse



"""
UNDERSTAND:


Given a list of integers, find the greatest difference between a number
and any of the numbers that PRECEDE it, so with a list

arr = [1050, 270, 1540, 3800, 2]

It should return 3530 because the largest difference between a number and the number
that precedes it is 3800 - 270. Note that the 2 does not factor in because you can't
subtract anything FROM 2 at the start of the list that yields a number higher than
3580


PLAN:

Pseudocode:

profits = []
for index in range(len(prices)):
  if index > 0:
    for i in range(len(prices[:index])):
      profits.append(prices[index] - prices[i])

return max(profits)

Actually, that ended up being actual code


"""

def find_max_profit(prices):
    # Setting up an empty list to fill with each difference
    profits = []
    # for each index in the list
    for index in range(len(prices)):
      # You can only buy the first index, so skip it
      if index > 0:
        # For each index prior to the current index
        for i in range(len(prices[:index])):
          # subtract the index you "sell" from the index you "bought"
          profits.append(prices[index] - prices[i])
    # Return the max of the values
    return max(profits)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

