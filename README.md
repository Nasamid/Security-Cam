# Security-Cam
A work in progress... This security camera, written in python, allows your computer to take a photo of the person who uses it every time your computer starts up or wakes-up from sleep. The photo is then automatically uploaded to your Google Drive account, which you can access remotely.

## How it Works
Note that this is only compatible with computers with attached or built-in webcams.

Upon computer start-up or log in, the designated camera will automatically detect a face or a body and then snapshots a photo to be stored locally and on the cloud (gDrive, if internet connection is available).

This process is fully automated and is hidden, so no window/s will pop up. The only way to know if it worked is if the photo is saved locally (within your chosen path), saved in your gDrive, or if your camera light flashes for a short period (usually the case for most laptops, since flash is a built-in laptop camera feature).

The photo will be stored in a .png format with its filename as the time when the photo was taken. (%day-%month-%year-%hour-%minute.png)

## Features
* Face & Body detection
* Can run automatically
* Stores the photos locally and online
* Can access photos remotely as long as you have access to your google drive
* Runs at computer startup and as computer wakes-up from sleep
* Uses google API for secure online processes

## Setup
* Download the source code above or type the following command in your terminal:
    ```
    git clone https://github.com/Nasamid/Security-Cam
    ```
* Install the following using the terminal:

    opencv
     ```
     pip install python-opencv
     ```
    dotenv
     ```
     pip install python-dotenv
     ```
* Create or choose an existing Google Account

* Go to console.cloud.google.com and create a new project.

     Project Setup: (You can either follow the steps below or watch this video {2:08-5:08} -> https://www.youtube.com/watch?v=fkWM7A-MxR0&t=978s)
     
        - Enable APIs and Services for Google Drive (https://console.cloud.google.com/apis/library/drive.googleapis.com?project=airy-dialect-355403)
        
        - In the OAuth Consent Screen, choose External then hit create.
        
        - Fill-up the necessary information needed (the ones with red asterisks) then hit Save and Continue.
        
        - Add the scope : Google Drive API (https://www.googleapis.com/auth/drive) then hit Save and Continue.
        
        - Add your email address as a test User then finish-up by going back to the Dashboard in the Summary tab.
        
        - Go to Credentials then hit "+Create Credentials"
        
        - Choose OAuth Client ID then set the Application type as "Desktop app".
        
        - Type any client app name, then hit create.
        
        - Download the .json file then place it in your folder containing the source code.
  
* Run quickstart.py

* It should create token.json where your REFRESH_TOKEN ("refresh_token"), CLIENT_ID ("client_id") and CLIENT_SECRET ("client_secret") are located.

                          **NOTE THAT THESE ARE SENSITIVE INFORMATION AND IT SHOULD NOT BE SHARED WITH ANYONE**

* Copy and paste these three inside template.env and make sure to remove the quotation marks and spaces before and after the equal (=) sign.

* For Automation, in Start Menu, search and open the Task Scheduler:

        - Create a New Task.
        
        - In the General settings, fill-in the desired name of the task.
        
        - Click "Run wheter the user is logged in or not" as well as check the checkbox below.
        
        - Click "Change User or Group" and in the object name, type your Username (be careful as it is case-sensitive)
        
        - On the Actions tab, create a new action.
        
        - Let the action be 'Start a Program', then you can use cmd and type 
       -------------------------------------------
        where python
       -------------------------------------------
        to locate your pythonw.exe file, and then paste its path inside the 'Program/Script' bar.
        
        - Add argument : main.pyw
        
        - Start in : copy and paste the path where in your main.pyw is located. In my case it would be:
       -------------------------------------------
          C:\Users\danil\Downloads\Security-Cam
       -------------------------------------------
        note that the path above does not include the python file !IMPORTANT!
        
        - If you are using a laptop, uncheck everything in the Conditions tab.
        
        - Setup Triggers by selecting New...
        
        - First trigger should be Begin Task : At system startup.
        
        - Then create a new one by clicking New... then selecting Begin Task : On an Event.
        
        - Select the following:
        
            - Log : System
            
            - Source : Power-Troubleshooter
            
            - Event ID : 1
            
         - The first trigger allows the script to run at system startup and the second one allows it to run at system log in (from sleep)
         
* All Done! 

## Debug
When ran for quite some time, (usually 1-2 weeks), the gDrive upload function may or may not work. To solve this, you will need to delete token.json, run quickstart.py, then replace the CLIENT_ID, CLIENT_SECRET, and REFRESH_TOKEN from the new token.json generated by running quickstart.py. 

### Special Thanks to
Daniel David N. Bador ([D4N13LxD4V1D](https://github.com/D4N13LxD4V1D)) for helping me in this project.
        

        
