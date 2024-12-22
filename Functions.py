# Create a Python program that implements a number analysis tool. The program should allow 
# the user to input a list of numbers and then perform various operations on them. 
# First, ask the user how many numbers they want to enter, then use a loop to collect 
# the inputs into an array. The program should display a menu where the user can choose 
# to print all the numbers, find the largest number, or calculate the sum of the numbers. 
# Each operation should be implemented as a separate static method: Print Numbers (int[] 
# numbers) to display all the numbers, GetMax(int[] numbers) to return the largest number, 
# and Get Sum (int[] numbers) to calculate the total sum. Use a loop to keep showing the 
# menu until the user chooses to exit. Ensure the program is user-friendly, handles invalid 
# inputs, and runs without errors. Optional features could include sorting the numbers or 
# adding input validation.

def PrintNumber(myNumbers):
    
    for element in myNumbers:
        print(element)
        
def GetMax(myNumbers):
    largest=myNumbers[0]
    for element in myNumbers:
        if element>largest:
            largest=element
    return(element)

def GetAve(myNumbers):
    total=0
    for element in myNumbers:
        total+=element
    return total/len(myNumbers)
    
Continue = 'T'
while Continue =='T':
    try :
        count=int(input('Please enter the total count of numbers you want :'))
        myNumbers=[]
        for i in range(count):
            num=int(input("Please enter Number :"))
            myNumbers.append(num)
            
       
        option=int(input(""" MENU :    
            1. Print all the numbers
            2. Find the largest number
            3. Calculte the average 
                  """))
              
        if option==1:
            PrintNumber(myNumbers)
        elif option==2:
            GetMax(myNumbers)
        elif option==3:
            GetAve(myNumbers)
        else:
            print('Invalid input:')
    except :
        print('Invalid Input')
        
    Continue=input("""
                  ENTER :
                    T : to continue
                    F : to Quit
                
                   """)
    
            
            
            
                  
              
      
