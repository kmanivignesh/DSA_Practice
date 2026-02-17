class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self , word):
        curr = self.root
        for i in word:
            if not i in curr.children:
                   curr.children[i] = Node()
            curr = curr.children[i]
        curr.eow = True

    def search(self , word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.eow
    
    def Prefix(self , prefix):
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr     

    def autocomplete(self , word):
        if not self.Prefix(word):
            return "Not An Prefix"
        curr = self.Prefix(word)
        result = []
        def dfs(curr , word , result):
            if curr.eow:
                result.append(word)
            for i,node in curr.children.items():
                dfs(node , word + i , result)

        dfs(curr , word , result)
        return result 


trie = Trie()
trie.insert("Vignesh")
trie.insert("Mani")
trie.insert("Venkat")
print(trie.search("Ven"))
print(trie.search("Venkat"))
trie.insert("apple")
trie.insert("app")
trie.insert("apron")
print(trie.autocomplete("ap"))