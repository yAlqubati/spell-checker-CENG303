from levensteinDistance import levensteinDistance
# Function calculates the distance between two letters on a QWERTY keyboard 
def keyboardDistance(let1, let2):
    # Define the QWERTY keyboard layout
    keyboardLayout = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    # Finds the coordinates of the letters on the keyboard
    def findCoordinates(letter):
        for row_idx, row in enumerate(keyboardLayout):
            if letter in row:
                col_idx = row.index(letter)
                return row_idx, col_idx

    # Gets coordinates for each letter
    coordinate1 = findCoordinates(let1.lower())
    coordinate2 = findCoordinates(let2.lower())

    if coordinate1 and coordinate2:
        # Checks if the letters are adjacent vertically, horizontally, or diagonally
        diffInRow = abs(coordinate1[0] - coordinate2[0])
        diffInColum = abs(coordinate1[1] - coordinate2[1])
        keyboardDistance = diffInRow + diffInColum
        if diffInRow <= 1 and diffInColum <= 1:
            return 1
        else:
            return keyboardDistance
    else:
        return "Invalid letters. Please provide valid letters from the QWERTY keyboard."



def is_neighbors(let1, let2):
    # Define the QWERTY keyboard layout
    keyboardLayout = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    # Finds the coordinates of the letters on the keyboard
    def findCoordinates(letter):
        for row_idx, row in enumerate(keyboardLayout):
            if letter in row:
                col_idx = row.index(letter)
                return row_idx, col_idx

    # Gets coordinates for each letter
    coordinate1 = findCoordinates(let1.lower())
    coordinate2 = findCoordinates(let2.lower())


    if coordinate1 and coordinate2:
        # Checks if the letters are adjacent vertically, horizontally, or diagonally
        diffInRow = abs(coordinate1[0] - coordinate2[0])
        diffInColum = abs(coordinate1[1] - coordinate2[1])
        

        if diffInRow <= 1 and diffInColum <= 1:
            return True
        else:
            return False
    else:
        return "Invalid letters. Please provide valid letters from the QWERTY keyboard."


def getWordDistance(source, target):

    if levensteinDistance(source, target) == 1:
        return 1
    # Define the QWERTY keyboard layout
    keyboardLayout = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    if canSwapLetter(source, target):
        return 1
    
    distance = 0
    length = min(len(source), len(target))

    for i in range(length):
        if source[i] != target[i]:
            distance += keyboardDistance(source[i], target[i])
    
    return distance


def canSwapLetter(word, correctWord):
    # Define the QWERTY keyboard layout
    keyboardLayout = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    for i in range(len(word)):
        for j in range(len(word)):
            # if i and j have a difference swap them and check if the word is equal to the correct word
            if i != j:
                temp = list(word)
                temp[i], temp[j] = temp[j], temp[i]
                temp = ''.join(temp)
                if temp == correctWord:
                    return True
    
    return False


# Example usage:
'''
#Test the distance between two letters on the keyboard
letter1 = 'q'
letter2 = 'k'
result = keyboardDistance(letter1, letter2)
print(f"The distance between {letter1} and {letter2} on the keyboard is: {result}")

# Test the distance between two letters on the keyboard
letter1 = 'a'
letter2 = 'w'
result = keyboardDistance(letter1, letter2)
print(f"The distance between {letter1} and {letter2} on the keyboard is: {result}")

# Test if two letters are neighbors on the keyboard
let1 = 'q'
let2 = 'k'
result = is_neighbors(let1, let2)
print(f"Are {let1} and {let2} neighbors on the keyboard? {result}")

# Test if two letters are neighbors on the keyboard
let1 = 'l'
let2 = 'p'
result = is_neighbors(let1, let2)
print(f"Are {let1} and {let2} neighbors on the keyboard? {result}")

'''