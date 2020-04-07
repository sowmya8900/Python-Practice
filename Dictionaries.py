person={"name":"Sowmya", "gender":"Female", "age":"19","address":"Lodhi Colony","phone":"9968959632"}
info=str(input("What info. do you want from the person")).lower()
print("The required information is displayed below:")
print(person.get(info, "Doesn't exist"))
