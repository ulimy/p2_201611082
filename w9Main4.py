﻿def CoffeeMilk():
    allData=list()
    allData=[["Coffee","Water","Milk","Icecream"],
      ["Espresso","No","No","No"],
      ["Long Black","Yes","No","No"],
      ["Flat White","No","Yes","No"],
      ["Cappuccino","No","Yes - Frothy","No"],
      ["Affogato","No","No","Yes"]]
    onlydata=allData[1:]
    nonmilk=0
    milk=0
    for i in onlydata:
        if i[2]=="No":
            nonmilk=nonmilk+1
        else:
            milk=milk+1
    milkproportion=milk/len(onlydata)*100
    nonmilkproportion=nonmilk/len(onlydata)*100
    print ("milkproportion: ",milkproportion)
    print ("nonmilkproportion: ",nonmilkproportion)

def SumAverage():
    result=list()
    result=[['English',100],
        ['Math',200],
        ['English',200],
        ['Math',200], 
        ['English',100],
        ['Math',300]]
    Esum=0
    Elen=0
    Msum=0
    Mlen=0
    for i in result:
        if i[0]=='English':
            Esum=Esum+i[1]
            Elen=Elen+1
        else:
            Msum=Msum+i[1]
            Mlen=Mlen+1
    Eaverage=Esum/Elen
    Maverage=Msum/Mlen
    print ("Sum of English: ",Esum)
    print ("Average of English: ",Eaverage)
    print ("Sum of Math: ",Msum)
    print ("Average of Math: ",Maverage)

def letitbe():
    lyrics=list()
    lyrics=['When I find myself in times of trouble',
    'Mother Mary comes to me',
    'Speaking words of wisdom let it be',
    'And in my hour of darkness',
    'She is standing right in front of me',
    'Speaking words of wisdom let it be',
    'Let it be let it be',
    'Let it be let it be',
    'Whisper words of wisdom let it be',
    'And when the broken-hearted people',
    'Living in the world agree',
    'There will be an answer let it be',
    'For though they may be parted',
    'There is still a chance that they will see',
    'There will be an answer let it be',
    'Let it be let it be',
    'Let it be let it be',
    'Yeah there will be an answer let it be',
    'Let it be let it be',
    'Let it be let it be',
    'Whisper words of wisdom let it be',
    'Let it be let it be',
    'Ah let it be yeah let it be',
    'Whisper words of wisdom let it be',
    'And when the night is cloudy',
    'There is still a light that shines on me',
    'Shine on until tomorrow let it be',
    'I wake up to the sound of music',
    'Mother Mary comes to me',
    'Speaking words of wisdom let it be',
    'Let it be let it be',
    'Let it be yeah let it be',
    'Oh there will be an answer let it be',
    'Let it be let it be',
    'Let it be yeah let it be',
    'Whisper words of wisdom let it be']
    d=dict()
    for line in lyrics:
        for c in line.split():
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
    up20=list()
    down20=list()
    for i in d:
        if d[i]>=20:
            up20.append(i)
        else:
            down20.append(i)
    print ("More than 20 times: ",up20)
    print ("Less than 20 times: ",down20)

def lab9():
    CoffeeMilk()
    SumAverage()
    letitbe()

def main():
    lab9()

if _name_=="_main_":
     main() 


