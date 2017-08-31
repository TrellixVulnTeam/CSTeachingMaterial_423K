import pydoc
"""This is what we want. how does TDD drive mosularity, see below

##bingoarr = ['b', 'i', 'n', 'g', 'o']
##
##print(bingoarr)
##i = 0
##while(i < len(bingoarr)):
##    bingoarr[i] = 'clap'
##    print(bingoarr)
##    i=i+1
"""

#Article for "self" - https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/

"""Class for all aspects for printing BingoRhyme"""
class BingoGame:
    #variables declared here are class variables
    
    """constructor to initialize the member variables"""
    def __init__(self):
        self.bingoarr = ['b', 'i', 'n', 'g', 'o']
        self.printstr = []
    """Function to get the length of the array - which is always 5 in our case"""
    def bingoarrlen(self):
        return len(self.bingoarr)
    """Function to return an element in the array given the index"""
    def bingoarray(self, i):
        return self.bingoarr[i]
    """Function to store the rhyme in printstr"""
    def bingorhyme(self):
        i = 0
        #This is a reference
        #printstr = self.bingoarr
        #2 ways below to make copy
        #printstr = self.bingoarr[:]
        printstr = list(self.bingoarr)
        #print(self.bingoarrlen())
        while(i < self.bingoarrlen()):
            self.bingoarr[i] = 'clap'
            printstr = list(self.bingoarr)
            i=i+1
            self.printstr.append(printstr)
            printstr = []
        #print(self.printstr)
    """private function directive to get the printable string - can be accessed outside"""
    def __getprintstr__(self):
        return self.printstr
    """Print the string"""
    def printbingorhyme(self):
        print(self.__getprintstr__())

#If we are running the code as is and not from a module
if __name__ == '__main__':
    bingo =  BingoGame()
    bingo.bingorhyme()
    bingo.printbingorhyme()
    
