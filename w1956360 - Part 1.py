# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956360 
# Date: 13th December 2022

#Part 1

import sys
command = 'y' # command variable gets the command to continue or quit the program.
count1 =  0 # count1, count2, count3, and, count4 variables count the number of times each outcome gets displayed.
count2 = 0
count3 = 0
count4 = 0
t_count = 0   # t_count(total count) variable counts how many times the program repeat.

def c_inputs(credit):
    ''' Collects inputs and checks its data type and the range.'''
    try:
        credit_inputs = int(input(credit)) 
        if credit_inputs in range(0,121,20):
            return credit_inputs
        else:
            print('out of range')
            sys.exit()     # https://learnpython.com/blog/end-python-script/#:~:text=Ctrl%20%2B%20C%20on%20Windows%20can,ends%20and%20raises%20an%20exception.
    except ValueError:
        print('Integer required')
        sys.exit()   # https://learnpython.com/blog/end-python-script/#:~:text=Ctrl%20%2B%20C%20on%20Windows%20can,ends%20and%20raises%20an%20exception.

while command == 'y' :            
    num_pass = (c_inputs('Enter your total PASS credits: '))    # num_pass(number of pass credits), num_defer(number of defer credits), num_fail(number of fail credits).
    num_defer = (c_inputs('Enter your total DEFER credits: '))
    num_fail = (c_inputs('Enter your total FAIL credits: '))

    total = num_pass+num_defer+num_fail

    if total == 120 :
        if num_pass == 120 :
            print('Progress')
            print()
            count1 += 1
        elif num_pass == 100 :
            print('Progress(module trailer)')
            print()
            count2 += 1 
        elif num_pass<=80 and num_fail<80 :
            print('Do not progress-module retriever')
            print()
            count3 += 1
        else:
            print('Exclude')
            print()
            count4 += 1
        t_count += 1
    else :
        print('Total incorrect')
        sys.exit()    # https://learnpython.com/blog/end-python-script/#:~:text=Ctrl%20%2B%20C%20on%20Windows%20can,ends%20and%20raises%20an%20exception. 
    command = input('Would you like to enter another set of data?\nEnter "y" for yes or "q" to quit and view results: ')
    print()

if command == 'q' :
    print('-----------------------------------------------------------')
    print('Histogram')
    print('Progress' , count1 , '\t:' , end='')
    for i in range(0,count1) :
        print('*', end='')
    print()
    print('Trailer' , count2 , '\t:' , end='')
    for i in range(0,count2) :
        print('*', end='')
    print()
    print('Retriever' , count3 , '\t:' , end='')
    for i in range(0,count3) :
        print('*', end='')
    print()
    print('Excluded' , count4 , '\t:' , end='')
    for i in range(0,count4) :
        print('*', end='')
    print()
    print()
    print(t_count , 'outcomes in total.')
    print('-----------------------------------------------------------')


    
            
              
        
