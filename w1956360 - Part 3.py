# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956360 
# Date: 13th December 2022

#Part 3

import sys
command = 'y'  # command variable gets the command to continue or quit the program.
count1 =  0   # count1, count2, count3, and, count4 variables count the number of times each outcome gets displayed.
count2 = 0
count3 = 0
count4 = 0
t_count = 0   # t_count(total count) variable counts how many times the program repeat.
i = 0
in_list = []   # in_list collects input data to the list.
out_list = []   # out_list collects 'outcomes' variable data to the list.

def c_inputs(credit):
    ''' Collects inputs and checks its data type and the range.'''
    try:
        global credit_inputs
        credit_inputs = int(input(credit))
        in_list.append(credit_inputs)
        
        if credit_inputs in range(0,121,20):
            return credit_inputs
        else:
            print('out of range')
            sys.exit()   # https://learnpython.com/blog/end-python-script/#:~:text=Ctrl%20%2B%20C%20on%20Windows%20can,ends%20and%20raises%20an%20exception.
    except ValueError:
        print('Integer required')
        sys.exit()   # https://learnpython.com/blog/end-python-script/#:~:text=Ctrl%20%2B%20C%20on%20Windows%20can,ends%20and%20raises%20an%20exception.
    

while command == 'y' :            
    num_pass = (c_inputs('Enter your total PASS credits: '))   # num_pass(number of pass credits), num_defer(number of defer credits), num_fail(number of fail credits). 
    num_defer = (c_inputs('Enter your total DEFER credits: '))
    num_fail = (c_inputs('Enter your total FAIL credits: '))

    data_list = [str(in_list[x:x+3]) for x in range(0, len(in_list), 3)]  # https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists#:~:text=You%20could%20use%20numpy%27s%20array_split,20%20nearly%20equal%20size%20chunks.
                                                                          # data_list stores the data from in_list as data triplets.                                   
    total = num_pass+num_defer+num_fail

    if total == 120 :
        if num_pass == 120 :
            print('Progress')
            outcome = 'Progress'
            print()
            count1 += 1
        elif num_pass == 100 :
            print('Progress(module trailer)')
            outcome = 'Progress(module trailer)'
            print()
            count2 += 1 
        elif num_pass<=80 and num_fail<80 :
            print('Do not progress-module retriever')
            outcome = 'Module retriever'
            print()
            count3 += 1
        else:
            print('Exclude')
            outcome = 'Exclude'
            print()
            count4 += 1
        t_count += 1
        out_list.append(outcome)
    else :
        print('Total incorrect')
        sys.exit()   # https://learnpython.com/blog/end-python-script/#:~:text=Ctrl%20%2B%20C%20on%20Windows%20can,ends%20and%20raises%20an%20exception.
    
    command = input('Would you like to enter another set of data?\nEnter "y" for yes or "q" to quit and view results: ')
    print()

    infile = open("inputdata.txt", "w+")   # infile stores data from out_list and data_list.
    for i in range(len(data_list)):
        infile.write(f'{out_list[i]} - {data_list[i]} \n') 
    infile.close()

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

    infile = open("inputdata.txt", "r")
    in_data = infile.read()
    infile.close()
    print(in_data)

    
