import matplotlib.pyplot as plt
import sys

with open(sys.argv[1], 'r') as myfile:
    raw=myfile.read().replace('\n', '')
s = raw.split(",")
s.pop()
print "number of data poits: " + str(len(s))

#print s
plt.plot(map(int,s))
plt.ylabel('some numbers')
plt.show()
