#!/usr/bin/env python

import sys

# replaces tabs with SPACES blank spaces, minimal error checking.
# 
# e.bonakdarian  mar 2016 - for students
#

SPACES = 4
REP = SPACES * ' '


def processFile(fn):
    with open(fn) as inf, open(fn+'.ft', 'w') as outf:
        for line in inf:
            line = line.replace('\t', REP)
            print >> outf, line,

def usage():
    print >> sys.stderr, 'Usage: fixTab.py filename\n'
    print >> sys.stderr, '       replaces tabs with %d spaces' %SPACES
    print >> sys.stderr, '       Output is stored in file in filename.ft'



if __name__ == '__main__':

    if len(sys.argv) != 2:
        usage()
    else:
        filename = sys.argv[1]
        processFile(filename)
