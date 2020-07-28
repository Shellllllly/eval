import logging
import grpc
import time
 
from atom.interceptors import header_manipulator_client_interceptor
from atom import meta_pb2
from atom import training_pb2
from atom import job_pb2
from atom import job_pb2_grpc
# -*- coding: utf-8 -*
 
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)
 
logging.basicConfig()
# endpoint = 'apiserver.atom.sl.supremind.info:443' # apiserver 地址，不同集群地址不一样
# p = 'PpxR8TMhGNQnbQSEmC7e' # your private token
# creator = 'shenxiaohan' # 创建者，一般为姓名拼音


 
def createJob(endpoint, cred, creator, nm, interceptor):
    with grpc.secure_channel(endpoint, cred) as channel:
        intercept_channel = grpc.intercept_channel(
            channel, interceptor)
        stub = job_pb2_grpc.JobServiceStub(intercept_channel)
 
        try: 
            # Creating a training job named 'test'
            resp = stub.CreateJob(job_pb2.CreateJobReq(
                job=job_pb2.Job(
                    meta=meta_pb2.Metadata(name=nm),
                    spec=job_pb2.JobSpec(
                        kind=job_pb2.TrainingJob,
                        common=job_pb2.JobCommon(
                            # Input args, only for running single script
                            args=['bash /workspace/mnt/storage/shenxiaohan/ssssss/evalModel.sh'],
                            # Image
                            image='reg.supremind.info/hub/atom/deep-learning/atom-pytorch:1.4-cuda100-py3',
                            # Resource package
                            package=meta_pb2.ResourceReference(
                                kind=meta_pb2.ResourceKindPackage, name='gpu-2080-1'),
                            # Mount storage
                            mounting=job_pb2.JobMounting(
                                storages=[job_pb2.StorageMounting(
                                    storage=meta_pb2.ResourceReference(
                                        kind=meta_pb2.ResourceKindStorage, name='test', creator=creator
                                    ),
                                    readOnly=False
                                ), job_pb2.StorageMounting(
                                    storage=meta_pb2.ResourceReference(
                                        kind=meta_pb2.ResourceKindStorage, name='ssssss', creator=creator
                                    ),
                                    readOnly=False
                                )]
                            )
                        ),
                        instruction=job_pb2.JobInstruction(
                            training=training_pb2.TrainingSpec(
                                enableJupyter=False,
                                enableSSH=False,
                                enableFinder=False,
                                enableLogger=True,
                            )
                        )
                    )
                )
            ))
            _LOGGER.info("Created training job: {}".format(resp)) 
        except grpc.RpcError as e:
            _LOGGER.error("Call failure: {}".format(e))



def startJob(endpoint, cred, creator, nm, interceptor):
    with grpc.secure_channel(endpoint, cred) as channel:
        intercept_channel = grpc.intercept_channel(
            channel, interceptor)
        stub = job_pb2_grpc.JobServiceStub(intercept_channel)
 
        try:
            # Start training job
            resp = stub.StartJob(job_pb2.StartJobReq(
                creator=creator, name=nm))
            _LOGGER.info("Started training job: {}".format(resp))
        except grpc.RpcError as e:
            _LOGGER.error("Call failure: {}".format(e))
 


def getJob(endpoint, cred, creator, nm, interceptor):
    with grpc.secure_channel(endpoint, cred) as channel:
        intercept_channel = grpc.intercept_channel(
            channel, interceptor)
        stub = job_pb2_grpc.JobServiceStub(intercept_channel)
 
        try:
            # Get training job
            resp = stub.GetJob(job_pb2.GetJobReq(
                creator=creator, name=nm))
            _LOGGER.info("Got training job: {}".format(resp))
        except grpc.RpcError as e:
            _LOGGER.error("Call failure: {}".format(e))


def delJob(endpoint, cred, creator, nm, interceptor):
    with grpc.secure_channel(endpoint, cred) as channel:
        intercept_channel = grpc.intercept_channel(
            channel, interceptor)
        stub = job_pb2_grpc.JobServiceStub(intercept_channel)
 
        try:
            resp = stub.RemoveJob(job_pb2.RemoveJobReq(
                creator=creator, name=nm))
            _LOGGER.info(f'Removed training job: {resp}')
            return
        except grpc.RpcError as e:
            _LOGGER.error("Call failure: {}".format(e))
 
            

def eval(endpoint, creator, nm, p):
    print("evaluating....")
    interceptor = header_manipulator_client_interceptor.header_adder_interceptor('authorization', 'private ' + p)
    cred = grpc.ssl_channel_credentials()
    try:
        delJob(endpoint, cred, creator, nm, interceptor)
        time.sleep(5)
    except:
        pass
        time.sleep(5)
    finally:
        createJob(endpoint, cred, creator, nm, interceptor)
        time.sleep(5)
        startJob(endpoint, cred, creator, nm, interceptor)




# if __name__ == '__main__':
    # createJob(endpoint, cred, creator, 'evalModel')
    # getJob(endpoint, cred, creator, 'evalModel')
    # time.sleep(5)
    # startJob(endpoint, cred, creator, 'test2')
    # delJob(endpoint, cred, creator, 'evalModel')
