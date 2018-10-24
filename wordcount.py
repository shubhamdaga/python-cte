import Lines,Words,Characters
x=input()
#opening file.txt in  read mode
File =open("{}.txt".format(x),"r")

#converting File to a string
File=File.read()

print("{} {} {}".format(Lines.lines(File),Words.words(File),Characters.characters(File)))