class BKNode:
    def __init__(self,word):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self):
        """
        Initializes a new instance of the BKTree class.

        """
        self.root = None

    # to insert one word into the tree in a recursive way
    def insert(self, word):
            """
            Inserts a word into the BKTree.

            Parameters:
            word (str): The word will be inserted in the tree.

            Returns: None 
            """
            # if the tree is empty
            if self.root is None:
                self.root = BKNode(word)
                return
            
            else:
                
                # use a temp node to traverse the tree
                temp = self.root
                # calculate the edit distance between the new word and the root(need to be implemented)
                distance = 10 # temp value we'll change it later

                #check if that distance is already in the children of the root
                if distance in temp.children:
                    # if its already there we'll go to that node and insert the word there
                    self.insert(temp.children[distance], word)
                
                # if the distance is not in the children of the root we'll add it
                else:
                    temp.children[distance] = BKNode(word)
                    return

    # to insert one word into the tree in a recursive way
    
