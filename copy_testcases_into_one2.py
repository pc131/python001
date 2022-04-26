import openpyxl as xl
import os
# copies transactions from multiple excel files into 1 excel file with these transactions
working_dir = "C:\\Users\\tomasz.skoczylas\\Downloads\\11\\TEST_CASES\\"
mylist = os.listdir(working_dir)
for filename in mylist:
    if "CON-" not in filename or "z" in filename:
        mylist.remove(filename)
#mylist.remove("Bilaterals 1.4.0.0 master.xlsx")
master_excel = working_dir + "Bilaterals 1.4.0.0 master.xlsx"
wb1 = xl.load_workbook(master_excel)
ws11 = wb1.worksheets[0]
ws12 = wb1.worksheets[1]
total_transactions = 0

for a in mylist:
    print(a)

for i in range(len(mylist)):
    source_excel = working_dir + "\\" + mylist[i]
    con_rule = "Testing " + mylist[i][8:16]
    wb = xl.load_workbook(source_excel)
    test_case_sequence_sheet = wb.worksheets[0]
    test_case_data_sheet = wb.worksheets[1]
    max_cols = test_case_data_sheet.max_column
    number_of_transactions = 0
    while test_case_sequence_sheet.cell(row = number_of_transactions + 4, column = 3).value != "-":
        number_of_transactions += 1
        trading_party = test_case_sequence_sheet.cell(row = number_of_transactions + 3, column = 3)
        # print("File: ") + con_rule
        print("Trading party at row " + str(number_of_transactions + 3) + " , column 3 = " + trading_party.value)
        transaction = test_case_sequence_sheet.cell(row = number_of_transactions + 3, column = 5)
        print("Transaction at row " + str(number_of_transactions + 3) + " , column 5 = " + transaction.value)
        print("Total transactions = " + str(total_transactions + 1))
        print("Number of transactions = " + str(number_of_transactions))
        ws11.cell(row = total_transactions + number_of_transactions + 3, column = 3).value = trading_party.value
        print("Writing trading party to new excel, cell " + str(total_transactions + number_of_transactions + 3) + ",3")
        ws11.cell(row = total_transactions + number_of_transactions + 3, column = 5).value = transaction.value
        print("Writing transaction to new excel, cell " + str(total_transactions + number_of_transactions + 3)+ ",5")
        print("----------------------")
        ws11.cell(row = total_transactions + number_of_transactions + 3, column = 7).value = con_rule
        for col in range(7, max_cols+1):
            # reading cell value from source excel file
            value1 = test_case_data_sheet.cell(row = 3*(number_of_transactions-1) + 6, column=col)
            # writing the read value to destination excel file
            ws12.cell(row=3*total_transactions + 3*(number_of_transactions-1) + 6, column=col).value = value1.value
        
    total_transactions += number_of_transactions
wb1.save(filename = working_dir + 'NEWFILE.xlsx')