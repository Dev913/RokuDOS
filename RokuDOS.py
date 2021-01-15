from os import system
import time
system('pip install roku')
system('clear')
from roku import Roku
system('clear')
ip = input('Please input the IP of the roku: ')
roku = Roku('' + ip)
while time.time:
    roku.home()
    print('Done.')
    time.sleep(1)
