STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

def writeTextToFile(vstup):
    filename = "file.txt"
    file = open(filename, "w")
    file.write(STATICKY_TEXT + str(vstup))
    file.close()
    return filename

print(writeTextToFile("ololololo"))
