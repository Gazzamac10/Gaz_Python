GH Python
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext
import clr
clr.AddReference("Grasshopper")
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper import DataTree
from System import Object

#list to tree
def raggedListToDataTree(raggedList):
    rl = raggedList
    result = DataTree[object]()
    for i in range(len(rl)):
        temp = []
        for j in range(len(rl[i])):
            temp.append(rl[i][j])
        #print i, " - ",temp
        path = GH_Path(i)
        result.AddRange(temp, path)
    return result


def dataTreeToList(aTree):
    theList = []
    for i in range(aTree.BranchCount ):
        thisListPart = []
        thisBranch = aTree.Branch(i)
        for j in range(len(thisBranch)):
            thisListPart.append( thisBranch[j] )
        theList.append(thisListPart)
    return theList



inputlist = []
for i in range(len(ghenv.Component.Params.Input)):
    inputlist.append(ghenv.Component.Params.Input[i])

def infoinlist(x):
    b = []
    for item in x.VolatileData:
        b.append(item)
    return b

paramlist = []
for item in inputlist:
    paramlist.append(infoinlist(item))

list  = [[j[i] for j in paramlist] for i in range(len(paramlist))]


import os

dir = "C:\\temp\Python\Dev\Autodesk Library\Columns and Framing\Structural Framing\Steel\British Standard"
os.listdir(dir)

path = dir + "\\" + "_ACM_S_SBM_UB.csv"
f = open(path, 'r')
a = f.readlines()


import xlrd

name = "C:\\temp\Python\Dev\Blue Book Steelwork\Direct Export\UB-secpropsdimsprops-EC3(UKNA)-UK-8-8-2017.xlsx"
workbook = xlrd.open_workbook(name)
sheet = workbook.sheet_by_index(0)

columns = []
for colx in range(sheet.ncols):
    columns.append(sheet.col_values(colx))

rows = []
for rowx in range(sheet.nrows):
    rows.append(sheet.row_values(rowx))

f = open(Path,"w")
for item in fileout:
    f.write("%s\n" % item)
f.close()