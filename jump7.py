for a in range(1,101):
    b=a%10
    c=a%7
    if b==7:
        continue
    elif c==1:
        continue
    elif a in range(71,80):
    # elif a//10==7:
        continue
    else:
        print(a)
