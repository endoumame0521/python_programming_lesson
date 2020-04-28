from optparse import OptionParser


def main():
    usage = 'usage %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='file name')

    parser.add_option('n', '--num', action='store', type='int', dest='num')

    options, args = parser.parse_args()
    print(options.filename)
    print(args)


if __name__ == '__main__':
    main()
