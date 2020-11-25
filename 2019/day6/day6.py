class treeNode:
    def addChild(self, child):
        self.children.append(child)
    
    def __init__(self, inputName):
        self.name = inputName
        self.parent = None
        self.children = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
def addToTree(tree, object1, object2):
    node1 = None
    node2 = None
    if object1 not in tree:
        node1 = treeNode(object1)
    else:
        node1 = tree[object1]
    if object2 not in tree:
        node2 = treeNode(object2)
    else:
        node2 = tree[object2]
    node1.addChild(node2)
    node2.parent = node1
    tree[object1] = node1
    tree[object2] = node2

def numberOfParents(node, parent):
    sum = 0
    while node.parent is not parent:
        sum += 1
        node = node.parent
    return sum

def countNumOrbits(tree):
    sum = 0
    for key,value in tree.items():
        sum += numberOfParents(value, None)
    return sum

def findLowestAncestor(node1, node2):
    node1Ancestors = []
    while node1.parent is not None:
        node1Ancestors.append(node1.parent)
        node1 = node1.parent
    while node2.parent is not None:
        if node2.parent in node1Ancestors:
            return node2.parent
        node2 = node2.parent
    return None
        

def countTransfers(node1, node2):
    lca = findLowestAncestor(node1, node2)
    return numberOfParents(node1, lca) + numberOfParents(node2, lca)

if __name__ == '__main__':
    tree = {}
    with open('input.txt') as f:
        for i in f:
            i = i.strip('\n')
            i = i.split(')')
            addToTree(tree, i[0], i[1])
    print(countNumOrbits(tree))
    print(countTransfers(tree['YOU'],tree['SAN']))
        
        
