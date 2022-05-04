#This program takes XSD for Bilaterals and JSON messanes from the browser and comapres them
#In XSD we search for something like xs:element name="T551.M and we search until next transaction and we save it to the list
#This limitation requires to add another transaction in XSD afer last one (currently 551.M)
#Next JSON file is parsed as a text flie and data items are retrieved and saved to a list
#Next we compare these lists and if discrepanies are found we mark it wit little star * character

import xml.etree.ElementTree as ET

xsd_filename = 'BilateralsHviMessage.V1.0.3.1.xsd'
tree = ET.parse(xsd_filename)
transaction = 'T365.R'
next_transaction = '365.M' # what is the next transaction in XSD file after transaction above

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
    #remove from XSD list CustomerContact and SelectedMeter elements
    if not ('SelectedMeter' in str(transaction_XSD[j]) or 'CustomerConsent' in str(transaction_XSD[j]) or 'RepairedMeter' in str(transaction_XSD[j])):
        data_item_end = str(transaction_XSD[j]).find(',') - 1
        transaction_XSD1.append(str(transaction_XSD[j])[10:data_item_end])
###truncate data items from {'name' stuff from XSD and save just element names of data items

# remove empty elements form the list, and remove first 5 elements like trx name payload, header etc
transaction_XSD2 = list(filter(None, transaction_XSD1))
transaction_XSD3 = transaction_XSD2[5:]
# remove empty elements form the list, and remove first 5 elements like trx name payload, header etc

# for m in range(len(transaction_XSD3)):
#     print(str(transaction_XSD3[m]))

transactions_JSON = []

#import file with JSON transactions
filename = 'B7_T365.R.json'
f1 = open(filename, 'r') # open source file
lines = f1.readlines()
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

# for n in range(len(transactions_JSON)):
#     print(str(transactions_JSON[n]))

f1 = open(transaction + '_Tags_DataItems_comparison.txt', 'w')

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
else:
    print("XSD tags names are NOT equal to JSON data items names - check rows with *\n")
    f1.write("XSD tags names are NOT equal to JSON data items names check rows with *\n\n")
    print('XSD' + ' ' * 39 + '| JSON\n')
    f1.write('XSD' + ' ' * 39 + '| JSON\n\n')
    for r in range(len(transactions_JSON)):
        if transaction_XSD3[r]==transactions_JSON[r]:
            print('{0:41} | {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]))
            f1.write('{0:41} | {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]) + '\n')
        else:
            #if data items are not identical display * start in the row
            print('{0:41} * {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]))
            f1.write('{0:41} * {1:41}'.format(transaction_XSD3[r], transactions_JSON[r]) + '\n')
