# def kul_pattern(n):
#     if n < 3 or n % 2 == 0:
#         print("Enter a number an odd n > 3:")
#         return
#     for i in range(n):
#         for j in range(i+1):
#             print('e', end='')
#         for j in range(i,n):
#             print('e', end='')
#         for j in range(i-1):
#             print('*', end='')
#         print()
# # Function calling
# kul_pattern(3)
# print()
# kul_pattern(5)                 

def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print('e', end=' ')
            elif j == 0 or j == n -1:
                print('e', end=' ')
            else:
                print('*', end=' ')
        print()
print_pattern(3)
print()
print_pattern(5)                                