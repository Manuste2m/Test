import xlrd , unittest

def func(filename):
    workbook = xlrd.open_workbook(filename)
    sheed = workbook.sheet_by_index(0)
    listHead = []
    for x in range(sheed.ncols):
        listHead.append(str(sheed.cell_value(0, x)))
    return listHead

#def test_answer():
    #assert func("/Users/Verapong/Desktop/Bi/test.xlsx") == ['Zone','County','Sale','Date','Quantity']



class TestStringMethods(unittest.TestCase):

  def test_Head(self):
      self.assertEquals(func("/Users/Verapong/Desktop/Bi/test.xlsx"),['Zone','County','Sale','Date','Quantity'])


if __name__ == '__main__':
    unittest.main()