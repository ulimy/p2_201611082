def h1():
    myfile=open('output.txt','w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third'
    myfile.write(line3)
    myfile.close()
    fin=open('output.txt','r')
    fout=open('outputUpper.txt','w')
    import time
    for line in fin:
        words=line.split()
        if line.find('line')>=0:
            msg='[YL edited {0}]'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
            fout.write(msg)
        for word in words:
            if word=='line':
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()

def h2():
    data=[1,2,3,4,5,6,7,8,9,10]
    dataopen=open('dataopen.txt','w')
    for i in data:
        if i%2:
            dataopen.write("{0}\t".format(i))
        else:
            dataopen.write("{0}\t\n".format(i))
    dataopen.close() 

def lab12(): 
    h1() 
    h2() 
 
 
def main(): 
    lab12() 
 
if __name__=="__main__": 
    main()  
 
 

