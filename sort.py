list = []
file = open('word_freq.txt','r')
for i in file:
    tup = i.split(' ')
    list.append([tup[0],int(tup[1])])
list =sorted(list,key = lambda a:a[0])
out = open('processed.txt','w')
for i in list:
    out.write(i[0]+" "+str(i[1])+'\n')
out.close()