from fleet import Fleet
from herd import Herd
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def Run_Battle(self):
        print("Welcome")
        print("heres the robots " + self.fleet.robots[0].name + self.fleet.robots[1].name + self.fleet.robots[2].name  )
    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass


