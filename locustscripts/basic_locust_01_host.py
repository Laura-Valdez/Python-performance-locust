
from locust import HttpUser, task, between
from datetime import datetime

class MyUser(HttpUser): #  cuando es httpUser Representa un "usuario" HTTP que se va a generar y atacar el sistema que se va a probar con la carga.
    # cuando no es httpuser sino solo user es solo un usuario
    wait_time = between(1,3) ## Método que devuelve el tiempo (en segundos) entre la ejecución de tareas locust. Se puede anular para TaskSets individuales.
    #host = "http://newtours.demoaut.com/"
    @task
    def login_URL(self):
        print("I am loggin into URL")
       # print(datetime.now())

#  locust -f .\locustscripts\anyscript.py --host="http://newtours.demoaut.com/"  el problema como es web, este host no se coloca en el campo correspondiendte por lo tato no sirve, amenos
# que se coloque la pagina en el camopo
