import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1) #Puerto COM3 en 9600 baudios

ser.write(b'p') #Enviar datos a arduino

ser.close() #Cerrar la conexion 