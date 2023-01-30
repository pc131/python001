from requests_pkcs12 import get, post

environment = 'asr'
random_numbers = [86,97,53,53,49,108,49,107,49]

cert_rtl = 'C:/Users/cgi/Desktop/_downloads/BIL_DEV_MOSL_MOSLTEST-R_B2B_412.pfx'
cert_wsl = 'C:/Users/cgi/Desktop/_downloads/BIL_DEV_MOSL_MOSLTEST-W_B2B_411.pfx'

match environment:
    case 'asr':
        vald_env = 'https://moservicesdev.mosl.co.uk/assurance/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/assurance/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/assurance/notification/hvi/dequeue'
    case 'tst':
        vald_env = 'https://moservicesdev.mosl.co.uk/test/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/test/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/test/notification/hvi/dequeue'
    case 'uat':
        vald_env = 'https://moservicesdev.mosl.co.uk/uat/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/uat/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/uat/notification/hvi/dequeue'
    case 'ppr':
        vald_env = 'https://moservicesdev.mosl.co.uk/preprod/validation/hvi/servicerequest'
        peek_env = 'https://moservicesdev.mosl.co.uk/preprod/notification/hvi/peek'
        dequ_env = 'https://moservicesdev.mosl.co.uk/preprod/notification/hvi/dequeue'

string_numbers = ''.join(chr(i) for i in random_numbers)

def peek_rtl():
    peek_request = get(peek_env, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl,  pkcs12_password = string_numbers)
    doc_ref_num = peek_request.text[88:126]
    dequeue_body = '{"DequeueMessageRequest":{"DocumentReferenceNumber":'+doc_ref_num+'}}'
    dequeue_request = post(dequ_env, data = dequeue_body, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_rtl,  pkcs12_password = string_numbers)
    return peek_request.text

def peek_wsl():
    peek_request1 = get(peek_env, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl,  pkcs12_password = string_numbers)
    doc_ref_num = peek_request1.text[88:126]
    dequeue_body = '{"DequeueMessageRequest":{"DocumentReferenceNumber":'+doc_ref_num+'}}'
    dequeue_request = post(dequ_env, data = dequeue_body, headers = {'Content-Type': 'application/json'}, pkcs12_filename = cert_wsl,  pkcs12_password = string_numbers)
    return peek_request1.text

# rtl_ntf = peek_rtl()
# print(rtl_ntf)
# while '{}' not in rtl_ntf:
#     peek_rtl()
#     print(rtl_ntf)

wsl_ntf = peek_wsl()
print()
if '{}' not in wsl_ntf:
    wsl_ntf_not_empty = 1
    print(wsl_ntf)
else:
    wsl_ntf_not_empty = 0
while wsl_ntf_not_empty == 1:
    peek_wsl()
    print(wsl_ntf)
    if '{}' in wsl_ntf:
        wsl_ntf_not_empty = 0