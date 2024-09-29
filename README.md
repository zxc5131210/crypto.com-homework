Task 1
-------------
Based on the current date, check for the date nine days ahead to determine if the ninth day’s date appears on the screen. If the date for the ninth day is not present, the test should fail. If it is present, take a screenshot to use as the basis for determining success.
    
Video Demo
===========
https://drive.google.com/file/d/1tbS27_jh40Bfrgqrc7MnXIKXJ3gxpNlN/view?usp=sharing

Setup for Test
----------
`pip install requirements.txt`

install appium desktop and start the appium server

Run Appium
----------
	Appium configured and launch a server
  	$ appium
  
Test
====
Clone this github
-----------------
	$git clone https://github.com/zxc5131210/crypto.com-homework.git

Run Test
-------------
  	Go to the folder: cd crypto.com-homework/task1
  	pytest test_ninth_day_weather.py




Task 2
-------------
Execute the test_ninth_day_weather.py file to check the ninth day date. If the date does not exist, the test should fail. If that date exists, the test should pass.
And print the result and save the received data as json file.
    

    Go to the folder: cd crypto.com-homework/task2
    python3 test_ninth_day_weather.py

    