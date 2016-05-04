x=list()
x=[[74425,76326],
   [61164,61636],
   [109688,115744],
   [144796,146776],
   [174996,181676],
   [177841,177434],
   [204630,205980],
   [223373,232245],
   [161055,166130],
   [171576,176735],
   [279169,293772],
   [239450,251066],
   [148690,156510],
   [182977,196992],
   [237792,242641],
   [283869,296762],
   [209344,210282],
   [118965,114441],
   [186503,186856],
   [195734,203014],
   [254381,249472],
   [212401,229111],
   [271654,295354],
   [319197,335045],
   [229829,231671]
  ]
mansum=0
womansum=0
for i in x:
    mansum=mansum+i[0]
print ("man sum: ",mansum)
manaverage=mansum/len(x)
print ("man average: ",manaverage)
for i in x:
    womansum=womansum+i[1]
print ("womansum: ",womansum)
womanaverage=womansum/len(x)
print ("womanaverage: ",womanaverage)
y=list()
for i in x:
    sum=i[0]+i[1]
    y.append(sum)
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
plt.bar(range(len(y)),y,align='center')
plt.show