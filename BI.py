import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import datetime, xlrd ,time, sys , os ,csv

#GUI Business intelligence
class Window:
    def __init__(self, master):
        self.filename = "" #filename_waitOpen
        self.root = master #createGUI
        self.root.title("Business intelligence") #GUI_name

        menuBar = Menu(self.root) #createMenuBarOnGUI
        fileMenu = Menu(menuBar)    #createMenu
        fileMenu.add_command(label = "Open",command=self.chooseFile) #addMenu_Open
        fileMenu.add_command(label = "Close",command=self.closeGUI) #addMenu_Closef
        menuBar.add_cascade(label = "File",menu=fileMenu) #addMenuInMenuBarFile
        self.root.config(menu=menuBar) #ShowMenuBarOnGui

        self.f1 = Frame(self.root,width=1200, height=550) #CreatePage1_onGui
        self.f2f = Frame(self.root,width=1200, height=550) #CreatePage2_onGui

        for frame in (self.f1, self.f2f):
            frame.grid(row=0, column=0, sticky='news') #ShowPage

        #ButtonDimensions
        self.HeadButton = []
        self.listHeadShow = []

        #ButtonInDimensions
        self.inDimensionsButton = []
        self.listInDimensionsButton = []
        self.listInDimensionsPlot = []

        #ButtonAllInDimensions
        self.DimensionsButton = []
        self.listDimensionsButton = []
        self.listDimensionsPlot = []

        #ButtonMeasures
        self.MeasuresButton = []
        self.listMeasuresButton = []
        self.listMeasuresPlot = []

        #ButtonDate
        self.DateButton = []
        self.listDateButton = []
        self.listDatePlot = []

        #ButtonTypePlot
        self.checkTypePlot = []
        self.listTypePlot = []
        self.plotType = []

        #PlotShow
        self.canvas = []
        self.plotTypeOlt = []

    #CreteScrollbarONPage2_by_len(listInDimensions)
    def scrollbarInFrame2(self,lenForH):

        #Add a canvas to the Page2
        self.canvasInf2 = Canvas(self.f2f,bg="white")
        self.canvasInf2.grid(column=0, row=0, sticky=N+S+E+W)

        #Allow the canvas (in row/column 0,0)
        #to "grow" to fill the entire window.
        self.f2f.grid_rowconfigure(0, weight=1)
        self.f2f.grid_columnconfigure(0, weight=1)


        #Add a scrollbar that will scroll the canvas vertically
        vscrollbar = Scrollbar(self.f2f)
        vscrollbar.grid(column=1, row=0, sticky=N+S)
        #Link the scrollbar to the canvas
        self.canvasInf2.config(yscrollcommand=vscrollbar.set)
        vscrollbar.config(command=self.canvasInf2.yview)

        #Add a scrollbar that will scroll the canvas horizontally
        hscrollbar = Scrollbar(self.f2f, orient=HORIZONTAL)
        hscrollbar.grid(column=0, row=1, sticky=E+W)
        self.canvasInf2.config(xscrollcommand=hscrollbar.set)
        hscrollbar.config(command=self.canvasInf2.xview)

        #CreateFrame for CreatePage2
        self.f2inF = Frame(self.canvasInf2)

        #SetSize_Page2 and ShowPage2
        lenForH = lenForH + 11
        height = lenForH * 30
        if height < 530 :
            height = 530
        else :
            height = height

        self.f2 = Canvas(self.f2inF,bg="white",width=1900, height=height)
        self.f2.grid(row=0, column=0)

        #Add the frame to the canvas
        self.canvasInf2.create_window((0,0), anchor=NW, window=self.f2inF)

        #IMPORTANT:
        self.f2inF.update_idletasks() #REQUIRED: For f.bbox() below to work!

        #Tell the canvas how big of a region it should scroll
        self.canvasInf2.config(scrollregion= self.f2inF.bbox("all"))

    #Function OpenFile
    def chooseFile(self):
        self.filename = filedialog.askopenfilename() #Get a filename to open
        nameFolder = self.fileName(self.filename) #Filename
        self.ensure_dir(nameFolder) #Function_SearchFolde,andCreateFileData
        os.chdir('/Users/Verapong/Desktop/'+(str(nameFolder))) #Working directory On Given path
        self.headDimensions() #UseFunctionHeadDimensions
        self.raise_frame(self.f1) #Go to the Page1

    #Function return Filename From filename
    def fileName(self,filename):
        x = 0
        x2 = 0
        for i in range(len(filename)):
            if filename[i] == '/' :
                x = i+1
            if filename[i] == '.' :
                x2 = i
        return (filename[x:x2])

    #Function searchNamelist in the Headname
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

    #Function searchAllNamelist in the Headname
    def listINhead(self,head):
        listName = []
        numHead = self.searchHead(head)
        for x in range(1,self.sheed.nrows):
            listName.append(str(self.sheed.cell_value(x,numHead)))
        return (listName)

    #Function searchHead from the Headname
    def searchHead(self,name):
        for x in range(len(self.listHead)):
            if(self.listHead[x]==name):
                return x

    #Function Cut_RepiatWord into list
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

    #Function searchColumn from the theNameinHeadname
    def listDimensionsFunc(self,nameHead,name):
        numlist = []
        Head = self.searchHead(nameHead)
        for x in range(1, self.sheed.nrows):
            if((self.sheed.cell_value(x, Head))==name):
                    numlist.append(x)
        return numlist

    #Function searchColumn from the InDimensionslist
    def listInDimensionsFunc(self,name):
        for i in range(len(self.listTypeInDimensions)):
            for j in range (len(self.listTypeInDimensions[i])):
                if name == self.listTypeInDimensions[i][j] :
                    return (self.listDimensionsFunc(self.listTypeDimensions[i],name))

    #Function searchColumn from Year and rowHead
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

    #Function createFolder and creteCSVdatefile if don't have Folder On the Desktop
    def ensure_dir(self,nameFolder):
        MeasuresList = ["Sale","Quantity"]
        DontDimensions = ["Name","ID"]
        locationFolder = '/Users/Verapong/Desktop/'+str(nameFolder)
        newpath = locationFolder
        if os.path.exists(newpath):
            print ("Have, This Folder On the Desktop")
        else:
            self.raise_frame(self.f1)
            os.makedirs(newpath) #Create Folder
            os.chdir(newpath)
            workbook = xlrd.open_workbook(self.filename)
            self.sheed = workbook.sheet_by_index(0)
            self.listHead = []
            for x in range(self.sheed.ncols):
                        self.listHead.append(str(self.sheed.cell_value(0, x)))
            print (self.listHead)

            self.listTypeMeasures = []
            self.listTypeMeasuresLocation = []

            self.listTypeDimensions = []
            self.listTypeDimensionsLocation = []

            self.listTypeDate = []
            self.listTypeDateLocation = []

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

            print (self.listTypeDimensions)
            print (self.listTypeDimensionsLocation)

            DontTypeDimensions = []
            DontTypeDimensionsLocation = []
            for j in range(len(DontDimensions)):
                for x in range (len(self.listTypeDimensions)):
                    if (DontDimensions[j] in self.listTypeDimensions[x]):
                        DontTypeDimensions.append(self.listTypeDimensions[x])
                        DontTypeDimensionsLocation.append(self.listTypeDimensionsLocation[x])

            for i in range(len(DontTypeDimensions)):
                self.listTypeDimensions.remove(DontTypeDimensions[i])

            for i in range(len(DontTypeDimensionsLocation)):
                self.listTypeDimensionsLocation.remove(DontTypeDimensionsLocation[i])


            self.listTypeInDimensions = []
            self.listSaveGUI = []
            print ("Wait")
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


            print (self.listTypeMeasures)
            print (self.listTypeMeasuresLocation)

            with open("Measures.csv",'w',newline='') as fp:
                a = csv.writer(fp,delimiter=',')
                data= [['listTypeMeasures','listTypeMeasuresLocation']]
                a.writerows(data)
                for i in range(len(self.listTypeMeasures)):
                    data= [[self.listTypeMeasures[i],self.listTypeMeasuresLocation[i]]]
                    a.writerows(data)

            print (self.listTypeDimensions)
            print (self.listTypeDimensionsLocation)

            with open("Dimensions.csv",'w',newline='') as fp:
                a = csv.writer(fp,delimiter=',')
                data= [['listTypeDimensions','listTypeDimensionsLocation']]
                a.writerows(data)
                for i in range(len(self.listTypeDimensions)):
                    data= [[self.listTypeDimensions[i],self.listTypeDimensionsLocation[i]]]
                    a.writerows(data)

            print (self.listTypeDate)
            print (self.listTypeDateLocation)

            with open("Date.csv",'w',newline='') as fp:
                a = csv.writer(fp,delimiter=',')
                data= [['listTypeDate','listTypeDateLocation']]
                a.writerows(data)
                for i in range(len(self.listTypeDate)):
                    data= [[self.listTypeDate[i],self.listTypeDateLocation[i]]]
                    a.writerows(data)

            with open("InDimensions.csv",'w',newline='') as fp:
                a = csv.writer(fp,delimiter=',')
                for i in range(len(self.listTypeInDimensions)):
                    listDimensions = self.listTypeInDimensions[i]
                    data= [listDimensions]
                    a.writerows(data)

            yearlist = []
            countylist = []


            for i in range(len(self.listTypeInDimensions)):
                countylist.append([])
                for j in range(len(self.listTypeInDimensions[i])):
                    print (self.listTypeInDimensions[i][j])
                    countylist[i].append(self.listInDimensionsFunc(self.listTypeInDimensions[i][j]))

            print ("=====Check======")

            ##Year
            print (len(self.listTypeDate))

            for countDate in range(len(self.listTypeDate)):
                dateHead = self.searchHead(self.listTypeDate[countDate])
                print (self.listTypeDate[countDate])

                for x in range(1, self.sheed.nrows):
                    load = self.sheed.cell_value(x, dateHead)
                    timeNew = xlrd.xldate_as_tuple(load,0)
                    timeNewer = str(datetime.datetime(*timeNew))
                    dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
                    year = str(("%s"%dateAll.year))
                    yearlist.append(year)

                listYearnew = (self.wordAgain(yearlist))
                listYearnew.sort()
                print (listYearnew)

                print ("Wait")

                listYearNews = []
                for i in range(len(listYearnew)):
                    listYearNews.append(self.listYear(listYearnew[i],dateHead))
                #print (listYearNews)

                print ("=====Check======")

                listCountyYear = []
                for i in range(len(countylist)):
                    listCountyYear.append([])
                    for j in range(len(countylist[i])):
                        listCountyYear[i].append([])
                        for k in range(len(listYearNews)):
                            listCountyYear[i][j].append([])
                            for l in range(len(listYearNews[k])):
                                for m in range(len(countylist[i][j])):
                                    if(listYearNews[k][l]==countylist[i][j][m]):
                                        listCountyYear[i][j][k].append(listYearNews[k][l])

                for countMeasures in range(len(self.listTypeMeasures)):
                    print (self.listTypeMeasures[countMeasures])
                    plotHead = self.searchHead(self.listTypeMeasures[countMeasures])
                    saleCountyAll = []
                    for i in range(len(listCountyYear)):
                        saleCountyAll.append([])
                        for j in range(len(listCountyYear[i])):
                            saleCountyAll[i].append([])
                            for k in range(len(listCountyYear[i][j])):
                                sumSale = 0
                                for l in range(len(listCountyYear[i][j][k])):
                                    sumSale = sumSale + self.sheed.cell_value(listCountyYear[i][j][k][l], plotHead)
                                saleCountyAll[i][j].append(sumSale)

                    ##ใส่ลิสใน CSV ไม่ได้ ต้องหาวิธี พักก่อน
                    for i in range(len(saleCountyAll)):
                        for j in range(len(saleCountyAll[i])):
                            #เขียนไฟล์
                            filename = self.listTypeInDimensions[i][j]
                            with open(""+str(self.listTypeDate[countDate])+str(filename)+str(self.listTypeMeasures[countMeasures])+".csv", "w") as fp:
                                a = csv.writer(fp,delimiter=',')
                                listYearnewToCSV = listYearnew
                                data= [listYearnewToCSV,saleCountyAll[i][j]]
                                a.writerows(data)
            ##Date
            for countDate in range(len(self.listTypeDate)):
                numlist = []
                datelist = []
                dateNofloat = []
                dateHead = self.searchHead(self.listTypeDate[countDate])
                for x in range(1, self.sheed.nrows):
                    load = self.sheed.cell_value(x, dateHead)
                    timeNew = xlrd.xldate_as_tuple(load,0)
                    timeNewer = str(datetime.datetime(*timeNew))
                    dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
                    year = int(("%s"%dateAll.year))
                    month = int(("%s"%dateAll.month))
                    day = int(("%s"%dateAll.day))

                    m = (year,month,day)
                    d = (str(day)+"/"+str(month)+"/"+(str(year)))

                    numlist.append(x)
                    datelist.append(load)
                datelist = self.wordAgain(datelist)
                datelist.sort()
                print (datelist)

                for date in range(len(datelist)):
                    timeNew = xlrd.xldate_as_tuple(datelist[date],0)
                    timeNewer = str(datetime.datetime(*timeNew))
                    dateAll = datetime.datetime.strptime(timeNewer, '%Y-%m-%d %H:%M:%S')
                    year = int(("%s"%dateAll.year))
                    month = int(("%s"%dateAll.month))
                    day = int(("%s"%dateAll.day))

                    d = (str(day)+"/"+str(month)+"/"+(str(year)))
                    dateNofloat.append(d)
                print (dateNofloat)
                print ("Check")

                listDateNews = []
                for i in range(len(dateNofloat)):
                    listDateNews.append(self.listDate(dateNofloat[i],dateHead))
                print (listDateNews)

                listCountyYear = []
                for i in range(len(countylist)):
                    listCountyYear.append([])
                    for j in range(len(countylist[i])):
                        listCountyYear[i].append([])
                        for k in range(len(listDateNews)):
                            listCountyYear[i][j].append([])
                            for l in range(len(listDateNews[k])):
                                for m in range(len(countylist[i][j])):
                                    if(listDateNews[k][l]==countylist[i][j][m]):
                                        listCountyYear[i][j][k].append(listDateNews[k][l])

                for countMeasures in range(len(self.listTypeMeasures)):
                    print (self.listTypeMeasures[countMeasures])
                    plotHead = self.searchHead(self.listTypeMeasures[countMeasures])
                    saleCountyAll = []
                    for i in range(len(listCountyYear)):
                        saleCountyAll.append([])
                        for j in range(len(listCountyYear[i])):
                            saleCountyAll[i].append([])
                            for k in range(len(listCountyYear[i][j])):
                                sumSale = 0
                                for l in range(len(listCountyYear[i][j][k])):
                                    sumSale = sumSale + self.sheed.cell_value(listCountyYear[i][j][k][l], plotHead)
                                saleCountyAll[i][j].append(sumSale)

                    ##ใส่ลิสใน CSV ไม่ได้ ต้องหาวิธี พักก่อน

                    for i in range(len(saleCountyAll)):
                        for j in range(len(saleCountyAll[i])):
                            filename = self.listTypeInDimensions[i][j]
                            with open(""+str(self.listTypeDate[countDate])+"All"+str(filename)+str(self.listTypeMeasures[countMeasures])+".csv", "w") as fp:
                                a = csv.writer(fp,delimiter=',')
                                data= [['Date','Sale']]
                                a.writerows(data)
                                for m in range(len(saleCountyAll[i][j])):
                                        #เขียนไฟล์
                                        dateNofloatToCSV = dateNofloat
                                        data= [[dateNofloatToCSV[m],saleCountyAll[i][j][m]]]
                                        a.writerows(data)

    #Depart from Gui
    def closeGUI(self):
        self.root.destroy()

    #Add UserInterface from Data On Page1
    def headDimensions(self):
        self.button = []
        self.countCheck = 0
        self.countDimensionsCheck = 0
        self.locationY = 0
        self.locationY2 = 0
        self.DimensionList = self.read_CSVFile('Dimensions.csv','listTypeDimensions')
        for x in range(len(self.DimensionList)):
                self.HeadButton.insert(self.countDimensionsCheck,False)
                checkButton = Checkbutton(self.f1,
                                          text = self.DimensionList[x],
                                          command = lambda
                                          textCount = self.countDimensionsCheck:
                                          self.checkHead(textCount)).place(x = 20, y = 10 + self.locationY*30 +self.locationY2*30)
                self.countDimensionsCheck = self.countDimensionsCheck + 1
                self.locationY = self.locationY + 1
        Button(self.f1, text='Next',command = self.toPage2).place(x = 20, y = 10 + self.locationY*30 +self.locationY2*30)

    #Add UserInterface from Data On Page2
    def headInDimensions(self):
        self.countInDimensionsCheck = 0
        self.countMeasuresCheck = 0
        self.countDateCheck = 0
        self.locationY = 0
        self.locationY2 = 0

        listInDimensions = self.read_CSV_InDimensions(self.listHeadShow[0])
        self.scrollbarInFrame2((len(listInDimensions)))
        HeadDimensions = self.DimensionList[self.listHeadShow[0]]
        self.DimensionsButton.insert(0,False)
        self.listDimensionsButton.insert(0,(HeadDimensions))
        checkButton = Checkbutton(self.f2,
                                  text = HeadDimensions,
                                  command = lambda
                                  textCount = 0:
                                  self.checkbuttonDimensions(textCount)).place(x = 20, y = 10 + self.locationY*30 +self.locationY2*30)

        for y in range (len(listInDimensions)):
            self.inDimensionsButton.insert(self.countInDimensionsCheck,False)
            self.listInDimensionsButton.insert(self.countInDimensionsCheck,(listInDimensions[y]))
            checkButton = Checkbutton(self.f2,
                                              text = (listInDimensions[y]),
                                              command = lambda
                                              textCount = self.countInDimensionsCheck:
                                              self.checkbuttonInDimensions(textCount)).place(x = 50, y = 40 + self.locationY*30 + self.locationY2*30)
            self.countInDimensionsCheck = self.countInDimensionsCheck + 1
            self.locationY2 = self.locationY2 + 1
        self.locationY = self.locationY + 1



        button = Button(self.f2,text = "Measures",
                        command = lambda
                        textButton = "Measures" :
                        self.testCom(textButton)).place(x = 20, y = 10 + self.locationY*30 + self.locationY2*30, width=120, height=25)
        self.MeasuresList = self.read_CSVFile('Measures.csv','listTypeMeasures')
        for i in range(len(self.MeasuresList)):
            self.MeasuresButton.insert(self.countMeasuresCheck,False)
            self.listMeasuresButton.insert(self.countMeasuresCheck,self.MeasuresList[i])
            checkbutton = Checkbutton(self.f2,
                        text = self.MeasuresList[i],
                        command = lambda
                        textCount = self.countMeasuresCheck :
                        self.checkbuttonMeasures(textCount)).place(x = 50, y = 40 + self.locationY*30 + self.locationY2*30)
            self.countMeasuresCheck = self.countMeasuresCheck + 1
            self.locationY2 = self.locationY2 + 1
        self.locationY = self.locationY + 1

        self.locationX = 0
        button = Button(self.f2,text = "Date",
                        command = lambda
                        textButton = "Date" :
                        self.testCom(textButton)).place(x = 20, y = 10 + self.locationY*30 + self.locationY2*30, width=120, height=25)
        self.DateList = self.read_CSVFile('Date.csv','listTypeDate')
        for i in range(len(self.DateList)):
            self.DateButton.insert(self.countDateCheck,False)
            self.listDateButton.insert(self.countDateCheck,self.DateList[i])
            checkbutton = Checkbutton(self.f2,
                        text = self.DateList[i],
                        command = lambda
                        textCount = self.countDateCheck :
                        self.checkbuttonDate(textCount)).place(x = 50 + self.locationX*100, y = 40 + self.locationY*30 + self.locationY2*30)
            self.countDateCheck = self.countDateCheck + 1
            self.locationX = self.locationX + 1
        self.locationY2 = self.locationY2 + 1
        self.locationY = self.locationY + 1

        button = Button(self.f2,text = " Type Plot",
                        command = lambda :
                        self.testPlot()).place(x = 20, y = 10 + self.locationY*30 + self.locationY2*30, width=120, height=25)

        self.checkTypePlot.insert(0,False)
        self.listTypePlot.insert(0,"Plot")
        checkbutton = Checkbutton(self.f2,
                    text = "Plot",
                    command = lambda
                    textCount = 0 :
                    self.checkbuttonTypePlot(textCount)).place(x = 50, y = 40 + self.locationY*30 + self.locationY2*30)
        self.checkTypePlot.insert(1,False)
        self.listTypePlot.insert(1,"Pie")
        checkbutton = Checkbutton(self.f2,
                    text = "Pie",
                    command = lambda
                    textCount = 1 :
                    self.checkbuttonTypePlot(textCount)).place(x = 150, y = 40 + self.locationY*30 + self.locationY2*30)
        self.checkTypePlot.insert(2,False)
        self.listTypePlot.insert(2,"Bar")
        checkbutton = Checkbutton(self.f2,
                    text = "Bar",
                    command = lambda
                    textCount = 2 :
                    self.checkbuttonTypePlot(textCount)).place(x = 250, y = 40 + self.locationY*30 + self.locationY2*30)

        self.locationY2 = self.locationY2 + 1

        mButton = Button(self.f2,text="Plot",bd=5,command = self.Plot).place(x = 50, y = 40 + self.locationY*30 + self.locationY2*30)
        mButton = Button(self.f2,text="Delete",bd=5,command = self.delPlot).place(x = 105, y = 40 + self.locationY*30 + self.locationY2*30)

        self.locationY2 = self.locationY2 + 1
        self.locationY = self.locationY + 1
        Button(self.f2, text='Back', command=self.toPage1).place(x = 20, y = 10 + self.locationY*30 +self.locationY2*30)

    #Function onto the Page2
    def toPage2(self):
        self.headInDimensions()
        self.raise_frame(self.f2f)

    #Function onto the Page2
    def toPage1(self):
        del self.plotType[:]
        del self.listMeasuresPlot[:]
        del self.listDimensionsPlot[:]
        del self.listDatePlot[:]
        del self.listInDimensionsPlot[:]

        self.delPlot()
        self.raise_frame(self.f1)
        for widget in self.f2.winfo_children():
            widget.destroy()

    #Function ButtonDimensions
    def checkHead(self,x):
        self.HeadButton[x] = not self.HeadButton[x]
        if self.HeadButton[x] :
            self.listHeadShow.append(x)
        else:
            self.listHeadShow.remove(x)
        print (self.listHeadShow)

    #Function ButtonInDimensions
    def checkbuttonInDimensions(self,x):
        self.inDimensionsButton[x] = not self.inDimensionsButton[x]
        if self.inDimensionsButton[x] :
            self.listInDimensionsPlot.append(self.listInDimensionsButton[x])
        else:
            self.listInDimensionsPlot.remove(self.listInDimensionsButton[x])
        print (self.listInDimensionsPlot)

    #Function ButtonAllInDimensions
    def checkbuttonDimensions(self,x):
        self.DimensionsButton[x] = not self.DimensionsButton[x]
        if self.DimensionsButton[x] :
            self.listDimensionsPlot.append(self.listDimensionsButton[x])
        else:
            self.listDimensionsPlot.remove(self.listDimensionsButton[x])
        print (self.listDimensionsPlot)

    #Function ButtonMeasures
    def checkbuttonMeasures(self,x):
        self.MeasuresButton[x] = not self.MeasuresButton[x]
        if self.MeasuresButton[x] :
            self.listMeasuresPlot.append(self.listMeasuresButton[x])
        else:
            self.listMeasuresPlot.remove(self.listMeasuresButton[x])
        print (self.listMeasuresPlot)

    #Function ButtonDate
    def checkbuttonDate(self,x):
        self.DateButton[x] = not self.DateButton[x]
        if self.DateButton[x] :
            self.listDatePlot.append(self.listDateButton[x])
        else:
            self.listDatePlot.remove(self.listDateButton[x])
        print (self.listDatePlot)

    #Function ButtonTypePlot
    def checkbuttonTypePlot(self,x):
        self.checkTypePlot[x] = not self.checkTypePlot[x]
        if self.checkTypePlot[x] :
            self.plotType.append(self.listTypePlot[x])
        else:
            self.plotType.remove(self.listTypePlot[x])
        print (self.plotType)

    #Function onto the fameParameters
    def raise_frame(self,frame):
        frame.tkraise()

    #read_CSVFile By Name,row
    def read_CSVFile(self,nameFile,nameRow):
        listInCSV = []
        with open(nameFile) as csvfile:
             reader = csv.DictReader(csvfile)
             for row in reader:
                 listInCSV.append(row[nameRow])
        return listInCSV

    #read_InDimensions_CSVFile By column
    def read_CSV_InDimensions(self,x):
        listInDimensions = []
        with open('InDimensions.csv', newline='') as f:
            reader = csv.reader(f)
            if (x == 0):
                listInDimensions = next(reader)
            elif (x > 0):
                for i in range(x+1):
                    row1 = next(reader)
                listInDimensions = row1
        return (listInDimensions)

    #Function PlotGraph
    def Plot(self):
        self.delPlot()
        listSalePlot = []
        listLabel = []
        listDate = []

        tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                     (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                     (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                     (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                     (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

        for i in range(len(tableau20)):
            r, g, b = tableau20[i]
            tableau20[i] = (r / 255., g / 255., b / 255.)

        if (len(self.listDimensionsPlot)) == 1 :
            listInDimensions = self.read_CSV_InDimensions(self.listHeadShow[0])
            for i in range(len(listInDimensions)):
                filename = listInDimensions[i]
                listLabel.append(filename)
                ##เพิ่ม Date ตรงนี้
                with open(""+str(self.listDatePlot[0])+str(filename)+str(self.listMeasuresPlot[0])+".csv", newline='') as f:
                    reader = csv.reader(f)
                    row1 = next(reader)
                    row2 = next(reader)
                listSalePlot.append(row2)
            listDate = row1
        elif (len(self.listDimensionsPlot)) == 0:
            for i in range(len(self.listInDimensionsPlot)):
                filename = self.listInDimensionsPlot[i]
                listLabel.append(filename)
                with open(""+str(self.listDatePlot[0])+str(filename)+str(self.listMeasuresPlot[0])+".csv", newline='') as f:
                    reader = csv.reader(f)
                    row1 = next(reader)
                    row2 = next(reader)
                listSalePlot.append(row2)
            listDate = row1
        print (listDate)
        print (listLabel)
        print (listSalePlot)

        canvasPlot = 0
        print (len(self.canvas))
        for plot in range(len(self.plotType)):
            self.canvas.append("canvas"+str(plot))
            if (self.plotType[plot]=="Plot"):
                if (len(self.listMeasuresPlot)==1) and (len(self.listDatePlot)==1):
                    f = Figure(figsize=(6, 5), dpi=80)
                    f.set_facecolor("w")
                    plt = f.add_subplot(111)
                    for i in range(len(listSalePlot)):
                        print (listSalePlot[i])
                        plt.plot(listDate,listSalePlot[i],lw=2.5,color=tableau20[i],label=listLabel[i])
                    minX = (int(min(listDate)))
                    maxX = (int(max(listDate)))
                    x = range(minX, (maxX+1))
                    plt.set_xticks(x)
                    plt.set_xticklabels(listDate)
                    plt.set_title(str(self.listMeasuresPlot[0]))
                    plt.legend(loc='upper left', bbox_to_anchor=(0, 1),ncol=2, fancybox=True, shadow=True)
                    self.canvas[plot] = FigureCanvasTkAgg(f, master=self.f2)
                    self.canvas[plot].show()
                    self.canvas[plot].get_tk_widget().place(x = 300*canvasPlot + 350, y = 10)
                    self.canvas[plot]._tkcanvas.place(x = 300*canvasPlot + 350, y = 10)

            elif (self.plotType[plot]=="Pie"):
                if (len(self.listMeasuresPlot)==1) and (len(self.listDatePlot)==1):
                    f = Figure(figsize=(6, 5), dpi=80)
                    f.set_facecolor("w")
                    plt = f.add_subplot(111)
                    plt.set_title(str(self.listMeasuresPlot[0]))
                    saleCounty = []
                    colors = []
                    for i in range(len(listSalePlot)):
                        saleCountySum = 0
                        colors.append(tableau20[i])
                        for j in range(len(listSalePlot[i])):
                            saleCountySum = saleCountySum + float(listSalePlot[i][j])
                        saleCounty.append(saleCountySum)
                    print (saleCounty)
                    plt.pie(saleCounty, labels=listLabel, colors=colors,
                                autopct='%1.1f%%', shadow=True, startangle=90)
                    plt.axis('equal')
                    self.canvas[plot] = FigureCanvasTkAgg(f, master=self.f2)
                    self.canvas[plot].show()
                    self.canvas[plot].get_tk_widget().place(x = 300*canvasPlot + 350, y = 10)
                    self.canvas[plot]._tkcanvas.place(x = 300*canvasPlot + 350, y = 10)

            elif (self.plotType[plot]=="Bar"):
                if (len(self.listMeasuresPlot)==1) and (len(self.listDatePlot)==1):
                    f = Figure(figsize=(6, 5), dpi=80)
                    f.set_facecolor("w")
                    plt = f.add_subplot(111)

                    print (len(listDate))
                    width = 0.2
                    ind = np.arange(len(listDate))

                    for i in range(len(listSalePlot)):
                        listSalePlot[i] = [float(j) for j in listSalePlot[i]]
                        plt.bar(ind+(i*width),listSalePlot[i],width,color=tableau20[i],label=listLabel[i])
                    plt.set_xticks(ind+((width/2)*(len(listSalePlot))))
                    plt.set_xticklabels(listDate)
                    plt.set_title(str(self.listMeasuresPlot[0]))
                    plt.legend(loc='upper left', bbox_to_anchor=(0, 1),ncol=2, fancybox=True, shadow=True)
                    self.canvas[plot] = FigureCanvasTkAgg(f, master=self.f2)
                    self.canvas[plot].show()
                    self.canvas[plot].get_tk_widget().place(x = 300*canvasPlot + 350, y = 10)
                    self.canvas[plot]._tkcanvas.place(x = 300*canvasPlot + 350, y = 10)
            canvasPlot = canvasPlot + 1.5
            self.plotTypeOlt.append(canvasPlot)

    #Function delGraph
    def delPlot(self):
        if (len(self.plotTypeOlt)) == 1:
            self.canvas[0].get_tk_widget().destroy()
        elif (len(self.plotTypeOlt)) > 1:
            for plot in range(len(self.plotTypeOlt)):
                self.canvas[plot].get_tk_widget().destroy()
        elif  (len(self.plotTypeOlt)) == 0:
            print ("NoPlot")
        del self.plotTypeOlt[:]
root = Tk()
window=Window(root)
root.mainloop()
