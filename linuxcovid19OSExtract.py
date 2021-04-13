import os
import sqlite3
from sendEmailToUser import emailToUser
import datetime
from signup import queryFromDataBase

url = 'https://www.signupgenius.com/go/copvaccination4-17'
# url = 'https://www.signupgenius.com/go/4-16pfizermhcc'
# url = 'https://www.signupgenius.com/go/copvaccination4-18'


def retrieve_data(api_url):
    # os.system(f'curl -s {api_url} > tempSite.html')
    os.system('curl -s '+api_url+' > tempSite.html')

    stream = os.popen('wc -l tempSite.html')
    output = stream.readlines()
    length = output[0].split()[0]
    # print("length",length)
    if length == "0":
        return False
    # print("here")    
    stream = os.popen('grep "NO SLOTS AVAILABLE. SIGN UP IS FULL." tempSite.html')
    output = stream.readlines()

    # print("output:", len(output))
    if (len(output) == 0):
        return True
    # else:
    return False


def saveOpeningToDataBase(opening, db_name, url):
    # init_db(name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    # print(data[index])
    # print(opening, url)
    sql = '''
        update Sites 
        set openings = ?
        where url = ?;
        '''
    try:    
        cur.execute(sql, (opening, url,))
    except sqlite3.Error as e:
        print(e)
        return False
    conn.commit()
    cur.close
    conn.close()
    return True

def query_emails_on_url(db_name, url):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    sql = "select emails from Sites where url=?;"
    try:    
        cur.execute(sql, (url,))
    except sqlite3.Error as e:
        print(e)
        return
    emails = cur.fetchall()
    return emails


def check_availability_send_email(db_name):
    urls = queryFromDataBase(db_name, "select url from Sites")    
    there_an_opening = False

    date = datetime.datetime.now()
    for url in urls:
        found = retrieve_data(url[0])
        emails = query_emails_on_url(db_name, url[0])
        emails_list = emails[0][0].split(",")
        emailToUser(emails_list, url[0])
        print("Emails sent:", emails_list)
        if (found):
            # add "Yes" to openings
            there_an_opening = True
            saveOpeningToDataBase("Yes", db_name, url[0])
            emails = query_emails_on_url(db_name, url[0])
            emails_list = emails[0][0].split(",")
            emailToUser(emails_list, url[0])
            

            #LOGGING
            print(date, ": COVID VACCINE AVAILABLE on", url[0])
            print("Emails sent:", emails_list)

        else:
            saveOpeningToDataBase("No", db_name, url[0])

            #LOGGING
            print(date, ": COVID VACCINE NOT AVAILABLE on", url[0])

    return there_an_opening            
            

# check the websites
found = check_availability_send_email("covid19siteDB.db")


# if (found):
#     print(date, ": COVID VACCINE AVAILABLE")
#     #send emails to everyone from querying email database
#     #query emails from database and have a list for all emails
#     email_tuples = queryEmailFromDataBase('covid19siteDB.db')
#     # print("tuples", email_tuples)

#     email_list = []
#     for tuple in email_tuples:
#         email_list.append(tuple[0])
#     print("Email list:", email_list)

#     emailToUser(email_list, url)
# else:
#     print(date, ": COVID VACCINE NOT AVAILABLE")

