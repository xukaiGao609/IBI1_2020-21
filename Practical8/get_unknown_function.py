import re
dna = open('C:/Users/11877/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
c =''
Boole = False   #use boole to link unknown protein with following DNA sequence.
s=''
for line in dna:
    if line.startswith('>'):
        if Boole==True:
            s = s+'>'+b+'   '+str(len(c))+'\n'+c+'\n' #create the final format
            c=''
            Boole=False
        if re.findall(r'unknown',line):
            b=re.findall(r'^>.+?_',line)
            b=b[0]
            b=b[:-1]
            Boole=True
    else:
        if Boole==True:
                c=c+line.strip()  #put in the dna sequence
dna.close()
z=open('unknown_function.fa','w')
z.write(s)
z=open('unknown_function.fa','r')
print(z.read())
z.close()
