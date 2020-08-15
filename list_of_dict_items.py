##Week 8 - Dictionaries Assignment
##
##Please note that you will need to apply
##knowledge from prior weeks in order to complete this assignment!This
##week, I would like you to modify the program you wrote last week so that
##it takes the data from the final employee numbers, employee names,
##employee salary, total hourly rate, and company raises lists and
##combines it into a list of dictionary items that looks like a
##database-like structure. At the end of your program, print out the final
##list.Be sure to put comments in your code that clearly mark how you are
##performing your program logic. Also, be sure to apply the lessons about
##structuring dictionaries that were covered in the lecture.  In the
##submission comments of this assignment, please place the repository URL
##of your file submission.



# Data to store
employee_names = ['Jackie Grainger','Jignesh Thrakkar','Dion Green','Jacob Gerber', 'Sarah Sanderson', 'Brandon Heck','David Toma', 'Charles King']
employee_salary = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

employee_numbers = [1121, 1122, 1127, 1132, 1137, 1138, 1152, 1157]

hourly_rate = [28.886, 32.825, 37.375, 31.616000000000003, 30.485, 33.592, 29.445, 30.875]




# Creation of empty list to store data.
list_of_dict = []


# variable that will help us retrieve values from one of the lists
index_count = 0

# Iterating over employee names
for name in employee_names:
    
    # Introduce our empty list, assign it the current values data to store as we loop through them and

    # Combines it into a list of dictionary items
    list_of_dict.append({'name':name, 'number': employee_numbers[index_count],
                         'salary':employee_salary[index_count],
                         'hourly rate': hourly_rate[index_count]})

    # Increment our current index variable.
    index_count += 1


print(f"Printing the new list of dictionary:\n\n{list_of_dict}\n\n")

print(type(list_of_dict))



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



    num_ok = False

    while not num_ok:
        num = input('Enter number:')

        if num:
            

            try:

                int(num)
                num_ok = True

                if len(num)  <= 0 and len(num) >= 8:
                    num_ok = False

                else:
                    num_ok = True

            except:
                num_ok = False
                
        else:
            num_ok = False

    


    active = False
    chars =  list('!"\'#$%^&*()=+,<>/?;:[]{}\)')


    while not active:
        email = input('enter email:')

        if email:
            active = True
            if '@' in email:
                continue
                if '.' in email:
                     continue
                     for char in chars:
                         if char in email:
                             active = False
                         else:
                             active = True
                else:
                     active = False
            else:
                active = False
            if not active:
                email = input('Email was not entered properly\nPlease try again:')



    bad_chars = list("!\"'@$%^&*_=+<>?;:[]{}).")

    address_ok = False   


    while not address_ok:
        address = input('Enter postal address:  ')
        if address:
            pass
            if ' ' in address:
                pass
                for chars in bad_chars:
                    if chars in address:
                        address_ok = False

                    else:
                        address_ok = True
                    

            else:
                address_ok = False
        

        else:
            address_ok = False
##########

    name_ok = False

    while not name_ok:
        characters =  list('!"@#$%^&*()_=+,<\>/?;:[]{}\).')

        name = input('Enter name:')

        if name:
            name_ok = True

            if name.istitle():
                name_ok = True


                for character in characters:
                    for element in name:
                        if character == element:
                            name_ok = False


                    else:
                        name_ok = True

                
            else:
                print('Value entered not cceptable, Please try entering your name in title case.')
                name_ok = False
                
                

        else:
            name_ok = False

    #########
    employee_data.append(f"'user #': {users}, 'num': {num},  'name': {name}, 'address': {address}, 'email': {email}")
    users += 1

print(employee_data)


