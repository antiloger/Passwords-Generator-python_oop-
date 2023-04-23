import argparse
import random

char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char_cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
symbl = ['!','@','#','$','%','&','*','?']

class Psw_kick():

    def __init__(self, psw_lenth, psw_smp=True, psw_cap=True, psw_num=True, psw_smbl=True):
        self.psw_smp = psw_smp
        self.psw_lenth = psw_lenth
        self.psw_cap = psw_cap
        self.psw_num = psw_num
        self.psw_smbl = psw_smbl

    def char_gen(self):
        para = ['self.psw_smp','self.psw_cap', 'self.psw_num', 'self.psw_smbl']
        req_psw = []
        for i in para:
            org_value = eval(i)
            if org_value:
                if i == 'self.psw_smp':
                    req_psw.append("char")
                if i == 'self.psw_smbl':
                    req_psw.append("symbl")
                if i == 'self.psw_cap':
                    req_psw.append("char_cap")
                if i == 'self.psw_num':
                    req_psw.append("num")
                

        raw_psw = []

        for n in range(self.psw_lenth):
            for k in req_psw:
                raw_psw.append(random.choice(globals()[k]))
                if len(raw_psw) == self.psw_lenth:
                    break

            if len(raw_psw) == self.psw_lenth:
                break

        #print("raw_psw :", raw_psw)
        return raw_psw
    

    def shuffle_psw(self):
       raw_psw = self.char_gen()
       random.shuffle(raw_psw)
       org_psw = raw_psw
       orgPsw = "".join(orgPsw)
       return org_psw
    

        

def main():
    # set up command line argument parser
    parser = argparse.ArgumentParser(description="Generate a password with specified parameters.")
    parser.add_argument('length', type=int, help="length of password")
    parser.add_argument('-s', '--simple', action='store_true', help="include simple characters")
    parser.add_argument('-c', '--capital', action='store_true', help="include capital letters")
    parser.add_argument('-n', '--number', action='store_true', help="include numbers")
    parser.add_argument('-b', '--symbol', action='store_true', help="include symbols")
    args = parser.parse_args()

    # generate password with specified parameters
    psw = Psw_kick(args.length, args.simple, args.capital, args.number, args.symbol)
    log = psw.shuffle_psw()
    print(psw.__str__(log))

if __name__ == "__main__":
    main()
