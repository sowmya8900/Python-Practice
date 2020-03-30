months=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
birthday= input("enter your birthday in the format DD-MM-YYYY!")
month= int(birthday[3:5])
print("You were born in", months[month-1])

people=["sowmya","sushma","sujatha"]
name=str(input("enter the name of the person you want to add"))
people.append(name)
print(people)
