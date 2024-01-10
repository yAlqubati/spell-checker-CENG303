from SpellChecker import SpellChecker

# the parameters are the maximum distance, maximum keyboard distance, and the path to the dictionary file
# you can change them as you like, the higher the distance the more suggestions you will get
spellChecker = SpellChecker(2,3,"dictionary.txt")

inputText = input("Enter your text: ")
spellChecker.output(inputText)





