import openpyxl as xl
import os

from openpyxl.styles import numbers

working_dir = 'C:\\Users\\tomasz.skoczylas\\Downloads\\11\\'
transaction_name = 'T321.R'
transaction_name_simple=transaction_name[1:].replace('.', '')
test_cases_csv = 'Azure_Test_Cases_To_Import_T' + transaction_name_simple + '.csv'
business_rules_file = 'MOSL-Bilaterals-Business-Rules_V0.9.1.xlsx'


wb1 = xl.load_workbook(business_rules_file)
ws12 = wb1.worksheets[1] # Error codes

#define dictionary to change description
#substitute_list = [['must be', 'is not'], ['is mandatory', 'is not provided'], ['is not', 'is'], ['must not be', 'is'], ['is', 'is not']]

#loop through list of transactions in Excel and find column, for current transaction
col_number_trx = 0
for col_number_trx in range(6, 45):
    if(str(ws12.cell(row=2, column=col_number_trx).value)==transaction_name):
        trx_col_number = col_number_trx

#open CSV file for writing data from Excel
csv_file = open(test_cases_csv, 'w')

#wites a header of CSV file
csv_file.write('ID,Work Item Type,Title,Test Step,Step Action,Step Expected,Area Path,Assigned To,State\n')

#initiate list of elements [[Business Rule 1, Description 1], [Business Rule 2, Description 2], ...]
list_con_xxxx = []
#count number of business rules for current transacti
number_of_business_rules = 0
for row_number1 in range(4, 169):
    #calculate number of business rules and create list of elements [[Business Rule 1, Description 1], [Business Rule 2, Description 2], ...]
    if(str(ws12.cell(row=row_number1, column=trx_col_number).value)=='X'):
        number_of_business_rules += 1
        #keep adding to the list: ['CON-0005', 'Transaction must be submitted by a Retailer....']
        list_con_xxxx.append([ws12.cell(row=row_number1, column=1).value, ws12.cell(row=row_number1, column=5).value])      



for row_number1 in range(0, number_of_business_rules):

    con_number = list_con_xxxx[row_number1][0] 
    business_rule_description = list_con_xxxx[row_number1][1] 

    #check if decsription can be change according to the dictionary substitute_list[]
    # for element in range(len(substitute_list)):
    #     if substitute_list[element][0] in business_rule_description:
    #         business_rule_description = business_rule_description.replace(substitute_list[element][0], substitute_list[element][1])

    
    csv_file.write(',"Test Case","TC-' + transaction_name_simple + '-' + con_number + '",,,,"Bilaterals UAT Testing","Tomasz Skoczylas <tomasz.skoczylas@cgi.com>","Design"\n')
    csv_file.write(',,,"1","Submit the transaction ' + transaction_name + ' against following statement:\n\n' + business_rule_description +'","T209.M rejection notification is issued with ErrorReturnCode ' + con_number + ' and related DataItemReference, to the originator of the transaction",,,\n')


csv_file.close()