# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
#   For example, given:
#   [1, 7, 3, 4]
#   your function would return:
#   [84, 12, 28, 21]

import numpy as np
import random
#v =   [1, 7, 3, 4]

N = 20

v =  [random.randint(1, 10) for _ in range(N)]
mem = np.diag(v)


def getProdFromMemory(s,e):
    global mem
    prod = mem[s,e]
    if(prod > 0):
        return prod
    else:
        prod = v[s] * getProdFromMemory(s+1, e)
        mem[s,e] = prod
        return prod
    
output = [0]*N
for i in range(0,N):
    if(i == 0):
        output[i] = getProdFromMemory(i + 1, N -1)
        continue
    if(i == N-1):
        output[i] = getProdFromMemory(0,i - 1)
        continue
    
    prod_before = getProdFromMemory(0,i - 1)
    prod_after = getProdFromMemory(i + 1, N -1)
    output[i] = prod_before * prod_after
    
# The memory matrix resulted too big, and in the end only the first row, and last cols are required
# to obtain any result, because in fact these are the ones that store all the necessary info
# the recommended approach by the website is to keep track of only the prods_before and prods_after
# vectors, which are these row and col. Im a bit sad i didnt get ir right :(