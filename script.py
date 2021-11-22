import json
import argparse
import sys
from operator import itemgetter


def writing_to_file(infiles, outfile):
    merged_list = []
    for infile in infiles:
        with open(infile, 'r') as json_file:
            for strings in json_file:
                result = json.loads(strings)
                merged_list.append(result)
    merged_list.sort(key=itemgetter('timestamp'), reverse=False)
    with open(outfile, 'w+') as output_file:
        for items in merged_list:
            output_file.write("%s\n" % items)
    return 0


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', metavar='<path_to_log>', nargs='+', help='Merged files')
    parser.add_argument('-o', '--outfile', required=True, help='Output file')
    args = parser.parse_args(argv)
    merging = writing_to_file(args.infiles, args.outfile)
    return merging


if __name__ == '__main__':
    merging = main(sys.argv[1:])
    exit(merging)
