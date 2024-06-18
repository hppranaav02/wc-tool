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

    
    if args.c == True:
        print(os.stat(args.filename[0]).st_size, end=' ')
    if args.l == True:
        f = open(args.filename[0])
        print(len(f.readlines()), end=' ')
    if args.w == True:
        print()
    if args.c == False and args.l == False and args.w == False:
        f = open(args.filename[0])
        print(os.stat(args.filename[0]).st_size, end=' ')
        print(len(f.readlines()), end=' ')
    print(args.filename[0])




main()