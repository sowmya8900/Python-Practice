import random
colors=["blue","pink","orange","yellow","grey","violet","purple"]
while True:
   col= colors[random.randint(0,len(colors)-1)]
   guess= str(input("I'm thinking of a color! Can you guess it?"))
   count=0
   while (guess!=col):
        guess=str(input("guess again"))
        count+=1
   print("Waah! You guessed the color correctly in", count+1, "trials")
   again=str(input("do you want to play again? Yes/No"))
   if (again.lower()=="no"):
        break
   else:
       continue
print("it was fun")
