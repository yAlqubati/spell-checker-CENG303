from levensteinDistance import levensteinDistance

class BKNode:
    def __init__(self, word):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = BKNode(word)
            return
        else:
            temp = self.root
            distance = levensteinDistance(word, temp.word)
            if distance in temp.children:
                self.insert(temp.children[distance], word)
            else:
                temp.children[distance] = BKNode(word)
                return

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
    
