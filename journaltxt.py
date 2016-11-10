import optparse
import sys

def main():
    parser = optparse.OptionParser()
    parser.add_option('-q', '--query',action="store", dest="query",help="query string", default="spam")
    options, args = parser.parse_args()
    print ('Query string:', options.query)
    pass
if __name__ == '__main__': 
    sys.exit(main()) 

