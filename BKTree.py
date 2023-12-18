from collections import deque
from levensteinDistance import levensteinDistance
from keyBoardDistance import getWordDistance

class BKNode:
    def __init__(self, word):
        self.word = word
        self.distances = []
        # dictionary of children nodes, where the key is the distance
        self.children = {}

class BKTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        # If the tree is empty, create a root node
        if self.root is None:
            self.root = BKNode(word)
            return

        temp = self.root

        while True:
            distance = levensteinDistance(word, temp.word)

            # If the word is already in the tree, return
            if distance == 0:
                return
            
            # If the distance is already in the list of distances, go to the child node
            if distance in temp.distances:
                temp = temp.children[distance]
                continue

            # If the distance is not in the list of distances, add it to the list and create a child node
            temp.distances.append(distance)
            temp.children[distance] = BKNode(word)
            break

    def search(self, word, max_distance):
        if self.root is None:
            return []
        
        results = []
        container = deque([self.root])

        # BFS, while the container is not empty
        while container:
            # pop the first element in the container and check if it is in the range
            temp = container.popleft()
            distance = levensteinDistance(word, temp.word)

            if distance == 0:
                results.clear()
                results.append("The word is in the dictionary")
                return results

            # If the distance is in the range, add the word to the results
            if distance <= max_distance:
                results.append(temp.word)

            lower_bound = distance - max_distance
            upper_bound = distance + max_distance

            # Add the children of the node to the container if they are in the range
            container.extend(child for distance, child in temp.children.items() if lower_bound <= distance <= upper_bound)

        finalResults = []

        for suggestion in results:
            if getWordDistance(word, suggestion) <= max_distance:
                finalResults.append(suggestion)
        return finalResults

    def wordInTree(self):
        counter = 0
        if self.root is None:
            return counter
        else:
            def count(node):
                nonlocal counter  # Declare counter as a nonlocal variable
                if node is None:
                    return
                counter += 1
                for child in node.children.values():
                    count(child)
            
            count(self.root)
            return counter
    
    def insertFromFile(self, fileName):
        # store the words in the dictionary in a list
        with open(fileName) as file:
            # each word will be in a new line
            dictionary = [line.strip() for line in file]

        # insert all the words in the dictionary
        for word in dictionary:
            self.insert(word)

