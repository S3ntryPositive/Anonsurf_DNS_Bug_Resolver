import os #to send commands for moving files
import time #for sleep function
from time import sleep

print("Anonsurf DNS Bug Resolver...")
sleep(1)
print("This was created because of a known bug that is known to not change the DNS back to normal after stopping the anonsurf vpn client. this is created as a help for beginners (aka skids who want to ddos facebook) to change the dns")
print("The DNS is changed by copying the file to the directory where the file resolv.conf is located... Please lmk on discord if there are any issues at xq34#4689")
print("..............................................................................................................................................")
sleep(1)

os.system("sudo dnstool address 1.1.1.1")
print("Done! Please learn to fix problems. Thanks!")
sleep(1)
exit()