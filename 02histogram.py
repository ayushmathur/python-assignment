# Define a procedure histogram() that takes a list of integers 
# and prints a histogram to the screen

############################################################################################################
def histogram(array): #Histogram function which prints * as many times as the values in the passed array
    """A histogram function"""
    for x in range (0,len(array)):
        print ('*' * array[x])
    return
array=[]
num=int(input("Enter length of array: ")) 
for n in range(num):                    #Loop to take user inputs of values in array
    inp=int(input("Enter the element : "))
    array.append(inp)
histogram(array)