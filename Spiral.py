# import only system from os
from os import system

# import sleep to show output for some time period
from time import sleep

"""
clearConsole = lambda: print('\n' * 150)

clearConsole()

cls = lambda: system('cls')
clearConsole()
sleep(2)

print('\n\n')
print('\n'.join([''.join(['{:10}'.format(item) for item in row])
                 for row in local_matrix]))

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# print out some text
print('hello geeks\n' * 10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()
"""



# define 10x10 matrix
local_matrix = [[0] * 10] * 10

print('\n'.join([''.join(['{:10}'.format(item) for item in row])
                 for row in local_matrix]))



cls = lambda: system('cls')
cls()

sleep(2)

print('\n'.join([''.join(['{:10}'.format(item) for item in row])
                 for row in local_matrix]))




# sample of compute veector cross
print('\n\n\n\n\n\n')
#initialize arrays
#A = np.array([0, 1], [1, 0], [0, -1], [-1, 0])
A = np.array([0, 1])
B = np.array([0, 0, 1])
output = A
print(output)
#compute cross product
for i in range (10):
    output = np.cross(output, B)
    print(output[0] , output[1])


