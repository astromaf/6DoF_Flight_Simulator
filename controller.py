from pygame.locals import *
import pygame
import sys


class JoystickHandler(object):
    def __init__(self, id):
        self.id = id
        self.joy = pygame.joystick.Joystick(id)
        self.name = self.joy.get_name()
        self.joy.init()
        self.numaxes = self.joy.get_numaxes()
        self.axis = []
        for i in range(self.numaxes):
            self.axis.append(self.joy.get_axis(i))


class Input(object):
    def init(self):
        pygame.init()
        self.joycount = pygame.joystick.get_count()
        if self.joycount == 0:
            print("no joystick(s) detected!")
            pygame.quit()
            sys.exit(0)
        self.joy = []
        for i in range(self.joycount):
            self.joy.append(JoystickHandler(i))
    def run(self):
        x = []
        y = []
        screen_size = screen_width, screen_height = 1000, 1000
        center = (screen_width//2, screen_height//2)
        screen = pygame.display.set_mode(screen_size)
        rpx = center[0]
        rpy = center[1]
        while True:
            for i in range(self.joycount):
                joy = self.joy[i]
                if i == 0:
                    for j, v in enumerate(joy.axis):
                        if j == 0:
                            print(v)
                            x.append(v)
                            rpx = center[0] + int(v*center[0])
                            rudder_position = (rpx, rpy)
                            pygame.draw.circle(screen, (120, 0, 200), rudder_position, 8)
                        if j == 1:
                            print(v)
                            y.append(v)
                            rpy = center[1] + int(v*center[1])
                            rudder_position = (rpx, rpy)
                            pygame.draw.circle(screen, (120, 0, 200), rudder_position, 8)
                        pygame.display.flip()
            screen = pygame.display.set_mode(screen_size)
            for event in [pygame.event.wait(), ] + pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == JOYAXISMOTION:
                    self.joy[event.joy].axis[event.axis] = event.value


if __name__ == "__main__":
    program = Input()
    program.init()
    program.run()