import os, platform
os.system('git pull') 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from VAM import i
 
        i()
 
 
 
elif bit == "32bit":
 
        from VAM32 import i
 
 
        i()
