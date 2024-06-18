import os
import sys
import time
import urllib.request
import subprocess

# win + r
# type cmd
# type python --version
# install from https://www.python.org/ if needed
# change to directory where script is located: cd path\to\your\script
# start script: python 200.py
# stop script: ctrl + c
# the alarm will sound until you stop the script
# time of first successful request will be displayed with each successful request

def send_http_request(url):
    try:
        response = urllib.request.urlopen(url)
        return response.getcode() == 200
    except Exception as e:
        print(f"Error sending HTTP request: {e}")
        return False

def play_sound(sound_file):
    try:
        if sys.platform == 'darwin':
            subprocess.run(['afplay', sound_file])
        elif sys.platform.startswith('linux'):
            subprocess.run(['aplay', sound_file])
        elif sys.platform == 'win32':
            # For Windows, using winsound module
            import winsound
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
        else:
            print("Unsupported platform for playing sound.")
    except Exception as e:
        print(f"Error playing sound: {e}")

def main():
    domain = 'http://origins.habbo.com'  # Replace with the domain you want to check
    alert_sound_file = 'Alarm02.wav'
    
    first_200_response_time = None

    while True:
        if send_http_request(domain):
            if first_200_response_time is None:
                first_200_response_time = time.strftime('%H:%M:%S on %Y-%m-%d')
                print(f"200 OK response received. First response received at {first_200_response_time}")
                play_sound(alert_sound_file)
            else:
                print(f"200 OK response received. First response was at {first_200_response_time}")
                play_sound(alert_sound_file)
        else:
            print("Failed to receive a 200 response.")
        time.sleep(10)

if __name__ == '__main__':
    main()
