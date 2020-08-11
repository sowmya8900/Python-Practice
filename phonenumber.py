n = int(input())
l = []
for i in range(n):
    pn = str(input())
    l.append(pn)
for j in l:
    if(j.isnumeric() == True):
        k = int(j[0][0])
        if(len(j) == 10):
            if (k == 7 or k == 8 or k == 9):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
