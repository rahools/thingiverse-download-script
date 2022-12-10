# Thingiverse File Downloader

This repository contains a utility script that can be used to download files from Thingiverse.

## Problem

Sometimes the 'Download All Files' button on Thingiverse does not work, and it can be difficult to download the files manually.

## Solution

The script in this repository uses Python and Selenium to automate the process of downloading the files. This provides an alternative way to download the files even when the 'Download All Files' button is not working.

## Usage

To use the script, you will need to have pipenv installed. Then, you can use the following commands to run the script:

```
# Install the dependencies
pipenv install

# Run the script
pipenv run python download.py
```

You can also modify the script to customize the behavior and download files from specific Thingiverse pages.

## Requirements

- Python 3
- pipenv
- Selenium

## Script

The name of the main script is download.py. It uses Python and Selenium to navigate to the page and download the files. The Python environment is setup using pipenv.

## Additional Notes

Feel free to use and modify the script as needed. If you have any questions or suggestions, you can create an issue on the repository.

---

This readme was generated using [ChatGPT](https://chat.openai.com).