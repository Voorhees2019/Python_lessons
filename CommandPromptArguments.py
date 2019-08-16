import sys
import os
# -------------using sys--------------

print('Hello, Artur.')
# print taken arguments from command prompt
print(sys.argv)
# zero argument(sys.argv[0]) is always filename
print('first argument = ', sys.argv[1])


# -------------using os--------------
# use system commands
# dir - show list of directory in dos
os.system('dir')
# os.mkdir('new_dir')
