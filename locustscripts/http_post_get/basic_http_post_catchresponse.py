from locust import HttpUser,SequentialTaskSet,task,between

class UserBehaviour(SequentialTaskSet):

    @task
    def UserGet(self):
        with self.client.get("/api/users/2", name="single user",catch_response=True) as resp1:
            if("Janet" and "Weaver")in resp1.text:
                resp1.success()
                #print(resp1.text)
                print("success")
            else:
                print("fail")
                resp1.failure("failed to launch url")


    @task
    def login(self):
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


class MyUser(HttpUser):
    wait_time=between(1,2)
    host="https://reqres.in"
    tasks=[UserBehaviour]

#locust -f .\locustscripts\basic_http_post_catchresponse.py -u 1 -r 1 -t 30s --headless --only-summary