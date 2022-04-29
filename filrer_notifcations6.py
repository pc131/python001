import json

working_dir = 'C:\\Users\\skocz\\Downloads\\11\\'
bad_words = ['---- Start Time', 'Request:', 'Response:', 'Peek Message:']

filename = "TC-C1R-REGRESSION_01_2022-04-27_18-43-43.json"
source_file = working_dir + filename
source_json_file = source_file.replace(".json", "-json.json")
source_json_string = ""
oldfile = open(source_file, 'r')
newfile = open(source_json_file, 'w')
for line in oldfile:
    if not (any(bad_word in line for bad_word in bad_words) or line.isspace()):
        source_json_string += line.lstrip()
source_json_string = source_json_string.replace("\n", "").replace("}{", "}\n{")     
#print(source_json_string)
newfile.write(source_json_string)
oldfile.close()
newfile.close()

json_messages_list = []
print("Started Reading JSON file which contains multiple JSON document")
with open(source_json_file) as f:
    for jsonObj in f:
        json_message = json.loads(jsonObj)
        print("Type of json_message is: " + str(type(json_message)))
        #print(json_message)
        print(json_message['SendMessageRequest']['MessageContainer']['DocumentReferenceNumber'])
        print(json_message['SendMessageRequest']['MessageContainer']['Payload'])
        # print(json_message['SendMessageRequest']['MessageContainer']['Payload']['Transaction'][0]['Header'])
        # header = message_container['Payload']['Transaction']
        # print(header)
       # json_messages_list.append(json_message)

# print("Printing each JSON Decoded Object")
# for json_message in json_messages_list:
#     print(json_message)

def get_items(test_dict, lvl):
  
    # querying for lowest level
    if lvl == 0:
        yield from ((key, val) for key, val in test_dict.items()
                    if not isinstance(val, dict))
    else:
  
        # recur for inner dictionaries
        yield from ((key1, val1) for val in test_dict.values()
                    if isinstance(val, dict) for key1, val1 in get_items(val, lvl - 1))
  
  
# initializing dictionary
test_dict = json_message
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# initializing K
K = 2
  
# calling function
res = get_items(test_dict, K)
  
# printing result
print("Required items : " + str(dict(res)))