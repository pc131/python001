from requests_pkcs12 import get, post
from datetime import datetime, timedelta
import random
import uuid
import json
import string
import names
import time
import os
from random_address import real_random_address
from faker import Faker
from faker_biology.mol_biol import Enzyme

#working_dir = 'C:\\Users\\cgi\\Desktop\\_downloads\\11\\'
working_dir = 'C:\\Users\\tomasz.skoczylas\\Downloads\\11\\'

#environments
# asr - ASSURANCE
# tst - TEST
# uat - UAT
# ppr - PREPROD1

environment = 'tst'

# ALL_TRANSACTIONS
# T201W,T202W,T203W,T204R,T205W,T206W,T207R,T207W
# T208R,T210R,T211R,T211W,T212W,T213W,T214W,T215R
# T215W,T216R,T216W,T217W,T218R,T220W,T221R,T222W,
# T223W,T224W,T225R,T226W,T227R,T228R,T321R,T321W,
# T322W,T323W,T324R,T325R,T331W,T332W,T335R,T336W,
# T339R,T339W,T340W,T341R,T341W,T342W,T351R,T351W,
# T352W,T353R,T355R,T355W,T356W,T357W,T365R,T501R,
# T501W,T505R,T505W,T551R,T551W,T561R,T561W,T562R,
# T562W,T563W,T601R,T601W,T602W

#transactions_list = ['T601R', 'T201W', 'T226W', 'T227R']
#transactions_list = ['T505W', 'T201W', 'T215R']
#transactions_list = ['T321R','T201W','T323W','T351R','T201W','T203W','T505R','T201W','T222W','T501W','T201W','T217W','T551R','T201W','T353R','T201W','T220W','T355W','T201W','T224W','T365R','T201W','T205W','T331W','T201W','T211W','T341R','T201W','T226W','T561R','T201W','T562W','T201W','T563W','T335R','T202W']
#transactions_list = ['T353R', 'T201W', 'T205W','T365R', 'T201W', 'T205W','T355R', 'T201W', 'T205W','T355W', 'T201W', 'T205W'] #B1 B3 B7 VISITSCHED
#transactions_list = ['T601R', 'T201W', 'T203W', 'T204R', 'T205W', 'T226W', 'T228R', 'T602W', 'T208R']
#transactions_list = ['T601W', 'T201W', 'T203W', 'T204R', 'T205W', 'T226W', 'T228R', 'T602W', 'T208R']
#transactions_list = ['T601W', 'T201W', 'T226W', 'T228R']
#transactions_list = ['T601R', 'T201W', 'T201W']#, 'T602W']
#transactions_list = ['T601W', 'T201W', 'T602W', 'T210R',  'T202W', 'T210R', 'T201W', 'T217W', 'T204R', 'T218R', 'T226W', 'T227R', 'T211W']

transactions_list = ['T339W', 'T201W', 'T340W']

if environment in ('uat', 'tst', 'ppr'):
    SPIDS_METERS = {'3019178819W13':('KENT','000000000000189985'),'3019178827W10':('KENT','4A059235'),'3019178843W15':('KENT','4A026515'),'3019178851W12':('ELSTER','000000000008081344'),'301917886XW1X':('ARAD','152026121'),'3019178991W12':('KENT','000000000000221909'),'3019179017W10':('KENT','4A024157'),'3019179033W15':('KENT','2T021233'),'3019179130W16':('KENT','90P169156'),'3019179149W13':('KENT','3T042349'),'3019179173W15':('ARAD','09044840'),'3019179289W13':('KENT','AE188861'),'301917936XW1X':('KENT','4A023209'),'3019179386W14':('ARAD','16732739'),'3019179416W14':('ARAD','8004476'),'3019179483W15':('AMR','8569517'),'3019179564W11':('ARAD','9103911'),'3019179653W15':('KENT','000000000083235847'),'3019024854W11':('ARAD','9097878'),'3019025117W10':('SW_METER','9M129866'),'3019025125W18':('KENT','2M034061'),'3019025230W16':('KENT','3M310071'),'3019025486W14':('KENT','4M093717'),'3019025532W19':('ARAD','000000000008011122'),'3019025648W17':('ARAD','000000000008596289'),'3019025648W17':('ARAD','000000000008385953'),'3019025737W10':('KENT','4M058479'),'3019026067W10':('KENT','1M079127'),'301902644XW1X':('KENT','000000000090248995'),'3019027314W11':('ARAD','000000000008110959'),'3019027322W19':('KENT','1M202328'),'301902739XW1X':('KENT','000000000087080861')}
    SWG_SPIDS_METERS = {'3019601851S1X':('Elster','88025763'),'3019601916S11':('Elster','93A015953'),'3019602009S10':('Elster','93A614270'),'3019602734S19':('Elster','COWDRAYHALL'),'3019607736S11':('ZENNER','4.220703'),'301964108XS17':('PortsmouthWater','1800145069999'),'3019643848S14':('ELSTER','14163329'),'3019644402S16':('Elster','CP3152181945'),'3019648947S18':('Elster','A815013'),'3019650909S10':('KENT','81011123'),'3019669766S11':('ELSTER','2345942'),'3019670136S11':('ELSTER','13-40040803'),'3200061251S1X':('SIEMENS','N1F2250089'),'3200061448S14':('SIEMENS','469002H036'),'3200061464S19':('ABB','244813121X001'),'3200061510S13':('SIEMENS','7ME69201AA101AA0'),'3200061545S15':('ENDRESS_AND_HAUSER','S6257905'),'3200061588S14':('ELSTER','10S01131151428'),'320006160XS17':('ARAD','M10765299'),'3200061685S15':('SIEMANS','NIE4099400'),'3200061782S16':('SIEMENS','450702H425'),'3200061812S16':('SIEMENS','252002H164'),'3200061928S14':('SIEMENS','194502H524'),'3200062312S16':('ELSTER','10S01141641343'),'320006238XS17':('ELSTER','10S01141751319'),'3200062401S1X':('ELSTER','10S01141806328')}

if environment == 'asr':
    SPIDS_METERS = {'3200205725W18':('ELSTER','10W05271221493'),'3200205768W17':('ELSTER','10W05271251052'),'3200205768W17':('ELSTER','10W05271251110'),'3200205784W11':('ELSTER','10W05271306017'),'3200205784W11':('ELSTER','10W05271321005'),'3200205806W14':('ELSTER','10W05271315470'),'3200205806W14':('ELSTER','10W05271321048'),'3200255129W13':('ELSTER','10W07010442137'),'3200255234W11':('ELSTER','10W07010550556'),'3200255331W12':('ELSTER','10W07010716294'),'3200255331W12':('ELSTER','10W07010722006'),'3200255331W12':('ELSTER','10W07010722031'),'3200255331W12':('ELSTER','10W07010722073'),'3200255331W12':('ELSTER','10W07010722104'),'3200255331W12':('ELSTER','10W07010722169'),'3200255455W18':('ELSTER','10W07010816204'),'3200255463W15':('astar','20170701a'),'3200255463W15':('ELSTER','20170701mi'),'3200255498W17':('ELSTER','10W07010826253'),'3200255498W17':('ELSTER','10W07010831478'),'3200255498W17':('ELSTER','10W07010831491'),'3200255498W17':('ELSTER','10W07010831516'),'3200255498W17':('ELSTER','10W07010831529'),'3200255498W17':('ELSTER','10W07010831581'),'3200272465W18':('ELSTER','10W07271002164'),'3200325216W14':('ELSTER','10W09301106187'),'3200325291W12':('ELSTER','10W09301147156'),'3200325291W12':('ELSTER','10W09301146504'),'3200325291W12':('ELSTER','10X09301146185'),'3200325291W12':('ELSTER','10X09301146171')}
    SWG_SPIDS_METERS = {'3200011130S13':('ELSTER','10S10031211104'),'320001153XS17':('ELSTER','10S10031706164'),'3200012463S12':('ELSTER','10S10050906005'),'3200013834S19':('ELSTER','10S10101021253'),'3200014032S16':('ELSTER','10S10101226263'),'3200023368S14':('ELSTER','10S10271026045'),'3200025735S15':('ELSTER','10S10281611172'),'3200032758S14':('ELSTER','10S11081156102'),'3200036281S1X':('ELSTER','10S11141711001'),'3200060441S1X':('ELSTER','10S01121911028'),'3200060476S11':('ELSTER','10S01122211259')}

match environment:
    case 'asr':
        t216_url = 'https://moservicesdev.mosl.co.uk/assurance/attachments/bddf1ca7-62fe-4c58-89e0-d5875fc4029f'
    case 'tst':
        t216_url = 'https://moservicesdev.mosl.co.uk/test/attachments/2b070d96-d3cf-4f1a-882b-a70b29e32d84'
    case 'uat':
        t216_url = 'https://moservicesdev.mosl.co.uk/uat/attachments/1706b337-cd7d-40fa-93c6-476e5dfb7fa8'
    case 'ppr':
        t216_url = 'https://moservicesdev.mosl.co.uk/preprod/attachments/016b35c0-27c6-437b-8604-839e30e17973'

POSTCODES = ['B1 1HQ', 'BN88 1AH', 'BS98 1TL', 'BX1 1LT', 'BX2 1LB', 'BX3 2BB', 'BX4 7SB', 'BX5 5AT', 'CF10 1BH', 'CF99 1NA', 'CO4 3SQ', 'CV4 8UW', 'CV35 0DB', 'E14 5EY', 'DA1 1RT', 'DE99 3GG', 'DE55 4SW', 'DH98 1BT', 'DH99 1NS', 'E14 5HQ', 'E14 5JP', 'E16 1XL', 'E20 2AQ', 'E20 2BB', 'E20 2ST', 'E20 3BS', 'E20 3EL', 'E20 3ET', 'E20 3HB', 'E20 3HY', 'E98 1SN', 'E98 1ST', 'E98 1TT', 'EC2N 2DB', 'EC4Y 0HQ', 'EH12 1HQ', 'EH99 1SP', 'G58 1SB', 'GIR 0AA', 'IV21 2LR', 'L30 4GB', 'LS98 1FD', 'M50 2BH', 'M50 2QH', 'N1 9G', 'N81 1ER', 'NE1 4ST', 'NG80 1EH', 'NG80 1LH', 'NG80 1RH', 'NG80 1TH', 'PH1 5RB', 'PH1 2SJ', 'S2 4SU', 'S6 1SW', 'S14 7UP', 'SE1 0NE', 'SE1 8UJ', 'SM6 0HB', 'SN38 1NW', 'SR5 1SU', 'SW1A 0AA', 'SW1A 0PW', 'SW1A 1AA', 'SW1A 2AA', 'SW1A 2AB', 'SW1H 0TL', 'SW1P 3EU', 'SW1W 0DT', 'SW11 7US', 'SW19 5AE', 'TW8 9GS', 'W1A 1AA', 'W1D 4FA', 'W1N 4DJ', 'W1T 1FB']

