
from locust import HttpUser, task, between
from datetime import datetime

class MyUser(HttpUser):
    wait_time = between(1,3)
    host = "http://advantageonlineshopping.com"
    @task
    def login_URL(self):
        self.client.get("/#/category/Headphones/2", name= " prueba Headphone")

#locust -f .\basic_http_get.py
