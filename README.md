# RokuDOS
This is a python script that will send requests to a Roku Smart television and spam the home button.

## Instructions
* First before executing add sudo before "python RokuDOS.py".
* After first execution proceed to press ctrl + z after everything installed and you see an error about the roku script.
* Re-execute the script using "python3 RokuDOS.py".
* In order to gain an IP you need to have access to the network that the Roku is connected to.
* You can use many different applications. I reccommend nmap it is fast.
* Head to https://vitux.com/find-devices-connected-to-your-network-with-nmap/.
* Read and enter the command gather the IP the Roku TV or TV's and enter them into the RokuDOS script when asked and profit.
* If you are having issues finding it as they may be to many IPs on that network. Use fing it can pick out those devices and tell you usually which brand they are.

### Extras
* Open the python script in a text editor.
* Remove the bottom line "time.sleep(1)".
* Execute the script and profit. Now it is faster and not controllable.
* If you want it back to a little controllable (to make your victim/victims think it is the remote).

# Credits
<b>Dev913</b> (me) - developer of this simple dos.

<b>jcarbaugh</b> - developer of python-roku.

https://github.com/jcarbaugh/python-roku
