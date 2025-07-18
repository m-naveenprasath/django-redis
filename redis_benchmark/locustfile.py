# locustfile.py

from locust import HttpUser, task, between

class DjangoRedisUser(HttpUser):
    wait_time = between(1, 2)  # seconds between tasks for each simulated user

    @task(1)
    def no_cache_view(self):
        self.client.get("/no-cache/")

    @task(1)
    def with_cache_view(self):
        self.client.get("/with-cache/")
