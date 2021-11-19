import openpyxl as xl
import os
# list files in current directory
mylist = os.listdir("C:\\Users\\tomasz.skoczylas\\Downloads\\11\\")
# remove the template file from the list, so it is not used as source file
mylist.remove('Bilaterals 1.02 master B5.xlsx')

for f in mylist:

    filename1 = "C:\\Users\\tomasz.skoczylas\\Downloads\\11\\" + f
    # load the excel file - workbook
    wb1 = xl.load_workbook(filename1)
    # work on worksheet 2 - Test Data
    ws11 = wb1.worksheets[0]
    ws12 = wb1.worksheets[1]
    # update 6th row, AW column in excel, worksheet 2 (Test Data)
    ws12.cell(row=6, column=49).value = '[today+10]'
    ws11.cell(row=4, column=7).value = 'created with 1.1 excel template'
    # save updated file
    #wb1.save(str(filename1.replace("092", "102")))
    wb1.save(filename1)