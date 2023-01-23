
from locust import User, task, between, TaskSet, constant,constant_pacing
from datetime import datetime



class MyUser(User):
    wait_time = between(1,2)

    @task()
    class UserBehaivor(TaskSet):
        @task()
        def add_cart(userclass):
            print("I am add to cart")

        @task()
        def view_product(userclass):
            print("I am view product")
#locust -f .\basic_locust_taskclass2.py -u 1 -r 1 --headless --only-summary