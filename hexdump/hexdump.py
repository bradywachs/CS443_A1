import argparse
import binascii
from textwrap import wrap


def main():
    # get filename
    parser = argparse.ArgumentParser(description="Python implementation of hexdump tool")
    parser.add_argument("filename", type=str, help="Name of file that hexdump tool will be applied to")
    args = parser.parse_args()
    file = args.filename

    # integer representation of offset
    n = 0

    # logic contained in try block
    try:
        with open(file, "rb") as f:
            # iterate over every 16 byte chunk in file
            for chunk in iter(lambda: f.read(16), b''):
                hex_line = binascii.hexlify(chunk)
                hex_line = str(hex_line)
                col2 = " ".join(hex_line[i:i+2] for i in range(0, len(hex_line), 2))    # column2 is the byte values in hex
                col2 = f'{col2[:23]} {col2[23:]}'                                       # add extra space inbetween 8th and 9th byte
                # print(col2)

                col3 = ""
                for i in chunk:
                    # range of printable ascii characters [32,127] - range funct goes to stop - 1 value
                    if i in range(32,128):
                        col3 += chr(i)
                    else:
                        col3 += (".")

                # test
                print(f'{col2} |{col3}|')

                # increment int representation of offset
                n += 1
    
    except Exception as ex:
        print(f"ERROR - Exception: {ex}")

if __name__ == "__main__":
    main()