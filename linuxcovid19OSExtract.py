import os

url = 'https://www.signupgenius.com/go/copvaccination4-17'
# url = 'https://www.signupgenius.com/go/copvaccination4-17'


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
print("Found?", found)