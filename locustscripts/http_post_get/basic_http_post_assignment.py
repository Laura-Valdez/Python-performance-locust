from locust import HttpUser,SequentialTaskSet,task,between

class UserBehaviour(SequentialTaskSet):

    @task
    def launch_URL(self):
        resp1= self.client.get("/api/users/2", name="single user")
        print(resp1.text)
        print(resp1.status_code)
        print(resp1.headers)

    @task
    def login(self):
        resp2=self.client.post("/api/users", name="create", data={
                                                            "name": "morpheus",
                                                            "job": "leader"
                                                        })
        print(resp2.text)
        print(resp2.status_code)
        print(resp2.headers)
class MyUser(HttpUser):
    wait_time=between(1,2)
    host="https://reqres.in"
    tasks=[UserBehaviour]
# locust -f .\locustscripts\basic_http_post_assignment.py -u 1 -r 1 -t 10s --headless --only-summary