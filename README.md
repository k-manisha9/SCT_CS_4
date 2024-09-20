# Simple Keystroke Logger

This project is a **Keystroke Logger** built using Python's `pynput` library. It captures and records every key pressed by the user and logs them into a file.

## Features

- **Logs Keystrokes**: Captures all key presses, including special keys (e.g., Enter, Space, Shift) and records them into a file (`keylog.txt`).
- **Special Key Handling**: Recognizes and logs special keys like `Enter`, `Space`, `Tab`, etc.
- **Escape to Stop**: Stops the keystroke listener when the `Esc` key is pressed.

## How It Works

1. **Key Press Detection**: Every time a key is pressed, the key is logged into a file (`keylog.txt`), including normal alphanumeric keys and special keys.
2. **Key Release Detection**: If the `Esc` key is released, the logger stops capturing keystrokes.
3. **Log File**: The recorded keystrokes are appended to a log file (`keylog.txt`), where each key is logged as it's pressed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/keystroke-logger.git
   ```

2. Navigate to the project directory:
   ```bash
   cd keystroke-logger
   ```

3. Install the required dependencies:
   ```bash
   pip install pynput
   ```

## Usage

1. Run the script:
   ```bash
   python keylogger.py
   ```

2. The script will start capturing all keystrokes and log them into a file named `keylog.txt`.

3. To stop the logger, press the `Esc` key.

## Example

While running, the `keylog.txt` file will capture keystrokes like this:

```
hello [Key.space] world [Key.enter]
[Key.shift] Python [Key.space] is [Key.space] fun
```

## Warning

This keystroke logger is for **educational purposes only**. Using keyloggers maliciously (e.g., to steal personal information or passwords) is illegal and unethical. Please ensure that you have proper authorization before logging keystrokes on any device.

## Contributing

Feel free to fork this repository and contribute! Pull requests for improvements, such as encryption of the log file or additional features, are welcome.
