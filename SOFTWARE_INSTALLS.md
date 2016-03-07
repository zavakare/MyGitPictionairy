# Useful software and commands:

To update/grade your software:

* **sudo apt-get update**
* **sudo apt-get upgrade**

to install software

* **sudo apt-get install package**

---

## Recommendations for software everyone should have 
keep updating this as you install packages, this way everyone has the same software and you can copy/paste these command easily on your own systems :+1:


sudo apt-get install vim



################# Software used for voice recognition #########################

* **Prerequisites:
	* **sudo apt-get update
	* **sudo apt-get upgrade
	* **sudo apt-get install bison
	* **sudo apt-get install libasound2-dev
	* **sudo apt-get install swig
	* **sudo apt-get install python-dev
	* **sudo apt-get install mplayer
	* **sudo reboot
	* **sudo nano etc/asound.conf 
		* **Type code

* **For Sphinxbase:
	* **cd ~/
	* **wget http://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz
	* **tar -zxvf ./sphinxbase-5prealpha.tar.gz
	* **cd ./sphinxbase-5prealpha
	* **./configure --enable-fixed
	* **make clean all
	* **make check
	* **sudo make install

* **For PocketSphinx:
	* **cd ~/
	* **wget http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz
	* **tar -zxvf pocketsphinx-5prealpha.tar.gz
	* **cd ./pocketsphinx-5prealpha
	* **./configure
	* **make clean all
	* **make check
	* **sudo make install
	* **sudo lsconfig

* **Create a language model:
	* **Upload the text file here: http://www.speech.cs.cmu.edu/tools/lmtool-new.html

* **Other installs:
	* **sudo apt-get update
	* **sudo apt-get install pulseaudio
	* **sudo apt-get instal libpulse-dev
	* **sudo apt-get install osspd

################# Software for Buttons  #########################

* **GPIO:	
	* **sudo apt-get update
	* **sudo apt-get install python-rpi.gpio python3-rpi.gpio

* **To install the latest development version from the project source code library:
	* **sudo apt-get install python-dev python3-dev
	* **sudo apt-get install mercurial		
	* **sudo apt-get install python-pip python3-pip
	* **sudo apt-get remove python-rpi.gpio python3-rpi.gpio
	* **sudo pip install hg+http://hg.code.sf.net/p/raspberry-gpio-python/code#egg=RPi.GPIO
	* **sudo pip-3.2 install hg+http://hg.code.sf.net/p/raspberry-gpio-python/code#egg=RPi.GPIO

