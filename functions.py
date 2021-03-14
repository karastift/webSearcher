import requests as re
import random as ra
from bs4 import BeautifulSoup

class Functions():
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

    def validateArgs(self, amount, request, topleveldomain):
        failed = False
        if  isinstance(amount, int) != True:
            print(f'{self.FAIL}First argument has to be an integer!')
            failed = True
        if request != 'http://' and request != 'https://':
            print(f'{self.FAIL}Second argument has to be \'http://\' or \'https://\'! It was \'{request}\'.')
            failed = True
        if topleveldomain[0] != '.':
            print(f'{self.FAIL}Third argument has to have the \'.\' before your topleveldomain!')
            failed = True
        if failed:
            return True
        else:
            return False

    def generateUrl(self, request, topleveldomain):
        numbers = []
        numbers.append(str(ra.randint(0,9999)))
        url = str(request) + (''.join(numbers)) + str(topleveldomain)
        info = []
        info.append(url)
        url = ''
        return info

    def requestContent(self, info):
        r = re.get(info[0])
        info.append(r.content)
        return info

    def parseContent(self, info):
        soup = BeautifulSoup(info[1], 'html.parser')
        info.append(soup.title.string)
        return info

    def writeToFile(self, info):
        if ('sale' in info[2]) == True:
                f.write((info[0] + ' [SALE] \n'))
        elif ('Forbidden' in info[2]) == True:
            with open('output.txt', 'a') as f:
                f.write((info[0] + ' [FORBIDDEN] \n'))
        else:
            with open('output.txt', 'a') as f:
                f.write((info[0] + ' --> '))
                f.write((info[2] + '\n'))
        f.close()