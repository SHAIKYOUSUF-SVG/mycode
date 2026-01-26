'''
diffrence between python2 and python 3?
python2 will expand the range-performancewill decrese
python3 will not expand range
xrange is python2 to handle python3 range
python3 doesnot have xrange
'''

print "hi"


out=range(5000000000000000000)
print(out) #in python2 for this range fucn performence is low

out=xrange(4,7)
print(out) #xrange in python 2 to overcome the range


