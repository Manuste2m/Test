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

    def listMonth(self,month,dateHead):
        numlist = []
        for x in range(1, self.sheed.nrows):
            load = self.sheed.cell_value(x, dateHead)
            timeNew = xlrd.xldate_as_tuple(load,0)
            timeNewer = str(datetime.datetime(*timeNew))
            dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
            if(("%s"%dateAll.month)==month):
                numlist.append(x)
        return numlist

    def wordAgain(self,listAll):
        listAllnew = []
        for i in range(len(listAll)):
            x = 0
            for j in range(i+1,len(listAll)):
                if (listAll[i]==listAll[j]):
                    x = x+1
            if x == 0 :
                listAllnew.append(listAll[i])
        return listAllnew

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

    def setlist(self):
        MeasuresList = ["Sale","Quantity"]
        DontDimensions = ["Name","ID"]

        self.listTypeMeasures = []
        self.listTypeMeasuresLocation = []

        self.listTypeDimensions = []
        self.listTypeDimensionsLocation = []

        self.listTypeDate = []
        self.listTypeDateLocation = []

        self.listTypeInDimensions = []
        self.listSaveGUI = []

        DontTypeDimensions = []
        DontTypeDimensionsLocation = []

        for x in range(self.sheed.ncols):
            print (type(self.sheed.cell_value(1, x)))
            if type(self.sheed.cell_value(1, x)) == type(float()) :
                for j in range(len(MeasuresList)):
                    if(MeasuresList[j] in self.listHead[x]):
                        self.listTypeMeasures.append(self.listHead[x])
                        self.listTypeMeasuresLocation.append(x)
                if("Date" in self.listHead[x]):
                        self.listTypeDate.append(self.listHead[x])
                        self.listTypeDateLocation.append(x)

            if type(self.sheed.cell_value(1, x)) == type(str()) :
                if("Date" in self.listHead[x]):
                    self.listTypeDate.append(self.listHead[x])
                    self.listTypeDateLocation.append(x)
                else :
                    print (self.listHead[x])
                    self.listTypeDimensions.append(self.listHead[x])
                    self.listTypeDimensionsLocation.append(x)

        for j in range(len(DontDimensions)):
            for x in range (len(self.listTypeDimensions)):
                if (DontDimensions[j] in self.listTypeDimensions[x]):
                    DontTypeDimensions.append(self.listTypeDimensions[x])
                    DontTypeDimensionsLocation.append(self.listTypeDimensionsLocation[x])

        for i in range(len(DontTypeDimensions)):
            self.listTypeDimensions.remove(DontTypeDimensions[i])

        for i in range(len(DontTypeDimensionsLocation)):
            self.listTypeDimensionsLocation.remove(DontTypeDimensionsLocation[i])

        for x in range(len(self.listTypeDimensions)):
            print (self.listINheadN(self.listTypeDimensions[x]))
            if (len(self.listINheadN(self.listTypeDimensions[x]))) > 128 :
                print (self.listTypeDimensions[x])
                self.listSaveGUI.append(x)
            else:
                self.listTypeInDimensions.append(self.listINheadN(self.listTypeDimensions[x]))

        for x in range(len(self.listSaveGUI)):
            self.listTypeDimensions.remove(self.listTypeDimensions[self.listSaveGUI[x]])
            self.listTypeDimensionsLocation.remove(self.listTypeDimensionsLocation[self.listSaveGUI[x]])

    def setYearlist(self,dateHead):
        self.yearlist = []
        for x in range(1, self.sheed.nrows):
            load = self.sheed.cell_value(x, dateHead)
            timeNew = xlrd.xldate_as_tuple(load,0)
            timeNewer = str(datetime.datetime(*timeNew))
            dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
            year = str(("%s"%dateAll.year))
            self.yearlist.append(year)
        self.yearlist = (self.wordAgain(self.yearlist))
        self.yearlist.sort()

    def saleMonth(self,Name,Measures,month,year,dateHead):
        Sale = 0
        plotHead = self.searchHead(Measures)
        yearlist = self.listYear(year,dateHead)
        monthlist = self.listMonth(month,dateHead)
        datelist = self.returnMatches(yearlist,monthlist)
        print (datelist)
        namelist = self.listInDimensionsFunc(Name)
        sumlist = self.returnMatches(datelist,namelist)
        print (sumlist)
        if (len(sumlist) != 0):
            for i in range(len(sumlist)):
                Sale = Sale + self.sheed.cell_value(sumlist[i], plotHead)
        else:
            Sale = 0
        return  Sale

    def returnMatches(self,a,b):
       return list(set(a) & set(b))

    def getlistTypeDate(self):
        return self.listTypeDate
    def getlistTypeDateLocation(self):
        return self.listTypeDateLocation
    def getlistTypeDimensions(self):
        return self.listTypeDimensions
    def getlistTypeDimensionsLocation(self):
        return self.listTypeDimensionsLocation
    def getlistTypeMeasures(self):
        return self.listTypeMeasures
    def getlistTypeMeasuresLocation(self):
        return self.listTypeMeasuresLocation
    def getlistTypeInDimensions(self):
        return self.listTypeInDimensions
    def getlistSaveGUI(self):
        return self.listSaveGUI
    def getlistyear(self):
        return self.yearlist
    def getlistHead(self):
        return self.listHead

    def listDimensionsFunc(self,nameHead,name):
        numlist = []
        Head = self.searchHead(nameHead)
        for x in range(1, self.sheed.nrows):
            if((self.sheed.cell_value(x, Head))==name):
                    numlist.append(x)
        return numlist

    def listInDimensionsFunc(self,name):
        for i in range(len(self.listTypeInDimensions)):
            for j in range (len(self.listTypeInDimensions[i])):
                if name == self.listTypeInDimensions[i][j] :
                    return (self.listDimensionsFunc(self.listTypeDimensions[i],name))

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

Test()
B.Headlist()
B.setlist()
B.setYearlist(14)
yearlist = B.getlistyear()
print (yearlist)
sumA = B.listYear('2012',14)
sumB = B.listMonth('1',14)
sale = B.saleMonth('High','Sales','1','2012',14)
print (sale)


"""class TestStringMethods(unittest.TestCase):

    def test_Head(self):
        self.assertEquals((Headlist),['Zone','County','Sale','Date','Quantity'])

    def test_InHead(self):
        self.assertEquals(A.listINheadN(Headlist[0]),['Asia','Europe'])

    def test_location(self):
        self.assertEquals(show ,[1,7,9,10,12,18,20,21,23,29,31,32,34,40,42,43,45,51,53,54,56,62,64,65,67,73,75,76,78,84,86,87,89,95,97,98,100,106,108,109,111,117,119,120,122,128,130,131])
"""
#if __name__ == '__main__':
    #unittest.main()