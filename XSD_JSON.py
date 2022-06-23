#This program takes XSD for Bilaterals and JSON messanes from the browser and comapres them
#In XSD we search for something like xs:element name="T551.M and we search until next transaction and we save it to the list
#This limitation requires to add another transaction in XSD afer last one (currently 551.M)
#Next JSON file is parsed as a text flie and data items are retrieved and saved to a list
#Next we compare these lists and if discrepanies are found we mark it wit little star * character

#  IF JSON has more elements than XSD but is missing some from XSD, then it will not show, what's extra in XSD!!!!!!!!!!!!!!!!

import xml.etree.ElementTree as ET

xsd_filename = 'BilateralsHviMessage.V1.0.3.1.xsd'
tree = ET.parse(xsd_filename)
transaction = 'T365.M'
next_transaction = 'T501.R' # what is the next transaction in XSD file after transaction above

root = tree.getroot()

entire_XSD=[]
for descendant in root.iter():
    entire_XSD.append(descendant.attrib)

transaction_XSD = []

####look for specific transaction in the XSD and save it to transaction_XSD list
def trx_data_items(trx_name, next_trx_name):
    keep_current_line = False
    for data_item in entire_XSD:
        if trx_name in str(data_item):
            keep_current_line = True
        elif next_trx_name in str(data_item):
            keep_current_line = False
        if keep_current_line:
            transaction_XSD.append(data_item)
####look for specific transaction in the XSD and save it to transaction_XSD list

trx_data_items(transaction, next_transaction)

###truncate data items from {'name' stuff from XSD and save just element names of data items
transaction_XSD1 = []

for j in range(len(transaction_XSD)):
    data_item_end = str(transaction_XSD[j]).find(',') - 1
    transaction_XSD1.append(str(transaction_XSD[j])[10:data_item_end])

#remove non data items like 'SelectedMeter', 'CustomerConsent', 'Meter', 'RepairedMeter', 'InstallMeter'
transaction_XSD2 = list(filter(None, transaction_XSD1))
# print(len(transaction_XSD2))
new_x = []
for index, element in enumerate(transaction_XSD2):
    if element not in ('SelectedMeter', 'CustomerConsent', 'Meter', 'RepairedMeter', 'InstallMeter'):
        new_x.append(element)
transaction_XSD2 = new_x
#remove non data items like 'SelectedMeter', 'CustomerConsent', 'Meter', 'RepairedMeter', 'InstallMeter'

# remove empty elements form the list, and remove first 5 elements like trx name payload, header etc
transaction_XSD3 = transaction_XSD2[5:]
# remove empty elements form the list, and remove first 5 elements like trx name payload, header etc

for m in range(len(transaction_XSD2)):
    print(str(transaction_XSD2[m]))

transactions_JSON = []
    
#import file with JSON transactions
filename = 'T365M.json'
f1 = open(filename, 'r') # open source file
lines = f1.readlines()

JSON_transaction_name = lines[8]
JSON_transaction_name_start = lines[8].find('"')
JSON_transaction_name_end = lines[8].find(': {') 
JSON_transaction_name1  = JSON_transaction_name[JSON_transaction_name_start+1:JSON_transaction_name_end-1]
# print('JSON transaction name: ' + JSON_transaction_name1)
XSD_transaction_name = transaction_XSD2[0]
# print('XSD  transaction name: ' + XSD_transaction_name)

keep_current_line = False
for line in lines:
    # look for TransactionTimestamp in the lines and start copying from that place
    if 'TransactionTimestamp' in line:
        keep_current_line = True
    if keep_current_line:
        # do not keep lines with {}
        if not ('{' in line or '}' in line):      
            data_item_end1 = line.strip().find(':') -1
            data_item = line.strip()[1:data_item_end1]
            transactions_JSON.append(data_item)           

#remove first element from the list TransactionTimestamp
transactions_JSON = transactions_JSON[1:]

f1 = open(transaction + '_Tags_DataItems_comparison.txt', 'w')

print('\nJSON transaction name: ' + JSON_transaction_name1)
f1.write('JSON transaction name: ' + JSON_transaction_name1 + '\n')

print('XSD  transaction name: ' + XSD_transaction_name)
f1.write('XSD  transaction name: ' + XSD_transaction_name + '\n\n')

