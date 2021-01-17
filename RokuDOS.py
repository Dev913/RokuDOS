from os import system
import time
system('sudo apt-get install python3-pip')
system('pip3 install roku')
system('clear')
from roku import Roku
system('clear')
ip = input('Please input the IP of the roku: ')
roku = Roku('' + ip)
while time.time:
    roku.home()
    print('Done.')
    time.sleep(1)
