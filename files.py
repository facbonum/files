import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

#f = open("names.txt", "r") # by default, it already specifies read and text
f = open("names.txt")
print(f.read()) # FileNotFoundError if the IDE terminal is not pwd

# print(f.readline())
# print(f.readline())

for line in f:
  print(line)

f.close()


try:
  f = open("name_list.txt")
  print(f.read())
except:
  print("The file you want to read doesn't exist.")
finally:
  f.close()


  # Append - creates the file if it doesn't exist
  f = open("names.txt", "a")
  f.write("\nNeil")
  f.close()

  f = open("names.txt")
  print(f.read())
  f.close()

# Write (overwrite)
f = open("context.txt", "w") # w, write
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()


# Two ways to create a new file
# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
  f = open("dave.txt", "x") # x, create
  f.close()

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
  os.remove("dave.txt")
else:
  print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
  content = f.read()

with open("names.txt", "w") as f:
  f.write(content)