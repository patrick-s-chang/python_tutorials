# Read
names_file_read = open("names.txt", "r")
print(names_file_read.readable())
# print(names_file.read())

lines = names_file_read.readlines()

line_count = 1
for line in lines:
    print(str(line_count) + " " + line)
    line_count+=1

names_file_read.close()


# Append
names_file_append = open("names.txt", "a")
names_file_append.write("\nChristine Liow")
names_file_append.write("\nCatherine Liow")
names_file_append.write("\nJason Liow")

names_file_append.close()

# Write
names_file_write = open("names1.txt", "w")
names_file_write.write("Pikachu")
names_file_write.write("\nCharmander")
names_file_write.write("\nSquirtle")
names_file_write.write("\nBulbasaur")
names_file_write.close()