
def readFile(filename):
    data = ""
    # f = file("D:/a.html")
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0 :
            break

        data += line

    f.close()

    return data
