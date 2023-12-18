# just for checking if the word is true or false
# might change the data structure latter to hash or graph
# still need to find suggestions for the word and calculate the edit distance
# please if you'll modify the code add comments to explain what you did
# write a meaningful commit message

# just a test
from BKTree import BKTree
import time

tree = BKTree()

# insert all the words in the dictionary

filePath = "dictionary.txt"

start = time.time()
tree.insertFromFile(filePath)
end = time.time()
print("insertion time: ", end - start)

# search for a word
word = "peankt"
start = time.time()
suggestions = tree.search(word, 2)
end = time.time()
print("search time: ", end - start)
print(suggestions)

i = tree.wordInTree()
print(i)

