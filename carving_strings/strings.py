import argparse 
import binascii
import codecs
 

"""
Idea for be vs le:
- iterate over line 2 bytes at a time
- when converting be to ASCII do so using x[0], x[1] as order for hex to ascii conversion
- when using le - just reverse the order
"""



def print_file(file_obj):
    """for testing & troubleshooting"""
    lines = file_obj.readlines()
    for line in lines:
        print(line)


def print_utf16(file_obj):
    """for testing and troubleshooting
    *IMPORTANT: hexlify converts to 16-bit (2 byte, UTF-16) character type
    using hexlify makes binary string double length of original data
    """
    total_len = 0
    for chunk in iter(lambda: file_obj.read(16), b''):
        hex_line = binascii.hexlify(chunk)
        # print(len(hex_line))
        total_len += len(hex_line)
        print(hex_line)
        # print(hex_line[:3])
    print(f'Total UTF-16 Encodings: {total_len}\t|\tCorresponding to {total_len/2} bytes')


def print_utf8(file_obj):
    """for testing and troubleshooting
    FIXME: not working the way I am expecting
    FIXME: how to encode something (like hexlify) using utf-8 encoding"""
    total_len = 0
    for chunk in iter(lambda: file_obj.read(16), b''):
        utf16_line = binascii.hexlify(chunk)

        #FIXME: may need decode('utf-16be') -- compare output
        ## this does have an impact on the output - would need to manually convert and see what to expect
        utf8_line = utf16_line.decode('utf-16be').encode('utf-8')
        
        # print(len(utf8_line))
        total_len += len(utf8_line)
        print(utf8_line)
        # print(utf8_line[:3])
    print(f'Total UTF-8 Encodings (and Bytes): {total_len}')


def print_strings(file_obj, encoding, min_len): 
    """
    print(file_obj.name) 
    print(encoding) 
    print(min_len) 
    """
    # for chunk in iter(lambda: file_obj.read(16), b''):
    #     hex_line = binascii.hexlify(chunk)
    #     # hex_line = str(hex_line)
    #     print(hex_line)
    print_utf8(file_obj)

 
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