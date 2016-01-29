def printFile(fname):
    f = open(fname, 'r')
    for line in f:
        print(line, end = '')
    f.close()

printFile('C:\myfolder\myfile3.txt')



