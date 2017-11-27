# Given a list of integers, find the highest product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.
from itertools import islice

L = [1, 10, -5, 1, -100]

max_int = max(L[0],L[1])
min_int = min(L[0],L[1])
max_bi_prod = L[0]*L[1]
min_bi_prod = L[0]*L[1]
max_tri_prod = 0

for i in islice(L, 2, None):
    
    max_tri_prod  = max(max_tri_prod, max_bi_prod * i, min_bi_prod * i)
    
    max_bi_prod = max(max_bi_prod, i * max_int, i * min_int)
    
    min_bi_prod = min(min_bi_prod, i * min_int, i * max_int)
            
    max_int = max(max_int, i)
    
    min_int = min(min_int, i)
    
# My notes
# To make it in O(n) it is necessary to ask "What do i need to keep track of?"
# and be very careful, because there are many values you must keep track of
# especially because the case of negative numbers was tricky, i didn't consider it initially
# Be very very careful with the order with which we update the values!

# chose max and min from the first two elements, and set the initial min and max bi prods
# started from the third element of the list