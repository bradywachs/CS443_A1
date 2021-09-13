import argparse
import binascii


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
                # changing from binascii.hexlify to format as 02x had change on hash
                col2 = " ".join([f'{i:02x}' for i in chunk])
                col2 = f'{col2[0:23]} {col2[23:]}' 

                # using this join vs the larger if statement did not have impact on hash
                col3 = "".join([chr(i) if 32 <= i <= 127 else "." for i in chunk])

                # convert int to hex for offset
                output = '{:08x}'.format(n*16)

                # output
                print(f'{output} {col2:<49}  |{col3}|')

                # increment int representation of offset
                n += 1

            n -= 1
            # get number of hex characters and / 2 to find number of bytes
            num_bytes = int( len("".join(col2.split())) / 2 )
            last_offset = '{:08x}'.format((n*16)+num_bytes)
            print(f'{last_offset}')
    
    except Exception as ex:
        print(f"ERROR - Exception: {ex}")

if __name__ == "__main__":
    main()