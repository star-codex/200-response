# Website Status Checker

This Python script checks a specified domain at 10-second intervals to see if a 200 response is received. If a 200 response is received, an audible alert is triggered and the time of the first successful request is displayed.

## Requirements

- Python 3.x
- A `.wav` file for the alert sound (e.g., `alert.wav`)

## Instructions

### Setup

1. **Check Python Installation**
    - Press `Win + R`
    - Type `cmd` and press `Enter`
    - In the Command Prompt, type:

      ```bash
      python --version
      ```

    - If Python is not installed, download and install it from [https://www.python.org/](https://www.python.org/)

2. **Save the Script**
    - Save the script as `200.py` in your desired directory.

3. **Add the Alert Sound**
    - Place your alert sound file (`alert.wav`) in the same directory as the script.

### Running the Script

1. **Open Command Prompt**
    - Press `Win + R`
    - Type `cmd` and press `Enter`

2. **Navigate to the Script Directory**
    - Change to the directory where the script is located. For example:

      ```bash
      cd path\to\your\script
      ```

3. **Start the Script**
    - Run the script by typing:

      ```bash
      python 200.py
      ```

4. **Stop the Script**
    - To stop the script, press `Ctrl + C` in the Command Prompt.

### Behavior

- The alarm will sound when a 200 OK response is received.
- The time of the first successful request will be displayed with each successful request.

## Example Output

`200 OK response received. First response received at 14:32:21 on 2023-06-18`

`200 OK response received. First response was at 14:32:21 on 2023-06-18`

## Notes

- Ensure the alert sound file (`alert.wav`) exists in the same directory as the script.
- The script supports `.wav` files for the alert sound. Make sure the sound file format is compatible with your operating system's sound player.
