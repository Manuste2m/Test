import  xlrd , datetime , unittest

class Business:
    def __init__(self):
        self.filename = ''

    def setFilename(self,name):
        self.filename = name
        workbook = xlrd.open_workbook(self.filename)
        self.sheed = workbook.sheet_by_index(0)


    def Headlist(self):
        self.listHead = []
        for x in range(self.sheed.ncols):
                    self.listHead.append(str(self.sheed.cell_value(0, x)))
        return (self.listHead)

    #Function searchHead from the Headname
    def searchHead(self,name):
        for x in range(len(self.listHead)):
            if(self.listHead[x]==name):
                return x

    def listINheadN(self,name):
        listHead = []
        numHead = self.searchHead(name)
        word = 0
        for x in range(1,self.sheed.nrows):
            word = 0
            if x == 0 :
                listHead.append(str(self.sheed.cell_value(x,numHead)))
            if x > 0:
                for wordname in range(len(listHead)):
                    if (str(self.sheed.cell_value(x,numHead))) == listHead[wordname] :
                        word = 1
                if word == 0 :
                    listHead.append(str(self.sheed.cell_value(x,numHead)))
        return (listHead)

    def listDimensionsFunc(self,nameHead,name):
        numlist = []
        Head = self.searchHead(nameHead)
        for x in range(1, self.sheed.nrows):
            if((self.sheed.cell_value(x, Head))==name):
                    numlist.append(x)
        return numlist

    def listYear(self,year,dateHead):
        numlist = []
        for x in range(1, self.sheed.nrows):
            load = self.sheed.cell_value(x, dateHead)
            timeNew = xlrd.xldate_as_tuple(load,0)
            timeNewer = str(datetime.datetime(*timeNew))
            dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
            if(("%s"%dateAll.year)==year):
                numlist.append(x)
        return numlist

    def listDate(self,Date,dateHead):
        numlist = []
        for x in range(1, self.sheed.nrows):
            load = self.sheed.cell_value(x, dateHead)
            timeNew = xlrd.xldate_as_tuple(load,0)
            timeNewer = str(datetime.datetime(*timeNew))
            dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
            year = int(("%s"%dateAll.year))
            month = int(("%s"%dateAll.month))
            day = int(("%s"%dateAll.day))

            d = (str(day)+"/"+str(month)+"/"+(str(year)))
            if(d==Date):
                numlist.append(x)
        return numlist

B = Business()
A = Business()
A.setFilename("/Users/Verapong/Desktop/Bi/test.xlsx")

class display:
    def __init__(self,SomeThing):
        print (SomeThing)

class Test:
    def __init__(self):
        print ("TEST EIEI")
        B.setFilename("/Users/Verapong/Desktop/Bi/Mini.xlsx")

print (A.Headlist())
Headlist = A.Headlist()
HeadInlist = A.listINheadN(Headlist[1])
show = A.listDimensionsFunc(Headlist[1],HeadInlist[0])
print (show)


class TestStringMethods(unittest.TestCase):

    def test_Head(self):
        self.assertEquals((Headlist),['Zone','County','Sale','Date','Quantity'])

    def test_InHead(self):
        self.assertEquals(A.listINheadN(Headlist[0]),['Asia','Europe'])

    def test_location(self):
        self.assertEquals(show ,[1,7,9,10,12,18,20,21,23,29,31,32,34,40,42,43,45,51,53,54,56,62,64,65,67,73,75,76,78,84,86,87,89,95,97,98,100,106,108,109,111,117,119,120,122,128,130,131])

if __name__ == '__main__':
    unittest.main()