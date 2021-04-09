import requests
import sys
from bs4 import BeautifulSoup  #html passer

api_url = "https://www.signupgenius.com/go/copvaccination4-17"

def retrieveData(api_url):
    try:
        response = requests.get(api_url)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)
        exit(1)

    #the whole html of website
    html = response.content

    # print(html)

    #initialize bsoup html parser
    soup = BeautifulSoup(html, 'html.parser')

    containerhtml = soup.findChild('div', class_='mainbody').findChild('div', class_='container')
    print(containerhtml)

    signupValidStr = containerhtml.find('h1')
    # print(signupValidStr)

    slotAvailability = containerhtml.find('h1')
    # print(slotAvailability)

    #if the signupgenius website no longer exists
    if "The Sign Up Was Not Found" in signupValidStr:
        return False

    #if the website has available spots for covid vaccine sign up
    if "NO SLOTS AVAILABLE. SIGN UP IS FULL." in slotAvailability:
        return False

    return True

ableToSignUp = retrieveData(api_url)
print(ableToSignUp)