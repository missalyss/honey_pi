# How to Set Up Honey Pi for Newbee iOS App
==========

1. Configure SD card in your personal computer

- Acquire Raspian Jessie Img (not Lite!) from Raspberry Pi website.
- Install with diskutil. This [tutorial](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md) is easy to put together.
- Set up pi with SSH for running it remote with [this tutorial](https://gist.github.com/MrJadaml/8b0c1f39fa39fa5c148b5044d98f00f5). Be sure to use the wifi info you want the Pi to be running on. If you want some flexibility, skip this step until you're ready to plug your Pi in and leave it alone.

2. Install Dependencies

- After hooking up to the internet, clone this repo to your Pi and cd into it.
- Install dependencies: `$ pip install -r requirements.txt`
- You may have to install some dependencies individually.
`sudo pip install pytz`
`sudo pip install datetime`
- Clone Adafruit library: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
- Cd into Adafruit_Python_DHT, then enter `sudo apt-get install build-essential python-dev`
- Finish installation `sudo python setup.py install`
- [This tutorial can help with troubleshooting](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)

3. Change timezone in Honey Pi to PST

- If you're in the terminal, `sudo raspi-config` and follow the prompts.
- If you're in GUI, you can change it in rasperry preferences.
- **If you do not change the timezone, your chart will not display the proper time that data was recorded**

4. Set up Pi for remote
- After Pi is configured with SSH, ssh into it via the terminal
`$ ssh pi@<YOUR_PI'S_IP_ADDRESS_ON_THIS_NETWORK>`
and sign in with Pi's password ( `honey_pi` )
To edit .py file, in terminal run
`$ nano <YOUR_FILE_NAME>.py`

You can touch a script in, echo the full pathname for running your file (with the while loop in it) and enter this command to start running in the background.
// give yourself permission to run the script
`$ chmod u=rwx script.sh`
`$ /home/pi/honey_pi/script.sh & disown`

Want to disconnect running in background?
`$ ps ax | grep <YOUR_FILE_NAME>.py`
Identify the number next to the far left of the command running your file (the command with a `grep --color=auto` is the `ps ax` command you just ran to find the file)
`$ kill <4_DIGIT_NUMBER>`

To get out of the Pi's terminal:
`$ logout`
