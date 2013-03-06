from arithmetic import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    
    if len(tokens) == 2 or len(tokens) == 3:
        tokens[1] = int(tokens[1])

    if len(tokens) == 3:
        tokens[2] = int(tokens[2])

    if tokens[0] == 'q':
        break
    
    elif tokens[0] == '+':
        addition = add(tokens[1], tokens[2])
        print addition

    elif tokens[0] == '-':
        subtraction = subtract(tokens[1], tokens[2])
        print subtraction

    elif tokens[0] == '*':
        multiplication = multiply(tokens[1], tokens[2])
        print multiplication
    
    elif tokens[0] == '/':
        division = divide(tokens[1], tokens[2])
        print division
    
    elif tokens[0] == 'square':
        square_it = square(tokens[1])
        print square_it
    
    elif tokens[0] == 'cube':
        cube_it = cube(tokens[1])
        print cube_it
    
    elif tokens[0] == 'pow':
        power_it = power(tokens[1], tokens[2])
        print power_it
    
    elif tokens[0] == 'mod':
        mod_it = mod(tokens[1], tokens[2])
        print mod_it