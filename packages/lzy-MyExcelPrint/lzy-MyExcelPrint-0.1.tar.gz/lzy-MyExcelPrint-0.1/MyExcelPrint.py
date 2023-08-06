import win32com.client
from openpyxl.utils import column_index_from_string


class ExcelPrint:
    def __init__(self,Visible=True,**kwargs):
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        self.xlApp.Visible = Visible
        self.xlBook = self.xlApp.Workbooks.Open(kwargs.get('filepath'))
        del self.xlApp

    def SheetPrint(self,*args,**kwargs):
        coordinate = kwargs.get('coordinate')
        sheet_column= column_index_from_string("".join(list(filter(str.isalpha, coordinate))))
        sheet_row = "".join(list(filter(str.isdigit, coordinate)))
        for value in args:
            print_sheet = self.xlBook.Worksheets(kwargs.get('print_sheet'))
            print_sheet.Cells(int(sheet_row),int(sheet_column)).Value = value
            print_sheet.PrintOut()