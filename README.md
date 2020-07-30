# Script of performing validation using another thread and training job

Put both files under the same directory as the calling script and import thread.py. 
Using the following code to call the function.
```
thread = evalThread(threadID, threadName, 'bash /path/to/sh/file/xxx.sh', endpoint, creator, private_token, trainingJobName)
thread.start()
```

