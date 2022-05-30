import openpyxl as xl
import os
from datetime import datetime
import random
import string
import names
import sys
from random_address import real_random_address
from faker import Faker
from faker_biology.mol_biol import Enzyme

#working_dir = "C:\\Users\\skocz\\Downloads\\11\\"
working_dir = "C:\\Users\\tomasz.skoczylas\\Downloads\\11\\"
filename = working_dir + "Bilaterals 1.4.0.0 master.xlsx"
wb1 = xl.load_workbook(filename)
ws11 = wb1.worksheets[0]
ws12 = wb1.worksheets[1]

#SLAS B3
#TEST_CASE_TRANSACTIONS = ['T355.R','T355.R','T201.W','T355.R','T201.W','T203.W','T355.R','T201.W','T203.W','T204.R','T355.R','T201.W','T205.W','T355.R','T201.W','T205.W','T206.W','T355.R','T201.W','T224.W','T355.R','T201.W','T205.W','T357.W','T355.R','T202.W','T210.R','T355.W','T201.W','T217.W','T355.W','T201.W','T217.W','T218.R'] #SLAS B3

#T356.W CON-0200 ACTIVITY_STATUSES
#TEST_CASE_TRANSACTIONS = ['T355.R','T356.W','T355.R','T202.W','T356.W','T355.R','T202.W','T210.R','T356.W','T355.R','T201.W','T203.W','T356.W','T355.W','T201.W','T217.W','T356.W','T355.R','T201.W','T205.W','T206.W','T356.W','T355.R','T201.W','T220.W','T356.W']

#SLAS B7
#TEST_CASE_TRANSACTIONS = ['T365.R','T365.R','T201.W','T365.R','T201.W','T203.W','T365.R','T201.W','T203.W','T204.R','T365.R','T201.W','T205.W','T365.R','T201.W','T205.W','T206.W','T365.R','T201.W','T224.W','T365.R','T202.W','T210.R','T365.W','T201.W','T217.W','T365.W','T201.W','T217.W','T218.R'] #SLAS B7

#TEST_CASE_TRANSACTIONS = ['T321.R','T201.W', 'T213.W']

RETAILER = 'MOSLTEST-R'
WHOLESALER = 'MOSLTEST-W'
T216_URL = 'https://moservicesdev.mosl.co.uk/test/attachments/87ffc85e-ebd5-461c-99d6-2ac3eef43f7c'

### MAKE$ SURE THERE IS THE SAME NUMBER OF ELEMENTS IN PROCESSES AND PROC_NAMES DICTIONARIES/TUPLES
PROCESSES = ['B1R', 'B3R', 'B3W', 'B5R', 'B5W', 'B7R', 'C1R', 'C1W', 'F4R', 'F4W', 'F5R', 'F5W', 'G1R', 'G1W', 'G2AR', 'G2AW', 'G2BR', 'G2BW']

PROC_NAMES = {'B1R':'Request Meter Install Work', 'B3R':'Request Meter Accuracy Test', 'B3W':'Request Meter Accuracy Test', 'B5R':'Request Meter Repair Replacement Work', 'B5W':'Request Meter Repair Replacement Work', 'B7R':'Request Meter Change', 'C1R':'Request Meter And Supply Arrangement Verification', 'C1W':'Request Meter And Supply Arrangement Verification', 'F4R':'Submit Non-Household Customer Enquiry', 'F4W':'Submit Non-Household Customer Enquiry', 'F5R':'Submit Non-Household Customer Complaint', 'F5W':'Submit Non-Household Customer Complaint', 'G1R':'Submit Non-Household Customer TE Enquiry', 'G1W':'Submit Non-Household Customer TE Enquiry', 'G2AR':'Submit TE Consent Application With SPID', 'G2AW':'Submit TE Consent Application With SPID', 'G2BR':'Submit TE Consent Application Without SPID', 'G2BW':'Submit TE Consent Application Without SPID'}

TRANSACTION_NAMES = {'T201.W':'Accept Service Request', 'T202.W':'Reject Service Request', 'T203.W':'Request For Additional Information', 'T204.R':'Provide Additional Information', 'T205.W':'Update Site Visit Date', 'T206.W':'Update Site Visit Failure', 'T207.R':'Submit Trading Party Comments', 'T207.W':'Submit Trading Party Comments', 'T208.R':'Close Service Request', 'T210.R':'Resubmit Service Request', 'T211.R':'Cancel Service Request', 'T211.W':'Cancel Service Request', 'T212.W':'Visit Complete And Preparing Plan', 'T213.W':'Start Service Request Deferral', 'T214.W':'End Service Request Deferral', 'T215.R':'Provide Attachment', 'T215.W':'Provide Attachment', 'T216.R':'Request Attachment', 'T216.W':'Request Attachment', 'T217.W':'Request For Customer Details and Additional Information', 'T218.R':'Provide Customer Details and Additional Information', 'T220.W':'Provide Quote For Non Standard Activity', 'T221.R':'Accept Quote For Non Standard Activity', 'T222.W':'Advise Service Request Complete', 'T223.W':'Advise Meter Work Completion', 'T224.W':'Advise Process Delay', 'T321.R':'Request Meter And Supply Arrangement Verification', 'T321.W':'Request Meter And Supply Arrangement Verification', 'T322.W':'Update Corrections Complete for C1', 'T323.W':'Propose Corrections Plan for C1', 'T324.R':'Agree Proposed Corrections Plan for C1', 'T325.R':'Dispute Proposed Corrections Plan for C1', 'T351.R':'Request Meter Repair Replacement Work', 'T351.W':'Request Meter Repair Replacement Work', 'T352.W':'Advise Meter Repair Replacement Work Completion', 'T353.R':'Request Meter Install Work', 'T355.R':'Request Meter Accuracy Test', 'T355.W':'Request Meter Accuracy Test', 'T356.W':'Advise Meter Accuracy Test Complete', 'T357.W':'Awaiting Meter Accuracy Test', 'T365.R':'Request Meter Change', 'T501.R':'Submit Non Household Customer Complaint', 'T501.W':'Submit Non Household Customer Complaint', 'T505.R':'Submit Non Household Customer Enquiry', 'T505.W':'Submit Non Household Customer Enquiry', 'T551.R':'Submit Non Household Customer TE Enquiry', 'T551.W':'Submit Non Household Customer TE Enquiry', 'T555.R':'Submit TE Consent Application With SPID', 'T555.W':'Submit TE Consent Application With SPID', 'T556.R':'Submit TE Consent Application Without SPID', 'T556.W':'Submit TE Consent Application Without SPID', 'T557.W':'Advise TE Consent Application Outcome'}

