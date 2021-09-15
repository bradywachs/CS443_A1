import argparse 
import binascii
 


def print_file(file_obj):
    """for testing & troubleshooting"""
    lines = file_obj.readlines()
    for line in lines:
        print(line)


def print_hex(file_obj):
    """for testing and troubleshooting
    FIXME: not getting the expected output
    """
    total_len = 0
    for chunk in iter(lambda: file_obj.read(16), b''):
        hex_line = binascii.hexlify(chunk)
        hex_line = str(hex_line)
        print(len(hex_line))
        total_len += len(hex_line)
        # test
        print(hex_line)
    print(f'Total Bytes: {total_len}')


def print_strings(file_obj, encoding, min_len): 
    """
    print(file_obj.name) 
    print(encoding) 
    print(min_len) 
    """

 
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