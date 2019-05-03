#!/usr/bin/env python3

import os
import sys
import math

hit=0
miss=0

test=0



def LRU(arr,ref,val,t,dirty,x,tagL):
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
            #print(arr[i],x)
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
            
            
            val[i] = 1
            t[i] = tagL
            dirty[i] = 0
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
        return(arr,ref,val,t,dirty)
    
    #flag wasnt set, so LRU must replace numbers
    
    #replace highest ref count number with x
    ma = ref.index(max(ref))
    arr[ma] = x
    
    #set ref count to 0
    ref[ma] = 0
    val[i] = 1
    t[i] = tagL
    dirty[i] = 0
    #increment pageFault
    #pageFault++;
    #leave function
    miss+=1
    return(arr,ref,val,t,dirty)


    
def WRITE(arr,ref,val,t,dirty,ways,mem,tagL):
    #print("WRITE")
    global hit
    global miss
    global test
    flag=0
    for i in range(0,len(arr)):
        if(arr[i] == None):
            arr[i] = mem
            ref[i] = 0
            
            val[i] = 1
            t[i] = tagL
            dirty[i] = 1
            
            miss+=1
            flag=1
            break
        
        elif(arr[i] == mem and val[i] == 1):
            dirty[i] = 1
            hit+=1
            flag=1
            break
        
            '''ma = ref.index(max(ref))
            arr[ma] = x
    
            #set ref count to 0
            ref[ma] = 0
            val[i] = 1
            t[i] = tagL
            dirty[i] = 1'''
    if (flag==1):
        return(arr,ref,val,t,dirty) 
    print("HELLO WORLD")	
    ma = ref.index(max(ref))
    arr[ma] = x
    
    #set ref count to 0
    ref[ma] = 0
    val[i] = 1
    t[i] = tagL
    dirty[i] = 1
    miss+=1
    return(arr,ref,val,t,dirty) 

#checks to see if corrent arguments were entered
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

#get important args from command line
cacheSize = sys.argv[2]
ways = sys.argv[4]
file = sys.argv[6]

#calculate cache size
if (cacheSize[-2:]=='MB'):
    c = int(cacheSize[:-2])*1024*1024
elif (cacheSize[-2:]=='KB'):
    c = int(cacheSize[:-2])*1024
elif (cacheSize[-1:]=='B'):
    c = int(cacheSize[:-1])
else:
    c = int(cacheSize)

#calculate sets
sets = c/(int(ways)*64)
    
print("Simulating cache with size",cacheSize,"(",c,"bytes)",",associativity",ways,",sets",int(sets))


xFlag=0

#determine number of bits per entry
#if entry starts with '0x' readjust bit numv=ber 
fp = open(file,'r')
for line in fp:
    f = line.strip()
    l = f.split(" ")
    if(l[2][0:2] == '0x'):
        bits = len(l[2][2:])
        xFlag=1
    else:
        bits = len(l[2])
    print(l[2],bits)
    break
fp.close()

#compute offset/index/tag
#print to test if offset/index/tag are correct
blockSize = 64
print("Block Size",blockSize)
offset = math.floor(math.log(blockSize,2))
print("Offset",offset)
index = math.floor(math.log(sets,2))
print("Index",index)
tag = bits-offset-index

#reconfigure offset/index/tags, bc they could be incorrect
if(index>=bits-2):
    index=2
    print("new index",index)
if(tag<0):
    offset = 2
    tag = bits-offset-index
    print("new offset",offset)
print("Tag",tag)

#create empty list of size 'ways'
arr = [None]*int(ways)
ref = [None]*int(ways)
val = [0]*int(ways)
t = [None]*int(ways)
dirty = [0]*int(ways)

#get updated values of offset and tag
offset = int(offset)
l=[]
if(xFlag==1):
    i = int(tag)+2
else:
    i = int(tag)
j = -int(offset)
fp = open(file,'r')

total=0
x=1

#read in each line and determine what operation to conduct
for line in fp:

    #some files end in #eof
    if(line.find('#eof')!=-1):
        break
        
    #strip and split lines
    f = line.strip()
    l = f.split(" ")
    
    #grab operation
    operation = l[1]
    
    #if read, start LRU
    if(operation=='R'):
    
        #place value in LRU
        mem = l[2][i:j]
        tagL = l[2][2:tag+2]
        arr,ref,val,t,dirty = LRU(arr,ref,val,t,dirty,int(ways),mem,tagL)
    
    if(operation=='W'):
        mem = l[2][i:j]
        tagL = l[2][2:tag+2]
        #print(tagL)
        arr,ref,val,t,dirty = WRITE(arr,ref,val,t,dirty,ways,mem,tagL)
    #line number
    total+=1
    
    #if (x==147):
    #    break
    #x+=1

#print to test
print("ARR",arr)
print("REF",ref)
print("VALID",val)
print("TAG",t)
print("DIRTY",dirty)
print(test)
#update hit/miss percentages
hitPer = round((hit/total*100),2)
missPer = round(miss/total,13)

#print results
print("Results: total",total,", hits",hit,"(",hitPer,"%), misses",miss,"(",missPer,")")

#close file
fp.close()
