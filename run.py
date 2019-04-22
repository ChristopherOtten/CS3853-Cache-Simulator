#!/usr/bin/env python3

import os
import sys
import math

#def LRU(mem):
    #Size of LRU is ways?


if(len(sys.argv) !=7):
    print("Error incorrect number of arguments\n");
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

if not os.path.exists(sys.argv[6]):
    print("Error, file not found")
    sys.exit(1)

cacheSize = sys.argv[2]
ways = sys.argv[4]
file = sys.argv[6]

if (cacheSize[-2:]=='MB'):
    c = int(cacheSize[:-2])*1024*1024
elif (cacheSize[-2:]=='KB'):
    c = int(cacheSize[:-2])*1024

sets = c/(int(ways)*64)
	
print("Simulating cache with size",cacheSize,"(",c,"bytes)",",associativity",ways,",sets",int(sets))

fp = open(file,'r')
for line in fp:
    f = line.strip()
    l = f.split(" ")
    bits = len(l[2])
    print(l[2],bits)
    break
fp.close()

blockSize = math.log(int(ways),2)
print("Block Size",blockSize)
offset = math.log(blockSize,2)
print("Offset",offset)
index = math.log(sets/1024,2)
print("Index",index)
tag = bits-offset-index
print("Tag",tag)

offset = int(offset)
l=[]
i = int(tag)
j = -int(offset)
fp = open(file,'r')
for line in fp:
    f = line.strip()
    l = f.split(" ")
    mem = l[2][i:j]
    print(mem)
    #LRU(mem)
    break

fp.close()
