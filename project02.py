import random
from pygame import mixer
mixer.init()

class game:
    def __init__(self):                        
        print("_______________Gauss the SU____________")
        print("\n\nGauss the number between 1 to 10\n\n")
    def mode(self):
        c=input("Enter the mood\n users(u), bot(b), single(s)= ")
        if(c=='u'):
            return 0
        elif(c=='b'):
            return 1
        else:
            return 2
    def ran(self):
        r=random.randint(1,10)
        return r
        
    def user1(self,co):
        self.co=co
        a=int(input("Player1= "))
        if self.co==0:
            b=int(input("Player2= "))
        else:
            b=random.randint(1,10)
        return [a,b]
    
    def pro(self,LAN,cat):
        self.LAN=LAN
        self.cat=cat
        if(self.LAN[0]>self.cat):
            op=self.LAN[0]-self.cat
        else:
            op=self.cat-self.LAN[0]
        if(self.LAN[1]>self.cat):
            op1=self.LAN[1]-self.cat
        else:
            op1=self.cat-self.LAN[1]
        print("************************")
        print(f"\n\nNUMBER= {self.cat}")
        print(f"Player 2= {self.LAN[1]}")
        

        if op<op1:
            print('Player 1 Win')
        else:
            print('Player 2 Win')
        ret=input("\n\n RETRY-- ")
        if ret=='r':
            return True
        else:
            return False

    
    def sing(self,rand):
        
        self.rand=rand
        i=3 
        k=True
        while i>0: 
            print("<^>"*i )
            Y=int(input("Entre your NUM:- "))
            if Y>self.rand:
                print("You are away from him")
            elif Y<self.rand:
                print("You are behind him")
            else:
                print("\n\nComputer= ",self.rand)
                print("BINGO YOU WON ^-^")
                k=False
                break
            i-=1
        if k:
            print("\n\nComputer= ",self.rand)
            print("You lost")
        ret=input("\n\n RETRY-- ")
        if ret=='r':
            return True
        else:
            return False

         



c1=game()
mixer.music.load('C:\\Users\\Acer\\Downloads\\futuristic-beat-146661.mp3')
mixer.music.play()
c=c1.mode()
re=True
while re:
    ranNum=c1.ran()
    if (c==0 or c==1):
        LAN=c1.user1(c)
        re=c1.pro(LAN,ranNum)
    else:
        re=c1.sing(ranNum)
mixer.music.stop()

