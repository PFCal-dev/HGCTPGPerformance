#! /usr/bin/env python

import pandas as pd
import rootpy.ROOT as ROOT

def main(input_file):
    return


if __name__=='__main__':
    import sys
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--input', dest='input_file', help='Input file')
    (opt, args) = parser.parse_args()
    if not opt.input_file:
        parser.print_help()
        print 'Error: Missing input file name'
        sys.exit(1)
    main(opt.input_file)

