
from locust import User, task, between, events
from datetime import datetime
@events.test_start.add_listener # Se activa en cada nodo cuando se inicia una nueva prueba de carga. No se vuelve a activar si el número de usuarios cambia durante una prueba.
def script_start(**kwargs):
    print("I am connecting to BD")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am  disconnecting from DB")

class MyUser(User):
    wait_time = between(1,2)


    def on_start(self):
        print("I am loggin into URL")
       # print(datetime.now())
    @task
    def doing_work(self):
        print("I am doing my work")


    def on_stop(self):
        print("I am logging out")
        #locust -f .\on_start_stop.py -u 1 -r 1 --headless --only-summary
        #only-summary Solo imprime las estadísticas resumidas


# locust -f .\on_start_stop.py -u 2 -r 1 --headless --only-summary para