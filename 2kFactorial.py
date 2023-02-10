#%% Libraries used in the program. (Globally defined, though not strictly necessary)
import numpy as np
import math
import codecs
import itertools
from pyDOE2 import *

#%%Functions created for the program
#This function is used to iteratively create letters from its hexidecimal number
def var_name(i): 
    if(i<9):
        stri = 41+i        #"42434445464748494a4b4c4d4e4f505152535455565758595a" = Hex alphabet A-Z (capitalized)
    elif(i==9):
        stri = "4a"   
    elif(i==10):
        stri = "4b"   
    elif(i==11):
        stri = "4c"   
    elif(i==12):
        stri = "4d"   
    elif(i==13):
        stri = "4e"   
    elif(i==14):
        stri = "4f"   
    elif((i>14) and (i<25)):
        stri = 41+i-6
    elif(i==25):
        stri = "5a"
    else:
        stri = "343034"     #If, somehow, a wrong number is used, or more than
    string = str(stri)      #26 elements are called, the variable is named "404"
    b_str =codecs.decode(string, "hex")
    a_str = str(b_str, encoding = "ascii", errors ="ignore")
    key = (a_str)
    return key

#This is where the DOE test values are created
def twok(test,tm,n,i,o):
    A = 0
    B=1
    for j in range(2**n):
        if(o==1):
            A +=test[j]*tm[j][i]/(2**(n-1))
        else:
            for k in range (o):
                B*=tm[j][i[k]]
            A+=test[j]*B/(2**(n-1))
            B=1
    return (A)

#This is used to import the data from a file
def readfile(filename):
    data = np.loadtxt(filename + '.txt')
    return data

#This is used to write the results to a file
def writefile(filename,lib,n,i,savefile):
    fn = filename+".txt"
    file=open(fn,'a')
    with open(fn,'a') as fi:
        if (i==0):
            fi.write('A 2k factorial study was performed using '+str(n)+' variables\n')
            fi.write('The results come from the file named "'+str(savefile)+'"\n')
        fi.write(str(lib)+'\n')
        if (i==(n-1)):
            fi.write('\n')
    file.close()
    return

#%%This is the area to manipulate/ load data
#********************************************************
#Test values - ***Comment out which ever method you are not using***
    ###Handtyped values 
# test = [1154/2,1319/2,1234/2,1277/2,2089/2,1617/2,2178/2,1589/2]
    
    ###Read values from .txt - The other option is to load a txt file with the 
    ###data saved in the proper order
filename = "test_example"  #without the .txt file extension, just the saved name
test = readfile(filename)


#^^^ This is where the results of the experiments should be placed,
#^^^ ie the function value being evaluated for changes do to experimental 
#^^^ parameters. The order in which these are placed is crucial. The tests  
#^^^ should match what is produced in the test matrix "tm". "tm" starts with 
#^^^ the all low value cases. Uncomment out the print below "tm" to verify that
#^^^ your test order matches.


#*********************************************************
#Do you want to save the 2k factorial results to a .txt file?
savefile = 'y'          #Use 'y' to save a file
filewrite =' Results'   #If you do not change the file name it will append the 
                        #next results to the same file. I would recommend naming 
                        #this file the type of test/parameters being explored
#*********************************************************
k = int(math.log2(len(test))) # the k value is calculated based on the number of test results
tm = ff2n(k) 
# print(tm)
#^^^ This is the test matrix to compare your testing order. "-1" is a low value
#^^^ and "1" is high. You need to make sure the order of the results placed in 
#^^^ "test" match the matrix "tm". In general "tm" follows the following pattern:
    
#[-1,-1,-1]   #The pattern is that the first column alternates by ones, 
#[ 1,-1,-1]   #the second column alternates by twos, and the third  column
#[-1, 1,-1]   #alternates by fours, etc, all beginning with the low values.
#[ 1, 1,-1]   
#[-1,-1, 1]    
#[ 1,-1, 1]
#[-1, 1, 1]
#[ 1, 1, 1]

#%% The running part of the code. This is where the work is done. No changes 
#are needed here to run the study. 
g = []
combin = []
te = ''
for i in range(k): 
    exec(f"dict{i+1} = "+"{}") 

for i in range(k):
    key1 = var_name(i)
    for j in range(k-1-i):
        key2 = var_name(i)+var_name(j+1+i)
        p = [i,j+1+i]
        exec("dict2[key2]=twok(test,tm,k,p,2)")
    exec("dict1[key1]=twok(test,tm,k,i,1)")
    combin.append(i)
    
for z in range (k-2):
    o = z+3
    y3 = set(list(itertools.combinations(combin,o)))
    for i in range(1):
       for id,val in enumerate(y3):
           for j in range(o):
               g.append(val[j])
           for l in range(o):
               te+=var_name(g[l])
           exec(f"key{o} = te")
           exec(f"dict{o}[key{o}]=twok(test,tm,k,g,o)")
           g = []
           te = ''
if 'filename' in locals():
    check = 1
else:
    filename = "Unnamed - data entered by hand"

    exec(f"print(dict{i+1})")
    if savefile=='y':
        exec(f"writefile(filewrite, dict{i+1},k,i,filename)")