###MAKE SURE THERE IS THE SAME NUMBER AND THE SAME ORDER OF ELEMENTS IN PROCESSES AND PROC_NAMES ###
PROCESSES = ['B1R', 'B3R', 'B3W', 'B5R', 'B5W', 'B7R', 'C1R', 'C1W', 'C2', 'C3', 'C5R', 'C5W', 'F4R', 'F4W', 'F5R', 'F5W', 'G1R', 'G1W', 'G2AR', 'G2AW', 'G2BR', 'G2BW','H1R','H1W']
###MAKE SURE THERE IS THE SAME NUMBER AND THE SAME ORDER OF ELEMENTS IN PROCESSES AND PROC_NAMES ###
PROC_NAMES = {'B1R':'Request Meter Install Work', 'B3R':'Request Meter Accuracy Test', 'B3W':'Request Meter Accuracy Test', 'B5R':'Request Meter Repair Replacement Work', 'B5W':'Request Meter Repair Replacement Work', 'B7R':'Request Meter Change', 'C1R':'Request Meter And Supply Arrangement Verification', 'C1W':'Request Meter And Supply Arrangement Verification', 'C2':'Submit Gap Site Application For C2', 'C3':'Submit Gap Site Application For C3', 'C5R':'Submit Application For SPID Deregistration Or SC Removal', 'C5W':'Submit Application For SPID Deregistration Or SC Removal','F4R':'Submit Non-Household Customer Enquiry', 'F4W':'Submit Non-Household Customer Enquiry', 'F5R':'Submit Non-Household Customer Complaint', 'F5W':'Submit Non-Household Customer Complaint', 'G1R':'Submit Non-Household Customer TE Enquiry', 'G1W':'Submit Non-Household Customer TE Enquiry', 'G2AR':'Submit TE Consent Application With SPID', 'G2AW':'Submit TE Consent Application With SPID', 'G2BR':'Submit TE Consent Application Without SPID', 'G2BW':'Submit TE Consent Application Without SPID','H1R':'Submit Application For An Allowance Or Volumetric Adjustment','H1W':'Submit Application For An Allowance Or Volumetric Adjustment'}
###TRANSACTION NAMES DISPLAYED IN DIALOG
TRANSACTION_NAMES = {'T201.W':'Accept Service Request', 'T202.W':'Reject Service Request', 'T203.W':'Request For Additional Information', 'T204.R':'Provide Additional Information', 'T205.W':'Update Site Visit Date', 'T206.W':'Update Site Visit Failure', 'T207.R':'Submit Trading Party Comments', 'T207.W':'Submit Trading Party Comments', 'T208.R':'Close Service Request', 'T210.R':'Resubmit Service Request', 'T211.R':'Cancel Service Request', 'T211.W':'Cancel Service Request', 'T212.W':'Visit Complete And Preparing Plan', 'T213.W':'Start Service Request Deferral', 'T214.W':'End Service Request Deferral', 'T215.R':'Provide Attachment', 'T215.W':'Provide Attachment', 'T216.R':'Request Attachment', 'T216.W':'Request Attachment', 'T217.W':'Request For Customer Details and Additional Information', 'T218.R':'Provide Customer Details and Additional Information', 'T220.W':'Provide Quote For Non Standard Activity', 'T221.R':'Accept Quote For Non Standard Activity', 'T222.W':'Advise Service Request Complete', 'T223.W':'Advise Meter Work Completion', 'T224.W':'Advise Process Delay', 'T225.R':'Advise Incorrect TP Selected For Service Request', 'T226.W':'Propose Outcome', 'T227.R':'Agree Proposed Outcome', 'T228.R':'Proposed Outcome Not Agreed', 'T321.R':'Request Meter And Supply Arrangement Verification', 'T321.W':'Request Meter And Supply Arrangement Verification', 'T322.W':'Update Corrections Complete for C1', 'T323.W':'Propose Corrections Plan for C1', 'T324.R':'Agree Proposed Corrections Plan for C1', 'T331.W':'Submit Gap Site Application For C2', 'T332.W':'Advise Gap Site Application Outcome For C2', 'T335.R':'Submit Gap Site Application For C3', 'T336.W':'Advise Gap Site Application Outcome For C3', 'T325.R':'Dispute Proposed Corrections Plan for C1', 'T341.R':'Submit Application For SPID Deregistration Or SC Removal', 'T341.W':'Submit Application For SPID Deregistration Or SC Removal', 'T342.W':'Advise Application Outcome For C5', 'T351.R':'Request Meter Repair Replacement Work', 'T351.W':'Request Meter Repair Replacement Work', 'T352.W':'Advise Meter Repair Replacement Work Completion', 'T353.R':'Request Meter Install Work', 'T355.R':'Request Meter Accuracy Test', 'T355.W':'Request Meter Accuracy Test', 'T356.W':'Advise Meter Accuracy Test Complete', 'T357.W':'Awaiting Meter Accuracy Test', 'T365.R':'Request Meter Change', 'T501.R':'Submit Non Household Customer Complaint', 'T501.W':'Submit Non Household Customer Complaint', 'T505.R':'Submit Non Household Customer Enquiry', 'T505.W':'Submit Non Household Customer Enquiry', 'T551.R':'Submit Non Household Customer TE Enquiry', 'T551.W':'Submit Non Household Customer TE Enquiry', 'T561.R':'Submit TE Consent Application With SPID', 'T561.W':'Submit TE Consent Application With SPID', 'T562.R':'Submit TE Consent Application Without SPID', 'T562.W':'Submit TE Consent Application Without SPID', 'T563.W':'Advise TE Consent Application Outcome','T601.R':'Submit Application For Volumetric Allowance','T601.W':'Submit Application For Volumetric Allowance','T602.W':'Advise Application Outcome for H1'}
###TRANSACTION NAMES USED IN REAL TRANSACTIONS - MAKE SURE TO UPDATE WITH NEW PROCESS
TRANSACTIONS_XSD_NAMES = {'T201W':('T201.W','T201.W_AcceptServiceRequest'),'T201M':('T201.M','T201.M_NotifyServiceRequestAccepted'),'T202W':('T202.W','T202.W_RejectServiceRequest'),'T202M':('T202.M','T202.M_NotifyServiceRequestRejected'),'T203W':('T203.W','T203.W_RequestForAdditionalInformation'),'T203M':('T203.M','T203.M_NotifyAdditionalInformationRequested'),'T204R':('T204.R','T204.R_ProvideAdditionalInformation'),'T204M':('T204.M','T204.M_NotifyAdditionalInformationProvided'),'T205W':('T205.W','T205.W_UpdateSiteVisitDate'),'T205M':('T205.M','T205.M_NotifySiteVisitDate'),'T206W':('T206.W','T206.W_UpdateSiteVisitFailure'),'T206M':('T206.M','T206.M_NotifySiteVisitFailure'),'T207R':('T207.R','T207.R_SubmitTradingPartyComments'),'T207W':('T207.W','T207.W_SubmitTradingPartyComments'),'T207M':('T207.M','T207.M_NotifyTradingPartyComments'),'T208R':('T208.R','T208.R_CloseServiceRequest'),'T208M':('T208.M','T208.M_NotifyServiceRequestClosed'),'T209M':('T209.M','T209.M_NotifyTransactionRejected'),'T210R':('T210.R','T210.R_ResubmitServiceRequest'),'T210M':('T210.M','T210.M_NotifyServiceRequestResubmitted'),'T211R':('T211.R','T211.R_CancelServiceRequest'),'T211W':('T211.W','T211.W_CancelServiceRequest'),'T211M':('T211.M','T211.M_NotifyServiceRequestCancelled'),'T212W':('T212.W','T212.W_VisitCompleteAndPreparingPlan'),'T212M':('T212.M','T212.M_NotifyVisitCompleteAndPreparingPlan'),'T213W':('T213.W','T213.W_StartServiceRequestDeferral'),'T213M':('T213.M','T213.M_NotifyServiceRequestDeferralStarted'),'T214W':('T214.W','T214.W_EndServiceRequestDeferral'),'T214M':('T214.M','T214.M_NotifyServiceRequestDeferralEnded'),'T215R':('T215.R','T215.R_ProvideAttachment'),'T215W':('T215.W','T215.W_ProvideAttachment'),'T215M':('T215.M','T215.M_NotifyAttachmentURL'),'T216R':('T216.R','T216.R_RequestAttachment'),'T216W':('T216.W','T216.W_RequestAttachment'),'T216M':('T216.M','T216.M_SupplyRequestedAttachment'),'T217W':('T217.W','T217.W_RequestForCustomerDetailsandAdditionalInformation'),'T217M':('T217.M','T217.M_NotifyCustomerDetailsandAdditionalInformationRequested'),'T218R':('T218.R','T218.R_ProvideCustomerDetailsandAdditionalInformation'),'T218M':('T218.M','T218.M_NotifyCustomerDetailsandAdditionalInformationProvided'),'T219M':('T219.M','T219.M_NotifyTransactionAccepted'),'T220W':('T220.W','T220.W_ProvideQuoteForNonStandardActivity'),'T220M':('T220.M','T220.M_NotifyQuoteForNonStandardActivity'),'T221R':('T221.R','T221.R_AcceptQuoteForNonStandardActivity'),'T221M':('T221.M','T221.M_NotifyQuoteAcceptedForNonStandardActivity'),'T222W':('T222.W','T222.W_AdviseServiceRequestComplete'),'T222M':('T222.M','T222.M_NotifyServiceRequestComplete'),'T223W':('T223.W','T223.W_AdviseMeterWorkCompletion'),'T223M':('T223.M','T223.M_NotifyMeterWorkCompletion'),'T224W':('T224.W','T224.W_AdviseProcessDelay'),'T224M':('T224.M','T224.M_NotifyProcessDelay'),'T225R':('T225.R','T225.R_AdviseIncorrectTPSelectedForServiceRequest'),'T225W':('T225.W','T225.W_AdviseIncorrectTPSelectedForServiceRequest'),'T225M':('T225.M','T225.M_NotifyIncorrectTPSelectedForServiceRequest'),'T226W':('T226.W','T226.W_ProposeOutcome'),'T226M':('T226.M','T226.M_NotifyProposedOutcome'),'T227R':('T227.R','T227.R_AgreeProposedOutcome'),'T227M':('T227.M','T227.M_NotifyProposedOutcomeAgreed'),'T228R':('T228.R','T228.R_ProposedOutcomeNotAgreed'),'T228M':('T228.M','T228.M_NotifyProposedOutcomeNotAgreed'),'T291M':('T291.M','T291.M_NotifyServiceRequestTransferred'),'T321R':('T321.R','T321.R_RequestMeterAndSupplyArrangementVerification'),'T321M':('T321.M','T321.M_NotifyMeterAndSupplyArrangementVerificationRequest'),'T321W':('T321.W','T321.W_RequestMeterAndSupplyArrangementVerification'),'T322W':('T322.W','T322.W_UpdateCorrectionsCompleteForC1'),'T322M':('T322.M','T322.M_NotifyCorrectionsCompleteForC1'),'T323W':('T323.W','T323.W_ProposeCorrectionsPlanForC1'),'T323M':('T323.M','T323.M_NotifyProposedCorrectionsPlanForC1'),'T324R':('T324.R','T324.R_AgreeProposedCorrectionsPlanForC1'),'T324M':('T324.M','T324.M_NotifyCorrectionsPlanAgreedForC1'),'T325R':('T325.R','T325.R_DisputeProposedCorrectionsPlanForC1'),'T325M':('T325.M','T325.M_NotifyCorrectionsPlanDisputedForC1'),'T331W':('T331.W','T331.W_SubmitGapSiteApplicationForC2'),'T331M':('T331.M','T331.M_NotifyGapSiteApplicationForC2'),'T332W':('T332.W','T332.W_AdviseGapSiteApplicationOutcomeForC2'),'T332M':('T332.M','T332.M_NotifyGapSiteApplicationOutcomeForC2'),'T335R':('T335.R','T335.R_SubmitGapSiteApplicationForC3'),'T335M':('T335.M','T335.M_NotifyGapSiteApplicationForC3'),'T336W':('T336.W','T336.W_AdviseGapSiteApplicationOutcomeForC3'),'T336M':('T336.M','T336.M_NotifyGapSiteApplicationOutcomeForC3'),'T339R':('T339.R','T339.R_SubmitServiceComponentApplication'),'T339W':('T339.W','T339.W_SubmitServiceComponentApplication'),'T339M':('T339.M','T339.M_NotifyServiceComponentApplication'),'T340W':('T340.W','T340.W_AdviseServiceComponentApplicationOutcome'),'T340M':('T340.M','T340.M_NotifyServiceComponentApplicationOutcome'),'T341R':('T341.R','T341.R_SubmitApplicationForSPIDDeregistrationOrSCRemoval'),'T341W':('T341.W','T341.W_SubmitApplicationForSPIDDeregistrationOrSCRemoval'),'T341M':('T341.M','T341.M_NotifyApplicationForSPIDDeregistrationOrSCRemoval'),'T342W':('T342.W','T342.W_AdviseApplicationOutcomeForC5'),'T342M':('T342.M','T342.M_NotifyApplicationOutcomeForC5'),'T351R':('T351.R','T351.R_RequestMeterRepairReplacementWork'),'T351W':('T351.W','T351.W_RequestMeterRepairReplacementWork'),'T351M':('T351.M','T351.M_NotifyMeterRepairReplacementWork'),'T352W':('T352.W','T352.W_AdviseMeterRepairReplacementWorkCompletion'),'T352M':('T352.M','T352.M_NotifyMeterRepairReplacementWorkCompletion'),'T353R':('T353.R','T353.R_RequestMeterInstallWork'),'T353M':('T353.M','T353.M_NotifyMeterInstallWorkRequest'),'T355R':('T355.R','T355.R_RequestMeterAccuracyTest'),'T355W':('T355.W','T355.W_RequestMeterAccuracyTest'),'T355M':('T355.M','T355.M_NotifyMeterAccuracyTestRequest'),'T356W':('T356.W','T356.W_AdviseMeterAccuracyTestComplete'),'T356M':('T356.M','T356.M_NotifyMeterAccuracyTestComplete'),'T357W':('T357.W','T357.W_AwaitingMeterAccuracyTest'),'T357M':('T357.M','T357.M_NotifyMeterAccuracyTestAwaiting'),'T365R':('T365.R','T365.R_RequestMeterChange'),'T365M':('T365.M','T365.M_NotifyMeterChangeRequest'),'T501R':('T501.R','T501.R_SubmitNonHouseholdCustomerComplaint'),'T501W':('T501.W','T501.W_SubmitNonHouseholdCustomerComplaint'),'T501M':('T501.M','T501.M_NotifyNonHouseholdCustomerComplaint'),'T505R':('T505.R','T505.R_SubmitNonHouseholdCustomerEnquiry'),'T505W':('T505.W','T505.W_SubmitNonHouseholdCustomerEnquiry'),'T505M':('T505.M','T505.M_NotifyNonHouseholdCustomerEnquiry'),'T551R':('T551.R','T551.R_SubmitNonHouseholdCustomerTEEnquiry'),'T551W':('T551.W','T551.W_SubmitNonHouseholdCustomerTEEnquiry'),'T551M':('T551.M','T551.M_NotifyNonHouseholdCustomerTEEnquiry'),'T561R':('T561.R','T561.R_SubmitTEConsentApplicationWithSPID'),'T561W':('T561.W','T561.W_SubmitTEConsentApplicationWithSPID'),'T561M':('T561.M','T561.M_NotifyTEConsentApplicationWithSPID'),'T562R':('T562.R','T562.R_SubmitTEConsentApplicationWithoutSPID'),'T562W':('T562.W','T562.W_SubmitTEConsentApplicationWithoutSPID'),'T562M':('T562.M','T562.M_NotifyTEConsentApplicationWithoutSPID'),'T563W':('T563.W','T563.W_AdviseTEConsentApplicationOutcome'),'T563M':('T563.M','T563.M_NotifyTEConsentApplicationOutcome'),'T601R':('T601.R','T601.R_SubmitApplicationForAnAllowanceOrVolumetricAdjustment'),'T601W':('T601.W','T601.W_SubmitApplicationForAnAllowanceOrVolumetricAdjustment'),'T602W':('T602.W','T602.W_AdviseApplicationOutcomeForH1'),'T601M':('T601.M','T601.M_NotifyApplicationForAnAllowanceOrVolumetricAdjustment'),'T602M':('T602.M','T602.M_AdviseApplicationOutcomeForH1')}

SUBMITTING_TRANSACTIONS = {'T321R', 'T321W', 'T331W', 'T335R', 'T339.R', 'T339.W', 'T341R', 'T341W', 'T351R', 'T351W', 'T353R', 'T355R', 'T355W', 'T365R', 'T501R', 'T501W', 'T505R', 'T505W', 'T551R', 'T551W', 'T561R', 'T561W', 'T562R', 'T562W', 'T601R', 'T601W'}

