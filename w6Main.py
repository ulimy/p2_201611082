def year():
    year1=input("year?: ")
    year=int(year1)
    if (year %4==0) and (year %100!=0 or year %400==0):
        print ("yes!!")
    else:
        print ("no!!")

def hl():
    import random
    a=random.randint(1,200)
    guessTaken=0
    while guessTaken<10:
        guessTaken=guessTaken+1
        b1=input("choose number(range 1~200): ")
        b=int(b1)
        if a>b:
            print ("high↑")
        elif a<b:
            print ("low↓")
        elif a==b:
            print ("yes!!")

def lab6():
	year()
	hl()

def main():
	lab6()

if _name_=="_main_":
	main()
	

