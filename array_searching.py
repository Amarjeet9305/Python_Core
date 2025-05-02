# # Function Defintion

# def linearSearch(arr,x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1    
        

# # Driver code
# arr = [20,45,27,47,55,67,75,88,90]
# x=55
# # Function calling
# result = linearSearch(arr,x)
# print("Searching element at index postion:",result)
# Create a array size

# Function Defintion

def linearSearch(arr1,x):
    for i in range(len(arr1)):
        if arr1[i] == x:
            return i
        
    return -1    

arr1 = [100,101,103,105,106,107,108,110]


# Searching the arr of element on x=106
x=111
# Function calling
result = linearSearch(arr1,x)
# Show the output
print("Element of index position:",result)   