import random
import pyperclip 
import openpyxl as xl

working_dir = "C:\\Users\\skocz\\Downloads\\11\\"
# working_dir = "C:\\Users\\tomasz.skoczylas\\Downloads\\11\\"
spids_meters_filename = working_dir + "TEST_DATA.xlsx"
wb1 = xl.load_workbook(spids_meters_filename)
ws11 = wb1.worksheets[0]
ws12 = wb1.worksheets[1]

spids_meters_filename = working_dir + "TEST_DATA.xlsx"
standalone_spids = wb1.worksheets[1]

def pick_spid_meter_xlsx():
    # how many different SPIDS and METERS to pick from the Excel
    print("{", end = "")
    for a in range(151,451): #choose SPIDs from rows 150-450
        spid = standalone_spids.cell(row=a, column=1).value
        meter_mnf = standalone_spids.cell(row=a, column=4).value
        meter_ser = standalone_spids.cell(row=a, column=5).value
        print("'" + str(spid) + "':('" + str(meter_mnf) + "','" + str(meter_ser) + "')", end = "")
    print("}")
pick_spid_meter_xlsx()