fake = Faker()
fake.add_provider(Enzyme)

#pick random SPID, METER_MNF_ METER_SERIAL
def pick_spid_meter():
    spid_meter = random.choice(list(SPIDS_METERS.items()))
    spid = spid_meter[0]
    meter_mnf = spid_meter[1][0]
    meter_ser = spid_meter[1][1]
    return spid, meter_mnf, meter_ser

def pick_swg_spid_meter():
    swg_spid_meter = random.choice(list(SWG_SPIDS_METERS.items()))
    swg_spid = swg_spid_meter[0]
    swg_meter_mnf = swg_spid_meter[1][0]
    swg_meter_ser = swg_spid_meter[1][1]
    return swg_spid, swg_meter_mnf, swg_meter_ser

def random_email():
    return fake.company_email()

def random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15))

def random_name():
    return names.get_full_name()

def random_phone():
    return str(random.randint(1200000000, 4499999999))

def random_meter_ser():
    return '10W' + str(random.randint(0000000000, 9999999999))

def random_meter_mnf():
    return ''.join(random.choice(string.ascii_letters).upper() for _ in range(random.randint(4, 10)))

def random_gisx():
    return str(random.randint(82644, 655612))

def random_gisy():
    return str(random.randint(5186, 657421))

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

def get_random_address():
    rand_address =  real_random_address()
    return rand_address["address1"]

SPID, METER_MNF, METER_SER = pick_spid_meter()
SWG_SPID, SWG_METER_MNF, SWG_METER_SER = pick_swg_spid_meter()
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

#C1
D8036 = ['ERROR', 'DUPLICATE', 'SWITCHED', 'REJECTION', 'UNABLEASST', 'DISAGREEPLAN'] # T211.R T211.W Cancellation Reason Code
D8226 = ['NOCONTACT', 'UNCOOPCUST', 'INACCONTACT', 'MOREDETAILS'] # T203.W T217W Additional Information Request Code
D8228 = ['WHOL', 'NONWHOL'] # T206.W Site Visit Failure Code
D8229 = ['CUSTOMER', 'RETAILER', 'THIRDPARTY', 'CONSENTS', 'REGULAT', 'WEATHER', 'FORCEMAJ', 'INFOREQD', 'BULK'] # T213.W Request Deferral Code
D8230 = ['INACCURATE', 'DUPLICATE', 'WRONGPRO', 'POLICY', 'HOUSEHOLD', 'NOTWHOL', 'REJECTRESUBMIT'] # T202.W Reject Reason Code
D8231 = ['DISPREJECT', 'DISPCMOS', 'DISPQUOTE'] # T210.R Resubmit Reason Code
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
D8367 = ['AFTEREXCHG', 'ALREADYTESTED', 'INSITUTESTED']
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
D8384 =	['YES', 'NO', 'NA']
D8385 =	['YES', 'NO', 'NA']
D8386 =	['YES', 'NO', 'NA']

#C2 C3
D8391 = ['METERED','UNMETERED']
D8393 = ['WSPID', 'SSPID', 'WSSPID']
D8402 = ['GS', 'CU']
D2013 = ['VACANT','OCCUPIED']
D8411 = ['METER1','METER2','METER3','METER4','METER5','METER6']

#C5
D8412 = ['SPIDDEREG', 'REMOVESC']
D8413 = ['DEMOLISHED','MERGED','NOWAT','NOWATORSEWG','NOSC','LANDLORD','NOTELIGIBLE','COU','DUPLICATE']
D8414 = ['0', '1']
D8417 = ['0', '1']
D8418 = ['0', '1']
D8419 = ['0', '1']
D8420 = ['0', '1']
D8421 = ['0', '1']
D8422 = ['0', '1']
D8423 = ['0', '1']
D8424 = ['0', '1']
D8425 = ['0', '1']
D8426 = ['0', '1']
D8427 = ['0', '1']

D8430 = ['SINGLE','COMOCCUP','COMMGMT']
D8442 = ['AGREED','AMENDAGREED','NOTAGREED']
D8443 = ['SPIDDREG','AMENDED','NOTAMENDED']

D8446 = ['0', '1']
D8447 = ['0', '1']
D8448 = ['0', '1']
D8449 = ['0', '1']

D8450 = ['0', '1']
D8451 = ['0', '1']
D8452 = ['0', '1']
D8453 = ['0', '1']
D8454 = ['0', '1']
D8455 = ['0', '1']

D8462 = ['SPIDDEREG', 'REMOVESC']
D8463 = ['INCORRECTWHL', 'INCORRECTRTL']

#H1
D8464 = ['NEW', 'REVIEW']
D8465 = ['WATER', 'SEWERAGE', 'BOTH']
D8466 = ['FIREFIGHTING', 'LEAK', 'VOLUMEADJST', 'NONRTSCHANGE', 'SWAREACHANGE']
D8471 = ['VOLUMETRIC', 'METERBASED']
D8472 = ['FIREFIGHTING', 'FIREFIGHTINGTEST', 'FIREFIGHTINGTRNG', 'OTHER']
D8478 = ['LEAKPROPERTY', 'LEAKMETER', 'LEAKCUST', 'OTHER']
D8479 = ['REPSUPPLYPIPE', 'REPPREMISES', 'NEWINSTALL', 'OTHER']
D8481 = ['WHOLESALER', 'CUSTOMER']
D8482 = ['GROUND', 'DRAINAGESYSTEM']
D8483 = ['THIRDPARTY', 'DETERIORATION', 'LEAKONPIPE', 'FITTINGS', 'NEGLECT', 'OTHER']
D8490 = ['EVAPORATION', 'IRRIGATION', 'REMOVEDOFFSITE', 'ADDTOPRODUCT', 'LIVESTOCKDW', 'OTHER']
D8495 = ['AWARDNOAMEND', 'AWARDWITHAMEND', 'NOTAWARDED']
D8497 = ['PERCENT', 'M2', 'M3', 'TARIFF']

match environment:
    case 'tst':
        vald_env = 'https://moservicesdev.mosl.co.uk/test/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/test/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/test/notification/hvi/dequeue'
    case 'uat':
        vald_env = 'https://moservicesdev.mosl.co.uk/uat/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/uat/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/uat/notification/hvi/dequeue'
    case 'asr':
        vald_env = 'https://moservicesdev.mosl.co.uk/assurance/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/assurance/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/assurance/notification/hvi/dequeue'
    case 'ppr':
        vald_env = 'https://moservicesdev.mosl.co.uk/preprod/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/preprod/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/preprod/notification/hvi/dequeue'

retailer = 'MOSLTEST-R'
wholesaler = 'MOSLTEST-W'
retailer2 = 'MOSLTEST2-R'
wholesaler2 = 'MOSLTEST2-W'

cert_path = 'C:/Users/cgi/Desktop/_downloads/' #path to certificates
cert_mosltest_r = cert_path + 'BIL_DEV_MOSL_MOSLTEST-R_B2B_412.pfx' #MOSLTEST-R pfx certificate
cert_mosltest_w = cert_path + 'BIL_DEV_MOSL_MOSLTEST-W_B2B_411.pfx' #MOSLTEST-W pfx certificate
def unique_id1():
    return str(uuid.uuid4().hex) #unique ID used for DocumentReferenceNumber
def unique_id2():
    return str(uuid.uuid4().hex) #unique ID used for DataTransactionReferenceNumber
def unique_id3():
    return str(uuid.uuid4().hex) #unique ID used for OriginatorsReference
random_numbers = [86,97,53,53,49,108,49,107,49]
def transaction_timestamp():
    return datetime.today().strftime('%Y-%m-%dT%H:%M:%S') #used for Transaction Header Timestamp
now = datetime.today().strftime('%Y-%m-%dT%H-%M-%S')
def now1():
	return str(datetime.today().strftime('%Y-%m-%dT%H-%M-%S'))
