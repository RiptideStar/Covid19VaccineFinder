# import smtplib, ssl

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw

import smtplib

gmail_user, gmail_password = read_creds()

sent_from = gmail_user

to = ['mkz100@gmail.com', 'mkz100@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what\'s up?\n\n- KZhang Apps'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

# try:
port = 465
server = smtplib.SMTP_SSL('smtp.gmail.com', port)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()

print ('Email sent!')
# except:
#     print ('Something went wrong...')