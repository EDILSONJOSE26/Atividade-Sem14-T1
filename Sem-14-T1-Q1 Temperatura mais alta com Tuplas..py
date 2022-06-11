t = (float(input()),
     str(input()).upper().strip())

     
t2 = (float(input()),
      str(input()).upper().strip())

if t[1] == t2[1] and t > t2:
    print(t)
elif t[1] == t2[1] and t < t2:
    print(t2)
else:
    if t[1] != t2[1] and t[1] == 'C':
        F =  9 * t[0] / 5 + 32
        if F > t2[0]:
            print(t)
        else:
                print(t2)
    if t[1] != t2 and t[1] == 'F':
        C = (t[0] - 32) * (5/9)
        if C > t2[0]:
            print(t)
        else:
            print(t2)
