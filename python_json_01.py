import json

with open('states.json') as f:
  data = json.load(f)
  
transaction_name = ''
dict_header = {}
dict_payload = {}

def dFlatten(dico, d = {}): #if nested dict, omit keys of nested dict and print values 
    for k, v in dico.items():
        if isinstance(v, dict):
            dFlatten(v)
        else:
            d[k] = v
    return d

def print_depth(d, start=0): #print every element of nested json and its depth
    global transaction_name
    for key, value in d.items():
        pass
        #print(key, start + 1) #will not print actual items and depth
        if isinstance(value, dict):
            print_depth(value, start=start+1)
            if start==4: #transaction name
                transaction_name += key
                #print(key)
                dict_header.update(value)
            if start==5:
                dict_payload.update(value)

print_depth(data)

flat_header = dFlatten(dict_header)
flat_payload = dFlatten(dict_payload)

payload = dict(list(flat_payload.items())[6:])
header = dict(list(flat_header.items())[:6])

print(transaction_name)
print(header)
print(payload)