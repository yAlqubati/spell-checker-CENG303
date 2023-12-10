class TrieNode:
    def __init__(self,char = None):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self,word):
        current = self.root
        
        #travel through the trie
        for char in word:
            # if the letter is in the trie we move to the next node
            if char in current.children:
                current = current.children[char]

            # if the letter is not in the trie we add it
            else:
                new_node = TrieNode(char)
                current.children[char] = new_node
                current = new_node

        # mark the end of the word
        current.word_finished = True

    def search(self,word):

        current = self.root

        # travel through the trie
        for char in word:
            # if the letter is in the trie we move to the next node
            if char in current.children:
                current = current.children[char]

            # if the letter is not in the trie we return false
            else:
                return False
            
        # if we reach the end of the word we return true
        if current.word_finished == True:
            return True