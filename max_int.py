#Forrit þar sem user seturinn inn int þangað til að hann setur negatíva tölu og þá stoppar forritið


num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = num_int
while num_int > 0:
    num_int = int(input("Input a number: "))
    if max_int < num_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line

