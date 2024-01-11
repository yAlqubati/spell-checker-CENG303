## Spell Checker Project

### Contributors

- **Hasan Bera KABADAĞI 19050111006**

- **ABDULKAREEM AL-SARORI 19050141018**

- **Yahya Elimam 20050141048**

- **Yousef Saif 21050141023**

This project is a spell checker that utilizes a BK-tree to identify the closest word to a misspelled word. It employs Levenshtein distance (dynamic programming) and QWERTY keyboard distance for efficient word comparisons.

### How to Run

1. Ensure that all project files are in the same directory.
2. Run the `main.py` file.
   - Alternatively, execute `python main.py` from the terminal.

The program's loading time for the dictionary and tree construction is dependent on your computer's speed. After loading, you can input a word. If the word is not found in the dictionary, the program will suggest the closest match. You might enter a word not in the dictionary, as the dictionary contains 5000 words. Detailed instructions will be displayed on the screen.

### Implementation Details

- **BK-Tree Usage:**
  - The BK-tree efficiently stores the dictionary, facilitating quick searches due to its insertion mechanism.
  - Words are inserted into the tree based on Levenshtein distance, optimizing the search process.
  - During a search for a misspelled word, only 15%-20% of the words in the tree need to be visited.

- **Levenshtein Distance:**
  - Dynamic programming is employed to implement Levenshtein distance, ensuring optimal performance.
  
- **QWERTY Keyboard Distance:**
  - QWERTY keyboard distance is considered during word comparisons to enhance the spell-checking accuracy.

### Performance

The BK-tree, dynamic programming in Levenshtein distance, and QWERTY keyboard distance contribute to the project's efficient performance. The search process is streamlined, and the use of dynamic programming ensures that the Levenshtein distance is computed effectively.
