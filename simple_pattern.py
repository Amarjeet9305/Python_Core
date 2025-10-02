# n = 4
# for i in range(n):
#     for j in range(n):
        
#         print('*', end=' ')
#     print()        
#     # print('*'*4)


# Increasing Triangle pattern

# n = 5
# for i in range(5):
#     for j in range(i+1):
#         print("*", end='')
#     print()        

# Decreasing Triangle pattern

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*", end='')
#     print()        
# Right side Increase Triangle
# n =5 
# for i in range(n):
#     for j in range(i,n):
#         print('', end='')
#     for j in range(i+1):
#         print('*', end='')
#     print()            

# n =5
# for i in range(n):
#     for j in range(i+1):
#         print('', end='')
#     for j in range(i,n):
#         print('*', end='')
#     print()   

# HIll patter problem

n = 5
for i in range(n):
    for j in range(i,n):
        print('', end='')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')
    print()                 