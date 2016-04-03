def rsp():
    a=input('a!! r? s? p?:')
    b=input('b!! r? s? p?:')
    if a==b:
        print ("draw")
    elif a=='r':
        if b=='s':
            print ("a win")
        elif b=='p':
            print ("b win")
    elif a=='s':
        if b=='r':
            print ("b win")
        elif b=='p':
            print ("a win")
    elif a=='p':
        if b=='r':
            print ("a win")
        elif b=='s':
            print ("b win")
rsp()
wn.exitonclick
