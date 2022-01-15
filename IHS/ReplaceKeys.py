import sys
import os

mydict = {}
with open(sys.argv[1], 'r') as mapping_file:
    dictValues = mapping_file.readlines()
    for data in dictValues:
        dataLength = len(data) - 1
        while(dataLength > 0):

            # print(data)
            a = data.split(" ")
            mydict.update({a[0]: a[1].rstrip("\n")})
            dataLength -= 1
    print(mydict)

rootdir = sys.argv[2]

print('rootdir = ' + rootdir)

for dname, dirs, files in os.walk(os.path.abspath(rootdir)):
    for fname in files:
        fpath = os.path.join(dname, fname)
        print(fpath)
        for key, value in mydict.items():
            print(key, value)
            with open(fpath) as f:
                s = f.read()
            s = s.replace(key, value)
            with open(fpath, "w") as f:
                f.write(s)
