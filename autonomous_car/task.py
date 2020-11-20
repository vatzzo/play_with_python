import logging
import random
import time
import os

logging.basicConfig(level=logging.INFO, format='%(message)s')


def clearConsole():
    return os.system('cls')


class Car:
    def __init__(
            self, speed=0, wheel_angle=0,
            acceleration=5, braking_acc=5,
            max_speed=200):
        self.speed = speed
        self.wheel_angle = wheel_angle
        self.acceleration = acceleration
        self.braking_acc = braking_acc
        self.max_speed = max_speed

    def logInfo(self):
        logging.info("Car speed: {speed}".format(speed=self.speed))
        logging.info("Wheel angle: {angle}".format(angle=self.wheel_angle))

    def __accelerate(self, event):
        if self.speed < self.max_speed:
            self.speed = self.speed + self.acceleration*event.current_time
            if self.speed > self.max_speed:
                self.speed = self.max_speed

    def __brake(self, event):
        if self.speed > 0:
            self.speed = self.speed - self.braking_acc*event.current_time
            if self.speed < 0:
                self.speed = 0

    def __alarm(self, event):
        if event.current_time != 0:
            logging.info('BEEP')

    def __avoid(self, event):
        if event.current_time < event.duration/3:
            self.wheel_angle = -45
        elif event.current_time >= event.duration/3 and event.current_time < (2*event.duration)/3:
            self.wheel_angle = 45
        else:
            self.wheel_angle = 0

    def act(self, event):
        if event.name == "empty_road":
            event.logMsg()
            self.__accelerate(event)
            event.count()
        if event.name == "closed_road":
            event.logMsg()
            self.__brake(event)
            event.count()
        if event.name == "obstacle":
            event.logMsg()
            self.__accelerate(event)
            self.__avoid(event)
            self.__alarm(event)
            event.count()


class Event:
    def __init__(
            self, name, duration, msg):
        self.name = name
        self.duration = duration
        self.msg = msg
        self.current_time = 0

    def count(self):
        if self.current_time < self.duration:
            self.current_time = self.current_time + 1
        else:
            self.current_time = 0

    def logMsg(self):
        logging.info(self.msg)


if __name__ == "__main__":
    car = Car(50, 0, 5, 5, 200)
    events = []
    events.append(
        Event('empty_road', 10, 'The road is empty. I am starting to accelerate.'))
    events.append(
        Event('closed_road', 10, 'It seems that there is the end of the road.'))
    events.append(
        Event('obstacle', 10, 'There is an obstacle ! Overtaking in progess.'))

    state1 = False
    state2 = True
    i = 0
    while True:
        car.logInfo()
        if state2 == True:
            i = random.randint(0, 2)
            state2 = False
            state1 = True

        if i >= 0 and i <= len(events)-1 and state1:
            car.act(events[i])
            if events[i].current_time == events[i].duration:
                state1 = False
                state2 = True
        time.sleep(1)
        clearConsole()