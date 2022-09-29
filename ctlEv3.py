#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction)
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
l_motor = Motor(Port.C)
r_motor = Motor(Port.D)

robot = DriveBase(l_motor, r_motor, wheel_diameter=55.5, axle_track=104)

print('Motor On')
ev3.speaker.beep()

wait(10000)
robot.stop()