now_plus_1 = str((datetime.today()+timedelta(minutes=3)).strftime('%Y-%m-%dT%H:%M:%S')) #used for T205W D8263 SiteVisitDateAndTime
now_plus_2 = str((datetime.today()+timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%S')) #used for T205W D8261 SiteVisitDateAndEndTime
now_plus_3 = str((datetime.today()+timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')) #used for T323W D8260 Expected Completion Date
today = datetime.today().strftime('%Y-%m-%d') #used for DeclarationDate
torommorow = (datetime.today()+timedelta(days=1)).strftime('%Y-%m-%d') #used for EffectiveToDate
week_ago = (datetime.today()-timedelta(days=7)).strftime('%Y-%m-%d') #used for EffectiveFromDate
two_weeks_ago = (datetime.today()-timedelta(days=14)).strftime('%Y-%m-%d') #used for EffectiveFromDate
week_ahead = (datetime.today()+timedelta(days=7)).strftime('%Y-%m-%d') #used for EffectiveToDate
string_numbers = ''.join(chr(i) for i in random_numbers)
png_file = 'w7/DmMO/w6AgEEpGSUYgAQEBIGAgYCAgw7/DoSAiRXhpZiAgTU0gKiAgIAggAQESIAMgICABIAEgICAgICDDv8ObIEMgAgEBAgEBAgICAgICAgIDBQMDAwMDBgQEAwUHBgcHBwYHBwgJCwkICA0KCAcHDQoNCg0KCwwMDAwHCQ4PDQoMDgsMDAzDv8ObIEMBAgICAwMDBgMDBgwIBwgMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDMO/w4AgEQggHSAdAwEiIAIRAQMRAcO/w4QgHyAgAQUBAQEBAQEgICAgICAgIAECAwQFBgcICQ0KC8O/w4QgwrUQIAIBAwMCBAMFBQQEICABfQECAyAEEQUSITFBBhNRYQcicRQywoHigJjCoQgjQsKxw4EVUsORw7AkM2Jy4oCaCQ0KFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXrGkuKAnuKApuKAoOKAocuG4oCwxaDigJnigJzigJ3igKLigJPigJTLnOKEosWhwqLCo8KkwqXCpsKnwqjCqcKqwrLCs8K0wrXCtsK3wrjCucK6w4LDg8OEw4XDhsOHw4jDicOKw5LDk8OUw5XDlsOXw5jDmcOaw6HDosOjw6TDpcOmw6fDqMOpw6rDscOyw7PDtMO1w7bDt8O4w7nDusO/w4QgHwEgAwEBAQEBAQEBASAgICAgIAECAwQFBgcICQ0KC8O/w4QgwrURIAIBAgQEAwQHBQQEIAECdyABAgMRBAUhMQYSQVEHYXETIjLCgQgUQuKAmMKhwrHDgQkjM1LDsBVicsORDQoWJDTDoSXDsRcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl64oCaxpLigJ7igKbigKDigKHLhuKAsMWg4oCZ4oCc4oCd4oCi4oCT4oCUy5zihKLFocKiwqPCpMKlwqbCp8KowqnCqsKywrPCtMK1wrbCt8K4wrnCusOCw4PDhMOFw4bDh8OIw4nDisOSw5PDlMOVw5bDl8OYw5nDmsOiw6PDpMOlw6bDp8Oow6nDqsOyw7PDtMO1w7bDt8O4w7nDusO/w5ogDAMBIAIRAxEgPyDDvQLDvyDigJrLhn/DgUPDviRrP8K0fMW4wrN/w6zDny7igKLCpsO4w7tNwrHGklTDscOvwo91OzXCv8Kww7hxZXDCu8KtwqPFvcOZwr5Lwp1KdMO9w6RQw4nigJ7DmBXLnDIzwrw/PsOdf8OBI34aw7xGwoFuwr4seOKAucOiw5fDhsK/ETt54oCZw6seLcOxw57CqmUOckjigKArWcOhxaAYwoEnbGrCp2LDoGTDoyfigJTDveKAmsK1w68QeOKAocO2IcO44oCiw7HGksODccOpM3xKw7jDi8OjXxN4xb5JwrXCqeKEom0tw67igLpWxb7DgsOdZWzDrzbDtsORW8KjLCDFkuKCrMOIwrtLw6bCvcKzw7Z1w7DDj8OEwq8Gw7jDhsOiw5fDhMOfESPDuMKvw6DDnUdNS+KAuV12w6dJwrHDknUdOsO+N1jDpcK2MMOZw4ccUlvDisWSZFJXw4zigLDCo3RmwpAy4oCiw75Ew7Erwo/Ds8WTTmHigLDCo+KCrMOFfV7FvR5ywqbCoxlKM8WTwqHCpMW4NFd7w5k5RTTCvcOVKSZ+wrXDg3w74oCmwqfigKDCp18RRcOUdRJuTV4xwr7CqWvDlsObw6jDmsOrZHBwfsOLwr8XP2JHbxR+w4vCvxR8XMKvwqbCpsO3w7hhw6PCnXJ9d8OCesO0K8OzG2gew6nDmn06dsOnbMOpLhnigJM1csuGXcKrw7Qbw74Jw6/Du3R4c8O+DQoXw7s2w5jDuMO7QcKwwr7DkDUILsOnw5F8ScOhw51Dwo1Dw4LDmsOFwrELdcKnw5wMAiTCjcWgwpBZVMKyPGxVd20fBMO4HsOLw6PigKDCgcOxH8OCw7rDp+KAsMK+IGgXw4vDog0KRcOXXsO4fcO9xbhlDQrFuOKAocOsJlfDslrDisO9EFzDjXNuw4sWw78gOcOdLgPDjcKxIiI8eT/CjT9twr1bw74JYcO/IAUUw7jDgMO+E8OTYMOULMO+MHh7w4N+KcK+wrPigJR3w5nDrS9ibVLDhlnigJgXw6UPMsObRMOSNjLDrMKg4oCZTX3Cr+KAnsWTaeKEosOWw4d/YmbigKLDliFKDnDFoW3CtMOiw6zDosOkw5JyXVTCtV3CpSTDtMOxwrjCsyPCo0rigJrDh2HDqTpaw5nCpsKsxaF7SX5NfgjDrj4NCnhCP8OZO8O2wqzDuMKtw7sqw7jDgcO/IMKyYsOUPEXCqHxAw7hZcH93b8KuaDfDk8K1w5zCtnbDuSd0w5Y3BsOhJMWSwpDDrsKlwqRVCOKApsOrE8OAwr49w73CocK/YuKEojVvDQrDuMaSw6HigKDCscOxw78gw4NtwqhPd8KheMOHw4Ma4oCm4oCmxb7CpywywrZSw5dQwrDigKLCowksYG0zQ8O7wqLCuwYLBifDtMOTw7bDpMO/IOKAmn/DvDbDvyDigJrigJ7DvDHCtcOww5/DhB02w7Rcw6jDtz/DmhoGwr/CpMOdGx1zw4LDt8KjGy7DrG7igJ0WxaBVZUbDgQzFklE3wqMFAsK/L39twqvDvyDDmiPDvglhwq5pfh9fwo0+FsO4wr3CpsOq4oCYGSxuPFvDoCMewqVlCCzCqOKAmcOPZ38IwrnCkCrCjcOSwroGckkjJsK6wrjDk8OCw5xuIxlbF+KAokbCnVpVw580w6lUcsKNwqfDlnDFk1pqw7vCtMOk4oCiw5vCuuKAk8WTwqZPw4Yew48HDBYmc8Wg4oCmw6zDo2bFoXbDklF6O1lZw7TDqW1vw5nDvA7DsHfDhS8Yw7jDvyDDhV8XPjhNwqLDvC3DsMOMduKAmDbCncOgy5zCtStrw5jDtCtrUGTigLpQw5R1IAR+awXDpETDgijDoh83w443DsOTw74JX8O7L8Oof8OwUV8bfF7DvcKjPH3DoeKAnH3DoB8eXmnDnh/DuGVtwqlEw7DDjy7igLnCpS3Dij7CpBTDoeKAmTvDi8Kr4oSiw50SRVdRHnBV4oCiwo3Cj8OZwrPDvgk/wq1/w4FAfB/DocW4HcO+w5HDnxh1T8uGxb4Fwr0pwqnDmsO8NcOQdDTDsMOP4oChZOKAohzDrRfDpjnCpsK4wr/CjV0SREklUMKsxpI74oCdwrLFuMOTTQ9EwrLDsMOO4oC5Z8Kmw6nCtnbCun7CncKnw4DigJPDlsK2wrbDkSwww5tExaAVI0RQFVVUIBQgICANCsO6Tw/DvD/DhGVY4oCwZnnigLrigKHCtcOlUOKAninCp8OJThpoxZPCvcOpScOZJyd3wqPCvMKle8W+fxJxRMOxw7RhxpLCpyk6cMOWw7J6wrfDssORJcORemjCrH/Dv8OZ' #used for T215.R/W as attachement
pafaddresskey = str(random.randint(1, 99999999))
lastmeterread = str(random.randint(100, 9999))
physicalmetersize = str(random.randint(10, 20))
numberofdigits = str(random.randint(5, 10))
meterlocationcode = random.choice(D3025)
uprn = str(random.randint(1, 999999999999))
returntosewer = str(random.randint(0, 100))

#COMMON CUSTOMER BLOCK USED IN RETAILER TRANSACTIONS INCLUDED INSIDE TXXX.R TRANSACTION
CUSTOMER_BLOCK = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0027 "ConsentToContactCustomer":null
CUSTOMER_BLOCK_CON_0027 = '"ConsentToContactCustomer":null,"CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0028 "CustomerContactName1":null
CUSTOMER_BLOCK_CON_0028 = '"ConsentToContactCustomer":"1","CustomerContactName1":null,"CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0029 "CustomerContactNumber1":null
CUSTOMER_BLOCK_CON_0029 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":null,"CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0030 CustomerContactEmail incorrect format
CUSTOMER_BLOCK_CON_0030 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"incorrect_email_address.com","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0031 "CustomerAwareOfServiceRequest":null
CUSTOMER_BLOCK_CON_0031 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":null,"CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0032 "CustomerPreferredMethodOfContact":null
CUSTOMER_BLOCK_CON_0032 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":null,"CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0033 "CustomerPreferredContactTime":null
CUSTOMER_BLOCK_CON_0033 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":null,"CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0070 "ConsentToContactCustomer":"0" with Customer Contact data supplied
CUSTOMER_BLOCK_CON_0070 = '"ConsentToContactCustomer":"0","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0071 "CustomerContactEmail":"null when "CustomerPreferredMethodOfContact":"EMAIL"
CUSTOMER_BLOCK_CON_0071 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":null,"CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"'+RET_EMAIL+'"'

#CUSTOMER_BLOCK_CON_0072 "RetailerContactEmail":"incorrect_retailer_email.com" incorrect format
CUSTOMER_BLOCK_CON_0072 = '"ConsentToContactCustomer":"1","CustomerContactName1":"'+CUST_RANDOM_NAME+'","CustomerContactNumber1":"'+CUST_RANDOM_PHONE+'","CustomerExtension1":"105","CustomerContactName2":"'+CUST_RANDOM_NAME2+'","CustomerContactNumber2":"'+CUST_RANDOM_PHONE2+'","CustomerExtension2":"122","CustomerContactEmail":"'+CUST_EMAIL+'","CustomerAwareOfServiceRequest":"1","CustomerPreferredMethodOfContact":"EMAIL","CustomerPreferredContactTime":"'+random.choice(D8237)+'","CustomerAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerClassificationSensitiveCustomer":"'+random.choice(D2005)+'","LandlordTenantDetails":"'+fake.paragraph(nb_sentences=1)+'","RetailerContactName1":"'+RET_RANDOM_NAME+'","RetailerContactNumber1":"'+RET_RANDOM_PHONE+'","RetailerExtension1":"210","RetailerContactName2":"'+RET_RANDOM_NAME2+'","RetailerContactNumber2":"'+RET_RANDOM_PHONE2+'","RetailerExtension2":"224","RetailerContactEmail":"incorrect_retailer_email.com"'

#COMMON MEASURED AND UNMEASURED BLOCK FOR T321.R/W
def EXISTING_METERS():
    return '"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","TroughConnectionsFlag":"0","LastMeterRead":"'+lastmeterread+'","LastMeterReadDate":"'+week_ago+'","RemoveMeterFlag":"0","VerificationType":"METER","VerifyMeterManufacturer":"1","ProposedMeterManufacturer":"'+RANDOM_METER_MNF+'","VerifyMeterSerialNumber":"1","ProposedManufacturerMeterSerialNumber":"'+RANDOM_METER_SER+'","VerifyPhysicalMeterSize":"1","PhysicalMeterSize":"'+physicalmetersize+'","VerifyNumberofDigits":"1","NumberofDigits":"'+numberofdigits+'","VerifyGISX":"1","GISX":"'+RANDOM_GISX+'","VerifyGISY":"1","GISY":"'+RANDOM_GISY+'","VerifyMeterLocationCode":"1","MeterLocationCode":"'+meterlocationcode+'","VerifyMeterLocationDescriptor":"1","MeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","VerifyOutreaderGISX":"1","MeterOutreaderGISX":"'+OUTR_RANDOM_GISX+'","VerifyOutreaderGISY":"1","MeterOutreaderGISY":"'+OUTR_RANDOM_GISY+'","VerifyOutreaderLocationCode":"1","MeterOutreaderLocationCode":"'+meterlocationcode+'","VerifyOutreaderLocationDescriptor":"1","MeterOutreaderLocationFreeDescriptor":"'+RANDOM_OUTRE_LOC+'","MeterOutreaderLocationFreeDescriptor":"'+RANDOM_OUTRE_LOC+'","AdditionalInformation": "SUBMITTED_METER_'+RANDOM_STRING+'","AssociatedSPID":null'
def MISSING_METERS():
    return '"MissingMeterSerialNumber":"'+RANDOM_METER_SER+'","MissingMeterAdditionalInfo":"'+fake.paragraph(nb_sentences=1)+'"'
def UNMEASURED_ITEMS():
    return '"VerifyUnmeasuredItemsTypeA":"1","UnmeasuredItemsTypeACount":"1","UnmeasuredItemsTypeADescription":"DESC A","UnmeasuredItemsTypeAAdditionalInfo":"INFO A","VerifyUnmeasuredItemsTypeB":"1","UnmeasuredItemsTypeBCount":"11","UnmeasuredItemsTypeBDescription":"DESC B","UnmeasuredItemsTypeBAdditionalInfo":"INFO B","VerifyUnmeasuredItemsTypeC":"1","UnmeasuredItemsTypeCCount":"1","UnmeasuredItemsTypeCDescription":"DESC C","UnmeasuredItemsTypeCAdditionalInfo":"INFO C","VerifyUnmeasuredItemsTypeD":"1","UnmeasuredItemsTypeDCount":"1","UnmeasuredItemsTypeDDescription":"DESC D","UnmeasuredItemsTypeDAdditionalInfo":"INFO D","VerifyUnmeasuredItemsTypeE":"1","UnmeasuredItemsTypeECount":"1","UnmeasuredItemsTypeEDescription":"DESC E","UnmeasuredItemsTypeEAdditionalInfo":"INFO E","VerifyUnmeasuredItemsTypeF":"1","UnmeasuredItemsTypeFCount":"1","UnmeasuredItemsTypeFDescription":"DESC F","UnmeasuredItemsTypeFAdditionalInfo":"INFO F","VerifyUnmeasuredItemsTypeG":"1","UnmeasuredItemsTypeGCount":"1","UnmeasuredItemsTypeGDescription":"DESC G","UnmeasuredItemsTypeGAdditionalInfo":"INFO G","VerifyUnmeasuredItemsTypeH":"1","UnmeasuredItemsTypeHCount":"1","UnmeasuredItemsTypeHDescription":"DESC H","UnmeasuredItemsTypeHAdditionalInfo":"INFO H","VerifyPipeSize":"1","PipeSize":"'+physicalmetersize+'","SupplyArrangementCheckFlag":"1","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"'
#COMMON MEASURED AND UNMEASURED BLOCK FOR T321.R/W

#VERIFIED MEASURED AND UNMEASURED BLOCK FOR T322.W
VERIFIED_EXISTING_METERS = '"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","RemoveMeterFlag":"0", "UpdatedMeterManufacturer":"1","ProposedMeterManufacturer":"'+RANDOM_METER_MNF+'","UpdatedManufacturerMeterSerialNumber":"1","ProposedManufacturerMeterSerialNumber":"'+RANDOM_METER_SER+'","UpdatedPhysicalMeterSize":"1","PhysicalMeterSize":"'+physicalmetersize+'","UpdatedNumberofDigits":"1","NumberofDigits":"'+numberofdigits+'","UpdatedGISX":"1","GISX":"'+RANDOM_GISX+'","UpdatedGISY":"1","GISY":"'+RANDOM_GISY+'","UpdatedMeterLocationCode":"1","MeterLocationCode":"'+meterlocationcode+'","UpdatedMeterLocationFreeDescriptor":"1","MeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","UpdatedMeterOutreaderGISX":"1","MeterOutreaderGISX":"'+OUTR_RANDOM_GISX+'","UpdatedMeterOutreaderGISY":"1","MeterOutreaderGISY":"'+OUTR_RANDOM_GISY+'","UpdatedMeterOutreaderLocationCode":"1","MeterOutreaderLocationCode":"'+meterlocationcode+'","UpdatedMeterOutreaderLocationFreeDescriptor":"1","MeterOutreaderLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","AdditionalInformation": "T322W_COMPLETED_'+RANDOM_STRING+'"'
VERIFIED_MISSING_METERS = '"MissingMeterSerialNumber":"'+RANDOM_METER_SER+'","MissingMeterOutcome":"'+random.choice(D8262)+'","MissingMeterAdditionalInfo":"'+fake.paragraph(nb_sentences=1)+'"'
VERIFIED_UNMEASURED_ITEMS = '"UpdatedUnmeasuredItemsTypeA":"1","UnmeasuredItemsTypeACount":"1","UnmeasuredItemsTypeADescription":"DESC A","UpdatedUnmeasuredItemsTypeB":"1","UnmeasuredItemsTypeBCount":"11","UnmeasuredItemsTypeBDescription":"DESC B","UpdatedUnmeasuredItemsTypeC":"1","UnmeasuredItemsTypeCCount":"1","UnmeasuredItemsTypeCDescription":"DESC C","UpdatedUnmeasuredItemsTypeD":"1","UnmeasuredItemsTypeDCount":"1","UnmeasuredItemsTypeDDescription":"DESC D","UpdatedUnmeasuredItemsTypeE":"1","UnmeasuredItemsTypeECount":"1","UnmeasuredItemsTypeEDescription":"DESC E","UpdatedUnmeasuredItemsTypeF":"1","UnmeasuredItemsTypeFCount":"1","UnmeasuredItemsTypeFDescription":"DESC F","UpdatedUnmeasuredItemsTypeG":"1","UnmeasuredItemsTypeGCount":"1","UnmeasuredItemsTypeGDescription":"DESC G","UpdatedUnmeasuredItemsTypeH":"1","UnmeasuredItemsTypeHCount":"1","UnmeasuredItemsTypeHDescription":"DESC H","UpdatedPipeSize":"1","PipeSize":"'+physicalmetersize+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"'
#UPDATED MEASURED AND UNMEASURED BLOCK FOR T322.W

#potential meters T335.R T336.W 
POTENTIAL_METERS = '"PotentialMeter":"'+random.choice(D8411)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","MeterRead":"'+lastmeterread+'","MeterReadDate":"'+week_ago+'","PhysicalMeterSize":"'+physicalmetersize+'","NumberofDigits":"'+numberofdigits+'","GISX":"'+RANDOM_GISX+'","GISY":"'+RANDOM_GISY+'","MeterLocationCode":"'+meterlocationcode+'","MeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'"'
#potential meters T335.R T336.W

def rtl_preheader():
	return '{"SendMessageRequest":{"MessageContainer":{"DocumentReferenceNumber":"'+unique_id1()+'","DocumentTransactionType":"RetailerTransaction","DataTransactionFormat":"JSON","Payload":{'
def rtl_postheader():
	return '"DataTransactionReferenceNumber":"'+unique_id2()+'","OriginatorsReference":"'+unique_id3()+'","TransactionSourceOrgID":"'+retailer+'","TransactionDestinationOrgID":"MOSL-M","TransactionTimestamp":"'+transaction_timestamp()+'"}'
def wsl_preheader():
	return '{"SendMessageRequest":{"MessageContainer":{"DocumentReferenceNumber":"'+unique_id1()+'","DocumentTransactionType":"WholesalerTransaction","DataTransactionFormat":"JSON","Payload":{'
def wsl_postheader():
	return '"DataTransactionReferenceNumber":"'+unique_id2()+'","OriginatorsReference":"'+unique_id3()+'","TransactionSourceOrgID":"'+wholesaler+'","TransactionDestinationOrgID":"MOSL-M","TransactionTimestamp":"'+transaction_timestamp()+'"}'

global_orid = ''

def T201W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T201W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T201W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","WholesalerSystemReference": "ACCEPTED_'+RANDOM_STRING+'"}}}}}}}'
def T202W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T202W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T202W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","WholesalerSystemReference":"WSL_'+RANDOM_STRING+'","RejectReasonCode":"'+random.choice(D8230)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'
def T203W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T203W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T203W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformationRequestCode":"'+random.choice(D8226)+'","AdditionalInformation": "INFOREQST_'+RANDOM_STRING+'"}}}}}}}'
def T204R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T204R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T204R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "INFOPROVD_'+RANDOM_STRING+'"}}}}}}}'
def T205W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T205W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T205W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","SiteVisitDateAndTime":"'+now_plus_1+'","SiteVisitDateAndEndTime":"'+now_plus_2+'","AdditionalInformation": "VISITSCHED_'+RANDOM_STRING+'"}}}}}}}'
def T206W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T206W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T206W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","SiteVisitFailureCode":"'+random.choice(D8228)+'","AdditionalInformation": "VISITNOTCOMP_'+RANDOM_STRING+'"}}}}}}}'
def T207R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T207R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T207R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "RTL_COMMETED_'+RANDOM_STRING+'"}}}}}}}'
def T207W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T207W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T207W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "WSL_COMMETED_'+RANDOM_STRING+'"}}}}}}}'
def T208R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T208R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T208R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "CLOSED_'+RANDOM_STRING+'"}}}}}}}'
def T210R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T210R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T210R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ResubmitReasonCode":"'+random.choice(D8231)+'","AdditionalInformation": "RESUBMITTED_'+RANDOM_STRING+'"}}}}}}}'
def T211R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T211R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T211R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","CancellationReasonCode":"'+random.choice(D8036)+'","AdditionalInformation": "RTL_CANCELLED_'+RANDOM_STRING+'"}}}}}}}'
def T211W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T211W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T211W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","CancellationReasonCode":"'+random.choice(D8036)+'","AdditionalInformation": "WSL_CANCELLED_'+RANDOM_STRING+'"}}}}}}}'
def T212W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T212W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T212W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "PREPLAN_'+RANDOM_STRING+'"}}}}}}}'
def T213W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T213W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T213W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","RequestDeferralCode":"'+random.choice(D8229)+'","EffectiveFromDate":"'+today+'","EffectiveToDate":"'+torommorow+'","AdditionalInformation": "START_DEFERRAL_'+RANDOM_STRING+'"}}}}}}}'
def T214W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T214W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T214W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","EffectiveToDate":"'+today+'","AdditionalInformation": "END_DEFERRAL_'+RANDOM_STRING+'"}}}}}}}'
def T215R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T215R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T215R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ParentTransactionOriginatorsReference": null,"AttachedFileName": "img1png","AttachedFileType": "JPG", "AttachedFileContent": "'+png_file+'"}}}}}}}'
def T215W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T215W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T215W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ParentTransactionOriginatorsReference": null,"AttachedFileName": "img1png","AttachedFileType": "JPG", "AttachedFileContent": "'+png_file+'"}}}}}}}'
def T216R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T216R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T216R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","URL": "'+t216_url+'"}}}}}}}'
def T216W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T216W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T216W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","URL": "'+t216_url+'"}}}}}}}'
def T217W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T217W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T217W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","CustomerContactRequired":"1","AdditionalInformationRequestCode":"'+random.choice(D8226)+'","AdditionalInformation": "CUSTINFOREQST_'+RANDOM_STRING+'"}}}}}}}'
def T218R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T218R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T218R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","RetailerSystemReference":"RET_REF_'+RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent": {'+CUSTOMER_BLOCK+'},"AdditionalInformation": "CUSTINFOPROVD_'+RANDOM_STRING+'"}}}}}}}'
def T220W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T220W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T220W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation":"QUOTEPROPOSED_'+RANDOM_STRING+'"}}}}}}}'
def T221R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T221R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T221R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation":"QUOTEACCEPTED_'+RANDOM_STRING+'"}}}}}}}'
def T222W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T222W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T222W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ResponseType":"FOLLOWON","RequestResponse": "'+fake.paragraph(nb_sentences=1)+'","OutstandingActions": "'+fake.paragraph(nb_sentences=1)+'","ExpectedCompletionDate": "'+week_ahead+'","CustomerNotifiedOfPlan": "1","FollowonRequestORID": null,"RelatedRequestORID": null,"AdditionalInformation": "COMPLETED_'+RANDOM_STRING+'"}}}}}}}'
def T223W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T223W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T223W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","MeterWorkCompleteCode":"NEWINSTALL","AdditionalInformation": "'+fake.paragraph(nb_sentences=1)+'","Meter":{"NewMeterManufacturer":"'+RANDOM_METER_MNF+'","NewManufacturerMeterSerialNumber":"'+RANDOM_METER_SER+'","MeterRead":"'+str(random.randint(100, 1000))+'","MeterReadDate":"'+week_ago+'","PhysicalMeterSize":"'+str(random.randint(5, 15))+'","NumberofDigits":"'+str(random.randint(2, 6))+'","GISX":"'+RANDOM_GISX+'","GISY":"'+RANDOM_GISY+'","MeterLocationCode":"'+meterlocationcode+'","MeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","MeterOutreaderGISX":"'+OUTR_RANDOM_GISX+'","MeterOutreaderGISY":"'+OUTR_RANDOM_GISY+'","MeterOutreaderLocationCode":"'+meterlocationcode+'","MeterOutreaderLocationFreeDescriptor":"'+RANDOM_OUTRE_LOC+'","SecondaryAddressableObject":"'+RANDOM_STRING+'","PrimaryAddressableObject":"'+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+pafaddresskey+'"}}}}}}}}'
def T224W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T224W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T224W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","DelayReasonCode":"'+random.choice(D8227)+'","AdditionalInformation": "PROCDELAY_'+RANDOM_STRING+'"}}}}}}}'
def T225R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T225R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T225R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","IncorrectReasonCode":"'+random.choice(D8463)+'","AdditionalInformation": "T225R_INCORRECT_'+RANDOM_STRING+'","DeclarationDate":"'+today+'"}}}}}}}'
def T225W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T225W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T225W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","IncorrectReasonCode":"'+random.choice(D8463)+'","AdditionalInformation": "T225W_INCORRECT_'+RANDOM_STRING+'","DeclarationDate":"'+today+'"}}}}}}}'
def T226W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T226W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T226W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","WholesalerDecision":"'+random.choice(D8442)+'","AdditionalInformation": "OUTCOMEPROP'+RANDOM_STRING+'"}}}}}}}'
def T227R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T227R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T227R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "OUTCOMEAGREED_'+RANDOM_STRING+'"}}}}}}}'
def T228R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T228R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T228R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "OUTCOMENOTAGREED_'+RANDOM_STRING+'"}}}}}}}'
def T321R_MEASURED():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T321R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T321R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","WorkRequestType":"MEASURED","RetailerSystemReference": "RET_'+RANDOM_STRING+'","ParentRequestORID":null,"CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"ExistingMeters":{"ExistingMeter":[{'+EXISTING_METERS()+'}],"ExistingMeter":[{'+EXISTING_METERS()+'}]},"MissingMeters":{"MissingMeter":[{'+MISSING_METERS()+'}]}}}}}}}}'
def T321R_UNMEASURED():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T321R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T321R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","WorkRequestType":"UNMEASURED","RetailerSystemReference": "RET_'+RANDOM_STRING+'","ParentRequestORID":"null","CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"ExistingMeters":null,"MissingMeters":null,"UnmeasuredSupplyArrangements":{'+UNMEASURED_ITEMS()+'}}}}}}}}'
def T321R():
    return T321R_MEASURED()    
