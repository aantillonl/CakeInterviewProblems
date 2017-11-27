# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
#   For example, given:
#   [1, 7, 3, 4]
#   your function would return:
#   [84, 12, 28, 21]

import numpy as np
#import random

v =   [1, 7, 3, 4]
N = len(v)

#N = 20
#v =  [random.randint(1, 10) for _ in range(N)]

prods_before = [0]*N
prods_before[0] = 1
prods_after = [0]*N
prods_after[N-1] = 1
prod_before_so_far = 1
prod_after_so_far = 1

for i in range(1,N):
    prod_before_so_far = prod_before_so_far * v[i-1]
    prods_before[i] = prod_before_so_far
    
    prod_after_so_far = prod_after_so_far * v[N - i]
    prods_after[N -1 - i] = prod_after_so_far
    
    
output = [0]* N
for i in range (0,N):
    output[i] = prods_before[i]*prods_after[i]