from pywinauto import application
import schedule
import time
import random
from datetime import datetime, timedelta

now = datetime.now()
add_seconds = 3
soon = (now + timedelta(seconds=add_seconds)).strftime("%H:%M:%S")
email_subject = 'HVI TEST 3.0.8 report'

#soon1 = soon.strftime("%H:%M:%S")

def job():

    app = application.Application()
    #Process ID of outlook, can be found in Task Manager / Details
    app = app.connect(process=4192)
    #print([w.window_text() for w in app.windows()])
    new_email = app.window(title = email_subject + ' - Message (HTML) ', found_index = 0)
    new_email.move_window(x=190, y=110, width=1200, height=720, repaint=True)
    new_email.set_focus()
    #new_email.To.send_keys("tomasz.skoczylas@cgi1.com")
    new_email.Send.click()
    #new_email.print_control_identifiers()
    time.sleep(1)
    return schedule.CancelJob

# def job2():
#     app = application.Application()
#     cmd = app.connect(process=13376)
#     cmd_window =  cmd.window(title = email_subject + ' - Message (HTML) ', found_index = 0)

schedule.every().day.at("16:30:00").do(job)
#schedule.every().day.at("16:35:00").do(job2)
#schedule.every().day.at(soon).do(job)

while True:
    schedule.run_pending()
    time.sleep(2)
    if not schedule.jobs:
        break