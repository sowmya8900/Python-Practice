import random
maximum= int(input("Enter Maximum number of guessing"))
number= random.randint(0,maximum)
# print(number)
# This is the number system is guessing
guess= int(input("I'm thinking of a number! Can you guess it?"))
count=0
while (guess!=number):
    if (guess>number) :
        print("the number is less than", guess)
        count+=1
        guess=int(input("guess again"))
    elif(guess<number): 
        print("the number is greater than", guess)
        count+=1
        guess=int(input("guess again"))

print("Waah! You guessed the number correctly in", count+1, "times")
