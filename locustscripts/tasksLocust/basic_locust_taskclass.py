
from locust import User, task, between, TaskSet, constant,constant_pacing
from datetime import datetime

class UserBehaivor(TaskSet): #TaskSet : Si está probando el rendimiento de un sitio web que está estructurado de manera jerárquica, con secciones y subsecciones, puede ser útil estructurar su prueba de carga de la misma manera. Para este propósito, Locust proporciona la clase TaskSet . Es una colección de tareas que se ejecutarán de manera muy similar a las declaradas directamente en una clase de Usuario.
    #Los TaskSet son una función avanzada y rara vez son útiles. La mayoría de las veces, es mejor usar bucles regulares de Python y declaraciones de control para lograr lo mismo. También hay algunas trampas, la más frecuente es olvidarse de llamar a self.interrupt()
    @task()
    def add_cart(userclass):
        print("I am add to cart")

    @task()
    def view_product(userclass):
        print("I am view product")

class MyUser(User):
    wait_time = between(1,2)
    tasks =[UserBehaivor]
    #tasks ={add_cart:3, view_product:6}


# locust -f .\basic_locust_taskdecorator_weight.py -u 1 -r 1 --headless --only-summary
