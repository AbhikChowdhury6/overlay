import matplotlib.pyplot as plt
import sys
import fnmatch
import os

for file in os.listdir(sys.argv[1]):
    if fnmatch.fnmatch(file,'*ACCEL_X*'):
        Xf = file
    if fnmatch.fnmatch(file,'*ACCEL_Y*'):
        Yf = file
    if fnmatch.fnmatch(file,'*ACCEL_Z*'):
        Zf = file

with open(sys.argv[1]+Xf, 'r') as myfile:
    raw=myfile.read().replace('\n', '')
Xs = raw.split(",")
Xs.pop()
Xu=map(int,Xs)
X = [x / 16384.0 for x in Xu]




with open(sys.argv[1]+Yf, 'r') as myfile:
    raw=myfile.read().replace('\n', '')
Ys = raw.split(",")
Ys.pop()
Yu=map(int,Ys)
Y = [y / 16384.0 for y in Yu]



with open(sys.argv[1]+Zf, 'r') as myfile:
    raw=myfile.read().replace('\n', '')
Zs = raw.split(",")
Zs.pop()
Zu=map(int,Zs)
Z = [z / 16384.0 for z in Zu]



print "number of data poits X: " + str(len(X))
print "number of data poits Y: " + str(len(Y))
print "number of data poits Z: " + str(len(Z))


#print s
plt.plot(X)
plt.plot(Y)
plt.plot(Z)
plt.ylabel('Acceleration (m/s^2)')
plt.xlabel('Time (ms)')
plt.legend(['X', 'Y', 'Z'], loc='upper left')
plt.show()
