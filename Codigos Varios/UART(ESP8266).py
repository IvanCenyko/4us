from machine import UART
import time

uart = UART(1, baudrate=115200) #establezco conexion en pines a velocidad 115200

while True:
  uart.write('hello\r\n') #mando hello (\r\n es para que se imprima correctamente y saltando linea)
  time.sleep(1)
  
  #se ejecuta en consola como: sudo python3 hello.py
  
