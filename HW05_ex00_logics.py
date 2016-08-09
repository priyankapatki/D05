#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_input =''
    while user_input == '':
        try:
            user_input = int(input("Please enter an integer : "))
        except:
            print("Not a valid number")
    if user_input % 2 == 0:
        print(" The number you entered is even.")
    else:
        print(" The number you entered is odd.")



def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for count in range(1, 101):
        if count % 10 != 0:
            if count < 10:
                print(str(count) + ' ', end=' ')   # to allign numbers 1-10 with other numbers 
                                                  # on the grid
            else:
                print(str(count), end=' ')        # for other  2 digit numbers
        else:
                print(str(count))                 # to start a new line after 10, 20 ...

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = ''
    number_count = 0
    total = 0
    while user_input != 'done':
        user_input = input("Please enter a number : ")
        try:
            if user_input != 'done':
                user_input = float(user_input)

        except:
            print(" Not a valid number. Try again !")
            continue

        if user_input == 'done' and number_count == 0:
            return " No input yet"
        elif user_input != 'done':
            total += user_input
            number_count += 1
        else:
            total_avg = total/number_count
            return total_avg
           
##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    print('Even and odd: \n')
    even_odd()
    print('\nTen by ten: \n')
    ten_by_ten()

    print('\nFind Average:')
    print(find_average())

if __name__ == '__main__':
    main()
