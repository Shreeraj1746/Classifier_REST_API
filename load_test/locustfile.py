from locust import HttpLocust, TaskSet


def classify(l):
    l.client.get("/classify?text=Jim Morrison was the lead singer of the band"
                 + " The Doors and lived in California.")


def index(l):
    l.client.get("/")


class UserBehavior(TaskSet):
    tasks = {classify: 1}

    # def on_start(self):
    #     index(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
