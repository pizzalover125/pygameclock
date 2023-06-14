from datetime import datetime
import time
from os import system, name

x = 0

if name == 'nt':
    _ = system('cls')

else:
    _ = system('clear')

while x < 100000:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)
    x+=1
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')