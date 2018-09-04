#Forrit sem reiknar út sequence-ið  1, 2, 3, 6, 11, 20, 37, ___, ___, ___, ...

n = int(input("Enter the length of the sequence: ")) # Do not change this linegit 

num1 = 1
num2 = 2
num3 = 3

for i in range(1, n+1):
    if i < 4:
        print(i)
    else:
        nextnum = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = nextnum
        print(nextnum)
    

