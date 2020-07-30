# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
name_phoneNumber = {}
name_phoneNumber = dict(input().split() for _ in range(n))

try:
    while True:
        inp = str(input())    
        if (inp in name_phoneNumber.keys()):
            phoneNumber = name_phoneNumber[inp]
            print(inp+"="+phoneNumber)
        else:
            print("Not found")
    
except EOFError:
    pass
