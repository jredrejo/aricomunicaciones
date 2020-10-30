import serial
import time


arduino = serial.Serial('/dev/ttyACM0')
time.sleep(5)  # espera a que arduino se reinicie después de abrir el puerto

# borrar lo que hubiera en los buffers de comunicación:
arduino.flush()


while True:

    comando = input("Escribe la orden")
    arduino.write(comando.encode())
    if comando == 'P':
        leer_desde_arduino = arduino.readline().decode('UTF-8')
        print("Esto ha leído: ", leer_desde_arduino)


