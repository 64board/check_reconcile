#!/usr/bin/env python3

import re
import sys

class ReconcileFile:

    def __init__(self, file_name):

        self.matched = self.not_matched = 0
        self.file_name = file_name
        self.not_matched_lines = []

        # Just for later printing.
        if file_name[:3] == 'adv':
            self.stmt_src = 'Advantage'
        elif file_name[:3] == 'sto':
            self.stmt_src = 'Stone'
        else:
            self.stmt_src = 'UNKNOWN'

        # Open file and run the checks.
        try:
            with open(file_name, 'r') as f:
                self.lines = f.readlines()
            self._check()    
        except FileNotFoundError:
            print('File {} not found!'.format(file_name))

    def print(self):
        print(self.lines)

    def _check(self):
        """
        Uses REGEX to find lines that contain a sequence like ,0,0 which means
        there was no reconcile. The search jumps over a header line.
        The method updates 2 class variables self.matched and self.not_matched
        with the count of the corresponding matches.
        """

        header_pattern = re.compile(r'^Id')
        missing_pattern = re.compile(r',0,0')
        
        for line in self.lines:

            if header_pattern.match(line):
                continue

            if missing_pattern.search(line):
                self.not_matched = self.not_matched + 1
                self.not_matched_lines.append(line)
            else:
                self.matched = self.matched + 1

    def print_results(self):
        print('Checking: \t{}'.format(self.stmt_src))
        print('File: \t\t{}'.format(self.file_name))
        print('Matched: \t{}'.format(self.matched))
        print('Not Matched: \t{}'.format(self.not_matched))

        if (self.not_matched > 0):
            print('DIFFERENCES!!!\n')
            for line in self.not_matched_lines:
                print(line.rstrip())
            print()    
        else:
            print('ALL GOOD!!!\n')

def print_help():
    print('Argument with file name is required!')

def main():

    # The argument should be a file name to check.
    if len(sys.argv) == 1:
        print_help()
        sys.exit(1)
    else:
        file_name = sys.argv[1]

    # The checking part using File class.
    f = ReconcileFile(file_name)
    f.print_results()

if __name__ == '__main__':
    main()
