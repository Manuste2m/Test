import xlrd , unittest

workbook = xlrd.open_workbook("/Users/Verapong/Desktop/Bi/test.xlsx")
sheed = workbook.sheet_by_index(0)

def func():
    listHead = []
    for x in range(sheed.ncols):
        listHead.append(str(sheed.cell_value(0, x)))
    return listHead

def searchHead(name):
        for x in range(len(func())):
            if(((func()[x])==name)):
                return x
saveHead = func()
print (saveHead)

def listINheadN(name):
    listHead = []
    numHead = searchHead(name)
    word = 0
    for x in range(1,sheed.nrows):
        word = 0
        if x == 0 :
            listHead.append(str(sheed.cell_value(x,numHead)))
        if x > 0:
            for wordname in range(len(listHead)):
                if (str(sheed.cell_value(x,numHead))) == listHead[wordname] :
                    word = 1
            if word == 0 :
                listHead.append(str(sheed.cell_value(x,numHead)))
    return (listHead)

print (listINheadN(saveHead[1]))
saveInHead = listINheadN(saveHead[1])


def listDimensionsFunc(nameHead,name):
    numlist = []
    Head = searchHead(nameHead)
    for x in range(1, sheed.nrows):
        if((sheed.cell_value(x, Head))==name):
            numlist.append(x)
    return numlist

print (listDimensionsFunc(saveHead[1],saveInHead[0]))

#def test_answer():
    #assert func("/Users/Verapong/Desktop/Bi/test.xlsx") == ['Zone','County','Sale','Date','Quantity']



class TestStringMethods(unittest.TestCase):

    def test_Head(self):
        self.assertEquals(func(),['Zone','County','Sale','Date','Quantity'])

    def test_InHead(self):
        self.assertEquals(listINheadN(func()[0]),['Asia','Europe'])

    def test_location(self):
        self.assertEquals((listDimensionsFunc(saveHead[1],saveInHead[0])) ,[1,7,9,10,12,18,20,21,23,29,31,32,34,40,42,43,45,51,53,54,56,62,64,65,67,73,75,76,78,84,86,87,89,95,97,98,100,106,108,109,111,117,119,120,122,128,130,131])



if __name__ == '__main__':
    unittest.main()