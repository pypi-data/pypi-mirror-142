"""Sort all the functions within a module"""

#read in the file
fname = 'semi.py'
file = open(fname, mode='r')
contents = file.read()
file.close()

b = contents.split('def ')  # split the file at the def labels
c = b[1:]  # skip the first element with the import statements.
c.sort()  # sort in place
d = "def ".join(c)
d = b[0] + 'def '+ d

# write the file back to disk
file = open('sorted.py', mode='w')
file.write(d)
file.close()
