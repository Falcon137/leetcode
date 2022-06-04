class Trie:

    def __init__(self):
        self.root = Trie_Node()
        

    def insert(self, word: str) -> None:
        self.insert_helper(self.root,word)
    
    def insert_helper(self,node,word):
        if word == '':
            node.isWord = True
            return
        
        if word[0] not in node.next:
            node.next[word[0]] = Trie_Node()
            
        self.insert_helper(node.next[word[0]],word[1:])
        
        

    def search(self, word: str) -> bool:
        return self.search_helper(self.root,word)
    
    def search_helper(self,node,word):
        if word == '':
            return node.isWord
        
        if word[0] not in node.next:
            return False
        else:
            return self.search_helper(node.next[word[0]],word[1:])
            
        

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithHelper(self.root,prefix)
    
    def startsWithHelper(self,node,prefix):
        if prefix == '':
            return True
        
        if prefix[0] not in node.next:
            return False
        else:
            return self.startsWithHelper(node.next[prefix[0]],prefix[1:])
        
class Trie_Node:
    def __init__(self):
        self.isWord = False
        self.next = {}
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)