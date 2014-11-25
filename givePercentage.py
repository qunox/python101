from __future__ import  division

def givePercentage(value, originalValue):

    return (originalValue - value) / originalValue * 100

valueA = givePercentage(10 , 100)
print valueA
#will print --> 90.0
print givePercentage(20 ,100)
#will print --> 80.0

