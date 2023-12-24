from BKTree import BKTree

class SpellChecker:
 # when initializing we'll insert all the words from the dictionary
    def _init_(self,maxDistance,maxKeyboardDistance, filePath):
        self.tree = BKTree()
        self.maxDistance = maxDistance
        self.maxKeyboardDistance = maxKeyboardDistance
        self.tree.insertFromFile(filePath)

     # this function will return a list of suggestions for the word
    def check(self, word):
        return self.tree.search(word, self.maxDistance, self.maxKeyboardDistance)

    