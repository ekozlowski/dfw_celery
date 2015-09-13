from celery import Celery
import time
import random

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    time.sleep(20)
    return x + y

@app.task
def simulation(identifier):
    print("{} is working".format(identifier))
    time.sleep(random.randint(1,10))
    print("{} is done!".format(identifier))
