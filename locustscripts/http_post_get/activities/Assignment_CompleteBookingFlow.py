from locust import HttpUser,SequentialTaskSet,task,between

class UserBehaviour(SequentialTaskSet):

    def on_start(self):
        with self.client.post("/api/users", name="create", data={
            "name": "morpheus",
            "job": "leader"
        }, catch_response=True) as resp2:

            if ("morpheus") in resp2.text:
                resp2.success()
                print("success resp2")
            else:
                print("fail resp 2")
                resp2.failure("failed to login")
    @task()
    def find_flight(self):
        print("add post request to search flight")
        print("verify with catch response that flight search is successful")
        #Select a Flight


    @task()
    def select_flight(self):
        print("add post request to select flight")
        print("verify with catch response that select flight is successful")
        #Book a Flight

    @task()
    def book_flight(self):
        print("add post request to book flight")
        print("verify with catch response that flight book is successful")
        print("once success criteria is met, you can change criteria to wrong wordings to see fail criteria is working")
        #Flight Confirmation

class MyUser(HttpUser):
    wait_time=between(1,2)
    host="http://newtours.demoaut.com"
    tasks=[UserBehaviour]
