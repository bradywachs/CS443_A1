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
    FIXME: is hexlify be or le
    """
    total_len = 0
    for chunk in iter(lambda: file_obj.read(16), b''):
        hex_line = binascii.hexlify(chunk)
        # print(len(hex_line))
        total_len += len(hex_line)
        print(hex_line)
        # print(hex_line[:3])
    print(f'Total UTF-16 Encodings: {total_len}\t|\tCorresponding to {total_len/2} bytes')


def compare_encoding(file_obj):
    """for testing and troubleshooting
    comparing other conversion techniques to binascii.hexlify()
    FIXME: don't think I can pass a binary to format and cant convert normal string to hex
    """
    total_len = 0
    test_len = 0
    for chunk in iter(lambda: file_obj.read(16), b''):
        hex_line = binascii.hexlify(chunk)
        # clean_chunk = str(chunk)
        # clean_chunk = clean_chunk.lstrip("b'")
        # clean_chunk = clean_chunk.rstrip(" '")
        test = '{:08x}'.format(chunk)
        # print(len(hex_line))
        total_len += len(hex_line)
        test_len += len(test)
        print(hex_line)
        print(f'{test}\n')
        # print(hex_line[:3])
    print(f'Total UTF-16 Encodings: {total_len}\t|\tCorresponding to {total_len/2} bytes')


def print_utf8(file_obj, endian='be'):
    """for testing and troubleshooting
    FIXME: not working the way I am expecting
    FIXME: how to encode something (like hexlify) using utf-8 encoding"""
    total_len = 0
    for chunk in iter(lambda: file_obj.read(16), b''):
        utf16_line = binascii.hexlify(chunk)

        """problem: getting additonal hex characters somehow (up to 48 bytes)"""
        if endian == 'be':        
            utf8_line = utf16_line.decode('utf-16be').encode('utf-8')
        else:
            utf8_line = utf16_line.decode('utf-16le').encode('utf-8')

        # print(len(utf8_line))
        total_len += len(utf8_line)
        print(utf8_line)
        # print(utf8_line[:3])
    print(f'Total UTF-8 Encodings (and Bytes): {total_len/8}')


def decode_be(file_obj, min_len):
    total_len = 0  # Fixme
    all_lines = file_obj.readlines()
    for line in all_lines:
        utf16_line = binascii.hexlify(line)
        total_len += len(utf16_line)
        print(utf16_line)
    # test
    print(f'total len: {total_len}\t|\tCorresponding to {total_len/2} bytes')

def decode_le(file_obj, min_len):
    print('needs to be implemented')


def decode_s(file_obj, min_len):
    print('needs to be implemented')


def print_strings(file_obj, encoding, min_len): 
    if encoding == 's':
        decode_s(file_obj, min_len)
    elif encoding == 'l':
        decode_le(file_obj, min_len)
    elif encoding == 'b':
        decode_be(file_obj, min_len)
    else:
        print('ERROR: Encoding not recognized')
 

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