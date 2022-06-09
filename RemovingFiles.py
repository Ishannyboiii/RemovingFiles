import time
import os
import shutil

path = 'Users\Rakesh\Desktop\Coding\Python'
days = 1

time.time(days)
os.path.exists(path)

if os.path.exists == True :
     os.listdir(path)
     os.walk(path)
     os.path.join()
     ctime = os.stat(path).st_ctime
     return(ctime)
     #if ctime>days:
