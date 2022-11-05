from random import *
r = randint(1,5)
class Grandparents:
    speed = r
    sick = 'coronary heart disease'
    height = 150
class Parents(Grandparents):
    height = 165
    speed = 5
class Child(Parents):
    speed = 8
    def __init__(self):
        print(self.sick)
        print(self.height)
        print(self.speed)
max_roma_pavlo = Grandparents()
#lesson6
import requests
help(requests)
rq = requests
print("for Korsun ",requests.__cake__)
print(rq.__name__)
print(rq.__url__)
print(type(3))
ls = []
for i in dir(ls):
    print(i)
print(dir(ls))
