#move files#
os.rename("path/to/current/file.foo", "path/to/new/desination/for/file.foo")

import os
temp = os.listdir("P:\UKLON06-BE-Structural\Projects\Structures - Hong Kong T2\\5_BIM\\1_Stru\9_Rhino\Data\Sat_Files")


#Dynamo Get file in dir
from System.IO import Directory
dir = IN[0]
if Directory.Exists(dir):
	OUT = Directory.GetFiles(dir)

#findindexinlist#
def ifequal(a,b):
    return [i for i, item in enumerate(a) if item == b]


#If equal return Index(finding index of a in b)#
def ifequal(b,a):
	indiceslist = []
	for lA in a:
		counter = 0
		for lB in b:
			if (lA == lB):
				indiceslist.append(counter)
			counter += 1
	return indiceslist


#loops#
Rev =[Rev[i]+","+g[i] for i in xrange(len(a))]


#split string#
ASplit = [a[i].split(",") for i in range(len(a))


#remove at index#
[x.pop(0) for x in G_Beams]


#join string#
G_Beams = [",".join(G_Beams[i])for i in range(len(G_Beams))]


#open file#
Path = IN[0]
f = open(Path, 'r')
a = f.readlines()


#write file#
if Activate == True:
    f = open(Path,"w") #opens file with name of "test.txt"
    for item in Rev:
        f.write("%s\n" % item)
    f.close()

#open and change file#
with open(filename) as f:
    file_str = f.read()

# do stuff with file_str

with open(filename, "w") as f:
    f.write(file_str)



#Sort points by y then x#
list1 = y
list2 = x

values = sorted(set(map(lambda x: x, list1)))


def getitemsinlist1(string, list1, list2):
	lista = []
	for i in range(len(list1)):
		if list1[i] == string:
			lista.append(list1[i])
	return lista


def getitemsinlist2(string, list1, list2):
	lista = []
	for i in range(len(list1)):
		if list1[i] == string:
			lista.append(list2[i])
	return lista


def getitemsinlist3(string, list1, list2):
	lista = []
	for i in range(len(list1)):
		if list1[i] == string:
			lista.append(list2[i])
	return lista


ygroup = [getitemsinlist1(values[i], y, x) for i in range(len(values))]
xgroup = [getitemsinlist2(values[i], y, x) for i in range(len(values))]
pgroup = [getitemsinlist2(values[i], y, z) for i in range(len(values))]

a = ygroup[2]
b = xgroup[2]
OUT = pgroup[2]