# yolo_test

## Script of creating another thread and training job for validation

Put both files under same directory as the calling script and import thread.py. 
Using the following code to call the function.
```
thread = evalThread(1, "t1", 1)
thread.start()
```

One may need to customise the endpoint, creator and private token in thread.py
