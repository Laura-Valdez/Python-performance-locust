
from locust import User, task, between, TaskSet, constant,constant_pacing
from datetime import datetime

class UserBehaivor(TaskSet):
    @task(2)
    class cart_module(TaskSet):
        @task(4)
        def add_cart(self):
            print("I am add to cart")

        @task(2)
        def delete_cart(self):
            print("I am delete to cart")

        @task(1)
        def stop(self):
            print("I am stopping to cart")

    @task(4)
    class Product_Module(TaskSet):

        @task(4)
        def view_product(self):
            print("I am view product")

        @task(2)
        def add_product(self):
            print("I am add product")

        @task(1)
        def stop(self):
            print("I am stopping to product")


class MyUser(User):
    wait_time = between(1,2)
    tasks =[UserBehaivor]
    #tasks ={add_cart:3, view_product:6}


# locust -f .\locustscripts\basic_locust_taskclass_nesting.py -u 1 -r 1 -t 20s --headless --only-summary
