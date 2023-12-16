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
        # If there is no element in the tree return empty list.
        if self.root is None:
            return []

        def search_recursive(node, target, max_distance, results):
        # If the current node is None, return.
            if node is None:
                return

            # Calculate the Levenshtein distance between the target word and the current node's word.
            distance = levensteinDistance(target, node.word)

            # If the calculated distance is within the allowed max_distance, add the word to the results list.
            if distance <= max_distance:
                results.append(node.word)

            # Determine the lower and upper bounds for child nodes to visit.
            lower_bound = distance - max_distance
            upper_bound = distance + max_distance

            # Iterate through the range from lower_bound to upper_bound.
            for d in range(lower_bound, upper_bound + 1):
                # If the current distance 'd' exists in the children of the node,
                # recursively call this function on the child node.
                if d in node.children:
                    search_recursive(node.children[d], target, max_distance, results)

        # Initialize an empty list to store the results.
        results = []

        # Start the recursive search from the root of the tree.
        search_recursive(self.root, target, max_distance, results)

        # Return the list of words that stored.
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
