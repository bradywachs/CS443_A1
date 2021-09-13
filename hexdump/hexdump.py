import argparse
import binascii


def main():
    # get filename
    parser = argparse.ArgumentParser(description="Python implementation of hexdump tool")
    parser.add_argument("filename", type=str, help="Name of file that hexdump tool will be applied to")
    args = parser.parse_args()
    file = args.filename

    # try to open file
    try:
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(16), b''):
                hex_line = binascii.hexlify(chunk)
                print(hex_line)
    
    except Exception as ex:
        print(f"ERROR - Exception: {ex}")

if __name__ == "__main__":
    main()