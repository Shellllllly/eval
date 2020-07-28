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
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)

        endpoint = 'apiserver.atom.sl.supremind.info:443'
        creator = 'shenxiaohan' # 创建者，一般为姓名拼音
        private_token = 'PpxR8TMhGNQnbQSEmC7e'
        job.eval(endpoint, creator, 'testModel', private_token)

        print("Exiting " + self.name)

