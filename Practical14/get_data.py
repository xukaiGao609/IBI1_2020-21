from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
path = "C:/Users/11877/github/IBI1_2020-21/Practical14/go_obo.xml"
DOMTree = xml.dom.minidom.parse(path)
root = DOMTree.documentElement
terms = root.getElementsByTagName('term')

# create a dictionary to store the GO terms
def dictionary(terms):
    dict = {}
    for term in terms:
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        all_id = term.getElementsByTagName("id")[0].childNodes[0].data
        for fa_id in is_a:
            if not fa_id in dict:
                dict[fa_id] = [all_id]
            else:
                dict[fa_id].append(all_id)
    return dict

# find id of a specific biomolecules
def find(terms,molecule):
    gene = []
    for term in terms:
        # search the identified information
        defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data
        id_related = term.getElementsByTagName("id")[0].childNodes[0].data
        if not molecule.isupper():  # prevent missing capital version
            defstr = defstr.lower()
        if molecule in defstr:
            gene.append(id_related)
    return set(gene)  # delete repeated things

# use recursive method to save all the chilnodes
def get_all_chilnodes(dict,lists):
    all = []
    for f in lists:
        if f in dict:
            child = dict[f]
            all += child
            all += get_all_chilnodes(dict,child)
    return all

# count the childnodes
def count_childnodes(terms,molecule):
    dicts = dictionary(terms)
    match = find(terms,molecule)
    all_childnodes = get_all_chilnodes(dicts,match)
    num = len(set(all_childnodes))
    return num


# the molecules are DNA, RNA, Protein, and Glycoprotein. Use the function and print the results.
DNA = count_childnodes(terms,"DNA")
RNA = count_childnodes(terms,"RNA")
Protein = count_childnodes(terms,"protein")
Carbohydrate = count_childnodes(terms,"carbohydrate")

print("The number of childNodes of all DNA-associated terms:",DNA)
print("The number of childNodes of all RNA-associated terms:",RNA)
print("The number of childNodes of all protein-associated terms:",Protein)
print("The number of childNodes of all carbohydrate-associated terms:",Carbohydrate)

labels='DNA', 'RNA', 'Protein', 'Carbohydrate'
sizes=[DNA, RNA, Protein, Carbohydrate]
explode=(0, 0, 0, 0)
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.title('the proportion of childNodes associated with DNA, RNA, protein and carbohydrate')
plt.show()
