import serial
import pydirectinput
import time
serial_port = 'COM4'
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate, timeout=0.05)
current_key = None
drift_keys = []
def release_current_key():
    global current_key, drift_keys
    if current_key:
        pydirectinput.keyUp(current_key)
        current_key = None
    for key in drift_keys:
        pydirectinput.keyUp(key)
    drift_keys = []
try:
    ser.flushInput()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            if line:
                print(line)
                if line == "Forward":
                    if current_key != 'space':
                        release_current_key()
                        pydirectinput.keyDown('space')
                        current_key = 'space'
                elif line == "Backward":
                    if current_key != 'down':
                        release_current_key()
                        pydirectinput.keyDown('down')
                        current_key = 'down'
                elif line == "Left side":
                    if current_key != 'left':
                        release_current_key()
                        pydirectinput.keyDown('left')
                        current_key = 'left'
                elif line == "Right side":
                    if current_key != 'right':
                        release_current_key()
                        pydirectinput.keyDown('right')
                        current_key = 'right'
                elif line == "Left Drift":
                    if set(drift_keys) != {'left', 'down'}:
                        release_current_key()
                        pydirectinput.keyDown('left')
                        pydirectinput.keyDown('down')
                        drift_keys = ['left', 'down']
                elif line == "Right Drift":
                    if set(drift_keys) != {'right', 'down'}:
                        release_current_key()
                        pydirectinput.keyDown('right')
                        pydirectinput.keyDown('down')
                        drift_keys = ['right', 'down']
                elif line == "Waiting for input":
                    release_current_key()
        else:
            time.sleep(0.0005)
except KeyboardInterrupt:
    release_current_key()
    ser.close()
    print("Serial connection closed.")
