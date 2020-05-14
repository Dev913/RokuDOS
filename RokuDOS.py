from os import system
import time
import yaml
system('pip install roku')
system('reset')
print('Importing roku module for python! (in 1 seconds)')
time.sleep(1)
system('reset')
from roku import Roku
ip = raw_input('Please input the IP of the roku: ')
roku = Roku('' + ip)
with open('Data/data.yaml', 'r') as data:
    data = yaml.load(data)
user_preference = data['delay']
while time.time:
    roku.home()
    print('Done...')
    time.sleep(user_preference)