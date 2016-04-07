def year():
    year1=input("year?: ")
    year=int(year1)
    if (year %4==0) and (year %100!=0 or year %400==0):
        print ("yes!!")
    else:
        print ("no!!")

def lab6():
	year()

def main():
	lab6()

if _name_=="_main_":
	main()