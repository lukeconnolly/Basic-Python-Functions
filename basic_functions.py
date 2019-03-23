#Luke Connolly
#100999531

#Question 1
def greeting():
    '''This function prompts the user for their name and birth year, then
     prints their name and age.'''
    name=raw_input("Please enter your name. ")      #prompts for name
    birth=raw_input("What is your birth year? ")     #prompts for birthyear
    birth=int(birth)         #turns birthyear to integer for calculuations
    print("Hey "+name+", I'm %d old as well!"%(2015-birth))#calculates and gives message






#Question 2
def ctof(t):
    '''This function takes the celsius temperature as a parameter and returns
     the corresponding fahrenheit temperature.'''
    ftemp=(t*1.8+32) #sets variable that = celsius temp with conversion factor
    return ftemp    #returns fahrenheit temperature






#Question 3
def ftoc():
    '''This function prompts the user for a fahrenheir temperature, then
        returns the corresponding celsius temperature.'''
    ftemp=raw_input("What is the temperature in fahrenheit? ")#prompts user
    ftemp=float(ftemp)          #converts input to float for calculation
    ctemp=(ftemp-32)/1.8         #converts fahrenheit to celsius
    return round(ctemp,2)         #returns celsius temperature







#Question 4
def tipCalculator(bill,percentage):
    '''This function takes the cost of a bill and percent of a tip as parameters
     then tells the user the total cost and cost of the tip.'''
    x=bill              #sets variable as bill cost for calculations
    y=percentage*100     #sets another variable to display tip %
    z=x*(percentage+1)    #calculaes bill total
    print("Your total amount to pay on a $%.2f bill with a %.1f%% tip is $%.2f."%(x,y,z))
    print("The tip is $%.2f"%(z-x)) #prints statements about the bill total and tip cost





#Question 5
def calculate():
    '''This function prompts the user for 2 differnet numbers, which must be integers.
     It then calculates and displays the sum and product of the 2 numbers.'''
    x=raw_input("Enter a number: ")     #prompts user for a number
    x=int(x)                             #converts input to integer
    y=raw_input("Enter a second number ")  #prompts user for another number
    y=int(y)                             #converts other input to integer
    print("%d + %d = %d"%(x,y,x+y))     #prints addition calculation
    print("%d * %d = %d"%(x,y,x*y))      #prints multiplication calculation





'''Code testing:

>>> greeting()
Please enter your name. Luke
What is your birth year? 1997
Hey Luke, I'm 18 old as well!
>>> ctof(20.5)
68.9
>>> ctof(38)
100.4
>>> ftoc()
What is the temperature in fahrenheit? 68.9
20.5
>>> ftoc()
What is the temperature in fahrenheit? 100.4
38.0
>>> tipCalculator(42.50,0.15)
Your total amount to pay on a $42.50 bill with a 15.0% tip is $48.87.
The tip is $6.37
>>> tipCalculator(34.33,0.12)
Your total amount to pay on a $34.33 bill with a 12.0% tip is $38.45.
The tip is $4.12
>>> calculate()
Enter a number: 4
Enter a second number 10
4 + 10 = 14
4 * 10 = 40
>>> calculate()
Enter a number: 3
Enter a second number 5
3 + 5 = 8
3 * 5 = 15'''
