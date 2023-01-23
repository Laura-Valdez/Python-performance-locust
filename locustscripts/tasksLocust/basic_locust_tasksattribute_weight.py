
from locust import User, task, between
from datetime import datetime


def add_cart(userclass):
    print("I am add to cart")



def view_product(userclass): #userclass Lista de las clases de usuario disponibles para elegir en el selector de clase de usuario
    print("I am view product")

class MyUser(User):
    wait_time = between(1,2)
    #tasks =[add_cart, view_product]
    tasks ={add_cart:3, view_product:6} # son 2 formas de declarar las tareas que se quiere ejecutar hay mas probabilidad el doble  de ejecutar view_product
    # que add_cart


# locust -f .\basic_locust_taskdecorator_weight.py -u 1 -r 1 --headless --only-summary
