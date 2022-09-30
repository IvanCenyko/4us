import serial
ser = serial.Serial('/dev/serial0')
ser.baudrate(115200)

while 1:
  try:
    received_data = ser.read(7)
    print(received.data.decode('utf-8'))
  except serial.serialutil.SerialException:
    ser.close()
    ser = serial.Serial('/dev/serial0')
    ser.baudrate(115200)
