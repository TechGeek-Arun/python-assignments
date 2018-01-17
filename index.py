import socket 
import struct
import os
from xml.dom import minidom

print "################"
print "##Assignment 1##"
print "################"
mylist = range(4)
seclist = mylist
print seclist
mylist.append(4)
print seclist
seclist = mylist[:]
print seclist
mylist.append(5)
print seclist
'''
----------------
--Assignment 1--
----Output------
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
----------------
'''
print "################"
print "##Assignment 2##"
print "################"
def f(n):
    for x in range(n):
        yield x**3

for x in f(6):
    print x

'''
----------------
--Assignment 2--
----Output------
0
1
8
27
64
125
----------------
'''
print "################"
print "##Assignment 3##"
print "################"
count = 0
input_string = raw_input("Enter the input string:")

for c in input_string:
    if "e" in c:
        count += 1

if count == 2:
    print 'True'
else:
    print 'False'
'''
----------------
'''
print "################"
print "##Assignment 4##"
print "################"
counter = 1
def dolots(count):
  global counter
  for i in (1, 2, 3):
    counter = count + i

print dolots(4)
print counter
'''
----------------
--Assignment 4--
----Output------
None
7
----------------
'''
print "################"
print "##Assignment 5##"
print "################"
def countFile():
    characters = lines = words = 0
    with open("input.txt" , "r") as inputfile:
        for line in inputfile:
            lines += 1
            words += len(line.split())
            characters  += len(line)
    f = open("output.txt", "w")
    f.write("Number of Lines: %s \n Number of Words per line: %s \n Number of Characters per line: %s" %(lines,words,characters))

countFile()
print "Check output in output.txt in the file explorer"
'''
----------------
'''
print "################"
print "##Assignment 6##"
print "################"
#Initialise three lists
list1 = [5, 36, 2, 92, 125]
list2 = [63, 58, 100, 47, 22]
list3 = [27, 1, 59, 20, 80]

#Initialise maximum and minimum list
maxlist = []
minlist = []

#Initialise average of maximum and minimum list
avgMin = avgMax = 0

#function to create maximum and minimum list
def MaxMinList(list):
    copy_of_list=list[:]
    first = second = first_Last = second_Last= None
    copy_of_list.sort()
    n=len(copy_of_list)
    first, second , first_Last , second_Last = copy_of_list[n-1], copy_of_list[n-2], copy_of_list[0], copy_of_list[1]
    maxlist.extend([ first, second])
    minlist.extend([ first_Last, second_Last])

#calling MaxMinList(list) function
MaxMinList(list1)
MaxMinList(list2)
MaxMinList(list3)

#Printing average of maximum and minimum list
print "Maximum List = " , maxlist
print "Maximum List Average = " , sum(maxlist) / len(maxlist)
print "Minimum List = " , minlist
print "Minimum List Average = " , sum(minlist) / len(minlist)
'''
----------------
--Assignment 6--
----Output------
Maximum List =  [125, 92, 100, 63, 80, 59]
Maximum List Average =  86
Minimum List =  [2, 5, 22, 47, 1, 20]
Minimum List Average =  16
----------------
'''
print "################"
print "##Assignment 7##"
print "################"

data=raw_input("Enter the Prefix value:\n");
def cidrToNetmask(prefix):
    print socket.inet_ntoa(struct.pack(">I", (0xffffffff<<(32 - prefix))&0xffffffff))
cidrToNetmask(int(data))
'''
----------------
'''
print "################"
print "##Assignment 8##"
print "################"

document = minidom.parse('data.xml')
books = document.getElementsByTagName("book")
for book in books:
    print "-------------------------------------------"
    category =  book.getAttribute("category")
    title = book.getElementsByTagName("author")[0].firstChild.data
    year = book.getElementsByTagName("year")[0].firstChild.data
    price = book.getElementsByTagName("price")[0].firstChild.data
    print("Category:%s \n Title:%s \n Year:%s \n Price:%s" % (category, title, year, price))
    print "-------------------------------------------"
'''
----------------
'''
print "################"
print "##Assignment 9##"
print "################"

#finding all the files from current directory
for file in os.listdir("."):
    #finding sizr of each file
    size = os.stat(file).st_size
    #if file_size = 0 then print filename
    if(size == 0):
        print file
'''
----------------
'''
print "#################"
print "##Assignment 10##"
print "#################"

#defining a object set with duplicate values
things_set = {"table", "chair", "window", "door", "carpet", "monitor", "table", "telephone"}

#checking if duplicate value from above set has been removed
print(things_set)
'''
-----------------
--Assignment 10--
----Output-------
set(['door', 'monitor', 'telephone', 'window', 'table', 'chair', 'carpet'])
-----------------
'''
