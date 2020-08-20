
#########################################
# Week 8 - While Loops Assignment
# Please note that you will need to apply knowledge from prior weeks in
# order to complete this assignment! For this assignment, you need to
# modify the program you created in the User Input Assignment so that it
# can take up to 5 employees' worth of information. Also, when a user
# enters improper data, the program asks the user to re-enter it before
# continuing on. As employee information is added, create a list of
# dictionaries that hold all of the information. And the end of your
# program, print out the list. Be sure to put comments in your code that
# clearly mark how you are performing your program logic. Also, be sure to
# apply the lessons about structuring dictionaries that were covered in
# the lecture. In the submission comments of this assignment, please place
# the repository URL of your file submission.





employee_data = []
users = 0
while users < 5:


    #<<<<-----------User Employee ID------------>>>
    num_ok = False

    while not num_ok:
        num = input('Enter number:')


        # Check for bad characters in user input and terminate if  bad character is found.
        # Check to see user input isn't blank.
        if num:
            

            # Checking the user input to see if it is truly integer.
            # Using try and  except statement to control error output.
            try:

                int(num)
                num_ok = True
                
                # If length  is less than or equal to seven.
                if len(num) <= 7:
                    num_ok = True

                else:
                    num_ok = False

            except:
                num_ok = False
                
        else:
            num_ok = False

    #<<<------------User Employee Name------------>>>

    name_ok = False
    
    characters =  list('!"@#$%^&*()_=+,<\>/?;:[]{}\).')

    while not name_ok:
        

        name = input('Enter name:')

        if name.istitle():
            name_ok = True
            
        else:
            name_ok = False

   #<<<------------User Employee Address------------>>>

            
    bad_chars = list("!\"'@$%^&*_=+<>?;:[]{}).")

    # Flag = keeps while loop under control. 
    address_ok = False   


    while not address_ok:

        # Get user input.
        address = input('Enter postal address:  ')

        # Check to make sure user input is not blank.
        if address:

            #Empty string to help wih the check along the way.
            new_address = ''

            # For loop to iterate through elements of user input
            for element in address:
                
                # Validating address by check for numeric, alphabet and space(' ') character.
                if ((element.isnumeric() or element.isalpha()) or element.isspace()):

                    # If condition above is true concatenate the letter with  empty string from above.
                    new_address += element

                    # If element of address in the list of bad characters ask user for input.
                    if element in bad_chars:
                        address_ok = False
                        
                    else:
                        address_ok = True
                        
                        
        else:
            address_ok = False

    #<<<------------User Employee Email------------>>>
            
    active = False
    characters =  list('!"\'#$%^&*()=+,<>/?;:[]{}\)')


    while not active:
        email = input('Enter email:')

        
        # Check for bad characters in user input and terminate if  bad character is found.
        # Blank check
        if email:

            #Empty string to help wih the check along the way.
            new_email = ''

            # For loop to iterate through elements of user input.
            for letter in email:


                # Check for numbers, alphabets, '@' symbol and '.'.
                if (letter.isnumeric() or letter.isalpha()) or (letter == '@' or letter == '.'):

                     # If condition above is true concatenate the letter with our empty string from above.
                    new_email += letter


                    # Terminate the program if we have any bad character present in user input.
                    if letter in characters:
                        active = False
                        
                    else:
                        active = True

                #  If user input does not have characters of a real email address.
                # Return to start of while loop and ask user to enter email address again
                else:
                    
                    active = False
                    
                if not active:
                    
                    email = input('Email was not entered properly\nPlease try again:')



    employee_data.append(f"'#{users}': 'ID num': {num},  'Name': {name}, 'Employee Address': {address}, 'Employee Email': {email}")
    users += 1

print(employee_data)
