import json

with open('states.json') as f:
  data = json.load(f)

dict_payload = {}

def print_depth(d, start=0):
    for key, value in d.items():
        print(key, start + 1)
        if isinstance(value, dict):
            print_depth(value, start=start+1)
            if start==4:
                print(key)
            if start==5:
                dict_payload.update(value)

print_depth(data)

def dFlatten(dico, d = {}):
    for k, v in dico.items():
        if isinstance(v, dict):
            dFlatten(v)
        else:
            d[k] = v
    return d

flat_payload = dFlatten(dict_payload)

payload = dict(list(flat_payload.items())[6:])

print((payload))