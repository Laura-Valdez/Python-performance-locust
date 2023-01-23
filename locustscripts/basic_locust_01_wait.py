
from locust import User, task, between, constant,constant_pacing
from datetime import datetime

class MyUser(User):
    #wait_time = between(1,2) # Método que devuelve el tiempo (en segundos) entre la ejecución de tareas.
    #wait_time = constant(10) # Devuelve una función que solo devuelve el número especificado por el argumento wait_time
    # se espera a ejecutat  la tarea cada 10 segundo
    wait_time = constant_pacing(5) #la tarea siempre se ejecutará una vez cada 5 segundos, sin importar el tiempo de ejecución de la tare
    # Si la ejecución de una tarea excede el tiempo de espera especificado, la espera será 0 antes de comenzar la siguiente tarea
    @task
    def login_URL(self):
        print("I am loggin Web into URL")
        print(datetime.now())


