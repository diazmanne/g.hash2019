import sys

filename = sys.argv[1]
file = open(filename,"r")
temp = file.readline()
temp.rstrip('\n')
print(temp)

file.close()