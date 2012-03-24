#! /usr/bin/python

if __name__ == "__main__":
    import sys, re

    code = sys.stdin.readlines()
    labels = {}

    for line_number, line in enumerate(code, 1):
        label_matches = re.search(';___(.*)$', line)
        if label_matches:
            labels[label_matches.group(1)] = line_number

    for line in code:
        jumpto_matches = re.search(';JumpTo:___(.*)$', line)
        if jumpto_matches:
            line = re.sub('J .*?;(.*)', 'J %s;\\1' % labels[jumpto_matches.group(1)], line)

        print line,