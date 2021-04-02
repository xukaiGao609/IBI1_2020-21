import re
dna = open('C:/Users/11877/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
code = {
'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
'TTA':'L', 'TCA':'S', 'TAA':'stop', 'TGA':'stop',
'TTG':'L', 'TCG':'S', 'TAG':'stop', 'TGG':'W',
'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
'CTG':'L', 'CCG':'P', 'CAG':'Z', 'CGG':'R',
'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
'ATC':'I', 'ACC':'T', 'AAC':'B', 'AGC':'S',
'ATA':'J', 'ACA':'T', 'AAA':'K', 'AGA':'R',
'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G',
}
c =''
Boole = False   #use boole to link unknown protein with following DNA sequence.
s=''
for line in dna:
    if line.startswith('>'):
        if Boole==True:
            s = s+('>'+b+'   '+str(len(series))+'\n'+series+'\n')
            c=''
            Boole=False
        if re.findall(r'unknown',line):
            b=re.findall(r'^>.+?_',line)
            b=b[0]
            b=b[:-1]
            Boole=True
    else:
        if Boole==True:
                c=c+line.strip()
                series = ''
                for i in range(0,len(c)-2,3):
                    sery=c[i]+c[i+1]+c[i+2]
                    if code[sery]=='stop':
                        break
                    else:
                        series += code[sery]
dna.close()
z=open('unknown_protein.fa','w')
z.write(s)
z=open('unknown_protein.fa','r')
print(z.read())
z.close()
