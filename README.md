# track_screen
Python script that takes an image of screen every 10 seconds, along with a LaunchAgent for Mac to start it on wake.

### Purpose
I'm gonna use some computer vision to process all these screenshots to give me a dashboard of what I spend time on using my computer (kinda like screentime for apple devices)

### Setup
1. Install pillow for Python
2. Put plist file in ~/Library/LaunchAgents
3. Load plist into launchctl
4. Give everything permission as needed
5. All the images will appear in the `/images` folder in the repo



