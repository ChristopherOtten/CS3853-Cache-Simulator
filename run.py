#!/usr/bin/env python3

import os
import sys
import math

hit=0
miss=0

def LRU(arr,ref,x,ways):
    #Size of LRU is ways?
    #print("LRU")
    flag=0
    global hit
    global miss
    #check if x exists in arr or if 
    #it needs to be put in because theres
    #an open space
    for i in range(0,len(arr)):
        
        #if x is in arr
        if(arr[i] == x):
            
            #set ref count to 0
            ref[i]=0
                        
            #set flag
            flag=1
            
            hit+=1
            
            #break out of loop
            break
        
        #if open slot in arr, place x
        elif(arr[i] == None):
            
            #place x in arr
            arr[i] = x
            
            #ref count to 0
            ref[i]=0
            
            #Increment Page Faults
            #pageFault++;
                        
            #set Flag
            flag=1
			
            miss+=1
            
            #break out of loop
            break
    
    #For anything not x or -1(empty space in arr)
    #increment ref count
    for i in range(0,len(arr)):
        if(arr[i] != x and arr[i] != None):
            ref[i]+=1
    
    #IF flag is set, then correct operation
    #in LRU was done, quit function
    if(flag==1):
        return arr,ref
    
    #flag wasnt set, so LRU must replace numbers
    
    #replace highest ref count number with x
    ma = arr.index(max(arr))
    arr[ma] = x
    
    #set ref count to 0
    ref[ma] = 0
    
    #increment pageFault
    #pageFault++;
    
    #leave function
    miss+=1
    return arr,ref


    
def WRITE(mem):
    print("WRITE")


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

blockSize = math.floor(math.log(int(ways),2))
print("Block Size",blockSize)
offset = math.floor(math.log(blockSize,2))
print("Offset",offset)
index = math.floor(math.log(sets/1024,2))
print("Index",index)
tag = bits-offset-index
print("Tag",tag)

arr = [None]*int(ways)
ref = [None]*int(ways)


offset = int(offset)
l=[]
i = int(tag)
j = -int(offset)
fp = open(file,'r')

total=0

for line in fp:
    f = line.strip()
    l = f.split(" ")
    mem = l[2][i:j]
    #print(mem)
    operation = l[1]
    if(operation=='W'):
        WRITE(mem)
    elif(operation=='R'):
        arr,ref = LRU(arr,ref,mem,int(ways))
    total+=1
    
    #break
print(arr)
print(ref)

hitPer = round((hit/total*100),2)
missPer = round(miss/total,13)

print("Results: total",total,", hits",hit,"(",hitPer,"%), misses",miss,"(",missPer,")")

fp.close()
