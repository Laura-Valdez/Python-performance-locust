from locust import HttpUser,task,between

class MyUser(HttpUser):

    wait_time=between(1,2)
    host="https://reqres.in"

    @task
    def launch_URL(self):
        self.client.get("/api/users/2", name="single user")

    @task
    def login(self):
        self.client.post("/api/users",name="create",data={
    "name": "morpheus",
    "job": "leader"
})
