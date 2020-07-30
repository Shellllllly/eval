import threading

import job
import logging
import grpc
import time
 
from atom.interceptors import header_manipulator_client_interceptor
from atom import meta_pb2
from atom import training_pb2
from atom import job_pb2
from atom import job_pb2_grpc
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)
 
logging.basicConfig()



class evalThread(threading.Thread):
    def __init__(self, threadID, name, sh, endpoint, creator, private_token, job_name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        # self.counter = counter
        self.sh = sh
        self.endpoint = endpoint
        self.creator = creator
        self.private_token = private_token
        self.job_name = job_name

    def run(self):
        print("Starting " + self.name)
        job.eval(self.endpoint, self.creator, self.job_name, self.private_token, self.sh)
        print("Exiting " + self.name)

