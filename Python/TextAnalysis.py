class TextAnalysis():
    text = ''
    
    def __init__(self, filename):
        try:
            myfile = open(filename, 'r', encoding='utf-8')
            self.text = myfile.read()
        except:
            print("Error occured while trying to read file.")
            raise #remove this later
        else:
            myfile.close()

    def getLongestWord(self):
        maxLength = 0;
        tempText = self.text.split(not isdigit() and not isalpha()) #update to deliminate by nonalphanumeric characters
        tempList = []
        #find length of longest word in the file
        for x in tempText:
            if len(x) > maxLength:
                maxLength = len(x)
        #create a list of all the words of length maxLength
        for x in tempText:
            if len(x) == maxLength:
                tempList.append(x)
        return tuple(tempList)
        
