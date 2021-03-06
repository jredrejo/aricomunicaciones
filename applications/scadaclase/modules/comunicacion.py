import serial
import time
import datetime

# Instrucción para arrancar este programa:
#  python3 web2py.py -S scada  -M -R applications/scada/modules/comunicacion.py

arduino = serial.Serial('/dev/ttyACM0')
time.sleep(5)  # espera a que arduino se reinicie después de abrir el puerto

# borrar lo que hubiera en los buffers de comunicación:
arduino.flush()


# select() devuelve una lista, aunque esté vacía:
# direcciones = db(db.Signals.nombre=='Potenciómetro').select()

# con first cogemos sólo un registro, el primero que cumpla la condición:
direccion = db(db.Signals.nombre=='Potenciómetro').select().first()
direccion_id = direccion.id

led = db(db.Signals.nombre=='Led').select().first()
led_id = led.id


while True:
    arduino.write('P'.encode())
    leer_desde_arduino = arduino.readline().decode('UTF-8')
    print("Esto ha leído: ", leer_desde_arduino)

    db.Valores.insert(direccion=direccion_id, valor = float(leer_desde_arduino), Fecha = datetime.datetime.now())
    
    # Forzamos la escritura desde el buffer de memoria:
    db.commit()


    orden_led = db(db.Ordenes.direccion==led_id).select().first()
    if orden_led.valor == 1:
        arduino.write('E'.encode())
    else:
        arduino.write('A'.encode())
    
    time.sleep(1)


