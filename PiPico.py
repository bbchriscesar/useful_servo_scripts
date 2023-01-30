import serial

# Open the serial port at COM3 with a baud rate of 115200
ser = serial.Serial('COM3', 115200)

# Read and print any data received over the serial connection
while True:
    data = ser.readline()
    print(data)
