from datetime import datetime
import pyautogui
import subprocess
import time
import pandas
import os

# Specify the path to the Zoom application on your macOS
zoom_path = '/Applications/zoom.us.app'

current_directory = os.getcwd()
relative_csv_path = 'info.csv'
# Joining the current directory and the relative path to get the absolute path to the CSV file
csv_path = os.path.join(current_directory, relative_csv_path)

dates_and_times = []
meeting_ids = []
meeting_passcodes = []
meeting_links = []

def main():
    # Get the current date and time.
    date = datetime.now().date() 
    time = datetime.now().strftime("%I:%M:%S %p")
    print("Current Session: ["+ str(date) +"] - ["+ str(time) + "]")

    readCSVFile(relative_csv_path)
    # openZoom()
    # joinMeeting()

def readCSVFile(path):
    global dates_and_times, meeting_ids, meeting_passcodes, meeting_links
    # Read the CSV file into a pandas DataFrame
    df = pandas.read_csv(path)

    # Now you can access the columns as follows:
    dates_and_times = df['date_and_time'].tolist()
    meeting_ids = df['meeting_id'].tolist()
    meeting_passcodes = df['meeting_passcode'].tolist()
    meeting_links = df['meeting_link'].tolist()

    for i in range(len(dates_and_times)):
        print("\nDate and Time: " + dates_and_times[i])
        print("Meeting ID: " + str(meeting_ids[i]))
        print("Meeting Passcode: " + str(meeting_passcodes[i]))
        print("Meeting Link: " + str(meeting_links[i]) if pandas.notna(meeting_links[i]) else "Meeting Link: N/A")

def openZoom():
    """Open the Zoom app."""
    try: 
        # Open Zoom using subprocess
        # userName = input("Enter preferred user name: ")
        subprocess.run(['open', zoom_path])
        print("Opening Zoom...")
        time.sleep(3)
        print("Zoom opened.")

    except Exception as e:
        print(f"An error occurred: {e}")


def joinMeeting():
    """Join a meeting by entering the meeting number and passcode"""
    try:
        x,y = pyautogui.locateCenterOnScreen('join-a-meeting.png')
        pyautogui.moveTo(x/2,y/2,0.5)
        pyautogui.click()
        print("Clicked on the Join Meeting button.")
        time.sleep(0.5)
        
        # Meeting Info
        meetingID = "599 964 5575"
        meetingPassword = "R79xbj"

        meetX,meetY = pyautogui.locateCenterOnScreen('meetingID.png')
        pyautogui.moveTo(meetX/2,meetY/2,0.3)
        pyautogui.click()
        pyautogui.typewrite(meetingID)
        time.sleep(0.2)
        print("Clicked on the Meeting ID.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'meetingID' image not found.")
    
    try:
        locX,locY = pyautogui.locateCenterOnScreen('audio.png')
        pyautogui.moveTo(locX/2,locY/2,0.2)
        pyautogui.click()
        time.sleep(0.2)
        print("Checked off don't connect to audio.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'audio.png' image not found.")
    
    try:
        locX1,locY1 = pyautogui.locateCenterOnScreen('video.png')
        pyautogui.moveTo(locX1/2,locY1/2,0.2)
        pyautogui.click()
        time.sleep(0.2)
        print("Checked off don't show video.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'video.png' image not found.")

    try:
        locX2,locY2 = pyautogui.locateCenterOnScreen('join.png')
        pyautogui.moveTo(locX2/2,locY2/2,0.2)
        pyautogui.click()
        time.sleep(0.5)
        print("Clicked joined button.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'join.png' image not found.")

    try:
        locX3, locY3 = pyautogui.locateCenterOnScreen('pass.png')
        pyautogui.moveTo(locX3/2,locY3/2)
        pyautogui.click()
        pyautogui.typewrite(meetingPassword)
        time.sleep(0.2)
        print("Entered meeting password button.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'pass.png' image not found.")

    try:
        locX4,locY4 = pyautogui.locateCenterOnScreen('joinn.png')
        pyautogui.moveTo(locX4/2,locY4/2,0.2)
        pyautogui.click()
        time.sleep(0.2)
        print("Clicked joined button.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'joinn.png' image not found.")

def loginToZoom():
    """Login to Zoom by finding the Login button, clicking it, and typing in the username
    and password fields."""
    pass

def signUpForZoom():
    """Navigate to the Sign Up page of Zoom by positioning the cursor over the
    'Sign up' button on the homepage and pressing enter."""
    pass

if __name__ == "__main__":
    main()