def T321W_MEASURED():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T321W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T321W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","WorkRequestType":"MEASURED","ParentRequestORID":null,"DeclarationDate":"'+today+'","ExistingMeters":{"ExistingMeter":[{'+EXISTING_METERS()+'}]},"MissingMeters":{"MissingMeter":[{'+MISSING_METERS()+'}]}}}}}}}}'
def T321W_UNMEASURED():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T321W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T321W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","WorkRequestType":"UNMEASURED","ParentRequestORID":null,"DeclarationDate":"'+today+'","UnmeasuredSupplyArrangements":{'+UNMEASURED_ITEMS()+'}}}}}}}}'
def T321W():
    return T321W_MEASURED()  
def T322W_MEASURED():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T322W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T322W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ChargeToRetailerFlag":"1","VerifiedExistingMeters":{"VerifiedExistingMeter":[{'+VERIFIED_EXISTING_METERS+'}]},"VerifiedMissingMeters":{"VerifiedMissingMeter":[{'+VERIFIED_MISSING_METERS+'}]},"VerifiedUnmeasuredSupplyArrangements":null}}}}}}}'
def T322W_UNMEASURED():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T322W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T322W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ChargeToRetailerFlag":"1","VerifiedUnmeasuredSupplyArrangements":{'+VERIFIED_UNMEASURED_ITEMS+'}}}}}}}}'
def T322W():
    return T322W_MEASURED()  
