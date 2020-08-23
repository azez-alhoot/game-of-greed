import random
from collections import Counter
class GameLogic():

    @staticmethod
    def calculte_score(tup):
        scoure = 0
        cou = Counter(tup)
        if cou.most_common()[0] == (1,1):
            scoure+= 1500
            return scoure

        if cou.most_common()[0][1] == 2 and cou.most_common()[1][1] == 2 and cou.most_common()[2][1] == 2:
            scoure+= 750
            return scoure
        for i in range(1,len(tup)+1,1):
            if i == 1:
                if cou[i] == 1:
                    scoure+=100
                if cou[i] == 2:
                    scoure+=200
                if cou[i] == 3:
                    scoure +=1000
                if cou[i] == 4:
                    scoure +=2000
                if cou[i] == 5:
                    scoure +=3000
                if cou[i] == 6:
                    scoure +=4000
            if i == 2:
                if cou[i] == 1:
                    scoure +=0
                if cou[i] == 2:
                    scoure +=0
                if cou[i] == 3:
                    scoure +=200
                if cou[i] == 4:
                    scoure +=400
                if cou[i] == 5:
                    scoure +=600
                if cou[i] == 6:
                    scoure +=800
            if i == 3:
                if cou[i] == 1:
                    scoure +=0
                if cou[i] == 2:
                    scoure +=0
                if cou[i] == 3:
                    scoure +=300
                if cou[i] == 4:
                    scoure +=600
                if cou[i] == 5:
                    scoure +=900
                if cou[i] == 6:
                    scoure +=1200
            if i == 4:
                if cou[i] == 1:
                    scoure +=0
                if cou[i] == 2:
                    scoure +=0
                if cou[i] == 3:
                    scoure +=400
                if cou[i] == 4:
                    scoure +=800
                if cou[i] == 5:
                    scoure +=1200
                if cou[i] == 6:
                    scoure +=1600
            if i == 5:
                if cou[i] == 1:
                    scoure +=50
                if cou[i] == 2:
                    scoure +=100
                if cou[i] == 3:
                    scoure +=500
                if cou[i] == 4:
                    scoure +=1000
                if cou[i] == 5:
                    scoure +=1500
                if cou[i] == 6:
                    scoure +=2000
            if i == 6:
                if cou[i] == 1:
                    scoure +=0
                if cou[i] == 2:
                    scoure +=0
                if cou[i] == 3:
                    scoure +=300
                if cou[i] == 4:
                    scoure +=1200
                if cou[i] == 5:
                    scoure +=1800
                if cou[i] == 6:
                    scoure +=2400

        return scoure
    def roll_dice():
        pass

num =[]
for i in range(1,7):
    num.append(i)

print(GameLogic.calculte_score((2,2,4,5,4,5)))