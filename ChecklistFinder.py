# -------------------------#
# ChecklistFinder v.1.0"---#
# created by Nykram--------#
# ver. 1.0v----------------#
# -------------------------#



# Imports #
import os
import wx
import sys
import time
import PyPDF2
import progressbar
import tabula
import json

# Table for page index
pagesToPrint = []

# Table for request list
rqList = []
rqListIndex = []

# Req from slice
sliceReg = slice(0,11)
sliceReqSpec = slice(14,25)

# Table for check pages
pagesToCheck = []

#Creating PDF#
class PDFcreate:
    def __init__(self, targetpdf):
        self.checklist = targetpdf
        self.inputpdf = PyPDF2.PdfFileReader(self.checklist)
    def createPDF(self):
        print("Correct pages to print:")
        print(pagesToPrint)
        writer=PyPDF2.PdfFileWriter()
        print("Deleting chars")
        try:
            for i in range(len(pagesToPrint)):
                pagesToPrint.remove('')
        except:
            pass
        finally:
            print(pagesToPrint)
        writer.addBlankPage()
        for i in pagesToPrint:
            try:
                print("Strona", i)
                writer.addPage(self.inputpdf.getPage(i))
            except Exception:
                print("Error with last page, //todo")
                continue
        with open("output.pdf", "wb") as outfp:
            writer.write(outfp)
        pdfFrame.completeState(pdfFrame, True)
# PDF analising #
class PDFsearch:
    def __init__(self, tagetpdf):
        self.checklist = tagetpdf
        self.count = 1
        self.path = os.path.join(os.getcwd(), self.checklist)
        pdfFile = open(self.checklist, 'rb')
        pdfReadObj = PyPDF2.PdfFileReader(pdfFile)
        self.secondpage = False
        self.page = pdfReadObj.numPages
    def readAllPages(self):
        indexOfPage = []
        clear = lambda: os.system('cls')
        reqLen = len(rqList) * 3
        y = 0
        while reqLen > y:
            pagesToPrint.append("")
            y = y + 1
        print(pagesToPrint)
        with progressbar.ProgressBar(max_value=self.page) as bar:
            for i in range(self.page):
                bar.update(i)
                tabula.convert_into(self.checklist, "output.json", output_format="json", pages= i + 1)
                file = open('output.json')
                data = json.loads(file.read())
                datasize = os.path.getsize("output.json")
                for element in data:
                        try:
                            if element['data'][0][2]['text'] == "Anwender und System-Daten":
                                y = 0
                                while y < 15:
                                    reqWithText = element['data'][y][1]['text']
                                    request = reqWithText[sliceReg]
                                    for j in rqList:
                                        if j == request:
                                            rqIndex = rqList.index(request)
                                            pagesToPrint[(rqIndex * 2)] = i
                                            pagesToPrint[(rqIndex * 2)+1]  = i + 1
                                            rqListIndex.append(rqIndex)
                                            print("Added page", i)
                                            break
                                    y = y + 1
                        except:
                            pass
                print("Added pages:")
                print(pagesToPrint)
                file.close()
    def searchAllPDF(self):
        path = os.getcwd()
        PDFlist = []
        for file in os.listdir(path):
            if file.endswith(".pdf"):
                if file.startswith("output"):
                    continue
                else:
                    PDFlist.append(file)
        return PDFlist
    def readReqList(self):
        rqlist = open('reqlist.txt')
        rqlistR = rqlist.readlines()
        for i in rqlistR:
            i = i[sliceReg]
            if i == '\n':
                continue
            else:
                rqList.append(i)
        rqlist.close()
        print(rqList)
        print("Targets:")
        print(len(rqList))
    def checkLanguage(self):
        file = open(self.checklist, 'wb')
        PyPDF2.PdfFileReader()
# Window GUI #
class pdfFrame(wx.Frame):
    def __init__(self):
        self.allPdf = PDFsearch.searchAllPDF(self)
        print("Debug window:")
        super().__init__(parent=None, title="ChecklistFinder v.1.0")
        self.panel = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        self.SetIcon(wx.Icon('assets/pdf.png'))
        pdfFrame.my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.staticline = wx.StaticLine(self.panel, 5, style=wx.LI_HORIZONTAL, size=(2000, -1))
        pdfFrame.my_sizer.Add(self.staticline,0,wx.ALL | wx.CENTER,10)
        self.textlabel = wx.StaticText(self.panel, -1, "Select PDF:")
        pdfFrame.my_sizer.Add(self.textlabel,0,wx.ALL | wx.LEFT, 5)
        self.listbox = wx.ListBox(self.panel, 0, choices=[],style=wx.LB_SINGLE | wx.LB_NEEDED_SB)
        self.listbox.InsertItems(self.allPdf,0)
        pdfFrame.my_sizer.Add(self.listbox,0, wx.ALL | wx.LEFT)
        self.btnref = wx.Button(self.panel, label="Refresh")
        self.btnref.Bind(wx.EVT_BUTTON, self.on_refresh_btn)
        pdfFrame.my_sizer.Add(self.btnref,0,wx.ALL | wx.LEFT, 5)
        self.btn = wx.Button(self.panel, label="Run")
        self.btn.Bind(wx.EVT_BUTTON, self.runScript)
        pdfFrame.my_sizer.Add(self.btn,0,wx.ALL | wx.LEFT,5)
        self.panel.SetSizer(pdfFrame.my_sizer)  
        self.Centre()
        self.Show()
    def completeState(self,state):
        time.sleep(0.5)
        if state == True:
            message = wx.MessageBox('PDF its ready to print!', 'Completed!', wx.OK | wx.ICON_INFORMATION)
            sys.exit(0)
    def on_refresh_btn(self, event):
        i = 1
        while i <= len(self.allPdf):
            self.listbox.Delete(0)
            i += 1
        self.allPdf = PDFsearch.searchAllPDF(self)
        self.listbox.InsertItems(self.allPdf,0)
    def runScript(self, value):
            SelectedPDF = self.listbox.GetString(self.listbox.GetSelection())
            PDFsearch(SelectedPDF).readReqList()
            PDFsearch(SelectedPDF).readAllPages()
            PDFcreate(SelectedPDF).createPDF()
            sys.exit()

if __name__ == "__main__":
    app = wx.App(False)
    frame = pdfFrame()
    frame.Show(True)
    frame.SetMinSize(wx.Size(300,300))
    frame.SetSize(wx.Size(320,320))
    app.MainLoop()
