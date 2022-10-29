#!/usr/bin/env python

######################################################
#               Hash2Hash_Compare.py                 #
#                 BETA Version 0.2                   #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#         EGA Technology Specialists, LLC.           #
#                   GNU GPL v 3.0                    #
######################################################

import os
import sys

# - Create the "Report File":
with open(sys.argv[2], 'w') as F2:
    F2.write('Hash Values of Unknown/Modified Executables:'+'\n')

# - Open and Read the file containing all Executable Hashes from a suspect system:
    with open(sys.argv[1], 'r') as F1:
        for line_F1 in F1:
            matched = False
            hash1, path, *_ = line_F1.split()

# - Next, we read each line of the above file, looks at the first character of the 
#   hash value and compares it to each line of the corresponding Split Known Hash 
#   Files (NSRL_O.txt, NSRL_1.txt, NSRL_2.txt, etc. ...)

# "0" Hashes ------------------------------------------------------------------
            if hash1[0] != "0":
                pass

            if hash1[0] == '0':
                
                with open(os.path.join(sys.path[0], "NSRL_0.txt"), 'r') as f0:
                    
                    for line_f0 in f0:

                        if hash1 in line_f0:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "1" Hashes ------------------------------------------------------------------
            if hash1[0] != "1":
                pass

            if hash1[0] == '1':
                
                with open(os.path.join(sys.path[0], "NSRL_1.txt"), 'r') as f1:
                    
                    for line_f1 in f1:

                        if hash1 in line_f1:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "2" Hashes ------------------------------------------------------------------
            if hash1[0] != "2":
                pass

            if hash1[0] == '2':
                
                with open(os.path.join(sys.path[0], "NSRL_2.txt"), 'r') as f2:
                    
                    for line_f2 in f2:

                        if hash1 in line_f2:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "3" Hashes ------------------------------------------------------------------
            if hash1[0] != "3":
                pass

            if hash1[0] == '3':
                
                with open(os.path.join(sys.path[0], "NSRL_3.txt"), 'r') as f3:
                    
                    for line_f3 in f3:

                        if hash1 in line_f3:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "4" Hashes ------------------------------------------------------------------
            if hash1[0] != "4":
                pass

            if hash1[0] == '4':
                
                with open(os.path.join(sys.path[0], "NSRL_4.txt"), 'r') as f4:
                    
                    for line_f4 in f4:

                        if hash1 in line_f4:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "5" Hashes ------------------------------------------------------------------
            if hash1[0] != "5":
                pass

            if hash1[0] == '5':
                
                with open(os.path.join(sys.path[0], "NSRL_5.txt"), 'r') as f5:
                    
                    for line_f5 in f5:

                        if hash1 in line_f5:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "6" Hashes ------------------------------------------------------------------
            if hash1[0] != "6":
                pass

            if hash1[0] == '6':
                
                with open(os.path.join(sys.path[0], "NSRL_6.txt"), 'r') as f6:
                    
                    for line_f6 in f6:

                        if hash1 in line_f6:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "7" Hashes ------------------------------------------------------------------
            if hash1[0] != "7":
                pass

            if hash1[0] == '7':
                
                with open(os.path.join(sys.path[0], "NSRL_7.txt"), 'r') as f7:
                    
                    for line_f7 in f7:

                        if hash1 in line_f7:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "8" Hashes ------------------------------------------------------------------
            if hash1[0] != "8":
                pass

            if hash1[0] == '8':
                
                with open(os.path.join(sys.path[0], "NSRL_8.txt"), 'r') as f8:
                    
                    for line_f8 in f8:

                        if hash1 in line_f8:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "9" Hashes ------------------------------------------------------------------
            if hash1[0] != "9":
                pass

            if hash1[0] == '9':
                
                with open(os.path.join(sys.path[0], "NSRL_9.txt"), 'r') as f9:
                    
                    for line_f9 in f9:

                        if hash1 in line_f9:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "A" Hashes ------------------------------------------------------------------
            if hash1[0] != "A":
                pass

            if hash1[0] == 'A':
                
                with open(os.path.join(sys.path[0], "NSRL_A.txt"), 'r') as fA:
                    
                    for line_fA in fA:

                        if hash1 in line_fA:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "B" Hashes ------------------------------------------------------------------
            if hash1[0] != "B":
                pass

            if hash1[0] == 'B':
                
                with open(os.path.join(sys.path[0], "NSRL_B.txt"), 'r') as fB:
                    
                    for line_fB in fB:

                        if hash1 in line_fB:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "C" Hashes ------------------------------------------------------------------
            if hash1[0] != "C":
                pass

            if hash1[0] == 'C':
                
                with open(os.path.join(sys.path[0], "NSRL_C.txt"), 'r') as fC:
                    
                    for line_fC in fC:

                        if hash1 in line_fC:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "D" Hashes ------------------------------------------------------------------
            if hash1[0] != "D":
                pass

            if hash1[0] == 'D':
                
                with open(os.path.join(sys.path[0], "NSRL_D.txt"), 'r') as fD:
                    
                    for line_fD in fD:

                        if hash1 in line_fD:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "E" Hashes ------------------------------------------------------------------
            if hash1[0] != "E":
                pass

            if hash1[0] == 'E':
                
                with open(os.path.join(sys.path[0], "NSRL_E.txt"), 'r') as fE:
                    
                    for line_fE in fE:

                        if hash1 in line_fE:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
# "F" Hashes ------------------------------------------------------------------
            if hash1[0] != "F":
                pass

            if hash1[0] == 'F':
                
                with open(os.path.join(sys.path[0], "NSRL_F.txt"), 'r') as fF:
                    
                    for line_fF in fF:

                        if hash1 in line_fF:
                            matched = True
                            break

                if not matched:
                    F2.write(line_F1)
#End of file