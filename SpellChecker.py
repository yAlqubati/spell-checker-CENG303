from BKTree import BKTree

class SpellChecker:
    # when initializing we'll insert all the words from the dictionary
    def __init__(self,maxDistance,maxKeyboardDistance, filePath):
        self.tree = BKTree()
        self.maxDistance = maxDistance
        self.maxKeyboardDistance = maxKeyboardDistance
        self.tree.insertFromFile(filePath)

     # this function will return a list of suggestions for the word
    def check(self, word):
        return self.tree.search(word, self.maxDistance, self.maxKeyboardDistance)

    
    # this function will return the corrected text with the suggestions
    def output(self, inputText):

        # split the text into words
        words = inputText.split()
        output = ""

        for word in words:
            suggestions = self.check(word)

            if len(suggestions) == 0:
                print (f'This word "{word}" is not in the dictionary.')

            # if the word is in the dictionary, add it to the output
            elif suggestions[0] == "The word is in the dictionary":
                output += word + " "

            # if the word is not in the dictionary, ask the user to choose a word from the suggestions
            else:
                print(f'This word "{word}" is not valid. choose one of the following:')

                # print every word and the index 
                for i in range(len(suggestions)):
                    print(f"{i+1}. {suggestions[i]}")
                print(f"{len(suggestions)+1}. None of the above")

                # take input from user
                choosen = int(input("Enter the number of the word you want to choose: "))

                # if the user chose none of the above, add the word to the output
                if choosen == len(suggestions)+1:
                    output += word + " "

                # if the user chose a word from the suggestions, add it to the output
                else:
                    output += suggestions[choosen-1] + " "


                print()



        # return the corrected text
        return output
    
    def testFromFile(self,inputFile,outputFile):
        
        words = []
        with open(inputFile, 'r') as f:
            for line in f:
                words.append(line.strip())

        output = ""

        for word in words:
            suggestions = self.check(word)

            

            # if the word is in the dictionary, add it to the output
            if len(suggestions) > 0:
                output += f'This word "{word}" is not valid. here are the suggestions:'
                output += "\n"
                # print every word and the index 
                for i in range(len(suggestions)):
                    output += suggestions[i] + " "

                
                output += "\n"

            # write the output to the file
        with open(outputFile, 'w') as f:
            f.write(output)