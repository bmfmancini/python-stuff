### This code will reverse the letters in the word variable 
word = "hello"


def backward (word):
    index = len(word)
    while index > 0:
        letter = word[index -1]
        print (letter)
        index = index -1 

 
        


backward(word)

