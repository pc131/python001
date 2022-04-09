
import shutil
import os

mylist = os.listdir("C:\\Users\\tomasz.skoczylas\\Downloads\\11\\files")
working_dir = 'C:\\Users\\tomasz.skoczylas\\Downloads\\11\\'

test_cases_folder = working_dir + 'HTML_URLS'

if not os.path.exists(test_cases_folder):
    os.makedirs(test_cases_folder)

urls_for_uat_env = test_cases_folder + '\\TESTCASES_URLS_UAT.html'
urls_for_test_env = test_cases_folder + '\\TESTCASES_URLS_TEST.html'
trx_file_uat = test_cases_folder + '\\trx_uat.txt'
trx_file_test = test_cases_folder + '\\trx_test.txt'


urls_uat_file = open(urls_for_uat_env, 'w')
urls_test_file = open(urls_for_test_env, 'w')
trx_uat_file = open(trx_file_uat, 'w')
trx_test_file = open(trx_file_test, 'w')

urls_uat_file.write('<html>\n<head>\n</head>\n<body>\n')
urls_uat_file.write('<a href=\"https://bilateralhubtestharness-dev-as.azurewebsites.net/api/ExecuteTestCase?code=NbXUVu704AnFSJTiV1JYZ6gq7YCWBqJDxh//C0x/NBAUMnLGWN5uGg==&filename=_TEMP/T207RW_MOSLTEST_MOSLTEST2.xlsx&format=JSON\" target=\"_blank\">T207RW_MOSLTEST_MOSLTEST2</a><br><br>\n')
for x in range(0, len(mylist)):
    print(mylist[x][:-5])
    trx_uat_file.write(mylist[x][:-5] + '\t\n')
    urls_uat_file.write('<a href=\"https://bilateralhubtestharness-dev-as.azurewebsites.net/api/ExecuteTestCase?code=NbXUVu704AnFSJTiV1JYZ6gq7YCWBqJDxh//C0x/NBAUMnLGWN5uGg==&filename=TEST_SUITE_NAME/' +  mylist[x]  + '&format=JSON\">' + mylist[x][:-5]  + '</a><br><br>\n')
urls_uat_file.write('</body>\n<html>') 
urls_uat_file.close()

urls_test_file.write('<html>\n<head>\n</head>\n<body>\n')
urls_test_file.write('<a href=\"https://bilateralhubtestharness-dev-as.azurewebsites.net/api/ExecuteTestCase?code=NbXUVu704AnFSJTiV1JYZ6gq7YCWBqJDxh//C0x/NBAUMnLGWN5uGg==&filename=_TEMP/T207RW_MOSLTEST_MOSLTEST2.xlsx&format=JSON&environment=TEST\" target=\"_blank\">T207RW_MOSLTEST_MOSLTEST2</a><br><br>\n')
for x in range(0, len(mylist)):
    print(mylist[x][:-5])
    trx_test_file.write(mylist[x][:-5] + '\t\n')
    urls_test_file.write('<a href=\"https://bilateralhubtestharness-dev-as.azurewebsites.net/api/ExecuteTestCase?code=NbXUVu704AnFSJTiV1JYZ6gq7YCWBqJDxh//C0x/NBAUMnLGWN5uGg==&filename=TEST_SUITE_NAME/' +  mylist[x]  + '&format=JSON&environment=TEST\">' + mylist[x][:-5]  + '</a><br><br>\n')
urls_test_file.write('</body>\n<html>') 
urls_uat_file.close()