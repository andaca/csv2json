#!/usr/bin/env python3

import argparse
import csv
import json
from itertools import islice


def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('csv_file', help='input csv file')
    ap.add_argument('-d', '--delimiter', type=str,
                    help='delimiter used by the csv file',
                    default=',')
    ap.add_argument('-o', '--out', type=str, 
                    help='filename for output json')
    ap.add_argument('-t', '--take', type=int,
                    help='only take the first N rows')
    return ap.parse_args()


def get_dicts(fname, delimiter):
    with open(fname, 'r') as f:
        for d in csv.DictReader(f, delimiter=delimiter):
            yield d


def main():
    args = get_args()
    try:
        data = get_dicts(args.csv_file, args.delimiter)
    except Exception as e:
        raise SystemExit('ERROR READING FILE:\n{}'.format(e))
    
    data = islice(data, args.take)

    if args.out:
        try:
            with open(args.out, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            raise SystemExit('ERROR OPENING OUTPUT FILE:\n{}'.format(e))
    else:
        for d in data:
            print(json.dumps(d))
    

if __name__ == '__main__':
    main()


