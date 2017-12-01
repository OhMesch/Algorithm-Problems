# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"]. 

class GraphNode():
    def __init__(self,word):
        self.word = word
        self.children = []
        self.group = None

    def add_connection(self,other_node):
        self.children.append(other_node)

    def set_group(self, group):
        self.group = group

    def get_children(self):
        return(self.children)

    def get_word(self):
        return(self.word)

    def get_group(self):
        return(self.group)


class Solution(object):
    def __init__(self):
        self.visited = {}

    def connect_nodes(self,node1,node2):
        node1.add_connection(node2)
        node2.add_connection(node1)

    def DSF_group(self, node, group):
        self.visited[node] = 1
        node.set_group(group)

        for additional_node in node.get_children():
            if additional_node not in self.visited:
                self.DSF_group(additional_node,group)

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return(False)

        node_key = {}
        all_nodes = []
        for p1,p2 in pairs:
            if p1 not in node_key:
                node_key[p1] = GraphNode(p1)
                all_nodes.append(node_key[p1])

            if p2 not in node_key:
                node_key[p2] = GraphNode(p2)
                all_nodes.append(node_key[p2])
                
            if p1 != p2:
                self.connect_nodes(node_key[p1],node_key[p2])

        gp = 0
        for node in all_nodes:
            if node not in self.visited:
                self.DSF_group(node,gp)
                gp+=1

        for w1,w2 in zip(words1,words2):
            if w1 != w2:
                if (w1 not in node_key or w2 not in node_key) or node_key[w1].get_group() != node_key[w2].get_group():  
                    return(False)
        return(True)


# driver = Solution()
# print("\n")

# print('1')
# print('**',driver.areSentencesSimilarTwo(["great"],["great"],[]))
# print('-- True\n')

# print('2')
# print('**',driver.areSentencesSimilarTwo(["great","acting","skills"],["fine","drama","talent"],[["great","fine"],["drama","acting"],["skills","talent"]]))
# print('-- True\n')

# print('3')
# print('**',driver.areSentencesSimilarTwo(["great","cat","skills"],["fine","drama","talent"],[["great","fine"],["drama","acting"],["skills","talent"],["cat","cat"]]))
# print('-- False\n')

# print('4')
# print('**',driver.areSentencesSimilarTwo(["great","acting","skills"],["fine","drama","talent"],[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]))
# print('-- True\n')

# print('5')
# print('**',driver.areSentencesSimilarTwo(["this","summer","thomas","get","really","very","rich","and","have","any","actually","wonderful","and","good","truck","every","morning","he","drives","an","extraordinary","truck","around","the","nice","city","to","eat","some","extremely","extraordinary","food","as","his","meal","but","he","only","entertain","an","few","well","fruits","as","single","lunch","he","wants","to","eat","single","single","and","really","healthy","life"]
# ,["this","summer","thomas","get","very","extremely","rich","and","possess","the","actually","great","and","wonderful","vehicle","every","morning","he","drives","unique","extraordinary","automobile","around","unique","fine","city","to","drink","single","extremely","nice","meal","as","his","super","but","he","only","entertain","a","few","extraordinary","food","as","some","brunch","he","wants","to","take","any","some","and","really","healthy","life"]
# ,[["good","wonderful"],["nice","well"],["fine","extraordinary"],["excellent","good"],["wonderful","nice"],["well","fine"],["extraordinary","excellent"],["great","wonderful"],["one","the"],["a","unique"],["single","some"],["an","one"],["the","a"],["unique","single"],["some","an"],["any","the"],["car","wagon"],["vehicle","car"],["auto","vehicle"],["automobile","auto"],["wagon","automobile"],["truck","wagon"],["have","have"],["take","take"],["eat","eat"],["drink","drink"],["entertain","entertain"],["meal","food"],["lunch","breakfast"],["super","brunch"],["dinner","meal"],["food","lunch"],["breakfast","super"],["brunch","dinner"],["fruits","food"],["own","own"],["have","have"],["keep","keep"],["possess","own"],["very","very"],["super","super"],["really","really"],["actually","actually"],["extremely","extremely"]]))
# print('-- False\n')