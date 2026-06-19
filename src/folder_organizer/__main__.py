import sys

from core import organize_folder


def main():
    if len(sys.argv) < 2:
        print("Please input the target folder")
    else:
        organize_folder(sys.argv[1])


if __name__ == "__main__":
    main()