message1 = str(len(transaction_XSD3)) + ' tags in XSD schema for transaction ' + transaction
print(message1)
f1.write(message1 + '\n')
message2 = str(len(transactions_JSON)) + ' data items in JSON for transaction ' + transaction
print(message2 + '\n')
f1.write(message2 + '\n\n') 

transactions_JSON.sort()
transaction_XSD3.sort()

if(transactions_JSON==transaction_XSD3):
    print("XSD tags names are equal to JSON data items names\n")
    f1.write("XSD tags names are equal to JSON data items names\n\n")
    print('SR | XSD' + ' ' * 39 + '| JSON\n')
    f1.write('SR | XSD' + ' ' * 39 + '| JSON\n\n')
    for p in range(len(transactions_JSON)):
        print(str(p+1).rjust(2, '0') + ' | {0:41} | {1:41}'.format(transaction_XSD3[p], transactions_JSON[p]))
        f1.write(str(p+1).rjust(2, '0') + ' | {0:41} | {1:41}'.format(transaction_XSD3[p], transactions_JSON[p]) + '\n')
# else:
#     print("XSD tags names are NOT equal to JSON data items names - check rows with *\n")
#     f1.write("XSD tags names are NOT equal to JSON data items names check rows with *\n\n")
#     print('XSD' + ' ' * 39 + '| JSON\n')
#     f1.write('XSD' + ' ' * 39 + '| JSON\n\n')
#     for r in range(len(transactions_JSON)):
#         if transaction_XSD3[r]==transactions_JSON[r]:
#             print('{0:41} | {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]))
#             f1.write('{0:41} | {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]) + '\n')
#         else:
#             #if data items are not identical display * start in the row
#             print('{0:41} * {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]))
#             f1.write('{0:41} * {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]) + '\n')
elif (len(transactions_JSON)>len(transaction_XSD3)):
    print("XSD tags names are NOT equal to JSON data items names - check rows with *\n")
    f1.write("XSD tags names are NOT equal to JSON data items names check rows with *\n\n")
    print('XSD' + ' ' * 39 + '| JSON\n')
    f1.write('XSD' + ' ' * 39 + '| JSON\n\n')
    #create list3 and insert * for missing fields
    list3 = []
    for i in range(len(transactions_JSON)):
        if transactions_JSON[i] not in transaction_XSD3:
            list3.append('*')
        else:
            list3.append(transactions_JSON[i])
    #create list3 and insert * for missing fields
    for r in range(len(transactions_JSON)):
        if transactions_JSON[r]==list3[r]:
            print('{0:41} | {1:41}'.format(list3[r], transactions_JSON[r]))
            f1.write('{0:41} | {1:41}'.format(list3[r], transactions_JSON[r]) + '\n')
        else:
            #if data items are not identical display * start in the row
            print('{0:41} * {1:41}'.format(list3[r], transactions_JSON[r]))
            f1.write('{0:41} * {1:41}'.format(list3[r], transactions_JSON[r]) + '\n')
elif (len(transaction_XSD3)>len(transactions_JSON)):
    print("XSD tags names are NOT equal to JSON data items names - check rows with *\n")
    f1.write("XSD tags names are NOT equal to JSON data items names check rows with *\n\n")
    print('XSD' + ' ' * 39 + '| JSON\n')
    f1.write('XSD' + ' ' * 39 + '| JSON\n\n')
    #create list3 and insert * for missing fields
    list3 = []
    for i in range(len(transaction_XSD3)):
        if transaction_XSD3[i] not in transactions_JSON:
            list3.append('*')
        else:
            list3.append(transaction_XSD3[i])
    #create list3 and insert * for missing fields
    for r in range(len(transaction_XSD3)):
        if transaction_XSD3[r]==list3[r]:
            print('{0:41} | {1:41}'.format(transaction_XSD3[r], list3[r]))
            f1.write('{0:41} | {1:41}'.format(transaction_XSD3[r], list3[r]) + '\n')
        else:
            #if data items are not identical display * start in the row
            print('{0:41} * {1:41}'.format(transaction_XSD3[r], list3[r]))
            f1.write('{0:41} * {1:41}'.format(transaction_XSD3[r], list3[r]) + '\n')