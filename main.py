# just for checking if the word is true or false
# might change the data structure latter to hash or graph
# still need to find suggestions for the word and calculate the edit distance
# please if you'll modify the code add comments to explain what you did
# write a meaningful commit message

# just a test
from BKTree import BKTree
from BKTree import BKNode

tree = BKTree()
tree.insert("hello")
tree.insert("hi")
tree.insert("hola")
tree.insert("bye")

print(tree.search("bya",1))




