# Script of performing validation using another thread and training job

Put both files under same directory as the calling script and import thread.py. 
Using the following code to call the function.
```
thread = evalThread(1, "t1", 1)
thread.start()
```

One may need to customise the endpoint, creator and private token in thread.py
