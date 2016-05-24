%%writefile python.txt
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.[23][24] 
Its design philosophy emphasizes code readability, 
and its syntax allows programmers to express concepts in fewer lines of code 
than would be possible in languages such as C++ or Java.[25][26] 
The language provides constructs intended to enable clear programs on both a small and large scale.[27]

import os

def python():
    mydir=os.getcwd()
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    myfile=open(myfilename,'r')
    try:
        for line in myfile:  
            if line.find('Python')>=0:
                print (line)
    except IOError as e:
        print (e)
    myfile.close()
    
def line():
    myfile=open('output.txt','w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third'
    myfile.write(line3)
    myfile.close()
    mydir=os.getcwd()
    filename='output.txt'
    myfilename=os.path.join(mydir,filename)
    myfile=open(myfilename,'r')
    contents=myfile.readlines()
    for a in range(0,len(contents)):  
        if contents[a].find('line')>=0:
            print (contents[a].upper())
    myfile.close()
    

def lab12():
    python()
    line()

def main():
    lab12()

if _name_=="_main_": 
      main()  
