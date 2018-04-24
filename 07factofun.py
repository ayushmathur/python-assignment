"""Write a program that contains a function that has one parameter, n, representing an integer 
greater than 0. The function should return n! (n factorial). Then write a main function that 
calls this function with the values 1 through 20, one at a time, printing the returned results."""
##################################################################################################
def factorial(n):    # Function to find factorial of any number
    r=1
    if n <= 0:
        return 0
    else:
        for x in range(1,(n+1)):
            r= r*x
    return r

def main():     # Main function to find factorial of numbers 0-20
    for x in range(1,21):
        print(str(x)+" "+str(factorial(x)))

main()