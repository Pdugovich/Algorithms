#!/usr/bin/python

import math

"""
UNDERSTAND:

We need to compare two dictionaries, which contain key pairs of strings and integers
The first dictionary has the minimum values
The second dictonary has the values on hand

We need to determine how many full values of dict 1 go into dict 1
Find the lowest ratio, then round down and return that number


For example:
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

We should check like this:

milk2/milk1, butter2/butter 1, flour 2/flour 1
138/100, 48/50, 51/5

That gives us
1.38, 0.96, 10.2

The lowest number is 0.96, and that rounds down to 0, so we can make 0 batches



PLAN:

pseudocode:
ended up just coding it 
"""


def recipe_batches(recipe, ingredients):
  # Make an empty list to fill with ratios
  ratios = []
  # for each key/value pair in the recipe
  for k,v in recipe.items():
    # If that key is also in ingredients
    if k in ingredients.keys():
      # using floor division, get the ratio of ingredients to requirements
      ratio = ingredients.get(k) // recipe.get(k)
      # append that to the list of ratios to compare
      ratios.append(ratio)
    else:
      # If the key is not in ingredients, append 0 
      ratios.append(0)
  # Return the lowest, since the number of batches we can make depends on the
  # ingredients we have th least of relative to what we need
  return(min(ratios))




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))