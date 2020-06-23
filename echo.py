#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Kevin Blount"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("-u", "--upper", action="store_true",
                        help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true",
                        help="convert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true",
                        help="convert text to titlecase")
    parser.add_argument("text", help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if not args:
        parser.print_usage()
        sys.exit(1)

    my_text = ns.text
    if ns.upper:
        my_text = my_text.upper()
    if ns.lower:
        my_text = my_text.lower()
    if ns.title:
        my_text = my_text.title()
    print(my_text)


if __name__ == '__main__':
    main(sys.argv[1:])
