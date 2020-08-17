def reverseWord(sentence):
    word=sentence.split()
    word.reverse()
    return " ".join(word)


userinput=input("enter a sentence: ")
result=reverseWord(userinput)
print(result)