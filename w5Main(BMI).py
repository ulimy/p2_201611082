height=input("height(m) : ")
weight=input("weight(kg) : ")
print ("%.1f" %height, "%.1f" %weight )
BMI= weight/(height*height)
print ("%.1f" %BMI)
if BMI<=18.5:
     print ("low weight")
elif 18.5<BMI<=23:
     print ("normal weight")
elif 23<BMI<=25:
     print ("overweight")
elif BMI>25:
     print ("high obesity")