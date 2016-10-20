import serial,time
arduino = serial.Serial('COM3',9600,timeout=.1)
time.sleep(2)
data = "f"
while True:
    arduino.write(data.encode())
    time.sleep(2)
