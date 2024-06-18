import argparse
import sys

def main():

    # Set the arguments
    parser = argparse.ArgumentParser('wc','This is used to get a count of lines, words and bytes in a file or from standard input')
    parser.add_argument('-c',action='store_true',help='This is a flag used to get the byte count of the file or standard output')
    parser.add_argument('-l',action='store_true',help='This is to get the number of lines in the file or standard input')
    parser.add_argument('-w',action='store_true',help='This is a flag to provide the number of words in the file or standard input')
    parser.add_argument('filename', type=argparse.FileType('r'), nargs='?', default=sys.stdin)
    args = parser.parse_args()
    print('    ', end='')
    
    file = args.filename.read()

    if args.c == True:
        print(getBytes(file), end=' ')

    if args.l == True:
        print(getLines(file), end=' ')

    if args.w == True:
        print(getWords(file), end=' ')

    if args.c == False and args.l == False and args.w == False:
        print(getLines(file), end='   ')
        print(getWords(file), end='  ')
        print(getBytes(file), end=' ')
    if args.filename.name == '<stdin>':
        print('')
    else:
        print(args.filename.name)

def getLines(file):
    return len(file.splitlines())

def getBytes(file):
    return len(file.encode('utf-8'))

def getWords(file):
    count = 0;
    for line in file.splitlines():
        count += len(line.rstrip().split())
    return count

main()