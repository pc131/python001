import itertools

C1R_T201W_allowed = ['T203.W', 'T205.W', 'T322.W', 'T323.W']
C1R_T202W_allowed = ['T210.R']
C1R_T203W_allowed = ['T204.R']
C1R_T204R_allowed = ['T203.W', 'T205.W', 'T322.W', 'T323.W']
C1R_T205W_allowed = ['T206.W', 'T212.W', 'T322.W', 'T323.W']
C1R_T206W_allowed = ['T203.W', 'T205.W']
C1R_T210R_allowed = ['T201.W', 'T202.W']
C1R_T212W_allowed = ['T203.W', 'T323.W']
C1R_T321R_allowed = ['T201.W', 'T202.W']
C1R_T322W_allowed = ['T208.R', 'T210.R']
C1R_T323W_allowed = ['T324.R', 'T325.R']
C1R_T324R_allowed = ['T203.W', 'T205.W', 'T322.W']
C1R_T325R_allowed = ['T203.W', 'T323.W']

C1_all_transactions = []
for vars in dir():
    if vars.startswith("C1R"):
        #append list names of every list for current process to create list of any transactions for a process
        C1_all_transactions.append(eval(vars))
C1_all_transactions = list(set(itertools.chain(*C1_all_transactions)))
C1_all_transactions.sort()
#print(type(C1_all_transactions))
for e in C1_all_transactions:
    print(e)