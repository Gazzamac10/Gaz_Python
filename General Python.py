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
list1 = IN[0]
list2 = IN[1]
list3 = IN[2]

v = [round(item, 2) for item in list1]

values = sorted(set(map(lambda x: x, v)))


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


ygroup = [getitemsinlist1(values[i], v, list2) for i in range(len(values))]
xgroup = [getitemsinlist2(values[i], v, list2) for i in range(len(values))]
pgroup = [getitemsinlist2(values[i], v, list3) for i in range(len(values))]

OUT = ygroup, xgroup, pgroup


#sort list by Key list#
X = [1,3,2,4,6,7,5,3]
Y = [9,6,5,4,3,4,5,6]

t = [x for y, x in sorted(zip(X, Y))]

#flattenlist#
flat_list = [item for sublist in l for item in sublist]