# generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f'\n{decoration * 5} {statement} {decoration * 5}')


# displays instructions
def instructions():
    statement_generator('Instructions', '-')

    print('''
To use this program simply enter an integer between 1 and 200. This program will show the factors of your chosen integer. 

It will also tell you if your chosen number:
- is a prime number (has only 2 factors) 
- is a perfect square number (has only 3 factors)

To exit the program, please enter 'xxx'.
    ''')

# display instructions if requested
want_instructions = input('Press [ENTER] to see the instructions or any key to continue. ')
if want_instructions == '':
    instructions()

print('Program Continues...')