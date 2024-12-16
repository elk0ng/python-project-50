#!/usr/bin/python3


import argparse
from gendiff.scripts import generate_diff


string = 'Compares two configuration files and shows a difference.'
parser = argparse.ArgumentParser(description=string)
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')
parser.add_argument(
    "-f", "--format", default="stylish",
    help="output format, default: 'stylish'"
)
args = parser.parse_args()


def main():
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()