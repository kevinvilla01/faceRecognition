import serial
import time

ser = serial.Serial('COM3', 9600) #COM3 is the port that the Arduino is connected to

ser.write(b'P') #P is the command to turn on the LED

ser.close() #close the serial port