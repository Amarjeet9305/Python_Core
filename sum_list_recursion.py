# I have a list sum the each element using recursion function.
# First we defining a function
# total time complexity is o(n)
def lst_sum(lst1):
    # Weather check lenght of lst1
    
    if len(lst1) == 1:
        # if list have onle one element then return that element
        return lst1[0]
    else:
        # If the lst1 has more than one element,then return the lst_sum of the first element
        # and the result of recursively calling the lst_sum function on the rest of list
        
        return lst1[0] + lst_sum(lst1[1:])
# Calling the lst_sum function

print(lst_sum([1,2,3,4,5,6]))
    
