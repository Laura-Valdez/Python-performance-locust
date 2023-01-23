
from locust import User, task, between
from datetime import datetime

class MyUser(User):
    wait_time = between(1,2)


    @task(2) # el 2 es el peso de la tarea  Se utiliza como decorador de conveniencia para poder declarar tareas para un usuario o un conjunto de tareas en línea en la clase
    def add_cart(self):
        print("I am add to cart")

    @task(4)
    def view_product(self):
        print("I am view product")

# locust -f .\basic_locust_taskdecorator_weight.py -u 1 -r 1 --headless --only-summary
