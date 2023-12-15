def levensteinDistance(word1, word2):
    # Create a matrix of zeros
    rows = len(word1) + 1
    cols = len(word2) + 1
    
    # Initialize a 2D array to store the distances for adding, deleting, and replacing characters, initialize with 0s
    distances = [[0 for _ in range(cols)] for _ in range(rows)]

    # Populate the first row and column with the index of each character
    for row in range(rows):
        distances[row][0] = row
    for col in range(cols):
        distances[0][col] = col

    # Iterate over the matrix to compute the cost of each operation
    for col in range(1, cols):
        for row in range(1, rows):
            # If the characters are the same in the two strings in a given position then the cost is 0
            if word1[row - 1] == word2[col - 1]:
                distances[row][col] = distances[row - 1][col - 1]
            else:
                # for add, delete, replace respectively
                add = distances[row][col - 1]
                delete = distances[row - 1][col]
                replace = distances[row - 1][col - 1]
                # Get the minimum of the three operations
                distances[row][col] = 1 + min(add, delete, replace)

    # Return the edit distance between the two words
    return distances[row][col]

# Test cases
print(levensteinDistance("kitten", "sitting")) # 3
print(levensteinDistance("rosettacode", "raisethysword")) # 8
print(levensteinDistance("cool", "aool")) # 1