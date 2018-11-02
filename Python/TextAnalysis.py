##Blake Richey
##This program reads input from a file passed into the Class and has methods to query the data.

class TextAnalysis():
    text = ''
    
    def __init__(self, filename):
        try:
            myfile = open(filename, 'r', encoding='utf-8')
            self.text = myfile.read()
        except:
            print("Error occured while trying to read file.")
        else:
            myfile.close()
    
    #find length of longest word(s) in the file and return a tuple containing them
    def getLongestWord(self):
        maxLength = 0
        tempText = self.text
        longestWords = []
        wordsList = []
        
        #replace text nonalphanumeric characters with a white space and then split the words into a list
        #using a space as a delimeter.
        for x in range(0, len(tempText)):
            if(not(tempText[x].isalnum())):
                tempText = tempText[:x] + " " + tempText[x+1:] #replace nonalnum's with a space
        wordsList = tempText.split()
        
        #find length of longest word in the file
        for x in wordsList:
            if len(x) > maxLength:
                maxLength = len(x)
        
        #create a list of all the words of length maxLength
        for x in wordsList:
            if len(x) == maxLength:
                longestWords.append(x)
        return tuple(longestWords)

    def getMostUsedWords(self, length):
        tempText = self.text.lower()
        desiredWords = []
        wordsList = []

        #replace text nonalphanumeric characters with a white space and then split the words into a list
        #using a space as a delimeter.
        for x in range(0, len(tempText)):
            if(not(tempText[x].isalnum())):
                tempText = tempText[:x] + " " + tempText[x+1:] #replace nonalnum's with a space
        wordsList = tempText.split()

        #create a list of all the words of length 'length'
        for x in wordsList:
            if len(x) == length:
                desiredWords.append(x)

        #generates list of each unique word of length 'length'
        uniqueWords = []
        for x in desiredWords:
            if x not in uniqueWords:
                uniqueWords.append(x)

        #counts instances of each unique word of length 'length'
        ans = []
        maxCount = 0 #variable to keep up with greatest frequency 

        #finds frequency of most used word(s)
        for x in uniqueWords:
            if desiredWords.count(x) > maxCount:
                maxCount = desiredWords.count(x)
        if maxCount > 0:
            ans.append(maxCount)
        elif maxCount == 0:
            return "No words in file that are length " + str(length)

        #finds all words with frequency found in previous few lines, maxCount
        for x in uniqueWords:
            if desiredWords.count(x) == maxCount:
                ans.append(x)
        return tuple(ans)
        

        

    
