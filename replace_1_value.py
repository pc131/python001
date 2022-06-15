import openpyxl as xl
import os
# list files in current directory
mylist = os.listdir("C:\\Users\\tomasz.skoczylas\\Downloads\\22\\")
# remove the template file from the list, so it is not used as source file

for f in mylist:

    filename1 = "C:\\Users\\tomasz.skoczylas\\Downloads\\22\\" + f
    # load the excel file - workbook
    wb1 = xl.load_workbook(filename1)
    # work on worksheet 2 - Test Data
    ws11 = wb1.worksheets[1]
    # update 6th row, AW column in excel, worksheet 2 (Test Data)
    ws11.cell(row=6, column=7).value = "3013342404S19"
    # save updated file
    wb1.save(filename1)