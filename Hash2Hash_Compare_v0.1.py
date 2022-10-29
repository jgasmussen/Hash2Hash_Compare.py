#!/usr/bin/env python

import sys

with open(sys.argv[3], 'w') as f3:
    f3.write('Hash Values of Unknown/Modified Executables:'+'\n')

    with open(sys.argv[1], 'r') as f1:
        for line_f1 in f1:
            matched = False
            hash1, path1, *_ = line_f1.split()

            with open(sys.argv[2], 'r') as f2:
                for line_f2 in f2:
                    if hash1 in line_f2:
                        matched = True
                        break

            if not matched:
                f3.write(line_f1)