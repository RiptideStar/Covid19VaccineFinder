import os
import sqlite3
from sendEmailToUser import emailToUser

url = 'https://www.signupgenius.com/go/copvaccination4-17'
# url = 'https://www.signupgenius.com/go/copvaccination4-18'


def retrieve_data(api_url):
    # os.system(f'curl -s {api_url} > tempSite.html')
    os.system('curl -s '+api_url+' > tempSite.html')

    stream = os.popen('wc -l tempSite.html')
    output = stream.readlines()
    length = output[0].split()[0]
    print("length",length)
    if length == "0":
        return False
    print("here")    
    stream = os.popen('grep "NO SLOTS AVAILABLE. SIGN UP IS FULL." tempSite.html')
    output = stream.readlines()

    print("output:", len(output))
    if (len(output) == 0):
        return True
    # else:
    return False
    

found = retrieve_data(url)


def queryFromDataBase(db_name):
    # init_db(name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    emailList = []
    sql = '''
        Select email from Users
        '''
    cur.execute(sql)    
    emailList = cur.fetchall()
    conn.commit()
    cur.close
    conn.close()
    return emailList  


#query emails from database and have a list for all emails
email_tuples = queryFromDataBase('covid19siteDB.db')
print("tuples", email_tuples)

email_list = []
for tuple in email_tuples:
    email_list.append(tuple[0])
print("lists:", email_list)

emailToUser(email_list, url)

if (found):
    #send emails to everyone from querying email database
    print("COVID VACCINE AVAILABLE")



