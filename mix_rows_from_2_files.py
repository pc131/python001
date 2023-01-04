# combine 2 files, mix rows:

# 1 D4025 Wholesaler ID
# 2 D8186 Retailer System Reference
# 3 D2028 Developer/Business Name
# 11 'MOSLTEST-W',
# 12 'REF123',
# 13 'HOT WATERS',

#as

# 1 D4025 Wholesaler ID
# 11 'MOSLTEST-W',
# 2 D8186 Retailer System Reference
# 12 'REF123',
# 3 D2028 Developer/Business Name
# 13 'HOT WATERS',


working_dir = "C:\\Users\\tomasz.skoczylas\\Downloads\\11\\TEST_CASES\\"
file1 = working_dir + "file1.txt"
file2 = working_dir + "file2.txt"
file3 = working_dir + "file3.txt"

with open(file1) as xh:
  with open(file2) as yh:
    with open(file3,"w") as zh:
        #Read first file
        xlines = xh.readlines()
        #Read second file
        ylines = yh.readlines()
        #Combine content of both lists
        #combine = list(zip(ylines,xlines))
        #Write to third file
        for i in range(len(xlines)):
            line = xlines[i].strip() + '\n' + ylines[i]
            zh.write(line)