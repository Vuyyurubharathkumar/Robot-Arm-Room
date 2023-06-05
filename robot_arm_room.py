import random

class robo():
    def __init__(self,room1,room2,room3,robo_arm,robot):
        self.room1 = room1
        self.room2 = room2
        self.room3 = room3
        self.robo_arm = robo_arm
        self.robot = robot

    def initial_state(self):
        self.room3 = self.robot 
        while self.room3 == self.robot:
            print("")
            print("the robo is in room3 and has empty hand")
            break
        self.room1 = ['ball_1','ball_2','ball_3']
        self.room2 = ['ball_4','ball_5']
        self.robo_arm = 0
        print("------------------------------------------------------------")


    def robo_action(self):
        self.robo_arm = 0
        if self.robo_arm == 0:
            if len(self.room1) == 0 and len(self.room2) == 0:
                print("Both room1 and room2 are empty.")
                return
            if len(self.room1) == 0:
                choose = random.choice(self.room2)
                room_choice = 'room2'
            elif len(self.room2) == 0:
                choose = random.choice(self.room1)
                room_choice = 'room1'
            else:
                choose = random.choice([self.room1, self.room2]) #select the contents of "self"
                room_choice = 'room1' if choose == self.room1 else 'room2'
                choose = random.choice(choose)
                
            print("robo went to ",room_choice)
            print("robo picked ",choose)
            print(f"robo dropped {choose} in room_3")
            print("------------------------------------------------------------")
            if room_choice == 'room1':
                self.room1.remove(choose)
            else:
                self.room2.remove(choose)
            

action = robo(3,2,1,0,1)
action.initial_state()
action.robo_action()

while len(action.room1) > 0 or len(action.room2) > 0:
    action.robo_action()

print("All the balls are in room3.")
