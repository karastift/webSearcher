import functions
import argparse

def main():
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

    parser = argparse.ArgumentParser(description='check urls.')

    parser.add_argument('amount', metavar='amount', type=int,
                    help='an integer for the amount of domains to be checked')

    parser.add_argument('request', metavar='request', type=str,
                    help='a string that that says http:// or https://')
    
    parser.add_argument('topleveldomain', metavar='topleveldomain', type=str,
                    help='a string that that indicates the toplevelodomain: .com / .us ...')

    args = parser.parse_args()
    amount = args.amount
    request = args.request
    topleveldomain = args.topleveldomain

    fun = functions.Functions()

    if fun.validateArgs(amount, request, topleveldomain) == False:
        r = request
        t = topleveldomain
        a = amount
        for i in range(1, a+1, 1):
            print(f'{OKBLUE}{i}')
            url = fun.generateUrl(r, t)
            try:
                request = fun.requestContent(url)
                parser = fun.parseContent(request)
                fun.writeToFile(parser)
                print(f'{OKCYAN}{url[0]}')
            except:
                print(f'{FAIL}{url[0]}')
        print(f'{ENDC}finished checking {a} domains.')

if __name__ == '__main__':
    main()