def T323W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T323W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T323W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","UnableToFulfilRequestReason": "ABLE","SiteVisitDateAndTime":"'+now_plus_1+'","OtherSPIDOrMeterInvolved":"0","CustomerNotifiedOfPlan":"1","ExpectedCompletionDate":"'+now_plus_3+'","AdditionalInformation": "PLANPROP_'+RANDOM_STRING+'"}}}}}}}'
def T324R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T324R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T324R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "PLANAGREED_'+RANDOM_STRING+'"}}}}}}}'
def T325R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T325R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T325R"][0]+'",'+ rtl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","AdditionalInformation": "PLANDISP_'+RANDOM_STRING+'"}}}}}}}'
def T331W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T331W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T331W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+pick_spid_meter()[0]+'","GSrequestType":"UNMETERED","RateableValue":"123","GapSiteIdentifiedDate":"'+week_ago+'","ApplicationReason":"WSPID","ReasonForWaterOrSewerageOnlySPID":"Reason '+transaction_timestamp()+'","FoulSewerageServices":"0","HighwayDrainageServices":"0","SurfaceWaterDrainageServices":"0","TradeEffluentServices":"0","ExistingSPIDAtPremises":"1","TypeOfExistingSPID":"WSPID","OtherSPID":"0","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'"}}}}}}}'
def T332W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T332W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T332W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","CustomerLetterSentDate":"'+week_ago+'","GSConnectionType":"'+random.choice(D8402)+'","VOABAReference":"'+RANDOM_STRING+'","VOABAReferenceReasonCode":null,"UPRN":"'+uprn+'","UPRNReasonCode":null,"DeveloperBusinessName":"'+RANDOM_STRING+'","CustomerBannerName":"'+RANDOM_STRING+'","ContactName":"'+CUST_RANDOM_NAME+'","ContactEmail":"'+CUST_EMAIL+'","ContactNumber":"'+CUST_RANDOM_PHONE+'","FreeDescriptor":"'+fake.paragraph(nb_sentences=1)+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+pafaddresskey+'","BillingAddressLine1":"'+RANDOM_ADDRESS1+'","BillingAddressLine2":"'+RANDOM_ADDRESS2+'","BillingAddressLine3":"'+RANDOM_ADDRESS3+'","BillingAddressLine4":"'+RANDOM_ADDRESS4+'","BillingAddressLine5":"'+RANDOM_ADDRESS5+'","BillingAddressPostcode":"'+random.choice(POSTCODES)+'","OccupancyStatus":"'+random.choice(D2013)+'","LandlordSPID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'
def T335R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T335R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T335R"][0]+'",'+ rtl_postheader() + ',"Payload":{"WholesalerID":"MOSLTEST-W","RetailerSystemReference": "RET_'+RANDOM_STRING+'","DeveloperBusinessName":"'+RANDOM_STRING+'","CustomerBannerName":"'+RANDOM_STRING+'","FreeDescriptor":"'+fake.paragraph(nb_sentences=1)+'","SecondaryAddressableObject":"'+RANDOM_STRING+'","PrimaryAddressableObject":"'+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+pafaddresskey+'","VOABAReference":"'+RANDOM_STRING+'","UPRN":"'+uprn+'","GSRequestType":"METERED","RateableValue":null,"GapSiteIdentifiedDate":"'+week_ago+'","ApplicationReason":"WSPID","ReasonForWaterOrSewerageOnlySPID":"'+fake.paragraph(nb_sentences=1)+'","FoulSewerageServices":"0","HighwayDrainageServices":"0","SurfaceWaterDrainageServices":"0","TradeEffluentServices":"0","ExistingSPIDAtPremises":"0","TypeOfExistingSPID":null,"OtherSPID":null,"RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","WishToBeRetailerForThisGapSite":"1","CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"PotentialMeters":{"PotentialMeter":[{'+POTENTIAL_METERS+'}]}}}}}}}}'
def T336W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T336W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T336W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","GSCompletionCode":"RA","RetailerID":"MOSLTEST-R","GSConfirmed":"1","GSAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","SPID":"'+SPID+'","GSRequestType":"METERED","PaymentDueToRetailer":"1","AmountDueToRetailer":"'+lastmeterread+'","PaymentAdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","ChargeToRetailerFlag":"1","ChargeToRetailerReason":"'+fake.paragraph(nb_sentences=1)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","GSDetails":{"RateableValue":null,"CustomerLetterSentDate":"'+week_ago+'","GSConnectionType":"GS","VOABAReference":"'+RANDOM_STRING+'","VOABAReferenceReasonCode":null,"UPRN":"'+uprn+'","UPRNReasonCode":null,"DeveloperBusinessName":"'+RANDOM_STRING+'","CustomerBannerName":"'+RANDOM_STRING+'","ContactName":"'+CUST_RANDOM_NAME+'","ContactEmail":"'+CUST_EMAIL+'","ContactNumber":"'+CUST_RANDOM_PHONE+'","FreeDescriptor":"'+fake.paragraph(nb_sentences=1)+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+pafaddresskey+'","BillingAddressBuildingName":"'+RANDOM_STRING+'","BillingAddressLine1":"'+RANDOM_ADDRESS1+'","BillingAddressLine2":"'+RANDOM_ADDRESS2+'","BillingAddressLine3":"'+RANDOM_ADDRESS3+'","BillingAddressLine4":"'+RANDOM_ADDRESS4+'","BillingAddressLine5":"'+RANDOM_ADDRESS5+'","BillingAddressPostcode":"'+random.choice(POSTCODES)+'","OccupancyStatus":"'+random.choice(D2013)+'","LandlordSPID":null,"PotentialMeters":{"PotentialMeter":[{'+POTENTIAL_METERS+'}]}}}}}}}}}'
def T339R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T339R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T339R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","MissingServiceComponents": [{"MissingServiceComponent": "AW"}, {"MissingServiceComponent": "SW"}],"BusinessType":"Restaurant","ReturntoSewer":"'+returntosewer+'","SurfaceArea":"120","AreaDrained":null,"SewerageSystemConnectedSitePercentage":"30","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference": "RET_'+RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'}}}}}}}}'
def T339W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T339W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T339W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","MissingServiceComponents": [{"MissingServiceComponent": "AW"}, {"MissingServiceComponent": "SW"}],"BusinessType":"Restaurant","ReturntoSewer":"'+returntosewer+'","SurfaceArea":"120","AreaDrained":null,"SewerageSystemConnectedSitePercentage":"30","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'"}}}}}}}'
def T340W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T340W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T340W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","CompleteReasonCode":"SCUPDATED","SPIDNotUpdatedDetails":null,"UpdatedServiceComponents":[{"MissingServiceComponent":"AW","ServiceComponentEnabled":"1","AssignedTariffCode":"TARIFF-01","EffectiveFromDate":"'+today+'"}],"BusinessType":"Restaurant","FollowOnRequestORID":null,"ChargeToRetailerFlag":"1","ChargeToRetailerReason":"'+fake.paragraph(nb_sentences=1)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'
def T341R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T341R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T341R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SWG_SPID+'","SPIDUpdateRequestType":"REMOVESC","RequestReason":"MERGED","AllMetersImpacted":"0","ImpactedMeters":{"ImpactedMeter":[{"MeterManufacturer":"'+SWG_METER_MNF+'","ManufacturerMeterSerialNumber":"'+SWG_METER_SER+'"}]},"AdditionalImpactedMetersInfo":"'+fake.paragraph(nb_sentences=1)+'","MissingMetersInfo":"'+fake.paragraph(nb_sentences=1)+'","RemoveSCMPW":null,"RemoveSCMNPW":null,"RemoveSCAW":null,"RemoveSCUW":null,"RemoveSCWCA":null,"RemoveSCMS":"'+random.choice(D8422)+'","RemoveSCAS":"'+random.choice(D8423)+'","RemoveSCUS":"'+random.choice(D8424)+'","RemoveSCSW":"'+random.choice(D8425)+'","RemoveSCHD":"'+random.choice(D8426)+'","RemoveSCSCA":"'+random.choice(D8427)+'","PairedSPIDImpacted":"'+random.choice(D8450)+'","TypeOfImpact":"REMOVESC","RemoveOtherSPIDSCMPW":"'+random.choice(D8451)+'","RemoveOtherSPIDSCMNPW":"'+random.choice(D8452)+'","RemoveOtherSPIDSCAW":"'+random.choice(D8453)+'","RemoveOtherSPIDSCUW":"'+random.choice(D8454)+'","RemoveOtherSPIDSCWCA":"'+random.choice(D8455)+'","RemoveOtherSPIDSCMS":null,"RemoveOtherSPIDSCAS":null,"RemoveOtherSPIDSCUS":null,"RemoveOtherSPIDSCSW":null,"RemoveOtherSPIDSCHD":null,"RemoveOtherSPIDSCSCA":null,"DPID":"DPID_'+RANDOM_STRING+'","InvestigationDetails":"'+fake.paragraph(nb_sentences=1)+'","DateToRemoveServices":"'+week_ago+'","PremisesExtent":"'+random.choice(D8430)+'","PrimaryOrSecondaryUse":"PRIMARY","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference":"REF_'+RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"Merged":{"AssociatedWaterSPID":"3019178819W13","AssociatedSewerageSPID":null,"CustomerName":"'+CUST_RANDOM_NAME+'","CustomerBannerName":"'+CUST_RANDOM_NAME2+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","VOABAReference":"'+RANDOM_STRING+'","UPRN":"'+uprn+'","RateableValue":"'+lastmeterread+'","MetersSerialNumberInfo":"'+RANDOM_METER_SER+'","MultipleWaterSupplyConnections":"1","MultipleConnectionsFurtherInfo":"'+fake.paragraph(nb_sentences=1)+'","DatePropertyMerged":"'+week_ago+'"}}}}}}}}'
def T341W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T341W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T341W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SWG_SPID+'","SPIDUpdateRequestType":"REMOVESC","RequestReason":"MERGED","AllMetersImpacted":"0","ImpactedMeters":{"ImpactedMeter":[{"MeterManufacturer":"'+SWG_METER_MNF+'","ManufacturerMeterSerialNumber":"'+SWG_METER_SER+'"}]},"AdditionalImpactedMetersInfo":"'+fake.paragraph(nb_sentences=1)+'","MissingMetersInfo":"'+fake.paragraph(nb_sentences=1)+'","RemoveSCMPW":null,"RemoveSCMNPW":null,"RemoveSCAW":null,"RemoveSCUW":null,"RemoveSCWCA":null,"RemoveSCMS":"'+random.choice(D8422)+'","RemoveSCAS":"'+random.choice(D8423)+'","RemoveSCUS":"'+random.choice(D8424)+'","RemoveSCSW":"'+random.choice(D8425)+'","RemoveSCHD":"'+random.choice(D8426)+'","RemoveSCSCA":"'+random.choice(D8427)+'","PairedSPIDImpacted":"'+random.choice(D8450)+'","TypeOfImpact":"REMOVESC","RemoveOtherSPIDSCMPW":"'+random.choice(D8451)+'","RemoveOtherSPIDSCMNPW":"'+random.choice(D8452)+'","RemoveOtherSPIDSCAW":"'+random.choice(D8453)+'","RemoveOtherSPIDSCUW":"'+random.choice(D8454)+'","RemoveOtherSPIDSCWCA":"'+random.choice(D8455)+'","RemoveOtherSPIDSCMS":null,"RemoveOtherSPIDSCAS":null,"RemoveOtherSPIDSCUS":null,"RemoveOtherSPIDSCSW":null,"RemoveOtherSPIDSCHD":null,"RemoveOtherSPIDSCSCA":null,"DPID":"DPID_'+RANDOM_STRING+'","InvestigationDetails":"'+fake.paragraph(nb_sentences=1)+'","DateToRemoveServices":"'+week_ago+'","PremisesExtent":"'+random.choice(D8430)+'","PrimaryOrSecondaryUse":"PRIMARY","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","Merged":{"AssociatedWaterSPID":"3019178819W13","AssociatedSewerageSPID":null,"CustomerName":"'+CUST_RANDOM_NAME+'","CustomerBannerName":"'+CUST_RANDOM_NAME2+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","VOABAReference":"'+RANDOM_STRING+'","UPRN":"'+uprn+'","RateableValue":"'+lastmeterread+'","MetersSerialNumberInfo":"'+RANDOM_METER_SER+'","MultipleWaterSupplyConnections":"1","MultipleConnectionsFurtherInfo":"'+fake.paragraph(nb_sentences=1)+'","DatePropertyMerged":"'+week_ago+'"}}}}}}}}'
def T342W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T342W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T342W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","WholesalerDecision":"'+random.choice(D8442)+'","CompleteReasonCodeC5":"'+random.choice(D8443)+'","SiteVisitOrAssessmentDate":"'+week_ago+'","EffectiveFromDate":"'+week_ahead+'","AnalysisUndertakenInfo":"'+fake.paragraph(nb_sentences=1)+'","WaterSCApply":"'+random.choice(D8446)+'","SewerageSCApply":"'+random.choice(D8447)+'","SurfaceWaterDrainageSCApply":"'+random.choice(D8448)+'","HighwaysDrainageSCApply":"'+random.choice(D8449)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'
def T351R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T351R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T351R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RelatedRequestORID":null,"CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"SelectedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","AddressSameAsCMOS":"'+random.choice(D8330)+'","SecondaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","PrimaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+str(random.randint(1,99999999))+'","CombiMeterFlag":"0","CombiMeterSerialNumber":null,"PublicHealthIssue":"'+random.choice(D8332)+'","DataloggerNonWholesaler":"1","DataloggerStatus":"NOTREMOVED","DataloggerRemovalDate":"'+week_ahead+'","MeterModel":"'+random.choice(D8335)+'","MeterMenuReference":"METER_'+RANDOM_STRING+'","Fault1":"STOPPED","Fault2":"BACKWARD","Fault3":"SLOWED","OtherFaultDetails":null,"MeterRead":"'+str(random.randint(100,9999))+'","MeterReadDate":"'+week_ago+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}}'
def T351W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T351W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T351W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RelatedRequestORID":null,"DeclarationDate":"'+today+'","SelectedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","AddressSameAsCMOS":"'+random.choice(D8330)+'","SecondaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","PrimaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+str(random.randint(1,99999999))+'","CombiMeterFlag":"0","CombiMeterSerialNumber":null,"PublicHealthIssue":"'+random.choice(D8332)+'","DataloggerNonWholesaler":"1","DataloggerStatus":"NOTREMOVED","DataloggerRemovalDate":"'+week_ahead+'","MeterModel":"'+random.choice(D8335)+'","MeterMenuReference":"METER_'+RANDOM_STRING+'","Fault1":"STOPPED","Fault2":"BACKWARD","Fault3":"SLOWED","OtherFaultDetails":null,"MeterRead":"'+str(random.randint(100,9999))+'","MeterReadDate":"'+week_ago+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}}'
def T352W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T352W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T352W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","CompleteReasonCode":"REPLACED","RepairedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","NewMeterManufacturer":"'+RANDOM_METER_MNF+'","NewManufacturerMeterSerialNumber":"'+RANDOM_METER_SER+'","MeterRead":"120","MeterReadDate":"'+today+'","UpdatedPhysicalMeterSize":"1","PhysicalMeterSize":"12","UpdatedNumberofDigits":"1","NumberofDigits":"5","UpdatedGISX":"1","GISX":"'+RANDOM_GISX+'","UpdatedGISY":"1","GISY":"'+RANDOM_GISY+'","UpdatedMeterLocationCode":"1","MeterLocationCode":"I","UpdatedMeterLocationFreeDescriptor":"1","MeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","UpdatedMeterOutreaderGISX":"1","MeterOutreaderGISX":"'+OUTR_RANDOM_GISX+'","UpdatedMeterOutreaderGISY":"1","MeterOutreaderGISY":"'+OUTR_RANDOM_GISY+'","UpdatedMeterOutreaderLocationCode":"1","MeterOutreaderLocationCode":"O","UpdatedMeterOutreaderLocationFreeDescriptor":"1","MeterOutreaderLocationFreeDescriptor":"'+RANDOM_OUTRE_LOC+'","AdditionalInformation":"UPDATED_METER_T352W"}}}}}}}}'
def T353R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T353R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T353R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RelatedRequestORID":null,"CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"InstallMeter":{"MeterAddressSameAsSPIDAddress":"1","SecondaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","PrimaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+str(random.randint(1,99999999))+'","ProposedPhysicalMeterSize":"'+physicalmetersize+'","MeterModel":"'+random.choice(D8335)+'","MeterMenuReference":"METER_'+RANDOM_STRING+'","ProposedMeterLocationCode":"'+random.choice(D8346)+'","ProposedMeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}}'
def T355R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T355R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T355R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RelatedRequestORID":null,"CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"SelectedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","AddressSameAsCMOS":"'+random.choice(D8330)+'","SecondaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","PrimaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+str(random.randint(1,99999999))+'","CombiMeterFlag":"0","CombiMeterSerialNumber":null,"DataloggerNonWholesaler":"1","DataloggerStatus":"NOTREMOVED","DataloggerRemovalDate":"'+week_ahead+'","MeterModel":"'+random.choice(D8335)+'","MeterMenuReference":"METER_'+RANDOM_STRING+'","MeterAccuracyTestReasonCode":"'+random.choice(D8348)+'","OtherReasonDetails":"'+fake.paragraph(nb_sentences=1)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}}'
def T355W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T355W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T355W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RelatedRequestORID":null,"DeclarationDate":"'+today+'","SelectedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","AddressSameAsCMOS":"'+random.choice(D8330)+'","SecondaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","PrimaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+str(random.randint(1,99999999))+'","CombiMeterFlag":"0","CombiMeterSerialNumber":null,"DataloggerNonWholesaler":"1","DataloggerStatus":"NOTREMOVED","DataloggerRemovalDate":"'+week_ahead+'","MeterModel":"'+random.choice(D8335)+'","MeterMenuReference":"METER_'+RANDOM_STRING+'","MeterAccuracyTestReasonCode":"'+random.choice(D8348)+'","OtherReasonDetails":"'+fake.paragraph(nb_sentences=1)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}}'
def T356W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T356W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T356W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","WorkCompleteReasonCode":"'+random.choice(D8367)+'","MeterTestResult":"'+random.choice(D8368)+'","AllowanceAwarded":"1","AllocatedVolumetricAllowance":"'+lastmeterread+'","MeterRead":"'+lastmeterread+'","MeterReadDate":"'+week_ago+'","ChargeToRetailerFlag":"1","FollowonRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'
def T357W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T357W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T357W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","ReplacedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","NewMeterManufacturer":"'+RANDOM_METER_MNF+'","NewManufacturerMeterSerialNumber":"'+RANDOM_METER_SER+'","MeterRead":"120","MeterReadDate":"'+today+'","UpdatedPhysicalMeterSize":"1","PhysicalMeterSize":"12","UpdatedNumberofDigits":"1","NumberofDigits":"5","UpdatedGISX":"1","GISX":"'+RANDOM_GISX+'","UpdatedGISY":"1","GISY":"'+RANDOM_GISY+'","UpdatedMeterLocationCode":"1","MeterLocationCode":"I","UpdatedMeterLocationFreeDescriptor":"1","MeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'","UpdatedMeterOutreaderGISX":"1","MeterOutreaderGISX":"'+OUTR_RANDOM_GISX+'","UpdatedMeterOutreaderGISY":"1","MeterOutreaderGISY":"'+OUTR_RANDOM_GISY+'","UpdatedMeterOutreaderLocationCode":"1","MeterOutreaderLocationCode":"O","UpdatedMeterOutreaderLocationFreeDescriptor":"1","MeterOutreaderLocationFreeDescriptor":"'+RANDOM_OUTRE_LOC+'","AdditionalInformation":"AWAITEST_T357W"}}}}}}}}'
def T365R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T365R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T365R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RelatedRequestORID":null,"CustomerContactRequired":"1","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"SelectedMeter":{"MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","AddressSameAsCMOS":"'+random.choice(D8330)+'","SecondaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","PrimaryAddressableObject":"'+str(random.randint(1111,9999))+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+str(random.randint(1,99999999))+'","CombiMeterFlag":"0","CombiMeterSerialNumber":null,"PublicHealthIssue":"'+random.choice(D8332)+'","DataloggerNonWholesaler":"1","DataloggerStatus":"NOTREMOVED","DataloggerRemovalDate":"'+week_ahead+'","MeterWorkRequestType":"'+random.choice(D8326)+'","ProposedPhysicalMeterSize":"'+physicalmetersize+'","MeterModel":"'+random.choice(D8335)+'","MeterMenuReference":"METER_'+RANDOM_STRING+'","ProposedMeterLocationCode":"'+random.choice(D8346)+'","ProposedMeterLocationFreeDescriptor":"'+RANDOM_METER_LOC+'"}}}}}}}}'
def T501R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T501R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T501R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RequestReceivedDate":"'+week_ago+'","RequestDescription":"'+fake.paragraph(nb_sentences=1)+'","ComplaintLevel":"'+random.choice(D8356)+'","OtherComplaintDetails":"'+RANDOM_STRING+'","ComplaintCategory":"'+random.choice(D8358)+'","OtherCategoryDetails":"'+RANDOM_STRING+'","CompensationClaimed":"'+random.choice(D8360)+'","OtherCompensationDetails":"'+RANDOM_STRING+'","RelatedRequestORID":null,"CustomerContactRequired":"1","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'}}}}}}}}'
def T501W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T501W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T501W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RequestReceivedDate":"'+week_ago+'","RequestDescription":"'+fake.paragraph(nb_sentences=1)+'","ComplaintLevel":"'+random.choice(D8356)+'","OtherComplaintDetails":"'+RANDOM_STRING+'","ComplaintCategory":"'+random.choice(D8358)+'","OtherCategoryDetails":"'+RANDOM_STRING+'","CompensationClaimed":"'+random.choice(D8360)+'","OtherCompensationDetails":"'+RANDOM_STRING+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'"}}}}}}}'
def T505R():
    return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T505R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T505R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RequestReceivedDate":"'+week_ago+'","RequestType":"'+random.choice(D8364)+'","DrinkingWaterEnquiryType":"'+random.choice(D8365)+'","RequestDescription":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"CustomerContactRequired":"1","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'}}}}}}}}'
