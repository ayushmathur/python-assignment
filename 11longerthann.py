"""Write a function filter_long_words() that takes a list of words and an integer n 
and returns the list of words that are longer than n"""
################################################################################################

def filter_long_words(words,n):
    longerwords=[]
    for x in words:
        if len(x) > n:
            longerwords.append(x)
    return longerwords

given=['hello','i','am','robot','somuchfunitis']
print(filter_long_words(given,4))