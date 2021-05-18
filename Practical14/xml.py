from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

# parsing xml file
def parse(path):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    terms = collection.getElementsByTagName("term")
    return terms

#  getting the parent nodes (molecule_name in <defstr> of the parent nodes)
def get_primary_matches(terms, molecule_name):
    list = []
    for term in terms:
        defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
        data = defstr_text.data
        if molecule_name in data:
            list.append(term)
    return list

# define classes Vertex and Graph to structurize terms
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected = {}

    def addNeighbor(self, nbr, weight=0):
        self.connected[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
               + str([x.id for x in self.connected])

    def getConnection(self):
        return self.connected.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connected[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# build tree of terms
def Tree(terms):
    tree = Graph()
    for term in terms:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        for child in is_a:
            tree.addEdge(id, child)
    return tree

# assistant recursive function to find all childNodes as vertices
def getAllChildren(tree, vertices):
    allChildren = []
    for vertex in vertices:
        if vertex:
            if not vertex.connectedTo:
                allChildren.append(vertex)
            else:
                children = [vtx for vtx in vertex.connectedTo]
                allChildren.append(vertex)
                allChildren += getAllChildren(tree, children)
    return allChildren

# main function outputting the final result
def count_macromolecules(tree, molecule_name):
    list = get_primary_matches(terms, molecule_name)
    vertices_list = [tree.getVertex(term.getElementsByTagName("id")[0].childNodes[0].data) for term in list]
    count = len(list(set(getAllChildren(tree, vertices_list)))) - len(list)
    return count

# direct absolute path
path = "C:/Users/11877/github/IBI1_2020-21/Practical14/go_obo.xml"

# Parse the xml file
terms = parse(path)

# build tree
tree = Tree(terms)

# Calculate number of each term
dna = count_macromolecules(tree, "DNA")
rna = count_macromolecules(tree, "RNA")
protein = count_macromolecules(tree, "protein")
carbo = count_macromolecules(tree, "carbohydrate")

print("Number of DNA-associated terms: {}".format(dna))
print("Number of RNA-associated terms: {}".format(rna))
print("Number of protein-associated terms: {}".format(protein))
print("Number of carbohydrate-associated terms: {}".format(carbo))

# draw the pie chart
data = {"DNA": dna, "RNA": rna,
        "Protein": protein, "Carbohydrate": carbo}
values = np.array([i for i in data.values()])
labels = np.array([j for j in data.keys()])
plt.pie(values, labels=labels, shadow=True, autopct='%1.1f%%')
plt.title("proportion of 4 macromolecules")
plt.show()
