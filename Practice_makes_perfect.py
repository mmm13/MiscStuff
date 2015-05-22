{\rtf1\ansi\ansicpg1252\cocoartf1344\cocoasubrtf720
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 ####remove all odd numbers from num_list\
def purify(num_list):\
     return [ x for x in num_list if x % 2 == 0]      \
\
print (purify([1,2,3,4,5,6,7,8,9,10]))\
\
\
#### return # of times item is in sequence\
def count(sequence, item):\
    times =0\
    for i in sequence:\
        if i == item:\
            times += 1\
    return times\
\
######return product of list\
def product (int_list) :\
     product=1\
     for i in int_list:\
         product *= i\
    return product\
\
#####remove duplicates from a list\
def remove_duplicates(num_list) :\
    new_list=[]\
    for element in num_list:\
         if element not in new_list:\
             new_list.append(element)      \
    return new_list\
    \
    \
print (remove_duplicates([4,5,5,4]))   \
\
\
\
####finding the median\
def median(numlist):\
    sorted(numlist)\
    numlist = sorted(numlist)\
    if len(numlist) % 2 != 0:\
        return numlist[(len(numlist) / 2)]\
    else:\
        med1 = numlist[len(numlist) / 2 - 1]\
        med2 = numlist[len(numlist) / 2]\
        medTotal = (med1 + med2) / 2.0\
        return medTotal\
\
}