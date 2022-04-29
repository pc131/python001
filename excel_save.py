# pip install pywin32
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Add()
ws = wb.Worksheets.Add()
ws.Name = "MyNewSheet"
wb.SaveAs('c:\\Users\\skocz\\Downloads\\11\\add_a_worksheet.xlsx')
excel.Application.Quit()