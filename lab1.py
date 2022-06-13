#1/usr/bin/env python3

def calculate_age ():
    try:
        birth_year = input('What year were you born? ')
        current_year = 2022
        age = birth_year - current_year
    except:
        print('Please enter an int')
    return age

def helloWorld():
	print(‘Hello World’)


helloWorld()
    
