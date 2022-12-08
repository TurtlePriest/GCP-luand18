from locust import HttpUser, task

class testUser (HttpUser):

    @task
    def test(self):
        self.client.get("/")
        self.client.get("/consent")
        self.client.get("/main")
        self.client.get("/experiment-survey")
        self.client.get("/survey")
        self.client.get("/users/connect")