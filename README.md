Video Demo
===========
https://drive.google.com/file/d/1_Pv1rCQ-SVb7k6fjumUILssWR7f8KJa6/view?usp=drive_link

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
  	Go to the folder: cd crypto.com-homework
  	pytest test_ninth_day_weather.py

Task 1
-------------
Based on the current date, check for the date nine days ahead to determine if the ninth day’s date appears on the screen. If the date for the ninth day is not present, the test should fail. If it is present, take a screenshot to use as the basis for determining success.
    


Task 2
-------------
In Task 2, the JSON file contains data retrieved from the API response. Based on today's data from 00:00 to 23:00 (for the time range 09:30:00 to 09:30:23), determine if the humidity is within the specified range on the front end. If it is, the result is "pass"; if not, the result is "fail."
