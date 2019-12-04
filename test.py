import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

#cwd = os.path.join(dir, 'TwitterTranslate/files/')
files = os.listdir('TwitterTranslate/Files/')  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

# dir = os.path.dirname(__file__)
# # filename = os.path.join(dir, 'TwitterTranslate/files/TwitterAuth.txt')
# filename = 'TwitterTranslate/files/TwitterAuth.txt'