#!/usr/bin/env python

######################################################
#                Split_Hash_File.py                  #
#                 BETA Version 0.1                   #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#         EGA Technology Specialists, LLC.           #
#                   GNU GPL v 3.0                    #
######################################################

import sys

with open(sys.argv[1], 'r') as f:
	next(f)
	for line in f:
		hash1, *_ = line.split()

		if hash1[1] == "0":
			with open('NSRL_0.txt', 'a') as f0:
				f0.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "0":
			pass

		if hash1[1] == "1":
			with open('NSRL_1.txt', 'a') as f1:
				f1.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "1":
			pass

		if hash1[1] == "2":
			with open('NSRL_2.txt', 'a') as f2:
				f2.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "2":
			pass

		if hash1[1] == "3":
			with open('NSRL_3.txt', 'a') as f3:
				f3.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "3":
			pass

		if hash1[1] == "4":
			with open('NSRL_4.txt', 'a') as f4:
				f4.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "4":
			pass

		if hash1[1] == "5":
			with open('NSRL_5.txt', 'a') as f5:
				f5.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "5":
			pass

		if hash1[1] == "6":
			with open('NSRL_6.txt', 'a') as f6:
				f6.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "6":
			pass

		if hash1[1] == "7":
			with open('NSRL_7.txt', 'a') as f7:
				f7.write(hash1[1:41] + "\n")
				
		if hash1[1] != "7":
			pass

		if hash1[1] == "8":
			with open('NSRL_8.txt', 'a') as f8:
				f8.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "8":
			pass

		if hash1[1] == "9":
			with open('NSRL_9.txt', 'a') as f9:
				f9.write(hash1[1:41] + "\n")
				
		if hash1[1] != "9":
			pass

		if hash1[1] == "a":
			with open('NSRL_a.txt', 'a') as fa:
				fa.write(hash1[1:41] + "\n")
				
		if hash1[1] != "a":
			pass

		if hash1[1] == "A":
			with open('NSRL_A.txt', 'a') as fA:
				fA.write(hash1[1:41] + "\n")
				
		if hash1[1] != "A":
			pass

		if hash1[1] == "b":
			with open('NSRL_b.txt', 'a') as fb:
				fb.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "b":
			pass

		if hash1[1] == "B":
			with open('NSRL_B.txt', 'a') as fB:
				fB.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "B":
			pass

		if hash1[1] == "c":
			with open('NSRL_c.txt', 'a') as fc:
				fc.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "c":
			pass

		if hash1[1] == "C":
			with open('NSRL_C.txt', 'a') as fC:
				fC.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "C":
			pass

		if hash1[1] == "d":
			with open('NSRL_d.txt', 'a') as fd:
				fd.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "d":
			pass

		if hash1[1] == "D":
			with open('NSRL_D.txt', 'a') as fD:
				fD.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "D":
			pass

		if hash1[1] == "e":
			with open('NSRL_e.txt', 'a') as fe:
				fe.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "e":
			pass

		if hash1[1] == "E":
			with open('NSRL_E.txt', 'a') as fE:
				fE.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "E":
			pass

		if hash1[1] == "f":
			with open('NSRL_f.txt', 'a') as ff:
				ff.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "f":
			pass

		if hash1[1] == "F":
			with open('NSRL_F.txt', 'a') as fF:
				fF.write(hash1[1:41] + "\n")		
				
		if hash1[1] != "F":
			pass