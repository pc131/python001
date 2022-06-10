import json

#working_dir = 'C:\\Users\\skocz\\Downloads\\11\\'
working_dir = 'C:\\Users\\tomasz.skoczylas\\Downloads\\11\\'
bad_words = ['---- Start Time', 'Request:', 'Response:', 'Peek Message:']

filename = "T223W.json"
source_file = working_dir + filename
source_json_file = source_file.replace(".json", "-json.json")
source_json_string = ""
oldfile = open(source_file, 'r')
newfile = open(source_json_file, 'w')
for line in oldfile:
    if not (any(bad_word in line for bad_word in bad_words) or line.isspace()):
        source_json_string += line.lstrip()
source_json_string = source_json_string.replace("\n", "").replace("}{", "}\n{")
# print(source_json_string)
newfile.write(source_json_string)
oldfile.close()
newfile.close()

dict_message = {}

def print_depth(d, start=0):
    for key, value in d.items():
        print(key, start + 1)
        if key in ("SendMessageRequest", "SendMessageResponse", "PeekMessageResponse"):
            dict_message["RequestType"] = key
        if key == "DocumentReferenceNumber":
            dict_message["DocumentReferenceNumber"] = value
        if key == "Transaction":
            transaction = value.keys()
            *transaction1, = transaction
            dict_message["Transaction"] = transaction1[0]
        if key == "DataTransaction":
            dict_message["DataTransaction"] = value        
        if key == "OriginatorsReference":
            dict_message["OriginatorsReference"] = value    
        if key == "TransactionTimestamp":
            dict_message["TransactionTimestamp"] = value        
        if key == "ORID":
            dict_message["ORID"] = value
        if isinstance(value, dict):
            print_depth(value, start=start+1)

#list of JSON messages, each message as nested dictionary
json_messages = []
#list of part of JSON messages, each message as flat dictionary
json_messages1 = []
with open(source_json_file) as f:
    x = 0
    for line in f:     
        json_messages.append(json.loads(line))
        print_depth(json_messages[x])
        print('\n')
        print(dict_message)
        json_messages1.append(dict_message.copy())
        print('\n')
        x += 1

#print_depth(json_message)
# print('\n')
print(json_messages)
print('\n')
print(json_messages1)
# print('\n')
#print(json_message)