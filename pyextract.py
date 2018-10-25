#!/usr/bin/env python3

import argparse
import os
import subprocess
import logging
from pathlib import Path

def main():

    logging.basicConfig(format='%(message)s')

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="File/Folder to extract")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable Verbosity")
    parser.add_argument("-o", "--output", action='store', help="Output directory")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if not os.path.exists(args.input):
        logging.error("ERROR: Requested file/folder does not exists")
        exit(-1)

    if os.path.isfile(args.input):
        extract_file(args.input, args.output)
    else:
        extract_dir(args.input, args.output)

    exit(0)

def extract_file(filename, output):
    extract_cmd = ['7z']
    extract_cmd.extend(['x', filename])

    if filename.endswith(('.rar','.zip')):
        if output:
            extract_cmd.append('-o' + output)

        subprocess.call(extract_cmd)

    else:
        logging.error("ERROR: Unsupported file format: " + filename)


def extract_dir(directory, output):
    file_list = sorted(Path(directory).glob('**/*.rar'))
    file_list += sorted(Path(directory).glob('**/*.zip'))


    for x in file_list:
        logging.debug("Attempting to extract: " + os.fspath(x))
        extract_file(os.fspath(x), output)


if __name__ == '__main__':
    main()
