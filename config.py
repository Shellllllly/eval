# import configparser
# config = configparser.ConfigParser()
config = dict()

config['endpoint'] = 'apiserver.atom.sl.supremind.info:443'
config['private_token'] = 'PpxR8TMhGNQnbQSEmC7e'
config['creator'] = 'shenxiaohan'

# New training job settings
config['gpu'] = 'gpu-2080-1'
config['image'] = 'reg.supremind.info/hub/atom/deep-learning/atom-pytorch:1.4-cuda100-py3'
config['args'] = 'bash /workspace/mnt/storage/shenxiaohan/ssssss/evalModel.sh'

config['storages'] = [('test', 'shenxiaohan', False), ('ssssss', 'shenxiaohan', False)]
config['volumes'] = [('public-image', 'ava-admin', True)]

config['enableJupyter'] = False
config['enableSSH'] = False
config['enableFinder'] = False
config['enableLogger'] = True


