# WC Tool
This is an implementation of the `wc` command present in unix systems, in python. The `wc` command is used to count the number of bytes, words, and lines in a file. It can also be used to count the number of charaters in a file based on the locale settings. The input to the command can also be a pipe from the standard input such as from the `cat` command.
\newline
The `wc` command can be used in the following way:
```bash
python3 ccwc.py  [OPTION]... [FILE]...
```
The options that can be used with the `wc` command are:
- `-c` : This option is used to count the number of bytes in a file.
- `-m` : This option is used to count the number of characters in a file.
- `-l` : This option is used to count the number of lines in a file.
- `-w` : This option is used to count the number of words in a file.

The `wc` command can be used with multiple files as well. In that case, the `wc` command will display the total number of bytes, words, and lines in all the files. If no option is provided, the `wc` command will display the number of bytes, words, and lines in the file along with the file name.

