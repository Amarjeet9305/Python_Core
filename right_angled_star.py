# n = int(input("Enter the numnber of n:"))

# for i in range(1, n+1):
#     print('*' *i)

# WAP for number pattern using inner loop and outer loop

n = int(input("Enter the number of value n:"))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j,end='')
    print()    