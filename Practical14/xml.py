from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

def parse_xml(path):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    terms = collection.getElementsByTagName("term")
    return terms

def get_primary_matches(terms, molecule_name):
    match_list = []
    for term in terms:
        defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
        data = defstr_text.data
        if molecule_name in data:
            match_list.append(term)
    return match_list

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
               + str([x.id for x in self.connectedTo])

    def getConnection(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

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

def buildTree(terms):
    tree = Graph()
    for term in terms:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        for child in is_a:
            tree.addEdge(id, child)
    return tree

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

def count_childNodes_macromolecules_xml(tree, molecule_name):
    match_list = get_primary_matches(terms, molecule_name)
    vertices_list = [tree.getVertex(term.getElementsByTagName("id")[0].childNodes[0].data) for term in match_list]
    count = len(list(set(getAllChildren(tree, vertices_list)))) - len(match_list)
    return count

path = "C:/Users/11877/github/IBI1_2020-21/Practical14/go_obo.xml"

terms = parse_xml(path)

tree = buildTree(terms)

dna = count_childNodes_macromolecules_xml(tree, "DNA")  # 7271
rna = count_childNodes_macromolecules_xml(tree, "RNA")  # 8927
protein = count_childNodes_macromolecules_xml(tree, "protein")  # 27771
carbo = count_childNodes_macromolecules_xml(tree, "carbohydrate")  # 4743

print("Number of childNodes of all DNA-associated terms: {}".format(dna))
print("Number of childNodes of all RNA-associated terms: {}".format(rna))
print("Number of childNodes of all protein-associated terms: {}".format(protein))
print("Number of childNodes of all carbohydrate-associated terms: {}".format(carbo))

# Plot the pie chart
data = {"DNA": dna, "RNA": rna,
        "Protein": protein, "Carbohydrate": carbo}
values = np.array([i for i in data.values()])
labels = np.array([j for j in data.keys()])
plt.pie(values, labels=labels, shadow=True, autopct='%1.1f%%')
plt.title("Child Nodes of 4 macromolecules")
plt.show()
