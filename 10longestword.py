"""Write a function find_longest_word() that takes a list of words and returns the 
length of the longest one."""
###############################################################################################
def longest(x):
    length=0
    for n in x:
        if length < len(n):
            length=len(n)
    return length

given=['hello','i','am','robot','somuchfunitis']
print(longest(given))