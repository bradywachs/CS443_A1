import argparse 
from codecs import ignore_errors
import sys 

"""
decode('UTF-16-BE') or decode('UTF-16-LE')
- double check these before using them 
'"""


def print_strings(file_obj, encoding, min_len): 
    if encoding == 's':
        bytes_to_read = 1
        format = 'UTF-8'
    elif encoding == 'l':
        bytes_to_read = 2
        format = 'UTF-16-LE'
    elif encoding == 'b':
        bytes_to_read = 2
        format = 'UTF-16-BE'
    else:
        print('ERROR: Encoding not recognized')
        sys.exit()

    # string for ascii characters to make sure it is long enough
    potential_str = ""
    while(temp := file_obj.read(bytes_to_read)):
        # FIXME: double check what ignore does
        ascii = temp.decode(format, "ignore")
        ascii_int = ord(ascii)
        # test
        # print(f'{ascii}\t{ascii_int}')

        # ascii values between [U+20, U+7E]
        if 32 <= ascii_int <= 126:
            potential_str += ascii
        else:
            if len(potential_str) >= min_len:
                print(potential_str)
            # reset string
            potential_str = ""
    
    # check for if string ends at EOF
    if len(potential_str) >= min_len:
        print(potential_str)


def main(): 
    parser = argparse.ArgumentParser(description='Print the printable strings from a file.') 
    parser.add_argument('filename') 
    parser.add_argument('-n', metavar='min-len', type=int, default=4, 
                        help='Print sequences of characters that are at least min-len characters long') 
    parser.add_argument('-e', metavar='encoding', choices=('s', 'l', 'b'), default='s', 
                        help='Select the character encoding of the strings that are to be found. ' + 
                             'Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, ' + 
                             'l = little endian UTF-16.') 
    args = parser.parse_args() 
 
    with open(args.filename, 'rb') as f: 
        print_strings(f, args.e, args.n) 
 
if __name__ == '__main__': 
    main() 