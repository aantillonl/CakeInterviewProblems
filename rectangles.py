#A crack team of love scientists from OkEros (a hot new dating site) 
#have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
#They need help writing an algorithm to find the intersection of two users' love rectangles. 
#They suspect finding that intersection is the key to a matching algorithm 
#so powerful it will cause an immediate acquisition by Google or Facebook or 
#Obama or something.

#Write a function to find the rectangular intersection of two given love rectangles.

#As with the example above, love rectangles are always "straight" and never "diagonal." More rigorously: each side is parallel with either the x-axis or the y-axis.

#They are defined as dictionaries ↴ like this:

#  my_rectangle = {

#    # coordinates of bottom-left corner
#    'left_x': 1,
#    'bottom_y': 5,

#    # width and height
#    'width': 10,
#    'height': 4,

#}

#Your output rectangle should use this format as well.


r1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,
    # width and height
    'width': 4,
    'height': 4,
}

r2 = {
    # coordinates of bottom-left corner
    'left_x': 2,
    'bottom_y': 2,
    # width and height
    'width': 2,
    'height': 2,
}

rectangles = [r1, r2]


def findOverlap(rectangles):
    
    wi = 0
    hi = 0
    left_x_i = 0 
    bottom_y_i = 0
    
    leftest = min(rectangles, key = lambda r: r['left_x'])
    rightest  = next(r for r in rectangles if r is not leftest)
    lowest = min(rectangles, key = lambda r: r['bottom_y'])
    uppest = next(r for r in rectangles if r is not lowest)
    
    # it is important to identify the lowest, and leftest!
    if (
            # Check if the "rightest" rectangle starts before the leftest ends, to see if there is overlap on X
            leftest['left_x'] <= rightest['left_x'] < leftest['left_x']+leftest['width'] and 
            # Check if the "uppest" rectangle starts before the "lowest" ends, to see if there is overlap on Y
            lowest['bottom_y'] <= rightest['bottom_y'] < (leftest['bottom_y']+leftest['height'])):
        
        left_x_i = rightest['left_x']
        wi = min((leftest['left_x']+leftest['width']), (rightest['left_x'] + rightest['width'])) - left_x_i
    
        bottom_y_i = uppest['bottom_y']
        hi = min((lowest['left_x']+lowest['height']), (uppest['left_x'] + uppest['height'])) - bottom_y_i
    
    intersection = {
        # coordinates of bottom-left corner
        'left_x': left_x_i,
        'bottom_y': bottom_y_i,
        # width and height
        'width': wi,
        'height': hi,
    }
    return intersection

print(findOverlap(rectangles))


# The solution online does something slightly different, they do not label the rectangles as
# "lowest", "uppest", "leftest" or "rightest". I guess it simplifies a bit checking if the rectangles overlap
# Performance is O(1)
