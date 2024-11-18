#Martin Cahue
#October 22, 2024
I= 1
while I <=50:
    if I % 3 == 0 and I % 5 == 0:
        print(f"{I} is divisible by both")
    elif I % 3 == 0:
        print(f"{I} is divisible by three")
    elif I % 5 == 0:
        print(f"{I} is divisible by five")
    else:
        print(f"{I} is divisible by neither")
    I+=1
#problem 3- a program that iterates integers from 1 to 50. 
# Prints a message depending on if the number is divisible by three, five, both or neither.
