
import random
from collections import Counter
class GameLogic():

    @staticmethod
    def role_dice(num):
        output = []

        for i in range(num):
            output.append(random.randint(1,6))

        return tuple(output)
    

    @staticmethod
    def calculte_score(tup):
        scoure = 0
        cou = Counter(tup)
        # print(cou)
        if cou == ({1: 1, 5: 1, 4: 1, 2: 1, 6: 1, 3: 1}):
            scoure+= 1500
            return scoure

        if len(tup)==6:
            if cou.most_common()[0][1] == 2 and cou.most_common()[1][1] == 2 and cou.most_common()[2][1] == 2:
                scoure+= 1500
                return scoure

        for i in range(1,7):
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
                    scoure +=600
                if cou[i] == 4:
                    scoure +=1200
                if cou[i] == 5:
                    scoure +=1800
                if cou[i] == 6:
                    scoure +=2400
        return scoure


class Banker():
    total=0
    unbanked_points=0
    # def __init__(self,score):
        # self.score=score

    def shelf(self,score):
        """
        Input to shelf is the amount of points (integer) to add to shelf.
        shelf should temporarily store unbanked points.
        """
        Banker.unbanked_points=score
        return Banker.unbanked_points
    # _____________________________________
    def bank(self):
        """
         should add any points on the shelf to total and reset shelf to 0.
         output should be the amount of points added to total from shelf.
        """
        
        Banker.total+=Banker.unbanked_points
        Banker.clear_shelf(self)
        return Banker.total

    # _____________________________________
    def clear_shelf(self):
        """
        should remove all unbanked points.
        """
        Banker.unbanked_points=0
    




if __name__ == "__main__":
    # print("_"*50)  
    # test=Banker(40)
    # shelf_test=test.shelf() 
    # print(shelf_test) 
    # print("_"*50)  
    # bank_test=test.bank()
    # print(Banker.total) 
    # print(Banker.unbanked_points) 
    # test.clear_shelf()
    # print(Banker.total) 
    # print(Banker.unbanked_points) 
    # print("_"*50)  
    # test2=Banker(50)
    # shelf_test2=test2.shelf() 
    # bank_test2=test2.bank()
    # test.clear_shelf()
    # print(Banker.total) 
    # print(Banker.unbanked_points) 
    # print(GameLogic.calculte_score((6,6,6)))
    print(GameLogic.calculte_score((2,2,3,3,5,5)))
    # print(GameLogic.calculte_score((1, 1)))
    # print(GameLogic.role_dice((6,5,6,3,4)))
    print(GameLogic.role_dice(6))
    



