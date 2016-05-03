def charCount():
    import matplotlib
    import matplotlib.pyplot as plt
    d=dict()
    word=input("What is your word?:")
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print (d)
    plt.bar(range(len(d)),d.values(), align='center')     
    plt.xticks(range(len(d)), list(d.keys())) 
    plt.show()
    
def countDigitsLetters():
    import matplotlib
    import matplotlib.pyplot as plt
    d=dict()
    word=input("What is your word?:")
    d={"Digit":0 , "Letter":0}
    for c in word:
        if c.isdigit()==True:
            d["Digit"]=d["Digit"]+1
        elif c.isalpha()==True:
            d["Letter"]=d["Letter"]+1
    plt.bar(range(len(d)),d.values(), align='center')     
    plt.xticks(range(len(d)), list(d.keys())) 
    plt.show()  
    
def FindDifference():
    myhouse=set(['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
    friendhouse=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])
    print ("my house: " ,myhouse)
    print ("friend's house: ",friendhouse)
    print ("only my house: ",myhouse.difference(friendhouse))
    print ("only friend's house: ",friendhouse.difference(myhouse))
    print ("both: ",myhouse.intersection(friendhouse))
    print ("all: ",myhouse.union(friendhouse))
    print ("how many?: ",len(myhouse.union(friendhouse)))
    
def lab8():
    charCount()
    countDigitsLetters()
    FindDifference()
    
def main():
    lab8()
   
if _name_=="_main_":
    main()