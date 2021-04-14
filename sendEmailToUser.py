# import smtplib, ssl
import smtplib

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


gmail_user, gmail_password = read_creds()

sent_from = gmail_user


def emailToUser(email_list, url):
    api_url = url

    to = email_list
    subject = 'COVID Vaccine Appointments are Available!'
    body = '''\n There is an opening slot available for you for the covid vaccine.\n\n Check out '''+ url + '''
    \n\n Best of wishes for you, thanks for using our covid vaccine app! 
    \n- KZhang Apps
    \n\n Unregister at https://cutt.ly/myshot
    '''
    
    message = 'Subject: {}\n\n{}'.format(subject, body)

    # try:
    port = 465
    server = smtplib.SMTP_SSL('smtp.gmail.com', port)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message)
    server.close()

    # print ('Email sent!')
    # except:
    #     print ('Something went wrong...')