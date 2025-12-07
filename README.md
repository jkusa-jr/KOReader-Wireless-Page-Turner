# KOReader Wireless Page Turner

A wireless gamepad controller for KOReader that allows you to turn pages and adjust brightness remotely over WiFi.

## What it does

Control your KOReader device wirelessly using a gamepad connected to your computer:
- **Button 1**: Previous page
- **Button 2**: Next page  
- **Button 17**: Increase brightness
- **Button 19**: Decrease brightness

## Requirements

- Python 3.8+
- A gamepad/joystick connected to your computer
- KOReader device with HTTP API enabled on the same network

## Setup with uv (recommended)

1. Install [uv](https://docs.astral.sh/uv/):
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install pygame requests pynput
   ```

3. Configure your KOReader device IP:
   - Edit `main.py` and set the `IP` variable to your KOReader device's IP address
   - Example: `IP = "192.168.1.100"`

4. Enable KOReader HTTP API:
   - On your KOReader device: Settings ’ Network ’ HTTP API ’ Enable
   - Note the port (default is 8080)

## Usage

1. Connect your gamepad to your computer
2. Make sure your KOReader device is on the same WiFi network
3. Run the program:
   ```bash
   python main.py
   ```
4. Use your gamepad to control page turning and brightness!

## For Python Beginners

This project uses three main Python libraries:
- **pygame**: Handles gamepad input detection
- **requests**: Sends HTTP commands to KOReader
- **pynput**: Provides keyboard control capabilities

The program continuously listens for gamepad button presses and sends corresponding HTTP requests to your KOReader device's API.