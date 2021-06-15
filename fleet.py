from robot import Robot

class Fleet:
    def __init__(self,):
        self.robots = []
        self.create_robots()



    def create_robots(self):
        aida = Robot("Aida")
        robo_cop = Robot("Robo Cop")
        iron_man = Robot("Iron Man")
        self.robots.append(aida, robo_cop, iron_man)