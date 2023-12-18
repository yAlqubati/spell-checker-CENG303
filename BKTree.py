from bisect import bisect_left, bisect_right
from levensteinDistance import levensteinDistance
class BKNode:
    def __init__(self, word):
        self.word = word
        self.children = []  
        self.distances = []  

class BKTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = BKNode(word)
            return
        
        temp = self.root

        while True:
            distance = levensteinDistance(word, temp.word)

            if distance == 0:
                return
            
            elif distance in temp.distances:
                # find the child with the same distance
                child = temp.distances.index(distance)
                temp = temp.children[child]
            else:
                temp.distances.append(distance)
                temp.children.append(BKNode(word))
                break

    def search(self, target, max_distance):
        if self.root is None:
            return []
        
        def search_recursive(node, target, max_distance, results):
            if node is None:
                return

            distance = levensteinDistance(target, node.word)
            
            # if the distance is less than or equal to the max distance then we'll add it to the possible results
            if distance <= max_distance:
                results.append(node.word)

            # we use bisect_left and bisect_right to find the lower and upper bounds of the range of distances
            # we used binary search to improve the performance
            lower_bound = bisect_left(node.distances, distance - max_distance)
            upper_bound = bisect_right(node.distances, distance + max_distance)

            # we repeat the search for all the children in the range of distances
            for i in range(lower_bound, upper_bound):
                search_recursive(node.children[i], target, max_distance, results)

        # Initialize an empty list to store the results.
        results = []

        # Start the recursive search from the root of the tree.
        search_recursive(self.root, target, max_distance, results)
        return results
    
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
                for child in node.children:
                    count(child)
            
            count(self.root)
            return counter
    
    
    def insertFromFile(self,fileName):
            
            # store the words in the dictionary in a list
            with open(fileName) as file:
                # each word will be in a new line
                dictionary = [line.strip() for line in file]
    
            # insert all the words in the dictionary
            for word in dictionary:
                self.insert(word)