C1R_TRANSACTIONS = ['T321.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T212.W', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T322.W', 'T323.W', 'T324.R', 'T325.R']
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

C1W_TRANSACTIONS = ['T321.W', 'T201.W', 'T202.W', 'T217.W', 'T218.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T212.W', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T322.W', 'T323.W', 'T324.R', 'T325.R']
C1W_T201W_allowed = ['T217.W', 'T205.W', 'T322.W', 'T323.W']
C1W_T202W_allowed = ['T210.R']
C1W_T217W_allowed = ['T218.R']
C1W_T218R_allowed = ['T217.W', 'T205.W', 'T322.W', 'T323.W']
C1W_T205W_allowed = ['T206.W', 'T212.W', 'T322.W', 'T323.W']
C1W_T206W_allowed = ['T217.W', 'T205.W']
C1W_T210R_allowed = ['T201.W', 'T202.W']
C1W_T212W_allowed = ['T217.W', 'T323.W']
C1W_T321W_allowed = ['T201.W']
C1W_T322W_allowed = ['T208.R', 'T210.R']
C1W_T323W_allowed = ['T324.R', 'T325.R']
C1W_T324R_allowed = ['T217.W', 'T205.W', 'T322.W']
C1W_T325R_allowed = ['T217.W', 'T323.W']

B5R_TRANSACTIONS = ['T351.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T224.W', 'T352.W']
B5R_T201W_allowed = ['T203.W', 'T205.W', 'T224.W', 'T352.W']
B5R_T202W_allowed = ['T210.R']
B5R_T203W_allowed = ['T204.R']
B5R_T204R_allowed = ['T203.W', 'T205.W', 'T224.W', 'T352.W']
B5R_T205W_allowed = ['T206.W', 'T224.W', 'T352.W']
B5R_T206W_allowed = ['T203.W', 'T205.W']
B5R_T210R_allowed = ['T201.W', 'T202.W']
B5R_T224W_allowed = ['T203.W', 'T205.W', 'T352.W']
B5R_T351R_allowed = ['T201.W', 'T202.W']
B5R_T352W_allowed = ['T208.R', 'T210.R']

B5W_TRANSACTIONS = ['T351.W', 'T201.W', 'T202.W', 'T217.W', 'T218.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T224.W', 'T352.W']
B5W_T201W_allowed = ['T217.W', 'T205.W', 'T224.W', 'T352.W']
B5W_T202W_allowed = ['T210.R']
B5W_T217W_allowed = ['T218.R']
B5W_T218R_allowed = ['T217.W', 'T205.W', 'T224.W', 'T352.W']
B5W_T205W_allowed = ['T206.W', 'T224.W', 'T352.W']
B5W_T206W_allowed = ['T217.W', 'T205.W']
B5W_T210R_allowed = ['T201.W', 'T202.W']
B5W_T224W_allowed = ['T217.W', 'T205.W', 'T352.W']
B5W_T351W_allowed = ['T201.W']
B5W_T352W_allowed = ['T208.R', 'T210.R']

B1R_TRANSACTIONS = ['T353.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T220.W', 'T221.R', 'T224.W', 'T223.W']
B1R_T353R_allowed = ['T201.W', 'T202.W']
B1R_T201W_allowed = ['T203.W', 'T205.W', 'T220.W', 'T224.W', 'T223.W']
B1R_T202W_allowed = ['T210.R']
B1R_T203W_allowed = ['T204.R']
B1R_T204R_allowed = ['T203.W', 'T205.W', 'T220.W', 'T224.W', 'T223.W']
B1R_T205W_allowed = ['T206.W', 'T220.W', 'T224.W', 'T223.W']
B1R_T206W_allowed = ['T203.W', 'T205.W']
B1R_T210R_allowed = ['T201.W', 'T202.W']
B1R_T220W_allowed = ['T210.R', 'T221.R']
B1R_T221R_allowed = ['T205.W', 'T224.W', 'T223.W']
B1R_T224W_allowed = ['T203.W', 'T205.W', 'T220.W', 'T223.W']
B1R_T223W_allowed = ['T208.R', 'T210.R']

B3R_TRANSACTIONS = ['T355.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T220.W', 'T221.R', 'T224.W', 'T356.W', 'T357.W']
B3R_T355R_allowed = ['T201.W', 'T202.W']
B3R_T201W_allowed = ['T203.W', 'T205.W', 'T220.W', 'T224.W', 'T356.W']
B3R_T202W_allowed = ['T210.R']
B3R_T203W_allowed = ['T204.R']
B3R_T204R_allowed = ['T203.W', 'T205.W', 'T220.W', 'T224.W', 'T356.W']
B3R_T205W_allowed = ['T206.W', 'T220.W', 'T224.W', 'T357.W', 'T356.W']
B3R_T206W_allowed = ['T203.W', 'T205.W']
B3R_T210R_allowed = ['T201.W', 'T202.W']
B3R_T220W_allowed = ['T210.R', 'T221.R']
B3R_T221R_allowed = ['T205.W', 'T224.W', 'T356.W']
B3R_T224W_allowed = ['T203.W', 'T205.W', 'T220.W', 'T356.W']
B3R_T357W_allowed = ['T356.W']
B3R_T356W_allowed = ['T208.R', 'T210.R']

B3W_TRANSACTIONS = ['T355.W', 'T201.W', 'T202.W', 'T217.W', 'T218.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T220.W', 'T221.R', 'T224.W', 'T356.W', 'T357.W']
B3W_T355W_allowed = ['T201.W']
B3W_T201W_allowed = ['T217.W', 'T205.W', 'T220.W', 'T224.W', 'T356.W']
B3W_T202W_allowed = ['T210.R']
B3W_T217W_allowed = ['T218.R']
B3W_T218R_allowed = ['T217.W', 'T205.W', 'T220.W', 'T224.W', 'T356.W']
B3W_T205W_allowed = ['T206.W', 'T220.W', 'T224.W', 'T357.W', 'T356.W']
B3W_T206W_allowed = ['T217.W', 'T205.W']
B3W_T210R_allowed = ['T201.W', 'T202.W']
B3W_T220W_allowed = ['T210.R', 'T221.R']
B3W_T221R_allowed = ['T205.W', 'T224.W', 'T356.W']
B3W_T224W_allowed = ['T217.W', 'T205.W', 'T220.W', 'T356.W']
B3W_T357W_allowed = ['T356.W']
B3W_T356W_allowed = ['T208.R', 'T210.R']


B7R_TRANSACTIONS = ['T365.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T220.W', 'T221.R', 'T224.W', 'T223.W']
B7R_T365R_allowed = ['T201.W', 'T202.W']
B7R_T201W_allowed = ['T203.W', 'T205.W', 'T220.W', 'T224.W', 'T223.W']
B7R_T202W_allowed = ['T210.R']
B7R_T203W_allowed = ['T204.R']
B7R_T204R_allowed = ['T203.W', 'T205.W', 'T220.W', 'T224.W', 'T223.W']
B7R_T205W_allowed = ['T206.W', 'T220.W', 'T224.W', 'T223.W']
B7R_T206W_allowed = ['T203.W', 'T205.W']
B7R_T210R_allowed = ['T201.W', 'T202.W']
B7R_T220W_allowed = ['T210.R', 'T221.R']
B7R_T221R_allowed = ['T205.W', 'T224.W', 'T223.W']
B7R_T224W_allowed = ['T203.W', 'T205.W', 'T220.W', 'T223.W']
B7R_T223W_allowed = ['T208.R', 'T210.R']

F4R_TRANSACTIONS = ['T505.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T222.W']
F4R_T505R_allowed = ['T201.W', 'T202.W']
F4R_T201W_allowed = ['T203.W', 'T222.W']
F4R_T202W_allowed = ['T210.R']
F4R_T203W_allowed = ['T204.R']
F4R_T204R_allowed = ['T203.W', 'T222.W']
F4R_T210R_allowed = ['T201.W', 'T202.W']
F4R_T222W_allowed = ['T208.R', 'T210.R']

F4W_TRANSACTIONS = ['T505.W', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T222.W']
F4W_T505W_allowed = ['T201.W']
F4W_T201W_allowed = ['T217.W', 'T222.W']
F4W_T202W_allowed = ['T210.R']
F4W_T217W_allowed = ['T218.R']
F4W_T218R_allowed = ['T217.W', 'T222.W']
F4W_T210R_allowed = ['T201.W', 'T202.W']
F4W_T222W_allowed = ['T208.R', 'T210.R']

F5R_TRANSACTIONS = ['T501.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T222.W']
F5R_T501R_allowed = ['T201.W', 'T202.W']
F5R_T201W_allowed = ['T203.W', 'T222.W']
F5R_T202W_allowed = ['T210.R']
F5R_T203W_allowed = ['T204.R']
F5R_T204R_allowed = ['T203.W', 'T222.W']
F5R_T210R_allowed = ['T201.W', 'T202.W']
F5R_T222W_allowed = ['T208.R', 'T210.R']

F5W_TRANSACTIONS = ['T501.W', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T222.W']
F5W_T501W_allowed = ['T201.W']
F5W_T201W_allowed = ['T217.W', 'T222.W']
F5W_T202W_allowed = ['T210.R']
F5W_T217W_allowed = ['T218.R']
F5W_T218R_allowed = ['T217.W', 'T222.W']
F5W_T210R_allowed = ['T201.W', 'T202.W']
F5W_T222W_allowed = ['T208.R', 'T210.R']

G1R_TRANSACTIONS = ['T551.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T222.W']
G1R_T551R_allowed = ['T201.W', 'T202.W']
G1R_T201W_allowed = ['T203.W', 'T222.W']
G1R_T202W_allowed = ['T210.R']
G1R_T203W_allowed = ['T204.R']
G1R_T204R_allowed = ['T203.W', 'T222.W']
G1R_T210R_allowed = ['T201.W', 'T202.W']
G1R_T222W_allowed = ['T208.R', 'T210.R']

G1W_TRANSACTIONS = ['T551.W', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T222.W']
G1W_T551W_allowed = ['T201.W']
G1W_T201W_allowed = ['T217.W', 'T222.W']
G1W_T202W_allowed = ['T210.R']
G1W_T217W_allowed = ['T218.R']
G1W_T218R_allowed = ['T217.W', 'T222.W']
G1W_T210R_allowed = ['T201.W', 'T202.W']
G1W_T222W_allowed = ['T208.R', 'T210.R']

G2AR_TRANSACTIONS = ['T555.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W','T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T224.W', 'T557.W']
G2AR_T201W_allowed = ['T203.W', 'T205.W', 'T224.W', 'T557.W']
G2AR_T202W_allowed = ['T210.R']
G2AR_T203W_allowed = ['T204.R']
G2AR_T204R_allowed = ['T203.W', 'T205.W', 'T224.W', 'T557.W']
G2AR_T205W_allowed = ['T206.W', 'T224.W', 'T557.W']
G2AR_T206W_allowed = ['T203.W', 'T205.W']
G2AR_T210R_allowed = ['T201.W', 'T202.W']
G2AR_T224W_allowed = ['T203.W', 'T205.W', 'T557.W']
G2AR_T555R_allowed = ['T201.W', 'T202.W']
G2AR_T557W_allowed = ['T208.R', 'T210.R']

G2AW_TRANSACTIONS = ['T555.W', 'T201.W', 'T202.W', 'T217.W', 'T218.R', 'T205.W', 'T206.W','T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.W', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T224.W', 'T557.W']
G2AW_T201W_allowed = ['T217.W', 'T205.W', 'T224.W', 'T557.W']
G2AW_T202W_allowed = ['T210.R']
G2AW_T203W_allowed = ['T218.R']
G2AW_T204R_allowed = ['T217.W', 'T205.W', 'T224.W', 'T557.W']
G2AW_T205W_allowed = ['T206.W', 'T224.W', 'T557.W']
G2AW_T206W_allowed = ['T217.W', 'T205.W']
G2AW_T210R_allowed = ['T201.W', 'T202.W']
G2AW_T224W_allowed = ['T217.W', 'T205.W', 'T557.W']
G2AW_T555R_allowed = ['T201.W']
G2AW_T557W_allowed = ['T208.R', 'T210.R']

G2BR_TRANSACTIONS = ['T556.R', 'T201.W', 'T202.W', 'T203.W', 'T204.R', 'T205.W', 'T206.W','T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.R', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T224.W', 'T557.W']
G2BR_T201W_allowed = ['T203.W', 'T205.W', 'T224.W', 'T557.W']
G2BR_T202W_allowed = ['T210.R']
G2BR_T203W_allowed = ['T204.R']
G2BR_T204R_allowed = ['T203.W', 'T205.W', 'T224.W', 'T557.W']
G2BR_T205W_allowed = ['T206.W', 'T224.W', 'T557.W']
G2BR_T206W_allowed = ['T203.W', 'T205.W']
G2BR_T210R_allowed = ['T201.W', 'T202.W']
G2BR_T224W_allowed = ['T203.W', 'T205.W', 'T557.W']
G2BR_T555R_allowed = ['T201.W', 'T202.W']
G2BR_T557W_allowed = ['T208.R', 'T210.R']

G2BW_TRANSACTIONS = ['T556.W', 'T201.W', 'T202.W', 'T217.W', 'T218.R', 'T205.W', 'T206.W','T207.R', 'T207.W', 'T208.R', 'T210.R', 'T211.W', 'T213.W', 'T214.W', 'T215.R', 'T215.W', 'T216.R', 'T216.W', 'T224.W', 'T557.W']
G2BW_T201W_allowed = ['T217.W', 'T205.W', 'T224.W', 'T557.W']
G2BW_T202W_allowed = ['T210.R']
G2BW_T203W_allowed = ['T218.R']
G2BW_T204R_allowed = ['T217.W', 'T205.W', 'T224.W', 'T557.W']
G2BW_T205W_allowed = ['T206.W', 'T224.W', 'T557.W']
G2BW_T206W_allowed = ['T217.W', 'T205.W']
G2BW_T210R_allowed = ['T201.W', 'T202.W']
G2BW_T224W_allowed = ['T217.W', 'T205.W', 'T557.W']
G2BW_T555R_allowed = ['T201.W']
G2BW_T557W_allowed = ['T208.R', 'T210.R']

POSTCODES = ['B1 1HQ', 'BN88 1AH', 'BS98 1TL', 'BX1 1LT', 'BX2 1LB', 'BX3 2BB', 'BX4 7SB', 'BX5 5AT', 'CF10 1BH', 'CF99 1NA', 'CO4 3SQ', 'CV4 8UW', 'CV35 0DB', 'E14 5EY', 'DA1 1RT', 'DE99 3GG', 'DE55 4SW', 'DH98 1BT', 'DH99 1NS', 'E14 5HQ', 'E14 5JP', 'E16 1XL', 'E20 2AQ', 'E20 2BB', 'E20 2ST', 'E20 3BS', 'E20 3EL', 'E20 3ET', 'E20 3HB', 'E20 3HY', 'E98 1SN', 'E98 1ST', 'E98 1TT', 'EC2N 2DB', 'EC4Y 0HQ', 'EH12 1HQ', 'EH99 1SP', 'G58 1SB', 'GIR 0AA', 'IV21 2LR', 'L30 4GB', 'LS98 1FD', 'M50 2BH', 'M50 2QH', 'N1 9G', 'N81 1ER', 'NE1 4ST', 'NG80 1EH', 'NG80 1LH', 'NG80 1RH', 'NG80 1TH', 'PH1 5RB', 'PH1 2SJ', 'S2 4SU	', 'S6 1SW', 'S14 7UP', 'SE1 0NE', 'SE1 8UJ', 'SM6 0HB', 'SN38 1NW', 'SR5 1SU', 'SW1A 0AA', 'SW1A 0PW', 'SW1A 1AA', 'SW1A 2AA', 'SW1A 2AB', 'SW1H 0TL', 'SW1P 3EU', 'SW1W 0DT', 'SW11 7US', 'SW19 5AE', 'TW8 9GS', 'W1A 1AA', 'W1D 4FA', 'W1N 4DJ', 'W1T 1FB']

SPIDS_METERS = {'3019029147W10':('ARAD','9158366'),'3019029449W13':('ARAD','8174844'),'3019029546W14':('KENT','95A138505'),'301903020XW1X':('KENT','4M097305'),'3019031214W11':('AQUADIS','98PB300065'),'301903129XW1X':('ELSTER','4M093252'),'3019031559W13':('KENT','95A521326'),'3019031567W10':('KENT','93M154072'),'3019031591W12':('ELSTER','8999775'),'3019031621W12':('ARAD','8270804'),'301903258XW1X':('KENT','93A556059'),'3019032628W17':('KENT','91P033387'),'3019032946W14':('ARAD','19AI0097'),'3019032997W10':('KENT','PC502819'),'3019033004W11':('KENT','AE183174'),'3019033012W19':('KENT','79011716'),'3019033020W16':('KENT','73225966'),'3019033047W10':('ARAD','8013499'),'3019033101W12':('KENT','AM014229'),'3019033136W14':('ELSTER','10AC017906'),'3019033144W11':('KENT','82099364'),'3019033160W16':('NEPTUNE_MEASUREMENT','321187'),'3019033195W18':('ARAD','8584440'),'3019033322W19':('ELSTER','9080130'),'3019033330W16':('ELSTER','8288295'),'3019033381W12':('KENT','73260854'),'3019033411W12':('SW_METER','9M129985'),'301903342XW1X':('KENT','AL034255'),'301903275XW1X':('ELSTER','12207830'),'3019032938W17':('ARAD','9103768'),'3019032954W11':('ELSTER','9097938'),'3019033039W13':('KENT','97A080026'),'301903308XW1X':('ARAD','8567195'),'301903311XW1X':('KENT','529791'),'3019033128W17':('KENT','6259797'),'3019033152W19':('KENT','4A054549'),'3019033276W14':('ARAD','9089368'),'3019033306W14':('KENT','4T009453'),'3019033373W15':('ARAD','9108738'),'3019033438W17':('NEPTUNE_MEASUREMENT','368175'),'3019033594W11':('KENT','4A022325'),'3019033632W19':('KENT','82099358'),'3019033721W12':('KENT','638354'),'301903373XW1X':('KENT','3M060812'),'3019033837W10':('SW_METER','8T000006'),'3019033926W14':('SW_METER','14AI0081'),'3019033942W19':('KENT','88956495'),'3019034248W17':('ARAD','19AI0007'),'3019034302W19':('KENT','4T008504'),'3019034310W16':('ARAD','9110493'),'3019034329W13':('KENT','82099354'),'3019034353W15':('ELSTER','8519601'),'301903440XW1X':('KENT','4A023517'),'3019034442W19':('ARAD','8581881'),'3019034493W15':('SW_METER','9M085429'),'3019034523W15':('KENT','77103706'),'3019034531W12':('SW_METER','9M085488'),'3019034558W17':('KENT','4T001980'),'3019034604W11':('KENT','96PA186798'),'3019034620W16':('ELSTER','8121663'),'3019034647W10':('KENT','AG610527'),'3019034701W12':('KENT','AG610561'),'301903471XW1X':('KENT','82099636'),'3019034787W10':('ARAD','9104029'),'3019034868W17':('KENT','3T039347'),'3019033462W19':('KENT','4A052252'),'3019033500W16':('KENT','4T015998'),'3019033535W18':('KENT','4A022358'),'3019033578W17':('KENT','86027961'),'3019033624W11':('KENT','73261507'),'3019033659W13':('ARAD','9124697'),'3019033667W10':('KENT','88457019'),'3019033829W13':('KENT','4A023413'),'3019033845W18':('KENT','3A246396'),'3019033853W15':('KENT','8507331'),'3019033888W17':('ARAD','9120052'),'3019033985W18':('ARAD','8092170'),'3019034280W16':('ARAD','8129527'),'3019034426W14':('ARAD','9020503'),'3019034485W18':('KENT','93P015776'),'3019034515W18':('SW_METER','9M095672'),'301903454XW1X':('KENT','4T006850'),'3019034566W14':('KENT','220212'),'3019034612W19':('KENT','WPE043218'),'3019034639W13':('AMR','8343205'),'3019034671W12':('KENT','82089042'),'301903468XW1X':('SW_METER','7M074199'),'3019034728W17':('KENT','AF518192'),'3019034779W13':('KENT','88456965'),'3019034809W13':('SW_METER','8M397558'),'3019034833W15':('KENT','AL034252'),'3019034914W11':('SW_METER','9T015339'),'3019034949W13':('kent','73220220'),'3019034973W15':('ARAD','9140514'),'3019034981W12':('SW_METER','8M311480'),'301903499XW1X':('KENT','4A054417'),'3019035007W10':('KENT','4T008509'),'3019035023W15':('KENT','73305103'),'3019035201W12':('KENT','87023121'),'301903521XW1X':('KENT','82095757'),'3019035228W17':('KENT','95A508431'),'3019035260W16':('KENT','AE183187'),'3019035317W10':('KENT','8299361'),'3019035325W18':('NEPTUNE_MEASUREMENT','321190'),'3019035384W11':('KENT','85014753'),'3019035414W11':('AQUADIS','95AL000831'),'3019035570W16':('KENT','4T012592'),'3019035619W13':('KENT','80049472'),'3019035643W15':('SW_METER','9T029602'),'3019035678W17':('NEPTUNE_MEASUREMENT','91P017267'),'3019035988W17':('KENT','220219'),'3019036089W13':('SW_METER','7A107117'),'3019036143W15':('KENT','4M024093'),'3019036240W16':('SW_METER','9M141944'),'3019036380W16':('KENT','91M073839'),'3019036380W16':('SW_METER','8M000313'),'3019036380W16':('KENT','4M197330'),'3019036925W18':('KENT','82077936'),'3019037107W10':('KENT','283701'),'3019034876W14':('ARAD','15A10253'),'3019034892W19':('ARAD','8082645'),'3019034930W16':('KENT','AG529758'),'3019035155W18':('KENT','95A512022'),'3019035236W14':('KENT','4A023551'),'3019035309W13':('KENT','529755'),'3019035627W10':('NEPTUNE_MEASUREMENT','321203'),'301903616XW1X':('ARAD','11M50051'),'3019036399W13':('ARAD','12A10045'),'3019036453W15':('KENT','3M335594'),'3019036518W17':('KENT','94A019448'),'301903681XW1X':('ARAD','8284361'),'3019037034W11':('KENT','4A226311'),'301903728XW1X':('KENT','5M194944'),'3019037522W19':('SW_METER','9A002004'),'3019037565W18':('KENT','3M084158'),'301903759XW1X':('ELSTER','8966848'),'3019037786W14':('KENT','98AQ400449'),'3019037816W14':('KENT','4T006847'),'3019037867W10':('KENT','4M199310'),'3019037891W12':('KENT','99A800249'),'3019037921W12':('SCHLUMBERGER','A818084'),'3019038332W19':('SCHLUMBERGER','AM064395'),'3019038383W15':('KENT','4M210802'),'3019038472W19':('KENT','1M219589'),'3019038480W16':('ELSTER','1M219595'),'3019038820W16':('arad','16744175'),'3019038901W12':('SCHLUMBERGER','AM081632'),'3019038928W17':('SCHLUMBERGER','97AQ243744'),'3019039053W15':('KENT','4M059132'),'3019039088W17':('KENT','88462105'),'3019039142W19':('SCHLUMBERGER','1M067158'),'3019039274W11':('KENT','2M234032'),'3019037182W19':('ABB','2A187212'),'3019037360W16':('KENT','6M176862'),'3019037441W12':('KENT','4T012469'),'3019037484W11':('KENT','6M425941'),'3019037506W14':('ARAD','8043511'),'3019037573W15':('ARAD','4T032767'),'3019037700W16':('SW_METER','8A083610'),'3019037743W15':('LEEDS','1542982'),'3019037824W11':('KENT','79011720'),'3019038146W14':('KENT','6A098406'),'3019038464W11':('KENT','1M219587'),'3019038499W13':('ELSTER','1M219598'),'3019038502W19':('KENT','5M001605'),'3019038510W16':('KENT','4A023433'),'3019038537W10':('ARAD','8961523'),'3019038561W12':('KENT','4M101597'),'3019038782W19':('SCHLUMBERGER','99AQ497048'),'3019038979W13':('KENT','4M080206'),'3019039029W13':('KENT','4M080207'),'3019039118W17':('KENT','4M080597'),'3019039150W16':('SCHLUMBERGER','AM024355'),'3019039320W16':('KENT','1A138138'),'301903941XW1X':('KENT','4M154071'),'3019039460W16':('SW_METER','7M088732'),'301903969XW1X':('KENT','5M228906'),'3019040191W12':('KENT','99A821994'),'3019040248W17':('KENT','3M143309'),'3019040302W19':('ELSTER','8075202'),'3019040361W12':('ELSTER','14A10320'),'3019040388W17':('KENT','4M080592'),'3019040396W14':('KENT','4M080561'),'3019040515W18':('KENT','2M169236'),'3019040523W15':('KENT','2M200561'),'301904054XW1X':('ARAD','8454324'),'3019039363W15':('KENT','4A225912'),'3019039428W17':('KENT','4M135961'),'3019039606W14':('SW_METER','11A10390'),'301903972XW1X':('ELSTER','8H701245'),'301903972XW1X':('SW_METER','8M132666'),'3019039940W16':('KENT','91M132387'),'3019040035W18':('KENT','99S000677'),'3019040159W13':('ARAD','8387320'),'3019040183W15':('ELSTER','8031782'),'3019040310W16':('ELSTER','8114237'),'3019040345W18':('ARAD','8152946'),'3019040477W10':('SCHLUMBERGER','98AQ818736'),'3019040507W10':('KENT','1M087304'),'3019040574W11':('KENT','2M200506'),'3019040612W19':('KENT','A803702'),'3019040736W14':('SW_METER','7M581364'),'3019040760W16':('SW_METER','9M330905'),'3019040787W10':('SW_METER','8038001'),'3019040825W18':('KENT','4A061578'),'3019040892W19':('ARAD','8050166'),'3019040906W14':('ARAD','8278090'),'3019040914W11':('KENT','4M093744'),'301904099XW1X':('ARAD','8571996'),'3019041007W10':('ARAD','8546933'),'3019041252W19':('ARAD','9079176'),'301904152XW1X':('SCHLUMBERGER','98AQ318794'),'3019041570W16':('ARAD','11A10204'),'3019041899W13':('ARAD','9119470'),'3019041929W13':('KENT','4A219342'),'3019041953W15':('SCHLUMBERGER','97PA082083'),'3019042402W19':('SCHLUMBERGER','97AQ195462'),'3019042526W14':('ARAD','8242307'),'3019042623W15':('NA','16A10037'),'3019042720W16':('ARAD','193015905'),'3019043042W19':('KENT','94A009976'),'3019043050W16':('KENT','4A093824'),'3019043107W10':('ARAD','12MS2541'),'3019040566W14':('KENT','2M200564'),'301904068XW1X':('KENT','4M154076'),'3019040701W12':('SW_METER','6M403670'),'3019040779W13':('SW_METER','3M326375'),'3019040973W15':('ARAD','13MS0544'),'3019041058W17':('ARAD','9073476'),'3019041104W11':('ARAD','15AI0197'),'3019041325W18':('ARAD','9079629'),'3019041341W12':('ARAD','9032093'),'3019041481W12':('KENT','82095771'),'3019041651W12':('KENT','96A511301'),'3019041813W15':('KENT','91P028446'),'3019041961W12':('KENT','72127097'),'3019042178W17':('KENT','4A052782'),'3019042224W11':('KENT','5A207109'),'3019042461W12':('ARAD','9146392'),'3019042739W13':('KENT','4T001954'),'301904278XW1X':('ARAD','9M022455'),'3019043336W14':('ARAD','8478760'),'3019044049W13':('SW_METER','9M031356'),'3019044057W10':('ATLANTIC_PLASTIC','4M026220'),'301904426XW1X':('ELSTER','9M022292'),'3019044405W18':('KENT','4A029996'),'3019044448W17':('ELSTER','8033850'),'3019044685W18':('KENT','1M234270'),'3019044839W13':('NEPTUNE_MEASUREMENT','4A035621'),'3019045037W10':('ELSTER','8187996'),'3019045355W18':('ABB','93A769075'),'3019045487W10':('SW_METER','8M000051'),'3019045665W18':('KENT','93M178526'),'3019045681W12':('KENT','94M083342'),'3019045703W15':('ARAD','8011043'),'301904572XW1X':('KENT','93A637555'),'3019045835W18':('KENT','82117218'),'3019045886W14':('KENT','4T008477'),'3019043492W19':('ELSTER','8M007735'),'3019043557W10':('ARAD','8258278'),'3019043859W13':('SCHLUMBERGER','96A526434'),'3019043875W18':('ARAD','3M326279'),'3019043891W12':('ARAD','9133305'),'301904393XW1X':('KENT','81079413'),'301904409XW1X':('NEPTUNE_MEASUREMENT','99AL011921'),'3019044189W13':('ELSETR','9052258'),'3019044383W15':('ELSTER','8M115498'),'301904474XW1X':('KENT','93A769285'),'3019044782W19':('ELSTER','10A10096'),'3019044812W19':('SCHLUMBERGER','96AQ104874'),'3019044863W15':('KENT','82099502'),'3019045061W12':('KENT','5M001411'),'3019045088W17':('ARAD','9114084'),'3019045169W13':('SW_METER','4T023709'),'3019045282W19':('ELSTER','8068457'),'301904538XW1X':('KENT','25036'),'301904569XW1X':('KENT','94M082961'),'301904586XW1X':('KENT','86081627'),'3019046106W14':('ARAD','8466909'),'3019046181W12':('KENT','4S000195'),'3019046203W15':('KENT','99AQ489687'),'3019046211W12':('KENT','4A096864'),'3019046262W19':('KENT','72135824'),'3019046335W18':('KENT','95M101084'),'3019046750W16':('KENT','4T018328'),'3019046777W10':('ARAD','9135711'),'3019046939W13':('ARAD','8113381'),'3019047161W12':('NEPTUNE_MEASUREMENT','AB105976'),'3019047277W10':('SCHLUMBERGER','98AQ366589'),'3019047293W15':('KENT','3M244804'),'3019047471W12':('SCHLUMBERGER','AF382207'),'3019047579W13':('KENT','95M118258'),'3019047587W10':('ABB','97PC600154'),'3019047617W10':('KENT','6M091526'),'3019045940W16':('ATLANTIC_PLASTIC','94A019422'),'3019045975W18':('KENT','90P194319'),'3019045991W12':('KENT','91542482'),'3019046025W18':('ARAD','8549593'),'3019046068W17':('ARAD','9105399'),'301904619XW1X':('KENT','5M061497')}

fake = Faker()
fake.add_provider(Enzyme)

#pick random SPID, METER_MNF_ METER_SERIAL
def pick_spid_meter():
    spid_meter = random.choice(list(SPIDS_METERS.items()))
    spid = spid_meter[0]
    meter_mnf = spid_meter[1][0]
    meter_ser = spid_meter[1][1]
    return spid, meter_mnf, meter_ser

def random_email():
    return fake.company_email()

def random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15))

def random_name():
    return names.get_full_name()

def random_phone():
    return random.randint(4400000000, 4499999999)

def random_meter_ser():
    return '10W' + str(random.randint(0000000000, 9999999999))

def random_meter_mnf():
    return ''.join(random.choice(string.ascii_letters).upper() for _ in range(random.randint(4, 10)))

def random_gisx():
    return random.randint(82644, 655612)

def random_gisy():
    return random.randint(5186, 657421)

def random_meter_loc():
    return random.choice(['UNDER_THE_TREE', 'SOMEWHERE', 'IN_THE_BASEMENT', 'ON_THE_ROOF', 'UNDER_THE_SINK', 'NO_IDEA_WHERE', 'IN_THE_BACKYARD', 'BELOW_THE_WINDOW'])

def date_not_weekend():
    if datetime.today().weekday() >=0 and datetime.today().weekday() <=3:
        return '[today+' + str(4 - datetime.today().weekday()) + ']'
    else:
        return '[today+3]'

def time_not_weekend():
    if datetime.today().weekday() >=0 and datetime.today().weekday() <=3:
        return '[now+' + str(4 - datetime.today().weekday()) + ']'
    else: 
        return '[now+3]'
    
def get_random_address(): # !!!!!!!!!! LEARN HOW TO USE IT
    rand_address =  real_random_address()
    return rand_address["address1"]

#C1
D8036 = ['ERROR', 'DUPLICATE', 'SWITCHED', 'REJECTION', 'UNABLEASST', 'DISAGREEPLAN'] # T211.R T211.W Cancellation Reason Code
D8226 = ['NOCONTACT', 'UNCOOPCUST', 'INACCONTACT', 'MOREDETAILS'] # T203.W T217W Additional Information Request Code
D8228 = ['WHOL', 'NONWHOL'] # T206.W Site Visit Failure Code
D8229 = ['CUSTOMER', 'RETAILER', 'THIRDPARTY', 'CONSENTS', 'REGULAT', 'WEATHER', 'FORCEMAJ', 'INFOREQD'] # T213.W Request Deferral Code
D8230 = ['INACCURATE', 'DUPLICATE', 'WRONGPRO', 'POLICY', 'HOUSEHOLD', 'NOTWHOL'] # T202.W Reject Reason Code
D8231 = ['DISPREJECT', 'DISPCMOS'] # T210.R Resubmit Reason Code
D8236 = ['EMAIL', 'TEL', 'BOTH'] # T321.R T321.W Customer Preferred Method of Contact
D2005 = ['SEMDV', 'NA'] # T321.R T321.W Customer Classification – Sensitive Customer
D8237 = ['AM', 'PM', 'BOTH'] # T321.R T321.W
D8242 = ['METER', 'SUPPLY', 'BOTH'] # T321.R T321.W
D8262 = ['ACCEPT', 'REJECT'] # T321.R T321.W
D8242 = ['PDF', 'JPG', 'PNG'] # T215.R T215.W
D3025 = ['I', 'O']

#B1 #B7
D8327 = ['NEWINSTALL', 'CHGNEW', 'LOCCHGNEW', 'LOCCHGEXG', 'UNFEASIBLE'] # B1 B7 COMPLETED T223.W -> Meter Work Complete Code

#B3
D8346 = ['INSIDE', 'OUTSIDE', 'UNKNOWN'] # T353.R Meter Location Code
D8348 = ['OVERRECORD', 'UNDERRECORD', 'OTHER'] # T353.R Meter Location Code
D8367 = ['AFTEREXCHG', 'ALREADYTESTSED', 'INSITUTESTED']
D8368 = ['WITHIN', 'OUTSIDE']
D8369 = ['1', '0']

#B5
D8227 = ['PARTS', 'STREETWORKS', 'THIRDPARTY', 'CUSTCONFRM', 'PREPWORK', 'OTHER'] # T224.W Delay Reason Code - B5R B5W - Advise Process Delay
D8332 = ['NOISSUE', 'NOWATER', 'FLOODING'] # T351.R T351.W Public Health Issue
D8333 = ['REMOVED', 'NOTREMOVED'] # T351.R T351.W Datalogger Status
D8335 = ['STD', 'NONSTD'] # T351.R T351.W Meter Model
D8337 = D8838 = D8839 = ['STOPPED', 'BACKWARD', 'SLOWED', 'BURRIED', 'CONDENS', 'ELECT', 'BURST', 'SMASHED', 'REMOVED', 'NONMETER', 'OTHER'] # T351.R T351.W Meter Fault
D8330 = ['0', '1'] #T351.R T351.W Meter Fault address same as CMOS
D8341 = ['REPLACED', 'REPAIRED', 'NOUPDATE', 'NOFAULT', 'NONMETER', 'UPDATE'] # T352.W Complete Reason Code

#B7
D8326 = ['CHGTYPE', 'CHGSSIZE', 'CHGLSIZE', 'CHGLOC'] # B7 T365.R Request Meter Change -> Meter Work Request Type

#F4
D8364 = ['DWENQUIRY', 'OTHERENQUIRY'] # F4 T505.R Request Type
D8365 = ['WATERQUALITY', 'FLUORIDE', 'HARDNESS', 'QUALITYREPT', 'GENERAL', 'ANIMALS', 'LEAD', 'PUBLICINFO'] # F4 T505.R Drinking Water Enquiry Type - D8364 = 'DWENQUIRY'
D8352 = ['FOLLOWON', 'NOFOLLOWON'] #F4 T222.W Response Type

#F5
D8356 = ['FIRST', 'FURTHER', 'CCWLEVEL', 'ADR', 'OTHER'] #F5 T501.R/W Complaint Level
D8358 = ['ADMINISTRATION', 'METERINGASSET', 'BILLING', 'WATER', 'SEWERAGE', 'OTHER'] #F5 T501.R/W Complaint Category
D8360 = ['GSSFAILURE', 'OTHER', 'NONE'] #F5 T501.R/W Compensation Claimed

#G2A G2B
D8371 = ['NEWCONSENT', 'NEWTEMPCONSENT', 'RENEWCONSENT']
D8374 =	['YES', 'NO', 'NA']
D8375 =	['YES', 'NO', 'NA']
D8376 =	['YES', 'NO', 'NA']
D8377 =	['YES', 'NO', 'NA']
D8378 =	['YES', 'NO', 'NA']
D8379 =	['YES', 'NO', 'NA']
D8380 =	['YES', 'NO', 'NA']
D8381 =	['YES', 'NO', 'NA']
D8382 =	['NOTREQD', 'GRANTED', 'NOTGRANTED']
D8383 =	['PERMANENT', 'TEMPORARY', 'RENEWAL']

test_case_sequence = []
def generate_test_case(loop_times):
    global test_case_sequence
    new_filename = ""
    program_mode = input("Do you want to run in [I]interactive or [P]redefined mode? ")
    while program_mode not in ('I', 'P'):
        program_mode = input("You can choose only from [I]interactive or [P}redefined mode? What's your choice? ")
    if program_mode == 'I':
        ############################################################### ASK USER WHICH TEST CASE HE/SHE WANTS
        available_processes = ""
        for b in range(len(PROC_NAMES)):
            ################################################################### get process name from PROC_NAMES  + get process description
            available_processes = available_processes + "{:2}".format(b+1) + " - " + list(PROC_NAMES.keys())[b] + " - " +  PROC_NAMES.get(list(PROC_NAMES.keys())[b])+ "\n"
        chosen_process = input("Choose process to start with - available are: \n\n" + available_processes + "\n")
        while ((not chosen_process.isdigit()) or (int(chosen_process) not in range(1, len(PROC_NAMES)+1))):
                chosen_process = input("\nWrong choice! You can only choose from available processes: \n" + available_processes + "\nChoose process:")
        chosen_proc = int(chosen_process)
        print("\nYour choice: " + str(list(PROC_NAMES.keys())[chosen_proc-1]) + " - " +  PROC_NAMES.get(PROCESSES[chosen_proc-1])) 
        
        #choose 1st transaction from chosen process i.e. C1R + _TRANSACTIONS
        chosen_process1 = globals()[PROCESSES[chosen_proc-1] + '_TRANSACTIONS']
        starting_transaction = chosen_process1[0]
        
        #append initiating transaction to the TEST_CASE_SEQUENCE
        test_case_sequence.append(starting_transaction)
        more_transactions = input("I will generate test case with transaction:\n" + starting_transaction + " - " + TRANSACTION_NAMES.get(starting_transaction) + "\nDo you want to add more transactions for current process? [Y]/[N], [C]hange process or [A]ny transaction from current process?\n")
        while more_transactions not in ('Y', 'N', 'C', 'A'):
            more_transactions = input("You can only choose [Y]es, [N]o, [C]hange or [A]ny. Do you want to add more transactions for current process? [Y]/[N], [C]hange process or [A]ny transaction from current process?\n")
        if more_transactions =='N':
            print("Generating a test case, thank you. Bye!")
        if more_transactions == 'C':
            generate_test_case(max_loop) # REPEAT FROM START - TEST_CASE_SEQUENCE WILL NOT BE OVERWRITTEN!!!!    
            
        # when A selected loop through all transactions in the process, when Y selected loop through available transactions in the process    
        while more_transactions == 'Y' or more_transactions == 'A':
            if  more_transactions == 'A':
                next_transactions = globals()[PROCESSES[chosen_proc-1] + '_TRANSACTIONS']
            if more_transactions == 'Y':   
                next_transactions = globals()[PROCESSES[chosen_proc-1] + '_' + starting_transaction.replace('.', '') + '_allowed']
            print("\nAvailable transactions for this process are:")
            next_transactions1 = ""
            for i in range(len(next_transactions)):
                next_transactions1 += str(i+1) + " " + next_transactions[i] + "\n" 
                print(str(i+1) + " " + str(next_transactions[i]) + " - " + TRANSACTION_NAMES.get(next_transactions[i]))
            print('\n')
            next_transaction = input("Which transaction you want next?\n")
            #allow user to choose only valid transactions - check if user inpur is digit and it is from allowed range
            while ((not next_transaction.isdigit()) or (int(next_transaction) not in range(1, len(next_transactions)+1))):
                    next_transaction = input("You can only choose from available transactions \n" + next_transactions1  + "\nChoose transaction: ")
            next_tran = int(next_transaction)
            print("Your choice: " + str(next_transactions[next_tran-1])) 
            test_case_sequence.append(next_transactions[next_tran-1])
            # if in available processes mode exit when found T208.R
            if more_transactions == 'Y' and str(next_transactions[next_tran-1]) == 'T208.R':
                print("\nTest case sequence:")
                print(test_case_sequence)
                print("\nT208.R was the last transaction. Generating a test case, thank you. Bye!")
                break
            print("\nTest case sequence:")
            print(test_case_sequence)
            starting_transaction = next_transactions[next_tran-1]
            more_transactions = input("Do you want to add more transactions for current process? [Y]/[N], [C]hange process or [A]ny transaction from current process?\n")
            while more_transactions not in ('Y', 'N', 'C', 'A'):
                more_transactions = input("You can only choose [Y]es, [N]o, [C]hange or [A]ny. Do you want to add more transactions for current process? [Y]/[N], [C]hange process or [A]ny transaction from current process?\n")
            if more_transactions == 'C':
                generate_test_case(max_loop) # REPEAT FROM START - TEST_CASE_SEQUENCE WILL NOT BE OVERWRITTEN!!!!                   
            if more_transactions =='N':
                print("Generating a test case, thank you. Bye!") 
    if program_mode == 'P':
        test_case_sequence = TEST_CASE_TRANSACTIONS        
##############################################################################    
    for a in range(loop_times):
        # assign random SPID, METER_MNF, METER_SERIAL to variables - use EXCEL or SPIDS_METERS static dictionary
        SPID, METER_MNF, METER_SER = pick_spid_meter()
        CUST_EMAIL = random_email()
        RET_EMAIL = random_email()
        RANDOM_STRING = random_string()
        CUST_RANDOM_NAME = random_name()
        CUST_RANDOM_PHONE = random_phone()
        RET_RANDOM_NAME = random_name()
        RET_RANDOM_PHONE = random_phone()
        CUST_RANDOM_NAME2 = random_name()
        CUST_RANDOM_PHONE2 = random_phone()
        RET_RANDOM_NAME2 = random_name()
        RET_RANDOM_PHONE2 = random_phone()
        RANDOM_METER_SER = random_meter_ser()
        RANDOM_METER_MNF = random_meter_mnf()
        RANDOM_GISX = random_gisx()
        RANDOM_GISY = random_gisy()
        OUTR_RANDOM_GISX = random_gisx()
        OUTR_RANDOM_GISY = random_gisy()
        RANDOM_METER_LOC = random_meter_loc()
        RANDOM_OUTRE_LOC = random_meter_loc()
        DATE_NOT_WEEKEND = date_not_weekend()
        TIME_NOT_WEEKEND = time_not_weekend()
        RANDOM_ADDRESS1 = get_random_address()
        RANDOM_ADDRESS2 = get_random_address()
        RANDOM_ADDRESS3 = get_random_address()
        RANDOM_ADDRESS4 = get_random_address()
        RANDOM_ADDRESS5 = get_random_address()

        T321R_data_items = [# basic data
                        SPID, 'MEASURED', 'RET_' + RANDOM_STRING, '', '1', '[today]', '1',
                        # customer and retailer data
                        CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                        RANDOM_STRING, random.choice(D2005), RANDOM_STRING, RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                        # first meter details
                        METER_MNF, METER_SER, '0', '120', '[today-1]', '0', 'METER', '1', RANDOM_METER_MNF, '1', RANDOM_METER_SER, '1', '5', '1', '5',
                        '1', RANDOM_GISX, '1', RANDOM_GISY, '1', 'O', '1', RANDOM_METER_LOC, '1', OUTR_RANDOM_GISX, '1', OUTR_RANDOM_GISY, '1', 'I', '1', RANDOM_OUTRE_LOC, RANDOM_STRING, '',
                        # second meter details empty
                        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                        # missing meters
                        '', '', '', '',
                        # unmeasrued data empty
                        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
                        ]
        T321W_data_items = [# basic data
                        SPID, 'MEASURED', '', '[today]',
                        # first meter details
                        METER_MNF, METER_SER, '0', '120', '[today-1]', '0', 'METER', '1', RANDOM_METER_MNF, '1', RANDOM_METER_SER, '1', '5', '1', '5',
                        '1', RANDOM_GISX, '1', RANDOM_GISY, '1', 'O', '1', RANDOM_METER_LOC, '1', OUTR_RANDOM_GISX, '1', OUTR_RANDOM_GISY, '1', 'I', '1', RANDOM_OUTRE_LOC, RANDOM_STRING, '',
                        # second meter details empty
                        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                        # missing meters
                        '', '', '', '',
                        # unmeasrued data empty
                        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
                        ]
        T201W_data_items = ['[orid]', 'ACCEPTED']
        T202W_data_items = ['[orid]', 'WSL-123456', random.choice(D8230), 'REJECTED']
        T203W_data_items = ['[orid]', random.choice(D8226), 'INFOREQST']
        T204R_data_items = ['[orid]', 'INFOPROVD']
        T205W_data_items = ['[orid]', DATE_NOT_WEEKEND, '', 'VISITSCHED']
        T206W_data_items = ['[orid]', random.choice(D8228), 'VISITNOTCOMP']
        T207R_data_items = ['[orid]', 'RETAILER_COMMENT']
        T207W_data_items = ['[orid]', 'WHOLESALER_COMMENT']
        T208R_data_items = ['[orid]', 'CLOSED']
        T210R_data_items = ['[orid]', random.choice(D8231), 'RESUBMITTED']
        T211R_data_items = ['[orid]', random.choice(D8036), 'RTL CANCELLED']
        T211W_data_items = ['[orid]', random.choice(D8036), 'WSL CANCELLED']
        T212W_data_items = ['[orid]', 'PREPPLAN']
        T213W_data_items = ['[orid]', random.choice(D8229), '[today]', '[today+1]', 'START_DEFERRAL']
        T214W_data_items = ['[orid]', '[today]', 'END_DEFERRAL'] # can think of function to peek working day
        T215R_data_items = ['[orid]', '', 'img1png', 'PNG', '4oCwUE5HChoKICAgCklIRFIgICADICAgAwgCICAgxa5KIsSNICAgCXBIWXMgIA7DhCAgDsOEAeKAoisOGyAgICdJREFUCOKEomPDlG7Dn8O2y5nLmX8BNnbCpn/LmcWjMTMzH8OrxI9nYmXLmXd5w7cmxLrFmBAgxZDFnwrFpH4uJsKsICAgIElFTkTCrkJg4oCa']
        T215W_data_items = ['[orid]', '', 'img1png', 'PNG', '4oCwUE5HChoKICAgCklIRFIgICADICAgAwgCICAgxa5KIsSNICAgCXBIWXMgIA7DhCAgDsOEAeKAoisOGyAgICdJREFUCOKEomPDlG7Dn8O2y5nLmX8BNnbCpn/LmcWjMTMzH8OrxI9nYmXLmXd5w7cmxLrFmBAgxZDFnwrFpH4uJsKsICAgIElFTkTCrkJg4oCa']
        T216R_data_items = ['[orid]', T216_URL]
        T216W_data_items = ['[orid]', T216_URL]
        T217W_data_items = ['[orid]', '1', random.choice(D8226), 'CUSTINFOREQST']

        T218R_data_items = ['[orid]', 'RET_' + RANDOM_STRING, '[today]',
                             '1', CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', 
                             random.choice(D8237),  RANDOM_STRING, random.choice(D2005), RANDOM_STRING,RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', 
                             RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL, 'CUSTINFOPROVD']
        T220W_data_items = ['[orid]', fake.paragraph(nb_sentences=1)]
        T221R_data_items = ['[orid]', fake.paragraph(nb_sentences=1)]
        T222W_data_items = [# basic data
                            '[orid]', random.choice(D8327), fake.paragraph(nb_sentences=1), random.randint(100, 1000), '[today-' + str(random.randint(2, 30))  +']', random.randint(5, 15), random.randint(2, 6), RANDOM_GISX, RANDOM_GISY, 
                            #meter work completion data
                            RANDOM_METER_SER, RANDOM_METER_MNF, random.randint(100, 1000), '[today-' + str(random.randint(2, 30))  +']', random.randint(5, 15), random.randint(2, 6), RANDOM_GISX, RANDOM_GISY, random.choice(D3025), RANDOM_METER_LOC, OUTR_RANDOM_GISX, OUTR_RANDOM_GISY, random.choice(D3025), RANDOM_OUTRE_LOC, RANDOM_STRING, RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999)
                            ]
        T223W_data_items = [# basic data
                            '[orid]', 'NEWINSTALL', fake.paragraph(nb_sentences=1),
                            #meter work copletion data
                            RANDOM_METER_MNF, RANDOM_METER_SER, random.randint(100, 1000), '[today-' + str(random.randint(2, 30))  +']', random.randint(5, 15), random.randint(2, 6), RANDOM_GISX, RANDOM_GISY, random.choice(D3025), RANDOM_METER_LOC, OUTR_RANDOM_GISX, OUTR_RANDOM_GISY, random.choice(D3025), RANDOM_OUTRE_LOC, RANDOM_STRING, RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999)
                            ] 
        T224W_data_items = ['[orid]', random.choice(D8227), 'PROCDELAY_' + RANDOM_STRING]
        T323W_data_items = ['[orid]', 'ABLE', TIME_NOT_WEEKEND, '0', '1', DATE_NOT_WEEKEND, 'PLANPROP']
        T324R_data_items = ['[orid]', 'PLANAGREED']
        T325R_data_items = ['[orid]', 'PLANDISP']
        T322W_data_items = [# basic data
                            '[orid]', '1', 
                            # 1st meter data
                            METER_MNF, METER_SER, '0', '1', RANDOM_METER_MNF, '1', RANDOM_METER_SER, '1', '12', '1', '5',
                            '1', RANDOM_GISX, '1', RANDOM_GISY, '1', 'I', '1', RANDOM_METER_LOC, '1', OUTR_RANDOM_GISX, '1', OUTR_RANDOM_GISY, '1', 'O', '1', RANDOM_OUTRE_LOC, 'MORE_INFO_T322W',
                            # 2nd meter data
                            '', '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                            # missing meters data
                            '', '', '', '', '', '',
                            # unmeasured  data
                            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 
                            '', '', '']
        T351R_data_items = [# basic data
                            SPID, 'RET_' + RANDOM_STRING, '', '1', '[today]', '1',
                            # customer and retailer data
                            CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            RANDOM_STRING, random.choice(D2005), RANDOM_STRING, RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            # meter details
                            METER_MNF, METER_SER, random.choice(D8330), str(random.randint(1111, 9999)) + RANDOM_STRING, str(random.randint(1111, 9999)) + RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), '0', '',
                            random.choice(D8332), '1', 'NOTREMOVED', '[today+' + str(random.randint(1, 15))  +']', random.choice(D8335), 'METER_' + RANDOM_STRING, 'STOPPED', 'BACKWARD', 'SLOWED', '', random.randint(100, 9999), '[today-' + str(random.randint(1, 45))  +']', fake.paragraph(nb_sentences=1)
                            ]
        T351W_data_items = [# basic data
                            SPID, '', '[today]',
                            # meter details
                            METER_MNF, METER_SER, random.choice(D8330), str(random.randint(1111, 9999)) + RANDOM_STRING, str(random.randint(1111, 9999)) + RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), '0', '',
                            random.choice(D8332), '1', 'NOTREMOVED', '[today+' + str(random.randint(1, 15))  +']', random.choice(D8335), 'METER_' + RANDOM_STRING, 'STOPPED', 'BACKWARD', 'SLOWED', '', random.randint(100, 9999), '[today-' + str(random.randint(1, 45))  +']', fake.paragraph(nb_sentences=1)
                            ]
        T352W_data_items = [# basic data
                            '[orid]', 'REPLACED', # random.choice(D8341), # when other option than REPLACED no NEW METER can be provided - CONSIDER RULE!
                            # meter data
                            METER_MNF, METER_SER, RANDOM_METER_MNF, RANDOM_METER_SER, '120', '[today]', '1', '12', '1', '5', '1', RANDOM_GISX, '1', RANDOM_GISY, '1', 'I', '1', RANDOM_METER_LOC,
                            '1', OUTR_RANDOM_GISX, '1', OUTR_RANDOM_GISY, '1', 'O', '1', RANDOM_OUTRE_LOC, 'UPDATED_METER_T352W',
                            ]
        T353R_data_items = [# basic data
                            SPID, 'RET_' + RANDOM_STRING, '', '1', '[today]', 
                            # customer and retailer data
                            '1', CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            RANDOM_STRING, random.choice(D2005), RANDOM_STRING, RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            # install meter details
                            '1', RANDOM_STRING, RANDOM_STRING,  RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), random.randint(10, 30), random.choice(D8335), 'METER_' + RANDOM_STRING, random.choice(D8346), fake.paragraph(nb_sentences=1), fake.paragraph(nb_sentences=1)
                            ]
        T355R_data_items = [# basic data
                            SPID, 'RET_' + RANDOM_STRING, '', '1', '[today]', 
                            # customer and retailer data
                            '1', CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            RANDOM_STRING, random.choice(D2005), RANDOM_STRING, RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            # request accuracy meter details
                            METER_MNF, METER_SER, '1', RANDOM_STRING, RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), '0', '', '1', 'NOTREMOVED', '[today+' + str(random.randint(1, 15))  +']', random.choice(D8335), 'METER_' + RANDOM_STRING, 'OVERRECORD', '', fake.paragraph(nb_sentences=1) #D8434 cannot be used randmly because CON-0203 here is OVERRECORD
                            ]
        T355W_data_items = [# basic data
                            SPID, '', '[today]', 
                            # request accuracy meter details
                            METER_MNF, METER_SER, '1', RANDOM_STRING, RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), '0', '', '1', 'NOTREMOVED', '[today+' + str(random.randint(1, 15))  +']', random.choice(D8335), 'METER_' + RANDOM_STRING, 'OVERRECORD', '', fake.paragraph(nb_sentences=1) #D8434 cannot be used randmly because CON-0203 here is OVERRECORD
                            ]
        T356W_data_items = [# basic data
                            '[orid]',
                            # rAwaiting Meter Accuracy Test data
                            METER_MNF, METER_SER, random.choice(D8367), random.choice(D8368), '1', random.randint(100, 9999), random.randint(100, 9999), '[today-' + str(random.randint(1, 45))  +']', '1', '', fake.paragraph(nb_sentences=1)
                            ]
        T357W_data_items = [# basic data
                            '[orid]',
                            # rAwaiting Meter Accuracy Test data
                            METER_MNF, METER_SER, RANDOM_METER_MNF, RANDOM_METER_SER, random.randint(100, 9999), '[today-' + str(random.randint(1, 45))  +']', '1', random.randint(3, 10), '1', random.randint(2, 6), '1', RANDOM_GISX, '1', RANDOM_GISY, '1', random.choice(D3025), '1', RANDOM_METER_LOC, '1', OUTR_RANDOM_GISX, '1', OUTR_RANDOM_GISY, '1', random.choice(D3025), '1', RANDOM_OUTRE_LOC, fake.paragraph(nb_sentences=1)
                            ]
        T365R_data_items = [# basic data
                            SPID, 'RET_' + RANDOM_STRING, '', '1', '[today]', 
                            # customer and retailer data
                            '1', CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            RANDOM_STRING, random.choice(D2005), RANDOM_STRING, RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            # Meter Change details
                            METER_MNF, METER_SER, '1', RANDOM_STRING, RANDOM_STRING,  RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), '0', '', random.choice(D8332), '1', 'NOTREMOVED', '[today+' + str(random.randint(1, 15))  +']', random.choice(D8326), random.randint(10, 30), random.choice(D8335), 'METER_' + RANDOM_STRING, random.choice(D8346), fake.paragraph(nb_sentences=1), fake.paragraph(nb_sentences=1)
                            ]
        T501R_data_items = [# basic data
                            SPID, 'RET_' + RANDOM_STRING, '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1), random.choice(D8356), RANDOM_STRING, random.choice(D8358), RANDOM_STRING,random.choice(D8360), RANDOM_STRING, '', '1', fake.paragraph(nb_sentences=1), '[today]', '1',
                            # customer and retailer data
                            CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            fake.paragraph(nb_sentences=1), random.choice(D2005), fake.paragraph(nb_sentences=1), RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            ]
        T501W_data_items = [# basic data
                            SPID, '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1), random.choice(D8356), ''.join(random.choice(string.ascii_letters) for _ in range(15)), random.choice(D8358),''.join(random.choice(string.ascii_letters) for _ in range(15)),random.choice(D8360), ''.join(random.choice(string.ascii_letters) for _ in range(15)), '', fake.paragraph(nb_sentences=1), '[today]'      # [today - 0] = [today]!!!
                           ]
        T505R_data_items = [# basic data
                            SPID, 'RET_' + RANDOM_STRING, '[today-' + str(random.randint(0, 7))  +']', 'DWENQUIRY', random.choice(D8365), fake.enzyme(), '', '1', fake.paragraph(nb_sentences=1), '[today]', '1',       # [today - 0] = [today]!!!
                            # customer and retailer data
                            CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            fake.paragraph(nb_sentences=1), random.choice(D2005), fake.paragraph(nb_sentences=1), RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            ]
        T505W_data_items = [# basic data
                            SPID, '[today-' + str(random.randint(0, 7))  +']', 'DWENQUIRY',random.choice(D8365),  fake.enzyme(), '', fake.paragraph(nb_sentences=1),   '[today]', # [today - 0] = [today]!!!
                            ]
        T551R_data_items = [# basic data
                            SPID, 'DPID_' + RANDOM_STRING, 'RET_' + RANDOM_STRING, '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1), '', '1',  fake.paragraph(nb_sentences=1), '[today]', '1',    # [today - 0] = [today]!!!
                            # customer and retailer data
                            CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            fake.paragraph(nb_sentences=1), random.choice(D2005), fake.paragraph(nb_sentences=1), RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            ]
        T551W_data_items = [# basic data
                            SPID, 'DPID_' + RANDOM_STRING, '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1), '', fake.paragraph(nb_sentences=1), '[today]'      # [today - 0] = [today]!!!
                           ]
        T555R_data_items = [# basic data
                            SPID, 'DPID_' + RANDOM_STRING, 'RET_' + RANDOM_STRING, '', '1', random.choice(D8371), '[today+' + str(random.randint(0, 7))  +']', '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1),'[today]',
                            # customer and retailer data
                            '1', CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            fake.paragraph(nb_sentences=1), random.choice(D2005), fake.paragraph(nb_sentences=1), RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            # Group Attached Application
                            random.choice(D8374), random.choice(D8375), random.choice(D8376), random.choice(D8377), random.choice(D8378), random.choice(D8379), random.choice(D8380), 'Yes' #random.choice(D8381), - at least 1 Yes
                            ]
        T555W_data_items = [# basic data
                            SPID, 'DPID_' + RANDOM_STRING, 'RET_' + RANDOM_STRING, '', random.choice(D8371), '[today+' + str(random.randint(0, 7))  +']', '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1),'[today]',
                            # Group Attached Application
                            random.choice(D8374), random.choice(D8375), random.choice(D8376), random.choice(D8377), random.choice(D8378), random.choice(D8379), random.choice(D8380), 'Yes' #random.choice(D8381), - at least 1 Yes
                            ]
        T556R_data_items = [# basic data
                            'RET_' + RANDOM_STRING, '1', '', 'MOSLTEST-W', 'MOSLTEST-W', 'MOSLTEST-W', 'SEC_' + RANDOM_STRING, 'PRI_' + RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), RANDOM_STRING, random.randint(1, 99999999), random.choice(D8371), '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1),'[today]',
                            # customer and retailer data
                            '1', CUST_RANDOM_NAME, CUST_RANDOM_PHONE, '105', CUST_RANDOM_NAME2, CUST_RANDOM_PHONE2, '122', CUST_EMAIL, '1', 'EMAIL', random.choice(D8237),
                            fake.paragraph(nb_sentences=1), random.choice(D2005), fake.paragraph(nb_sentences=1), RET_RANDOM_NAME, RET_RANDOM_PHONE, '210', RET_RANDOM_NAME2, RET_RANDOM_PHONE2, '224', RET_EMAIL,
                            # Group Attached Application
                            random.choice(D8374), random.choice(D8375), random.choice(D8376), random.choice(D8377), random.choice(D8378), random.choice(D8379), random.choice(D8380), 'Yes' #random.choice(D8381), - at least 1 Yes
                            ]
        T556W_data_items = [# basic data
                            'RET_' + RANDOM_STRING, '1', '', 'MOSLTEST-W', 'MOSLTEST-W', 'MOSLTEST-W', 'SEC_' + RANDOM_STRING, 'PRI_' + RANDOM_STRING, RANDOM_ADDRESS1, RANDOM_ADDRESS2, RANDOM_ADDRESS3, RANDOM_ADDRESS4, RANDOM_ADDRESS5, random.choice(POSTCODES), random.randint(1, 99999999), RANDOM_STRING, random.randint(1, 99999999), random.choice(D8371), '[today-' + str(random.randint(0, 7))  +']', fake.paragraph(nb_sentences=1),'[today]',
                            # Group Attached Application
                            random.choice(D8374), random.choice(D8375), random.choice(D8376), random.choice(D8377), random.choice(D8378), random.choice(D8379), random.choice(D8380), 'Yes' #random.choice(D8381), - at least 1 Yes
                            ]
        T557W_data_items = [# basic data
                            '[orid]', 'GRANTED', 'PERMANENT', '[today]', fake.paragraph(nb_sentences=1)
                            ]
        
        TEST_CASE_LENGTH = len(test_case_sequence)
        #gererate test case sequence in Excel file       
        for i in range(TEST_CASE_LENGTH):
            # build file name based on transactions chain. i.e. T321R_T201W_T322W....
            new_filename = new_filename + test_case_sequence[i] + '_'
            # if transaction has .R in the name, it is MOSLTEST-R as requestor
            # put the transaction Source Org ID in sheet Test Case Sequence, column C - Source ID
            ws11.cell(row=i+4+(a*TEST_CASE_LENGTH), column=5).value = test_case_sequence[i]
            if test_case_sequence[i][-1] == 'R':
                ws11.cell(row=i+4+(a*TEST_CASE_LENGTH), column=3).value = RETAILER
            else:
                ws11.cell(row=i+4+(a*TEST_CASE_LENGTH), column=3).value = WHOLESALER
            # then in second sheet 'Test case data' depending on the transaction, insert respctive data items
            match test_case_sequence[i]:
                case 'T321.R':
                    for k in range(len(T321R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T321R_data_items[k]
                case 'T321.W':
                    for k in range(len(T321W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T321W_data_items[k]
                case 'T201.W':
                    for k in range(len(T201W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T201W_data_items[k]
                case 'T202.W':
                    for k in range(len(T202W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T202W_data_items[k]
                case 'T203.W':
                    for k in range(len(T203W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T203W_data_items[k]
                case 'T204.R':
                    for k in range(len(T204R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T204R_data_items[k]
                case 'T205.W':
                    for k in range(len(T205W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T205W_data_items[k]
                case 'T206.W':
                    for k in range(len(T206W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T206W_data_items[k]
                case 'T207.R':
                    for k in range(len(T207R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T207R_data_items[k]
                case 'T207.W':
                    for k in range(len(T207W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T207W_data_items[k]
                case 'T208.R':
                    for k in range(len(T208R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T208R_data_items[k]
                case 'T210.R':
                    for k in range(len(T210R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T210R_data_items[k]
                case 'T211.R':
                    for k in range(len(T211R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T211R_data_items[k]
                case 'T211.W':
                    for k in range(len(T211W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T211W_data_items[k]
                case 'T212.W':
                    for k in range(len(T212W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T212W_data_items[k]
                case 'T213.W':
                    for k in range(len(T213W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T213W_data_items[k]
                case 'T214.W':
                    for k in range(len(T214W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T214W_data_items[k]
                case 'T215.R':
                    for k in range(len(T215R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T215R_data_items[k]
                case 'T215.W':
                    for k in range(len(T215W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T215W_data_items[k]
                case 'T216.R':
                    for k in range(len(T216R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T216R_data_items[k]
                case 'T216.W':
                    for k in range(len(T216W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T216W_data_items[k]
                case 'T217.W':
                    for k in range(len(T217W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T217W_data_items[k]
                case 'T218.R':
                    for k in range(len(T218R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T218R_data_items[k]
                case 'T220.W':
                    for k in range(len(T220W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T220W_data_items[k]
                case 'T222.W':
                    for k in range(len(T222W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T222W_data_items[k]
                case 'T221.R':
                    for k in range(len(T221R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T221R_data_items[k]
                case 'T223.W':
                    for k in range(len(T223W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T223W_data_items[k]
                case 'T224.W':
                    for k in range(len(T224W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T224W_data_items[k]
                case 'T322.W':
                    for k in range(len(T322W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T322W_data_items[k]                              
                case 'T323.W':
                    for k in range(len(T323W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T323W_data_items[k]
                case 'T324.R':
                    for k in range(len(T324R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T324R_data_items[k]
                case 'T325.R':
                    for k in range(len(T325R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T325R_data_items[k]
                case 'T351.R':
                    for k in range(len(T351R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T351R_data_items[k]
                case 'T351.W':
                    for k in range(len(T351W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T351W_data_items[k]
                case 'T352.W':
                    for k in range(len(T352W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T352W_data_items[k]
                case 'T353.R':
                    for k in range(len(T353R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T353R_data_items[k]
                case 'T355.R':
                    for k in range(len(T355R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T355R_data_items[k]
                case 'T355.W':
                    for k in range(len(T355W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T355W_data_items[k]
                case 'T356.W':
                    for k in range(len(T356W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T356W_data_items[k]
                case 'T357.W':
                    for k in range(len(T357W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T357W_data_items[k]
                case 'T365.R':
                    for k in range(len(T365R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T365R_data_items[k]
                case 'T501.R':
                    for k in range(len(T501R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T501R_data_items[k]
                case 'T501.W':
                    for k in range(len(T501W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T501W_data_items[k]
                case 'T505.R':
                    for k in range(len(T505R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T505R_data_items[k]
                case 'T505.W':
                    for k in range(len(T505W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T505W_data_items[k]
                case 'T551.R':
                    for k in range(len(T551R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T551R_data_items[k]
                case 'T551.W':
                    for k in range(len(T551W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T551W_data_items[k]
                case 'T555.R':
                    for k in range(len(T555R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T555R_data_items[k]
                case 'T555.W':
                    for k in range(len(T555W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T555W_data_items[k]
                case 'T556.R':
                    for k in range(len(T556R_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T556R_data_items[k]
                case 'T556.W':
                    for k in range(len(T556W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T556W_data_items[k]
                case 'T557.W':
                    for k in range(len(T557W_data_items)):
                        ws12.cell(row=6+(3*i)+(3*a*TEST_CASE_LENGTH), column=k +
                                7).value = T557W_data_items[k]

    
    test_cases_folder = working_dir + 'TEST_CASES'
    if not os.path.exists(test_cases_folder):
        os.makedirs(test_cases_folder)

    if len(test_case_sequence) > 10:
        new_filename = "RECENT_TESTCASE"
    else:    
        new_filename = '_'.join(test_case_sequence)

    wb1.save(filename = test_cases_folder + '\\' + new_filename.replace('.','') + '.xlsx')

# loop_times repeats test case sequence in the excel file
# max_loop = int (100/TEST_CASE_LENGTH)
max_loop = 1
generate_test_case(max_loop)