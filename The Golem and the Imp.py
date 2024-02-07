import random

class TunnelGame:

    def __init__(self, imp_start=5, golem_start=0) -> None:
        self.imp_loc = imp_start
        self.golem_loc = golem_start
        self.tunnel = ['-' for x in range(0,50)]
        self.tunnel.append("X")
        self.tunnel[self.golem_loc] = 'G'
        self.tunnel[self.imp_loc] = 'I'
        self.winner = ''
        self.seconds = 0

    
    def __del__(self):
        pass

    def print_tunnel(self): 
        print(f"{''.join(x for x in self.tunnel)}\t\t{self.seconds}S")

    def take_step(self):
        self.seconds += 1
        self.tunnel[self.golem_loc] = '-'
        self.tunnel[self.imp_loc] = '-'
        self.golem_loc += random.randint(3, 5)
        self.imp_loc += random.randint(1, 9)

        if self.golem_loc >= self.imp_loc:
            self.winner = 'GOLEM'
        elif self.imp_loc >= 50:
            self.winner = 'IMP'
        else:
            self.tunnel[self.golem_loc] = 'G'
            self.tunnel[self.imp_loc] = 'I'

        
    def play_game(self):
        while (self.winner == ''):
            self.print_tunnel()
            self.take_step()
        if self.winner == 'IMP':
            print(f"THE IMP HAS ESCAPED TO FREEDOM AFTER {self.seconds} SECONDS.  MISCHIEF AND TRICKERY AWAIT!")
        else:
            print(f"SADLY, IT'S BACK TO THE TOWER FOR THE IMP AFTER A {self.seconds} SECOND-CHASE.")

my_game_instance = TunnelGame()

my_game_instance.play_game()