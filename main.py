from queue import Queue
from uuid import uuid4
from threading import Thread
from random import randint
from time import sleep
from logging import info, basicConfig, INFO

basicConfig(level=INFO, format="\033[97m%(message)s\033[0m")

class Request:
    def __init__(self):
        self.request_id = uuid4()
        info(f"Generated request {self.request_id}")

    def process(self):
        info(f"Processing request {self.request_id}")

class RequestQueue:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self):
        self.queue.put(Request())

    def process_request(self):
        if self.queue.empty():
            info("Queue is empty")
            return
        request = self.queue.get()
        request.process()

request_queue = RequestQueue()

def run_periodically(func):
    while True:
        delay = randint(1, 4)
        sleep(delay)
        func()

def check_queue_size():
    while True:
        sleep(3)
        info(f"Queue size: {request_queue.queue.qsize()}")

Thread(target=run_periodically, args=[request_queue.generate_request], daemon=True).start()
Thread(target=run_periodically, args=[request_queue.process_request], daemon=True).start()
Thread(target=check_queue_size, daemon=True).start()

while True:
    sleep(1)