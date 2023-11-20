#Lesson 18 :Recursion
#Recursion means cycle. More precisely it means feeding the answer back into the calculation.

#Example 1 :write a program that prints the calculations in the hailstorm process.
def hailstrom(N):
    if N==1:#This line is very important bcause it is the stop condition,without this it is stuck in a loop
        print("END")#No more hailstorm so it won't continue in tis recursion loop

    elif N%2 ==0:
        N /= 2#Divides N by two, its value is now halved
        print(N)
        hailstrom(N)
    else:
        N = 3*N + 1 #This means N is now 3 times plus 1 of its old value
        print(N)
        hailstrom(N)

hailstrom(77)

#Example 2: write a program using recursion that asks for a number
def askQuestion():
    x=int(input("Give me a number between 1 and 10:"))
    if x >= 1 and x <= 10:
        print("Thank you")
        return(x)
    else:
        print("No , that is not between 1 and 10")
        return(askQuestion())
x=askQuestion()#there is no input needed, because there is no calculation , its not a f(x) like function
print(f"You picked the number{x}")