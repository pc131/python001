script_path = 'C:\\Users\\tomasz.skoczylas\\Downloads\\11\\'
ORID = '2000027636C01'
filename = 'YORKSIRE-R_peeked_notifications.json'
f1_file = script_path + filename
f1_file_no_ext = f1_file.replace('.json', '')
f1 = open(f1_file, 'r')
f1_content= f1.read()
peeked_msgs_start = f1_content.find('Peek Message:')
peeked_notifications = f1_content[peeked_msgs_start:]
number_of_peeked_messages = peeked_notifications.count('Peek Message:')

f1.close()

f2_file = f1_file_no_ext + '_FILTERED' + '.json'
f2 = open(f2_file, 'w')

index_start = 1
index_end = peeked_notifications.find('\nPeek Message:') + 2 # start of "Peek Message:" string which is preceded by "}}"

peeked_notification = peeked_notifications[index_start-1:index_end-1]
correct_notifications = ''

for i in range(number_of_peeked_messages-1):
    # print(i)

    peeked_notification = peeked_notifications[index_start-1:index_end-1]

    if(ORID in peeked_notification):
        correct_notifications = correct_notifications + peeked_notification

    index_start = index_end
    
    if(i == number_of_peeked_messages-2):
        index_end = peeked_notifications.find('  }', index_start) + 2 # look for last message
        peeked_notification = peeked_notifications[index_start-1:]
        if(ORID in peeked_notification):
            correct_notifications = correct_notifications + peeked_notification

    else:
       index_end = peeked_notifications.find('\nPeek Message:', index_start) + 2 # start of "Peek Message:" string which is preceded by "}"

#print('ORID: "' + ORID + '" found ' + str(correct_notifications.count('Peek Message:')) + ' times in peeked messages in source file: "'+ f1_file + '"\nResults saved in output file: "' + f2_file +'"')
print('ORID: "' + ORID + '" found ' + str(correct_notifications.count('Peek Message:')) + ' times in peeked messages in source file: "'+ f1_file.replace(script_path,'') + '"\nResults saved in output file: "' + f2_file.replace(script_path,'')  +'"')

f2.write(correct_notifications)
f2.close