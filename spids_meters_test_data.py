import random
#import pyperclip 
import openpyxl as xl

#working_dir = "C:\\Users\\skocz\\Downloads\\11\\"
working_dir = "C:\\Users\\tomasz.skoczylas\\Downloads\\11\\"
spids_meters_filename = working_dir + "TEST_DATA.xlsx"
wb1 = xl.load_workbook(spids_meters_filename)
ws11 = wb1.worksheets[0]
ws12 = wb1.worksheets[1]

spids_meters_filename = working_dir + "TEST_DATA.xlsx"
standalone_spids = wb1.worksheets[1]

def pick_spid_meter_xlsx():
    # how many different SPIDS and METERS to pick from the Excel
    dict_spids = "{"
    for a in range(51,351): #choose SPIDs from rows 50-350
        spid = standalone_spids.cell(row=a, column=1).value
        meter_mnf = standalone_spids.cell(row=a, column=4).value
        meter_ser = standalone_spids.cell(row=a, column=5).value
        dict_spids += "'" + str(spid) + "':('" + str(meter_mnf) + "','" + str(meter_ser) + "'),"
    dict_spids = dict_spids[:-1] # remove last comma  
    dict_spids += "}"
    print(dict_spids)
    #pyperclip.copy(dict_spids)
pick_spid_meter_xlsx()