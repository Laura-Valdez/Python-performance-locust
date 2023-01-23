
from locust import User, task, between, constant,constant_pacing
from datetime import datetime

class MyWebUser(User):
    wait_time = between(1,2)
    #wait_time = constant(1)
    #wait_time = constant_pacing(5)
    weight = 3 #Probabilidad de que se elija la clase de usuario. Cuanto mayor sea el peso, mayor será la probabilidad de que sea elegido.
    @task
    def login_URL(self):
        print("I am loggin Web into URL")



class MyMobileUser(User):
    wait_time = between(1,2)
    #wait_time = constant(1)
    #wait_time = constant_pacing(5)
    weight = 1
    @task
    def login_URL(self):
        print("I am loggin Mobile into URL")
