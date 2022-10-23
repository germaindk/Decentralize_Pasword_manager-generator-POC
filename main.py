import random
import string




MasterPassword = str(input('your master password:'))
WebSite = str(input('The site:'))

random.seed(MasterPassword + WebSite)

#gen password
def gen_password():
    password = ''
    for i in range(18):
        password += random.choice(string.ascii_letters+ string.digits+ string.punctuation)
    return password
print(gen_password())

