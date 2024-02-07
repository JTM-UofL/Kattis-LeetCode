import random

class GISimple:

    def __init__(self, impSpd=(1,9), golemSpd=(3,5), headStart=5, exitPosition=50) -> None:
        self.impSpd = impSpd
        self.golemSpd = golemSpd
        self.impLoc = headStart
        self.golemLoc = 0
        self.exitPosition = exitPosition


    def __del__(self):
        pass

    def enter_values(self):
        self.impSpd = tuple(input("Please Enter the imp speed range in the following format: ( # , # )\n"))
        self.golemSpd = tuple(input("Please Enter the golem speed range in the following format: ( # , # )\n"))
        self.impLoc = int(input("Please enter the head start value (int)\n"))
        self.exitPosition = int(input("Please enter the exit position value (int)\n"))

    def take_step(self):
        self.golemLoc += random.randint(self.golemSpd[0], self.golemSpd[1])
        self.impLoc += random.randint(self.impSpd[0], self.impSpd[1])
        
    def play_game(self):

        if self.exitPosition < 1: 
            print("Please Enter a Valid Tunnel Length!\n")
            exit()

        while (self.impLoc < self.exitPosition and self.golemLoc < self.impLoc):
            self.take_step()

        if self.impLoc > self.golemLoc: 
            return True
        else:  
            return False

my_game_instance = GISimple()

if input("Enter 1 to customize settings:\n") == '1':
    my_game_instance.enter_values()
    print(my_game_instance.play_game())
else:
    print(my_game_instance.play_game())