
from locust import HttpUser, task, between
from datetime import datetime

class MyUser(HttpUser): #  cuando es httpUser Representa un "usuario" HTTP que se va a generar y atacar el sistema que se va a probar con la carga.
    # cuando no es httpuser sino solo user es solo un usuario
    wait_time = between(1,3) ## Método que devuelve el tiempo (en segundos) entre la ejecución de tareas locust. Se puede anular para TaskSets individuales.
    host = "http://newtours.demoaut.com/"
    @task
    def login_URL(self):
        print("I am loggin into URL")
       # print(datetime.now())

    ## locust -f .\basic_locust_01.py -u 5 -r 1 -t 10s --headless --logfile logfiles\mylog.log --loglevel DEBUG comando para cuando no se quiere subir el locust al puerto
    # -u (o --users) el numero de usuarios que van a ejecutar
    # Número máximo de usuarios Locust simultáneos. Se utiliza principalmente junto con –headless o –autostart. Se puede cambiar durante una prueba con las entradas del teclado w, W (generar 1, 10 usuarios) y s, S (detener 1, 10 usuarios)
    #  -r ( o --spawn-rate) el numero de usuarios que va a crecer por segundo
    #Tasa para generar usuarios en (usuarios por segundo). Se usa principalmente junto con –headless o –autostart
    # -t (o --run-time) Detener después de la cantidad de tiempo especificada, por ejemplo (300s, 20m, 3h, 1h30m, etc.). Solo se utiliza junto con –headless o –autostart
    #-headless Deshabilite la interfaz web y comience la prueba de inmediato. Utilice -u y -t para controlar el número de usuarios y el tiempo de ejecución
    #--logfile Ruta al archivo de registro.
    #--loglevel Elija entre DEBUG/INFO/WARNING/ERROR/CRITICAL. El valor predeterminado es INFORMACIÓN.

