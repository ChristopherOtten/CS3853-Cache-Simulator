#!/usr/bin/env python3

import os
import sys

#check arguments, if not present exit and print error
if(len(sys.argv) != 6):
	print("Error incorrent number of arguments\n")
	sys.exit(1)
	
if(sys.argv[1] != '-s'):
	print("Error -s needed")
	sys.exit(1)
	
if(sys.argv[3] != '-a'):
	print("Error -a needed")
	sys.exit(1)
	
if(sys.argv[5] != '-f'):
	print("Error -f needed")
	sys.exit(1)
	
#check if file exists, if not exit
if not os.path.exists(sys.argv[5]):
	print("Error, file not found")
	sys.exit(1)
	
#convert command line args to variables
cacheSize = int(sys.argv[1][0:2])
ways = sys.argv[3]
file = sys.argv[5]

print(cacheSize,ways,file);



	

	

