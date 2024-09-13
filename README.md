# Keylogger Script using `pynput`

This is a simple keylogger script written in Python using the `pynput` library. It logs keypresses to a file named `keylog.txt`. The script captures alphanumeric characters and spaces and writes them to the log file in real-time.

## Features

- Captures alphanumeric keys and spaces.
- Logs keypresses into a file named `keylog.txt`.
- Stops when the `ESC` key is pressed.

## How to Use

### 1. Install Dependencies

This script uses the `pynput` library to capture keyboard events. You can install it using `pip`:

```bash
pip install pynput
