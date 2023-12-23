# need to make a separate class to manage the input and output

# just a test
from BKTree import BKTree
import time
from levensteinDistance import levensteinDistance
from keyBoardDistance import getWordDistance

tree = BKTree()

# insert all the words in the dictionary

filePath = "dictionary.txt"

start = time.time()
tree.insertFromFile(filePath)
end = time.time()
print("insertion time: ", end - start)

# search for a word
word = "presidnecy"
start = time.time()
suggestions = tree.search(word, 2,3)
end = time.time()
print("search time: ", end - start)
print(suggestions)

i = tree.wordInTree()
print(i)
print(getWordDistance("accept", "acneptable"))




