#!/usr/bin/env python3
# set items are not orderd and not indexed

my_set = ["meso", "nagi", "100"]
def function(my_set):
    return True
result = filter(function, my_set)
for i in result:
    print (result)
