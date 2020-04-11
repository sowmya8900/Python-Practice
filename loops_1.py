import random
people=[]
print("Enter the name of the person")
for p in range(0,8):
  name=input(p)
  people.append(name)
print (people)
print(people[random.randint(0,7)+1])
