



class TRobot:
    def __init__(self,x=0,y=0,direction='NORTH'):
        self.x = x
        self.y = y
        self.direction = direction
        self.compass = ['NORTH','EAST','SOUTH','WEST']


    def place(self,x,y,direction):
        #user chooses a starting position on the table
        if x>-1 and x<=4 and y>-1 and x<=4 and direction in self.compass:
            self.x = x
            self.y = y
            self.direction = direction
            return True
        else:
            print('Position is not available')
            return False

    def move(self):
        #the robot moves one unit in a direction it is facing
        if self.direction == 'NORTH' and self.y<4:
            self.y+=1

        elif self.direction == 'SOUTH' and self.y>0:
            self.y-=1
        
        elif self.direction =='WEST' and self.x<4:
            self.x+=1

        elif self.direction =='EAST' and self.x>0:
            self.x-=1


    def right(self):
        #turn the robot 90° to right
        if self.direction == 'NORTH':
            self.direction =='EAST'
        elif self.direction == 'EAST':
            self.direction =='SOUTH'
        elif self.direction =='SOUTH':
            self.direction =='EAST'
        elif self.direction == 'EAST':
            self.direction =='NORTH'

    def left(self):
        #turn the robot 90° to left
        if self.direction =='NORTH':
            self.direction == 'EAST'
        elif self.direction =='EAST':
            self.direction =='SOUTH'
        elif self.direction =='SOUTH':
            self.direction =='WEST'
        elif self.direction =='WEST':
            self.direction =='NORTH'

    def report(self):
        #robot return it's current position and direction to the user
        return f'{self.x},{self.y},{self.direction}'


class TRobotSimulator:
    def __init__(self):
        self.robot=TRobot()

    def exec_a_command(self,command):
        
        
        if command.startswith('PLACE'):
            args = command.split()[1].split(',')
            x,y,direction = int(args[0]),int(args[1]),args[2]
            spot = self.robot.place(x,y,direction)
            return spot

        elif command =='MOVE':
            self.robot.move()
        elif command=='LEFT':
            self.robot.left()
        elif command =='RIGHT':
            self.robot.right()
        elif command =='REPORT':
            self.robot.report()

    def exec_commands(self,commands):
        for command in commands:
            to_do = self.exec_a_command(command)
            if to_do != None:
                print(to_do)


simulator = TRobotSimulator()
simulator.exec_commands(['PLACE 0,0,NORTH','MOVE','REPORT'])

simulator.exec_commands(['PLACE 6,0,NORTH'])

