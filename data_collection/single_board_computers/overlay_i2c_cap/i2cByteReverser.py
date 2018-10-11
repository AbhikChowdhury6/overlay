import os
import sys


with open(sys.argv[1], 'r') as myfile:
    raw=myfile.read().replace('\n', '')
s = raw.split(",")
s.pop()
print "number of data poits: " + str(len(s))
fo = open(sys.argv[2], "a+")

for i in s:
  secondbyte = int(i) % 256
  firstbyte = int(int(i) / 256)
  out = (secondbyte << 8)+ firstbyte
  print i + " to " + str(out)
  fo.write(str(out)+",")

print "converted data poits: " + str(len(s))
