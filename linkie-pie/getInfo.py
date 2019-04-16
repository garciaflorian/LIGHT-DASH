import time
from linkyParsing import *
import json

starttime=time.time()


 
for x in range(60):
    json_or_string = json.dumps(linkyParsing("COM5"))
    print(json_or_string)
    with open("out.txt", "a") as file:
        file.write(json_or_string)
        file.write("\n")
    file.close()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