def T505W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T505W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T505W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","RequestReceivedDate":"'+week_ago+'","RequestType":"'+random.choice(D8364)+'","DrinkingWaterEnquiryType":"'+random.choice(D8365)+'","RequestDescription":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'"}}}}}}}'
def T551R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T551R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T551R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","DPID":"DPID_'+RANDOM_STRING+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RequestReceivedDate":"'+week_ago+'","RequestDescription":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"CustomerContactRequired":"1","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'}}}}}}}}'
def T551W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T551W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T551W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","DPID":"DPID_'+RANDOM_STRING+'","RequestReceivedDate":"'+week_ago+'","RequestDescription":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'"}}}}}}}'
def T561R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T561R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T561R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SWG_SPID+'","DPID":"DPID_'+RANDOM_STRING+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","RelatedRequestORID":null,"CustomerContactRequired":"1","TEServiceRequestType":"'+random.choice(D8371)+'","ExpectedDischargeRenewalDate":"'+week_ahead+'","ApplicationReceivedDate":"'+week_ago+'","ReasonForDiscontinuationOrTermination":"'+fake.paragraph(nb_sentences=1)+'","DiscontinuationOrTerminationDate":"'+week_ahead+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"AttachedApplication":{"ApplicationType":"'+random.choice(D8374)+'","ApplicantOrganisationInformation":"'+random.choice(D8375)+'","TEDischargeDescription":"'+random.choice(D8376)+'","TEMonitoringDescription":"'+random.choice(D8377)+'","VolumeAssessment":"'+random.choice(D8378)+'","AllowancesInformation":"'+random.choice(D8379)+'","VariationInformation":"'+random.choice(D8384)+'","Discontinuation":"'+random.choice(D8385)+'","Termination":"'+random.choice(D8386)+'","HealthAndSafetyConsiderations":"'+random.choice(D8380)+'","DeclarationSigned":"YES"}}}}}}}}'
def T561W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T561W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T561W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SWG_SPID+'","DPID":"DPID_'+RANDOM_STRING+'","RelatedRequestORID":null,"TEServiceRequestType":"'+random.choice(D8371)+'","ExpectedDischargeRenewalDate":"'+week_ahead+'","ApplicationReceivedDate":"'+week_ago+'","ReasonForDiscontinuationOrTermination":"'+fake.paragraph(nb_sentences=1)+'","DiscontinuationOrTerminationDate":"'+week_ahead+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","AttachedApplication":{"ApplicationType":"'+random.choice(D8374)+'","ApplicantOrganisationInformation":"'+random.choice(D8375)+'","TEDischargeDescription":"'+random.choice(D8376)+'","TEMonitoringDescription":"'+random.choice(D8377)+'","VolumeAssessment":"'+random.choice(D8378)+'","AllowancesInformation":"'+random.choice(D8379)+'","VariationInformation":"'+random.choice(D8384)+'","Discontinuation":"'+random.choice(D8385)+'","Termination":"'+random.choice(D8386)+'","HealthAndSafetyConsiderations":"'+random.choice(D8380)+'","DeclarationSigned":"YES"}}}}}}}}'
def T562R():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T562R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T562R"][0]+'",'+ rtl_postheader() + ',"Payload":{"WholesalerID":"MOSLTEST-W","DPID":"DPID_'+RANDOM_STRING+'","RetailerSystemReference":"RET_'+RANDOM_STRING+'","CustomerContactRequired":"1","RelatedRequestORID":null,"CustomerName":"MOSLTEST-W","CustomerBannerName":"MOSLTEST-W","SecondaryAddressableObject":"SEC_'+RANDOM_STRING+'","PrimaryAddressableObject":"PRI_'+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+pafaddresskey+'","VOABAReference":"'+RANDOM_STRING+'","UPRN":"'+pafaddresskey+'","TEServiceRequestType":"'+random.choice(D8371)+'","ExpectedDischargeRenewalDate":"'+week_ahead+'","ApplicationReceivedDate":"'+week_ago+'","ReasonForDiscontinuationOrTermination":"'+fake.paragraph(nb_sentences=1)+'","DiscontinuationOrTerminationDate":"'+week_ahead+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"AttachedApplication":{"ApplicationType":"'+random.choice(D8374)+'","ApplicantOrganisationInformation":"'+random.choice(D8375)+'","TEDischargeDescription":"'+random.choice(D8376)+'","TEMonitoringDescription":"'+random.choice(D8377)+'","VolumeAssessment":"'+random.choice(D8378)+'","AllowancesInformation":"'+random.choice(D8379)+'","VariationInformation":"'+random.choice(D8384)+'","Discontinuation":"'+random.choice(D8385)+'","Termination":"'+random.choice(D8386)+'","HealthAndSafetyConsiderations":"'+random.choice(D8380)+'","DeclarationSigned":"YES"}}}}}}}}'
def T562W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T562W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T562W"][0]+'",'+ wsl_postheader() + ',"Payload":{"DPID":"DPID_'+RANDOM_STRING+'","RetailerID":"MOSLTEST-R","RelatedRequestORID":null,"CustomerName":"MOSLTEST-R1","CustomerBannerName":"MOSLTEST-R2","SecondaryAddressableObject":"SEC_'+RANDOM_STRING+'","PrimaryAddressableObject":"PRI_'+RANDOM_STRING+'","AddressLine1":"'+RANDOM_ADDRESS1+'","AddressLine2":"'+RANDOM_ADDRESS2+'","AddressLine3":"'+RANDOM_ADDRESS3+'","AddressLine4":"'+RANDOM_ADDRESS4+'","AddressLine5":"'+RANDOM_ADDRESS5+'","Postcode":"'+random.choice(POSTCODES)+'","PAFAddressKey":"'+pafaddresskey+'","VOABAReference":"'+RANDOM_STRING+'","UPRN":"'+pafaddresskey+'","TEServiceRequestType":"'+random.choice(D8371)+'","ExpectedDischargeRenewalDate":"'+week_ahead+'","ApplicationReceivedDate":"'+week_ago+'","ReasonForDiscontinuationOrTermination":"'+fake.paragraph(nb_sentences=1)+'","DiscontinuationOrTerminationDate":"'+week_ahead+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","AttachedApplication":{"ApplicationType":"'+random.choice(D8374)+'","ApplicantOrganisationInformation":"'+random.choice(D8375)+'","TEDischargeDescription":"'+random.choice(D8376)+'","TEMonitoringDescription":"'+random.choice(D8377)+'","VolumeAssessment":"'+random.choice(D8378)+'","AllowancesInformation":"'+random.choice(D8379)+'","VariationInformation":"'+random.choice(D8384)+'","Discontinuation":"'+random.choice(D8385)+'","Termination":"'+random.choice(D8386)+'","HealthAndSafetyConsiderations":"'+random.choice(D8380)+'","DeclarationSigned":"YES"}}}}}}}}'
def T563W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T563W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T563W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","TEApplicationOutcome":"'+random.choice(D8382)+'","TEConsentType":"'+random.choice(D8383)+'","EffectiveFromDate":"'+week_ago+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'

def T601R_FIREFIGHTING():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"FIREFIGHTING","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference":"RET_'+ RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"Firefighting":{"TypeOfCharge": "'+random.choice(D8471)+'","FirefightingVolumetricAdjustmentReason": "'+random.choice(D8472)+'","VolumetricAdjustmentReasonAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","AdjustmentVolume": "12","CustomerSubMeterFitted": "1","BeforeEventMeterRead": "12","BeforeEventMeterReadDate": "'+week_ago+'","AfterEventMeterRead": "13","AfterEventMeterReadDate": "'+today+'"}}}}}}}}'
def T601R_LEAK():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"LEAK","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference":"RET_'+ RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"Leak":{"LeakVolumetricAdjustmentReason": "'+random.choice(D8478)+'","VolumetricAdjustmentReasonAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","LeakDetails": "'+random.choice(D8479)+'","LeakDetailsAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","SourceOfLeak": "'+random.choice(D8481)+'","LeakDischargePoint": "'+random.choice(D8482)+'","CauseOfLeak": "'+random.choice(D8483)+'","CauseOfLeakAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","AdjustmentVolume": "12","FirstMeterRead": "2","FirstMeterReadDate": "'+week_ago+'","SecondMeterRead": "4","SecondMeterReadDate": "'+today+'"}}}}}}}}'
def T601R_VOLUMEADJST():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"VOLUMEADJST","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference":"RET_'+ RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"VolumeAdjst":{"GeneralVolumetricAdjustmentType": "'+fake.paragraph(nb_sentences=1)+'","GeneralVolumetricAdjustmentTypeReason": "'+fake.paragraph(nb_sentences=1)+'","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","AdjustmentVolume": "12","BeforeEventMeterRead": "12","BeforeEventMeterReadDate": "'+week_ago+'","AfterEventMeterRead": "13","AfterEventMeterReadDate": "'+today+'"}}}}}}}}'
def T601R_NONRTSCHANGE():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"NONRTSCHANGE","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference":"RET_'+ RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"Nonrtschange":{"ReasonNoRTS": "'+random.choice(D8490)+'","VolumetricAdjustmentReasonAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","CustomerSubMeterFitted": "1","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","ReturntoSewer": "'+returntosewer+'"}}}}}}}}'
def T601R_SWAREACHANGE():
	return rtl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601R"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601R"][0]+'",'+ rtl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"SWAREACHANGE","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","CustomerContactRequired":"1","RetailerSystemReference":"RET_'+ RANDOM_STRING+'","DeclarationDate":"'+today+'","CustomerConsent":{'+CUSTOMER_BLOCK+'},"Swareachange":{"SurfaceArea":"150","SewerageSystemConnectedSitePercentage":"25","EffectiveFromDate":"'+week_ago+'","EffectiveToDate":"'+today+'"}}}}}}}}'
def T601R():
    return T601R_SWAREACHANGE()

def T601W_FIREFIGHTING():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"FIREFIGHTING","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","Firefighting":{"TypeOfCharge": "'+random.choice(D8471)+'","FirefightingVolumetricAdjustmentReason": "'+random.choice(D8472)+'","VolumetricAdjustmentReasonAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","AdjustmentVolume": "12","CustomerSubMeterFitted": "1","BeforeEventMeterRead": "12","BeforeEventMeterReadDate": "'+week_ago+'","AfterEventMeterRead": "13","AfterEventMeterReadDate": "'+today+'"}}}}}}}}'
def T601W_LEAK():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"LEAK","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","Leak":{"LeakVolumetricAdjustmentReason": "'+random.choice(D8478)+'","VolumetricAdjustmentReasonAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","LeakDetails": "'+random.choice(D8479)+'","LeakDetailsAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","SourceOfLeak": "'+random.choice(D8481)+'","LeakDischargePoint": "'+random.choice(D8482)+'","CauseOfLeak": "'+random.choice(D8483)+'","CauseOfLeakAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","AdjustmentVolume": "12","FirstMeterRead": "2","FirstMeterReadDate": "'+week_ago+'","SecondMeterRead": "4","SecondMeterReadDate": "'+today+'"}}}}}}}}'
def T601W_VOLUMEADJST():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"VOLUMEADJST","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","VolumeAdjst":{"GeneralVolumetricAdjustmentType": "'+fake.paragraph(nb_sentences=1)+'","GeneralVolumetricAdjustmentTypeReason": "'+fake.paragraph(nb_sentences=1)+'","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","AdjustmentVolume": "12","BeforeEventMeterRead": "12","BeforeEventMeterReadDate": "'+week_ago+'","AfterEventMeterRead": "13","AfterEventMeterReadDate": "'+today+'"}}}}}}}}'
def T601W_NONRTSCHANGE():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"NONRTSCHANGE","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","Nonrtschange":{"ReasonNoRTS": "'+random.choice(D8490)+'","VolumetricAdjustmentReasonAdditionalInfo": "'+fake.paragraph(nb_sentences=1)+'","CustomerSubMeterFitted": "1","EffectiveFromDate": "'+week_ago+'","EffectiveToDate": "'+today+'","ReturntoSewer": "23.3"}}}}}}}}'
def T601W_SWAREACHANGE():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T601W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T601W"][0]+'",'+ wsl_postheader() + ',"Payload":{"SPID":"'+SPID+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","MeterManufacturer":"'+METER_MNF+'","ManufacturerMeterSerialNumber":"'+METER_SER+'","VolumetricAdjustmentApplicationCategory":"SWAREACHANGE","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","EligibilityCriteriaMet":"0","ReasonForNotMeetingCriteria":"'+fake.paragraph(nb_sentences=1)+'","RelatedRequestORID":null,"AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'","DeclarationDate":"'+today+'","Swareachange":{"SurfaceArea":"150","SewerageSystemConnectedSitePercentage":"25","EffectiveFromDate":"'+week_ago+'","EffectiveToDate":"'+today+'"}}}}}}}}'
def T601W():
    return T601W_SWAREACHANGE()

def T602W():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T602W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T602W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","VolumetricAdjustmentCompleteCode":"AWARDNOAMEND","VolumetricAdjustmentAdditionalInfo":"'+fake.paragraph(nb_sentences=1)+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","VolumetricAdjustmentApplicationCategory":"'+random.choice(D8466)+'","VolumetricAdjustmentUnit":"'+random.choice(D8497)+'","VolumetricAdjustmentAwarded":"1","TariffBandAmendment":"1","AmountOfOutOfCMOSAllowance":"125","EffectiveFromDate":"'+today+'","EffectiveToDate":"'+week_ahead+'",  "VolumetricAdjustmentReviewDate":"'+week_ahead+'","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","ChargeToRetailerFlag":"1","ChargeToRetailerReason":"'+fake.paragraph(nb_sentences=1)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'

def T602W_CON_0319_AWARDNOAMEND():
	return wsl_preheader() + '"Transaction":{"'+TRANSACTIONS_XSD_NAMES["T602W"][1]+'":{"Header":{"DataTransaction":"'+TRANSACTIONS_XSD_NAMES["T602W"][0]+'",'+ wsl_postheader() + ',"Payload":{"ORID":"'+global_orid+'","VolumetricAdjustmentCompleteCode":"AWARDNOAMEND","VolumetricAdjustmentAdditionalInfo":"'+fake.paragraph(nb_sentences=1)+'","VolumetricAdjustmentRequestType":"'+random.choice(D8464)+'","VolumetricAdjustmentType":"'+random.choice(D8465)+'","VolumetricAdjustmentApplicationCategory":"'+random.choice(D8466)+'","VolumetricAdjustmentUnit":"'+random.choice(D8497)+'","VolumetricAdjustmentAwarded":"1","TariffBandAmendment":"1","AmountOfOutOfCMOSAllowance":"125","EffectiveFromDate":null,"EffectiveToDate":"'+today+'",  "VolumetricAdjustmentReviewDate":"'+week_ahead+'","AttachmentsIncluded":"0","ReasonForNoAttachments":"'+fake.paragraph(nb_sentences=1)+'","ChargeToRetailerFlag":"1","ChargeToRetailerReason":"'+fake.paragraph(nb_sentences=1)+'","AdditionalInformation":"'+fake.paragraph(nb_sentences=1)+'"}}}}}}}'

def submit_transaction(trx_name):
    #trx_name1 = eval(trx_name)()
    trx_name1 = eval(trx_name.replace('.',''))()
    
    cert_rtl = working_dir + 'BIL_DEV_MOSL_MOSLTEST-R_B2B_631.pfx'
    cert_wsl = working_dir + 'BIL_DEV_MOSL_MOSLTEST-W_B2B_632.pfx'
    cert_rtl2 = working_dir + 'BIL_DEV_MOSL_MOSLTEST2-R_B2B_418.pfx'
    cert_wsl2 = working_dir + 'BIL_DEV_MOSL_MOSLTEST2-W_B2B_419.pfx'	
    
    if 'RetailerTransaction' in trx_name1 and 'MOSLTEST-R' in trx_name1:
        req = post(vald_env, data = trx_name1, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl,  pkcs12_password = string_numbers)
    elif 'WholesalerTransaction' in trx_name1 and 'MOSLTEST-W' in trx_name1:
        req = post(vald_env, data = trx_name1, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl,  pkcs12_password = string_numbers)
    elif 'RetailerTransaction' in trx_name1 and 'MOSLTEST2-R' in trx_name1:
        req = post(vald_env, data = trx_name1, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl2,  pkcs12_password = string_numbers)		
    elif 'WholesalerTransaction' in trx_name1 and 'MOSLTEST2-W' in trx_name1:
        req = post(vald_env, data = trx_name1, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl2,  pkcs12_password = string_numbers)		
    print('Request:')
    print(trx_name1)
    print(json.dumps(json.loads(trx_name1), indent=2))   
    submit_transactions.myfile.write('Request:\n' + json.dumps(json.loads(trx_name1), indent=2)+ '\n')
    print(str(req.text))
    if 'T219.M_NotifyTransactionAccepted' in str(req.text):
        print ('Response:')
        submit_transactions.myfile.write('Response:\n' + req.text+ '\n')
        print(req.text)
    else:
        print ('Response:')
        submit_transactions.myfile.write('Response:\n' + req.text+ '\n')
        print(req.text)
    if '"ORID":' in req.text:
        orid_pos = req.text.find('"ORID":')
        global global_orid
        global_orid = req.text[690:703]
   
   #IF TESTING CONS BUSINESS RULES
    if 'CON_' in trx_name: #in req.text:
        myfile2 = open(filename2, 'w')
        myfile2.write('Request:\n' + json.dumps(json.loads(trx_name1), indent=2)+ '\n')
        myfile2.write('Response:\n' + req.text+ '\n')
        myfile2.close()	
        if 'CON-' in str(req.text):
            os.rename(filename2, working_dir + environment.upper() + '-' +trx_name+ '-' +  now1() + '.json')
        elif 'T219.M_NotifyTransactionAccepted' in str(req.text):
            os.rename(filename2, working_dir + environment.upper() + '-' +trx_name+ '-' +  now1() + '_ACCEPTED' + '.json')
        elif 'MESS-' in str(req.text):
            mess_pos = req.text.find('MESS-')
            mess_error = req.text[mess_pos:mess_pos+9]
            os.rename(filename2, working_dir + environment.upper() + '-' +trx_name+ '-' +  now1() + '_' + mess_error + '.json')
			

    ### SAVE SUBMITTING TRANSACTION TO SEPARATE FILES
    # if trx_name in SUBMITTING_TRANSACTIONS:
    #     file11 = working_dir +  global_orid + '_' + trx_name + '.json'
    #     file111 = open(file11, 'w')
    #     file111.write(json.dumps(json.loads(trx_name1), indent=2))
    #     file111.close()
    
    ### PEEK AND DEQUEUE ### PEEK AND DEQUEUE ### PEEK AND DEQUEUE 

    peek_request = get(peek_env, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl,  pkcs12_password = string_numbers)
    #IF NOTHING HAS BEEN PEEK FOR RETAILER, DO NOT ADD EMPTY PEEK TO REPONSE AND DO NOT DEQUEUE
    if '{}' not in peek_request.text:
        submit_transactions.peeked_messages += 'Peek Message:\n' + peek_request.text + '\n'
        if '<Response [200]>' in str(peek_request):
            print('Peek message:\n' + peek_request.text)
        doc_ref_num = peek_request.text[88:126]
        dequeue_body = '{"DequeueMessageRequest":{"DocumentReferenceNumber":'+doc_ref_num+'}}'
        dequeue_request = post(dequ_env, data = dequeue_body, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl,  pkcs12_password = string_numbers)
    
    peek_request1 = get(peek_env, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl,  pkcs12_password = string_numbers)
    #IF NOTHING HAS BEEN PEEK FOR WHOLESALER, DO NOT ADD EMPTY PEEK TO REPONSE AND DO NOT DEQUEUE
    if '{}' not in peek_request1.text:
        submit_transactions.peeked_messages += 'Peek Message:\n' + peek_request1.text + '\n'
        if '<Response [200]>' in str(peek_request1):
            print('Peek message:\n' + peek_request1.text)
        doc_ref_num2 = peek_request1.text[88:126]
        dequeue_body2 = '{"DequeueMessageRequest":{"DocumentReferenceNumber":'+doc_ref_num2+'}}'
        dequeue_request = post(dequ_env, data = dequeue_body2, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl,  pkcs12_password = string_numbers)
	
    ### PEEK FOR MOSLTEST2 USERS ### ### PEEK FOR MOSLTEST2 USERS ### ### PEEK FOR MOSLTEST2 USERS ###
    peek_request2 = get(peek_env, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl2,  pkcs12_password = string_numbers)
    #IF NOTHING HAS BEEN PEEK FOR RETAILER, DO NOT ADD EMPTY PEEK TO REPONSE AND DO NOT DEQUEUE
    if '{}' not in peek_request2.text:
        submit_transactions.peeked_messages += 'Peek Message:\n' + peek_request2.text + '\n'
        if '<Response [200]>' in str(peek_request2):
            print('Peek message:\n' + peek_request2.text)
        doc_ref_num = peek_request2.text[88:126]
        dequeue_body = '{"DequeueMessageRequest":{"DocumentReferenceNumber":'+doc_ref_num+'}}'
        dequeue_request = post(dequ_env, data = dequeue_body, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl2,  pkcs12_password = string_numbers)
    
    peek_request3 = get(peek_env, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl2,  pkcs12_password = string_numbers)
    #IF NOTHING HAS BEEN PEEK FOR WHOLESALER, DO NOT ADD EMPTY PEEK TO REPONSE AND DO NOT DEQUEUE
    if '{}' not in peek_request3.text:
        submit_transactions.peeked_messages += 'Peek Message:\n' + peek_request3.text + '\n'
        if '<Response [200]>' in str(peek_request3):
            print('Peek message:\n' + peek_request3.text)
        doc_ref_num2 = peek_request3.text[88:126]
        dequeue_body2 = '{"DequeueMessageRequest":{"DocumentReferenceNumber":'+doc_ref_num2+'}}'
        dequeue_request = post(dequ_env, data = dequeue_body2, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl2,  pkcs12_password = string_numbers)
    ### PEEK FOR MOSLTEST2 USERS ### ### PEEK FOR MOSLTEST2 USERS ### ### PEEK FOR MOSLTEST2 USERS ###

    ### PEEK AND DEQUEUE ### PEEK AND DEQUEUE ### PEEK AND DEQUEUE 


filename = working_dir + 'TRANSACTIONS'
filename2 = working_dir + 'TRANSACTIONS2'

def submit_transactions(trx_list):
    submit_transactions.peeked_messages = ''
    submit_transactions.myfile = open(filename, 'w')
    for trx1 in trx_list:
        submit_transaction(trx1)
        time.sleep(0.5)
    submit_transactions.myfile.write(submit_transactions.peeked_messages)   
    submit_transactions.myfile.close()
    if '[' not in global_orid:
        os.rename(filename,filename + '-' + environment.upper() +  '-' + global_orid +  '-' +  now + '.json')
    else:
        os.rename(filename,filename + '-' + environment.upper() +  '-' +  now + '.json')  

submit_transactions(transactions_list)
