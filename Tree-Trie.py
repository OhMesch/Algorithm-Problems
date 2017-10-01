class TrieNode():
    def __init__(self, x = '$', count = 0):
        self.letter = x
        self.count = count
        self.lookup = {}
        self.children = []

    def addChild(self, node_val):
        index = len(self.children)
        self.lookup[node_val]=index
        self.children.append(TrieNode(node_val))

    def getLookup(self):
        return(self.lookup)

    def getNode(self,val):
        return(self.children[self.lookup[val]])


class Trei(object):
    def __init__(self):
        self.root = TrieNode()

    def printTrie(self):
        queue = [self.root]
        tree = []
        while len(queue) > 0:
            newQueue = []
            row =[]
            num = False
            for elm in queue:
                if elm == None:
                    row.append(None)
                    newQueue.extend([None,None])
                else:
                    num = True
                    current = elm
                    row.append(current.letter)
                    for child in current.children:
                        newQueue.append(child)

            if num == False:
                break
            queue = newQueue
            tree.append(row)
        print(tree)

    def add(self,word):
        r = 0
        node = self.root
        while r < len(word):
            all_keys = node.getLookup()
            if word[r] not in all_keys:
                node.addChild(word[r])
            node = node.getNode(word[r])
            r+=1


# Add children
# trieNodeDriver = TrieNode()
# print(trieNodeDriver.children)
# trieNodeDriver.addChild('a')
# for child in trieNodeDriver.children:
#     print(child.letter)

# Test Add and Print
# driver = Trei()
# driver.printTrie()
# driver.add('catfish')
# driver.add('cat')
# driver.add('catterbug')
# driver.add('fish')
# driver.add('chogath')
# driver.add('chat')
# driver.add('right')
# driver.add('champ')
# driver.printTrie()