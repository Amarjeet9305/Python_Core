# Binary search algorithem
# Function defintion

def binarySearch(arr,x,i,j):
    while i<=j:
        mid = i+(j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr,x,mid+1,j)
        else:
            return binarySearch(arr,x,i,mid-1)
    return -1    
    
    
# Driver code
# Taking user input

arr = list(map(int,input("Enter sorted element in list:",).split()))
x = int(input("Enter a searching element:"))
i = 0
j = len(arr) -1

# Function calling
result = binarySearch(arr,x,i,j)
print("Element at the index position:",result)  