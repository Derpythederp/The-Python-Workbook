#!~anaconda3/bin/python
running = False
try:
    first_value = float(input("Enter your first value: ")) #Prompt outside of loop is to throw the appropriate error if first value is 0
    if first_value == 0:
        running = False
        raise ValueError("0 entered as first value") #Raise Error 
    else:
        #This is to set up my variables outside of loop
        running = True #Since I'm using a while loop, I want to be able to terminate it
        numbers = [] #Set up empty list to store numbers
        numbers.append(first_value) #Add first value to new list
        
        while running:
            next_value = float(input("Enter next value: "))
            if next_value == 0:
                running = False #If input is 0, break out of loop and get average
            else:
                numbers.append(next_value) #if input is valid, add to list of numbers
        avg = sum(numbers)/len(numbers) #sum of everything in list, divide by number of items
        print(f"Average of entered numbers is {avg}") #String formatting
        
except TypeError: #Catch any illegal inputs at any point, as float("str") for example will throw TypeError
    print("Your input was not a number. Please try again!")
    


        
        
