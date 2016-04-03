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

#def test_answer():
    #assert func("/Users/Verapong/Desktop/Bi/test.xlsx") == ['Zone','County','Sale','Date','Quantity']



class TestStringMethods(unittest.TestCase):

  def test_Head(self):
      self.assertEquals(func(),['Zone','County','Sale','Date','Quantity'])

  def test_InHead(self):
      self.assertEquals(listINheadN(func()[0]),['Asia','Eupore'])

if __name__ == '__main__':
    unittest.main()