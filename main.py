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
    


def checker(che):
    if che == 'Y':
        che = True
    elif che == 'N':
        che == False
    else:
        print("re enter :not valid")

def main():
    p_lenth = input("password lenth:")
    p_lenth = int(p_lenth)

    p_smp = input("do you need to add simple letter? (Y=yes/N=no)")
    checker(p_smp)

    p_cap = input("do you need to add capitel letter? (Y=yes/N=no)")
    checker(p_cap)

    p_num = input("do you need to add numbers? (Y=yes/N=no)")
    checker(p_num)

    p_sym = input("do you need to add symbols? (Y=yes/N=no)")
    checker(p_sym)

    psw = Psw_kick(p_lenth, p_smp, p_cap, p_num, p_sym)

    log = psw.shuffle_psw()
    print(log)



if __name__ == "__main__":
    main()
