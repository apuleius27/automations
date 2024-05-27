# Achieve Gigabit speed on TP-Link VR1210v V1 Modem - Tested on Linux / MacOS

## Description

This script allows the TP-Link VR1210v V1 modem to reach 1 Gbit/s download speed, addressing an issue present for many users.

Due to unknown reasons (probably due to a firmware bug), if the modem is not rebooted every few hours (ca. 4h) the download speed becomes capped at 250 Mbit/s, for each connected device.

The script implements a workaround that allows to "uncap" the speed without the need to reboot.

It is best to schedule the script to run automatically (as described below), however you would need a device (e.g. raspberry pi) to be always active so that the script be run periodically.

## How It Works

The script uses the selenium library to automate the process of toggling the modem's Access Control setting on and off, uncapping the download speed neither without rebooting the modem nor causing connection issues.

## Prerequisites

- The script relies on toggling and keeping Access Control on the "Off" value. Make sure you don't use that feature

- Ensure you have the necessary Python packages installed, mainly:
  
  - `selenium` (version >= '4.21.0')

- Ensure you have ChromeDriver installed (and also Chromium in case of Linux usage)
1. **Ensure Python and Pip are installed on your system**

2. **Install selenium and check version**
   
   ```python
   pip install selenium
   pip show selenium
   ```

3. **Install the appropriate Webdriver**
   
   If on Linux (debian):
   
   Installl Webdriver:
   
   ```bash
   sudo apt update
   sudo apt install chromium-browser chromium-chromedriver
   ```
   
   Verify the installations (and take note of the path):
   
   ```bash
   which chromedriver
   which chromium-browser
   ```
   
   Ensure ChromeDriver is executable:
   
   ```bash
   sudo chmod +x /usr/bin/chromedriver # Insert your path noted above
   which chromedriver
   ```
   
   If on Mac:
   
   Install brew and Webdriver:
   
   ```bash
   brew install --cask chromedriver
   ```
   
   Verify the installations (and take note of the path):
   
   ```bash
   which chromedriver
   ```

**2. Install ChromeDriver (on Linux, also Chromium):**

   On Linux:

   Install Webdriver:

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

   Verify the installations (and take note of the path):

```bash
which chromedriver
which chromium-browser
```

   Ensure ChromeDriver is executable:

```bash
sudo chmod +x /usr/bin/chromedriver # Insert your path noted above
which chromedriver
```

   On Mac:

   Install Webdriver:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install --cask chromedriver
```

   Verify the installations (and take note of the path):

```bash
which chromedriver
```

## Usage

1. **Adjust parameters in the first part of the script** based on your configuration, and as indicated in the commented lines of the python file

2. **Run the Script** manually manually and test if it runs correctly by checking the outcomes generated on screen:
   
   ```python
   python main_linux_macos.py
   ```

3. **Schedule the Script as a cron job Cron:** 
   
   ```bash
   crontab -e
   ```
   
   Add a cron job to schedule the script (e.g., to run every 3 hours):
   
   ```bash
    0 */3 * * * /path/to/your/python /path/to/your/file/main_linux_macos.py # Run which python to get your python path
   ```

## Disclaimer

This solution has been tested on Linux debian-based OS and MacOs operating systems.

Use under your own responsibility.
