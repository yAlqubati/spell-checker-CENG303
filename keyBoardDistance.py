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
        # Calculates the distance as the sum of the absolute value of the differences in row and column indices
        distance = abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])
        return distance
    else:
        return "Invalid letters. Please provide valid letters from the QWERTY keyboard."



# Function checks if the letters are next to each other on the keyboard
def is_neighbors(letter1, letter2):
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
        # Calculates the distance as the sum of the absolute value of the differences in row and column indices
        distance = abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])
        if distance < 2:
            return True
        else:
            return False
    else:
        return "Invalid letters. Please provide valid letters from the QWERTY keyboard."





# Example usage:

#Test the distance between two letters on the keyboard
letter1 = 'q'
letter2 = 'k'
result = keyboardDistance(letter1, letter2)
print(f"The distance between {letter1} and {letter2} on the keyboard is: {result}")

# Test the distance between two letters on the keyboard
letter1 = 'q'
letter2 = 'w'
result = keyboardDistance(letter1, letter2)
print(f"The distance between {letter1} and {letter2} on the keyboard is: {result}")

# Test if two letters are neighbors on the keyboard
let1 = 'q'
let2 = 'k'
result = is_neighbors(let1, let2)
print(f"Are {let1} and {let2} neighbors on the keyboard? {result}")

# Test if two letters are neighbors on the keyboard
let1 = 'q'
let2 = 'w'
result = is_neighbors(let1, let2)
print(f"Are {let1} and {let2} neighbors on the keyboard? {result}")



