
from locust import User, task, between, TaskSet, constant,constant_pacing, SequentialTaskSet
from datetime import datetime

class UserBehaivor(SequentialTaskSet): #es un TaskSet cuyas tareas se ejecutarán en el orden en que se declaran. Es posible anidar SequentialTaskSets dentro de un TaskSet y viceversa.

    def on_start(self):
        print ("I will login")

    @task()
    def find_flight(self):
        print("I will fing flight by entering criteria")

    @task()
    def select_flight(self):
        print("slect_ flight ")

    @task()
    def book_flight(self):
        print("book flight ")

class MyUser(User):
    wait_time = between(1,2)
    tasks =[UserBehaivor]
    #tasks ={add_cart:3, view_product:6}

# locust -f .\basic_locust_taskclass_sequency.py -u 1 -r 1 --headless --only-summary

