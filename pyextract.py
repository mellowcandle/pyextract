#!/usr/bin/env python3

import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable Verbosity")
    parser.add_argument("-o", "--output", action='store', help="Output directory")
    args = parser.parse_args()

    if os.path.isfile(args.input):
        extract_file(args.input, args.output)
    else:
        extract_dir(args.input)


def extract_file(file, output):
    extract_args = ['7z']
    extract_args.extend(' x')

    if file.endswith('.rar'):
        if output:
            print(output)
            extract_args.extend('-o', output)


def extract_dir(directory):
    print("Extract a dir")


if __name__ == '__main__':
    main()
