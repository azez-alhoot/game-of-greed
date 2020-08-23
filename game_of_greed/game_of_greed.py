




































































































































class Banker():
    total=0
    unbanked_points=0
    def __init__(self,score):
        # self.score=int(score)
        self.score=score

    def shelf(self):
        """
        Input to shelf is the amount of points (integer) to add to shelf.
        shelf should temporarily store unbanked points.
        """
        # unbanked_points=score
        # unbanked_score=self.score
        Banker.unbanked_points=self.score
        return Banker.unbanked_points
        # pass
    # _____________________________________
    def bank(self):
        """
         should add any points on the shelf to total and reset shelf to 0.
         output should be the amount of points added to total from shelf.
        """
        # unbanked_points=Banker.shelf()
        # unbanked_points=20
        
        Banker.total+=Banker.unbanked_points
        # clear_shelf()
        
        return Banker.total

    # _____________________________________
    def clear_shelf(self):
        """
        should remove all unbanked points.
        """
        Banker.unbanked_points=0
        # pass
    



if __name__ == "__main__":
    print("_"*50)  
    test=Banker(40)
    shelf_test=test.shelf() 
    print(shelf_test) 
    print("_"*50)  
    bank_test=test.bank()
    print(Banker.total) 
    print(Banker.unbanked_points) 
    # test.clear_shelf()
    # print(Banker.total) 
    # print(Banker.unbanked_points) 
    print("_"*50)  
    test2=Banker(50)
    shelf_test2=test2.shelf() 
    bank_test2=test2.bank()
    test.clear_shelf()
    print(Banker.total) 
    print(Banker.unbanked_points) 




