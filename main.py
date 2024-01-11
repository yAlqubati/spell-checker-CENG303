from SpellChecker import SpellChecker

# the parameters are the maximum distance, maximum keyboard distance, and the path to the dictionary file
# you can change them as you like, the higher the distance the more suggestions you will get
spellChecker = SpellChecker(2,3,"dictionary.txt")

inputText = input("Enter your text: ")
spellChecker.output(inputText)

# if you want to test the spell checker from a file, uncomment the following line
# you can change the input and output files as you like
#spellChecker.testFromFile("testInput.txt", "testOutput.txt")



