#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ds4drv
import pigpio
from pygame.locals import *
import time
import pygame

pi = pigpio.pi()
pi.set_mode(4, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(22, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)

pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(19, pigpio.OUTPUT)

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

do = 1
start = time.time()

#front
while do==1:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN and event.button == 10:
            endtime = time.time() - start
            pi.hardware_PWM(18,150,0)
            pi.hardware_PWM(19,150,0)
            pi.write(4,0)
            pi.write(17,0)
            pi.write(22,0)
            pi.write(27,0)
            print("end:{0:.2f}".format(endtime))
            do=0
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        axes = joystick.get_numaxes()
        axis = joystick.get_axis(1)
        axis2 = joystick.get_axis(4)

        if axis > 0:
            pi.write(4,1)
            pi.write(17,0)
            if axis >0 and axis <=0.20:
                pi.hardware_PWM(18,150,200000)
                print("lb0.20")
            if axis >0.20 and axis <=0.40:
                pi.hardware_PWM(18,150,400000)
                print("lb0.40")
            if axis >0.40 and axis <=0.60:
                pi.hardware_PWM(18,150,600000)
                print("lb0.60")
            if axis >0.60 and axis <=0.80:
                pi.hardware_PWM(18,150,800000)
                print("lb0.80")
            if axis >0.80:
                pi.hardware_PWM(18,150,1000000)
                print("lb1")
        if axis < 0:
            pi.write(4,0)
            pi.write(17,1)       
            if axis <0 and axis >=-0.20:
                pi.hardware_PWM(18,150,200000)
                print("lf-0.20")
            if axis <-0.20 and axis >=-0.40:
                pi.hardware_PWM(18,150,400000)
                print("lf-0.40")
            if axis <-0.40 and axis >=-0.60:
                pi.hardware_PWM(18,150,600000)
                print("lf-0.60")
            if axis <-0.60 and axis >=-0.80:
                pi.hardware_PWM(18,150,800000)
                print("lf-0.80")
            if axis <-0.80:
                pi.hardware_PWM(18,150,1000000)
                print("lf-1")
        if axis == 0:
            pi.write(4,1)
            pi.write(17,1)
            pi.hardware_PWM(18,150,500000)
            print("l stop")
        if axis2 > 0:
            pi.write(27,1)
            pi.write(22,0)
            if axis2 >0 and axis2 <=0.20:
                pi.hardware_PWM(19,150,200000)
                print("rb0.20")
            if axis2 >0.20 and axis2 <=0.40:
                pi.hardware_PWM(19,150,400000)
                print("rb0.40")
            if axis2 >0.40 and axis2 <=0.60:
                pi.hardware_PWM(19,150,600000)
                print("rb0.60")
            if axis2 >0.60 and axis2 <=0.80:
                pi.hardware_PWM(19,150,800000)
                print("rb0.80")
            if axis2 >0.80:
                pi.hardware_PWM(19,150,1000000)
                print("rb1")
        if axis2 < 0:
            pi.write(27,0)
            pi.write(22,1)       
            if axis2 <0 and axis2 >=-0.20:
                pi.hardware_PWM(19,150,200000)
                print("rf-0.20")
            if axis2 <-0.20 and axis2 >=-0.40:
                pi.hardware_PWM(19,150,400000)
                print("rf-0.40")
            if axis2 <-0.40 and axis2 >=-0.60:
                pi.hardware_PWM(19,150,600000)
                print("rf-0.60")
            if axis2 <-0.60 and axis2 >=-0.80:
                pi.hardware_PWM(19,150,800000)
                print("rf-0.80")
            if axis2 <-0.80:
                pi.hardware_PWM(19,150,1000000)
                print("rf-1")
        if axis2 == 0:
            pi.write(27,1)
            pi.write(22,1)
            pi.hardware_PWM(19,150,500000)
            print("r stop")
            
            
pi.set_mode(4, pigpio.INPUT)
pi.set_mode(18, pigpio.INPUT)
pi.set_mode(17, pigpio.INPUT)
pi.set_mode(22, pigpio.INPUT)
pi.set_mode(27, pigpio.INPUT)
pi.stop()    
pygame.quit ()
