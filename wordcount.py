#opening file.txt in  read mode
File =open("file.txt","r")

#converting File to a string
File=File.read()

#spliting the File at every new line to count the number of lines
lines=len(File.split("\n"))

#intializing words and characters as zero for default
words=0
characters=0

#Splitting File into a matrix of lines
File=File.split("\n")

#iterating on every line
for line in File:

	#splitting words in a line
	words+=len(line.split())

	#counting every character in a line
	characters+=len(line)+1

#printing the result
print("{} {} {}".format(lines,words,characters))