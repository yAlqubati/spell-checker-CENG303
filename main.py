# just for checking if the word is true or false
# might change the data structure latter to hash or graph
# still need to find suggestions for the word and calculate the edit distance
# please if you'll modify the code add comments to explain what you did
# write a meaningful commit message

# just a test
from Trie import Trie

# create a trie
trie = Trie()

# read the file and insert the words into the trie
with open('dictionary.txt','r') as f:
    for line in f:
        word = line.strip()
        trie.insert(word)

# read the file and search the words in the trie
print(trie.search('imagination'))