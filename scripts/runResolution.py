#! /usr/bin/env python
from hgc_tpg.resolution.resolution import *
from utilities.parameters import parameters

def main(input_file, output_file):
    print 'Input file: ',input_file
    print 'output file: ',output_file
    print ' --> execution of the resolution analysis'
    
    # customization of the parameters
    conf = parameters()
    conf.minEta_C3d = 1.47
    conf.maxEta_C3d = 3.0
    conf.minPt_C3d = 5.0 
    conf.minEta_gen = 1.47
    conf.maxEta_gen = 3.0
    conf.minPt_gen = 5.0
    conf.particle_type = 22
    conf.particle_status = 1

    resolution(input_file, output_file, conf).plotResponse()
        
    return

if __name__=='__main__':
    import sys
    import optparse

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--input', dest='input_file', help='Input file')
    parser.add_option('--output', dest='output_file', help='Output file')
    (opt, args) = parser.parse_args()
    if not opt.input_file :
        parser.print_help()
        print 'Error: Missing input file name'
        sys.exit(1)
    if not opt.output_file :
        parser.print_help()
        print 'Error: Missing output file name'
        sys.exit(1)
    main(opt.input_file, opt.output_file)

