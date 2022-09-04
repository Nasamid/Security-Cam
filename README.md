# Security-Cam
A work in progress... This security camera, written in python, allows your computer to take a photo of the person who uses it every time your computer starts up and wakes-up from sleep. The photo is then automatically uploaded to your Google Drive account, which you can access remotely.

## How it Works
Note that this is only compatible with computers with attached or built-in webcams.

Upon computer start-up or log in, the designated camera will automatically detect a face or a body and then snapshots a photo to be stored locally and on the cloud (gDrive, if internet connection is available).

This process is fully automated and is hidden, so no window/s will pop up. The only way to know if it worked is if the photo is saved locally (within your chosen path), saved in your gDrive, or if your camera light flashes for a short period (usually the case for most laptops, since flash is a built-in laptop camera feature).

The photo will be stored in a .png format with its filename as the time when the photo was taken. (%day-%month-%year-%hour-%minute.png)

## Features

## Setup

