import argparse
import os

# driver function
def main():

    # Set the arguments
    parser = argparse.ArgumentParser('wc','This is used to get a count of lines, words and bytes in a file or from standard input')
    parser.add_argument('-c',action='store_true',help='This is a flag used to get the byte count of the file or standard output')
    parser.add_argument('-l',action='store_true',help='This is to get the number of lines in the file or standard input')
    parser.add_argument('-w',action='store_true',help='This is a flag to provide the number of words in the file or standard input')
    parser.add_argument('filename', type=str,nargs=1)
    args = parser.parse_args()
    print('    ', end='')
    
    if args.c == True:
        print(getBytes(args.filename[0]), end=' ')

    if args.l == True:
        print(getLines(args.filename[0]), end=' ')

    if args.w == True:
        print(getWords(args.filename[0]), end=' ')

    if args.c == False and args.l == False and args.w == False:
        print(getLines(args.filename[0]), end='   ')
        print(getWords(args.filename[0]), end='  ')
        print(getBytes(args.filename[0]), end=' ')
    print(args.filename[0])

def getLines(fileName):
    f = open(fileName)
    return len(f.readlines())

def getBytes(fileName):
    return os.stat(fileName).st_size

def getWords(fileName):
    count = 0;
    with open(fileName) as file:
        for line in file.readlines():
            count += len(line.rstrip().split())
    return count

main()