my_input = 'UUUR'


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, inst):
        assert len(inst) <= 1

        if inst == 'U':
            self.y += 1
        elif inst == 'D':
            self.y += -1
        elif inst == 'L':
            self.x += -1
        elif inst == 'R':
            self.x += 1
        else:
            raise Exception('what the hell are you doing broh')

my_mini_robot = Robot(0, 0)

for c in my_input:
    my_mini_robot.move(c)

print(f'({my_mini_robot.x}, {my_mini_robot.y})')
